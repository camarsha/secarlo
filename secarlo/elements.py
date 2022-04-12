"""
Tools for reading and working with the full
precision maps from COSY

-Caleb Marshall Ohio University/FRIB 2022
"""

import numpy as np
import transport
from tqdm import tqdm


def slow_transport(x0, coeff_array, power_array):
    """
    Python version of the fortran subroutine for checks
    """
    x = np.zeros(8)

    for i in range(8):
        for j in range(len(coeff_array)):
            if coeff_array[i, j] == 0.0:
                pass
            else:
                for k in range(8):
                    if power_array[i, j, k] == 0.0:
                        pass
                    else:
                        x[i] += coeff_array[i, j] * x0[i]**power_array[i, j, k]
    return x
                        
def read_map(filename):
    """
    The full precision cosy maps are a pain in the ass to read.
    """

    total_coeff = []
    total_power = []
    max_len = 0
    
    with open(filename, 'r') as f:
        coeff = []
        power = []

        for line in f:
            if '---' in line:
                if len(coeff) > max_len:
                    max_len = len(coeff)
                total_coeff.append(coeff)
                total_power.append(power)
                coeff = []
                power = []
            elif 'I' in line:
                pass
            else:
                line = line.split()
                temp = line[3:11]
                coeff.append(float(line[1]))
                power.append(np.asarray(temp, dtype='float64'))

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


class OpticalElement():

    def __init__(self):
        self.map_coeff = None
        self.map_power = None
        self.x_lim = np.inf
        self.y_lim = np.inf
        self.z_lim = None
        self.r_lim = None
        self.name = 'Unknown'

    def create_map(self, filename):
        self.map_coeff, self.map_power = read_map(filename)

    def transport(self, x0):

        x = np.zeros(x0.shape, dtype='float64', order='F')

        
        samples = x0.shape[0]
        n = self.map_coeff.shape[0]
        m = self.map_coeff.shape[1]
        x = transport.transport_element(n, m, samples, x0,
                                        self.map_coeff,
                                        self.map_power)

        return x

    def create_constraint(self, x, y, z, geometry='rectangle'):
        """
        Give the x, y, z limits for this element.
        """

        self.x_lim = x
        self.y_lim = y
        self.z_lim = z

        if geometry == 'rectangle':
            self.geometry = self.rect_geometry
        elif geometry == 'circle':
            self.r_lim = np.sqrt(self.x_lim**2.0 + self.y_lim**2.0)
            self.geometry = self.circ_geometry

    def rect_geometry(self, x):
        if (x[0] < self.x_lim) and (-1.0*self.x_lim < x[0]):
            if (x[2] < self.y_lim) and (-1.0*self.y_lim < x[2]):
                return True
        return False
    
    def circ_geometry(self, x):
        rx = np.sqrt(x[0]**2.0 + x[2]**2.0)
        if (rx < self.r_lim):
            return True
        return False
    
    def apply_constrain(self, x):
        """Check array x against the
        physical constrains of the element.
        x is assumed to have the COSY ordering.

        Before I make this more complicated, just
        assuming a rectangular beam pipe.

        :param x: array of current position
        :returns: flag of True or False
        """
        flag = self.geometry(x)
        return flag



class BeamLine():

    def __init__(self):
        self.elements = []
        self.num_elements = 0
        self.max_len = 0

    def add_element(self, map_filename, x_dim, y_dim, z_dim,
                    name=None, geometry='rectangle'):
        temp = OpticalElement()
        temp.create_constraint(x_dim, y_dim, z_dim, geometry=geometry)
        temp.create_map(map_filename)
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
        self.map_coeff = np.zeros((self.num_elements, 8,
                                  self.max_len), order='F')
        self.map_power = np.zeros((self.num_elements, 8,
                                  self.max_len, 8), order='F')
        # fill them out
        for i, ele in enumerate(self.elements):
            temp = ele.map_coeff.shape[1]
            self.map_coeff[i, :, :temp] = ele.map_coeff[:, :temp]
            self.map_power[i, :, :temp, :] = ele.map_power[:, :temp, :]
            
    def transport(self, x0):
        
        all_positions = np.zeros((len(x0), self.num_elements, 8))
        
        for i, ele in tqdm(enumerate(self.elements),
                           total=self.num_elements):
            all_positions[:, i, :] = ele.transport(x0)
            x0 = all_positions[:, i, :]
        return all_positions

    def fortran_transport(self, x0):
        all_positions = np.zeros((self.num_elements, 8), order='F')
        all_positions = transport.transport_system(8, self.max_len,
                                                   self.num_elements,
                                                   x0, self.map_coeff,
                                                   self.map_power)
        return all_positions
