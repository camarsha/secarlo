import numpy as np
from scipy.interpolate import UnivariateSpline


def ray_to_spline(ray, z, coor=0, k=3):
    x = ray[:, coor]
    f = UnivariateSpline(z, x, k=k)
    return f


def transmission(truth_array):
    total = truth_array.shape[0]
    loss = np.sum(np.any(truth_array == 0, axis=(1, 2)))
    return (1 - (loss / total)) * 100
