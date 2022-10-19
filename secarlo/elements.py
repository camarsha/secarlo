"""
Tools for reading and working with the full
precision maps from COSY

-Caleb Marshall Ohio University/FRIB 2022
"""

import numpy as np
import transport
from . import geometry
from tqdm import tqdm


def read_map(filename):
    """
    The full precision cosy maps are a pain in the ass to read.
    """

    total_coeff = []
    total_power = []
    max_len = 0

    with open(filename, "r") as f:
        coeff = []
        power = []

        for line in f:
            if "---" in line:
                if len(coeff) > max_len:
                    max_len = len(coeff)
                total_coeff.append(coeff)
                total_power.append(power)
                coeff = []
                power = []
            elif "I" in line:
                pass
            else:
                line = line.split()
                temp = line[3:11]
                coeff.append(float(line[1]))
                power.append(np.asarray(temp, dtype="float64"))

    # Make this a square array, pad with zeros
    coeff_array = np.zeros((8, max_len))
    power_array = np.zeros((8, max_len, 8))

    for i in range(8):
        length = len(total_coeff[i])
        coeff_array[i, :length] = total_coeff[i]
        power_array[i, :length, :] = total_power[i]

    coeff_array = np.asfortranarray(coeff_array)
    power_array = np.asfortranarray(power_array)

    return coeff_array, power_array


class OpticalElement:
    def __init__(self):
        self.map_coeff = None
        self.map_power = None
        self.z_lim = 0.0
        self.name = "Unknown"
        self.start_constraint = geometry.Geometry()
        self.end_constraint = geometry.Geometry()
        self.mistune = np.zeros(8, dtype="float64")

    def create_map(self, filename):
        self.map_coeff, self.map_power = read_map(filename)

    def set_mistune(self, E, m, q):
        """Sets a mistune of the element by the
        given parameters. This is not global, so after
        transport the mistune will be undone.

        :param E: Kinetic energy deviation
        :param m: mass deviation
        :param q: charge deviation

        """
        self.mistune += np.array([0.0, 0.0, 0.0, 0.0, 0.0, E, m, q])

    def transport(self, x0):
        x0_tuned = x0 + self.mistune
        x = np.zeros(x0.shape, dtype="float64", order="F")

        samples = x0.shape[0]
        n = self.map_coeff.shape[0]
        m = self.map_coeff.shape[1]
        x = transport.transport_element(
            n, m, samples, x0_tuned, self.map_coeff, self.map_power
        )
        x -= self.mistune
        return x

    def _check_constraint(self, geo_obj):

        if isinstance(geo_obj, geometry.Geometry):
            return geo_obj
        else:
            print("Need an instance of Geometry!")
            return geometry.Geometry()

    def set_start_constraint(self, geo_obj):
        """Set the beginning constrain with
        the instance of a geometry object.

        :param geo_obj: Geometry object
        :returns:

        """
        self.start_constraint = self._check_constraint(geo_obj)

    def set_end_constraint(self, geo_obj):
        """Set the end constrain with
        the instance of a geometry object.

        :param geo_obj: Geometry object

        """
        self.end_constraint = self._check_constraint(geo_obj)

    def apply_constraints(self, x):

        """Applies both the start and end constraints to
        the cosy vector x

        :param x: numpy array with cosy variables.
        :returns: Boolean

        """
        x_pos = x[0]
        y_pos = x[2]
        start = self.start_constraint.check_bounds(x_pos, y_pos)
        end = self.end_constraint.check_bounds(x_pos, y_pos)
        return start and end


class BeamLine:
    def __init__(self):
        self.elements = []
        self.num_elements = 0
        self.max_len = 0

    def add_element(
        self,
        map_filename,
        z_lim,
        name=None,
        geo_obj_start=None,
        geo_obj_end=None,
    ):
        temp = OpticalElement()
        temp.create_map(map_filename)
        temp.z_lim = z_lim
        if geo_obj_start:
            temp.set_start_constraint(geo_obj_start)
        if geo_obj_end:
            temp.set_end_constraint(geo_obj_end)
        if name:
            temp.name = name
        if temp.map_coeff.shape[1] > self.max_len:
            self.max_len = temp.map_coeff.shape[1]
        self.elements.append(temp)
        self.num_elements += 1

    def make_arrays(self):
        """
        This is an extra function, originally intended for
        a fortran subroutine to replace transport.
        That turned out to be slower, but I will leave it
        if it is worth looking at again.
        """
        self.map_coeff = np.zeros(
            (self.num_elements, 8, self.max_len), order="F"
        )
        self.map_power = np.zeros(
            (self.num_elements, 8, self.max_len, 8), order="F"
        )
        # fill them out
        for i, ele in enumerate(self.elements):
            temp = ele.map_coeff.shape[1]
            self.map_coeff[i, :, :temp] = ele.map_coeff[:, :temp]
            self.map_power[i, :, :temp, :] = ele.map_power[:, :temp, :]

    def create_z_array(self):
        self.z = np.zeros(self.num_elements + 1)
        self.z[0] = 0.0
        for i, ele in enumerate(self.elements):
            self.z[i + 1] = ele.z_lim
        self.z = np.cumsum(self.z)

    def transport(self, x0):
        """
        Pass entire rays to each element of the Beamline, and
        then transport in order through the system.
        """

        all_positions = np.zeros((len(x0), self.num_elements + 1, 8), order="F")
        all_positions[:, 0, :] = np.asfortranarray(x0[:])
        for i, ele in tqdm(enumerate(self.elements), total=self.num_elements):
            all_positions[:, i + 1, :] = ele.transport(all_positions[:, i, :])
        return all_positions

    def fortran_transport(self, x0):
        all_positions = np.zeros((self.num_elements, 8), order="F")
        all_positions = transport.transport_system(
            8,
            self.max_len,
            self.num_elements,
            x0,
            self.map_coeff,
            self.map_power,
        )
        return all_positions
