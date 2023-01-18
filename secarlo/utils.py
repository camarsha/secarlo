import numpy as np
from scipy.interpolate import UnivariateSpline


def ray_to_spline(ray, z, coor=0, k=3):
    x = ray[:, coor]
    f = UnivariateSpline(z, x, k=k)
    return f


def transmission(truth_rays):
    success = np.sum(np.all(truth_rays, axis=(1, 2)))
    total = float(truth_rays.shape[0])
    return success / total


def transmitted(rays, truth_rays):
    bool_arr = np.all(truth_rays, axis=(1, 2))
    return rays[bool_arr]


def shift_coordinates(cval, samples):
    """
    Shift physical values into cosy coordinates.
    dE = (E - E_central)/E_central
    """

    return (samples - cval) / cval
