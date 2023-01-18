import numpy as np
from scipy.interpolate import UnivariateSpline


def ray_to_spline(ray, z, coor=0, k=3):
    x = ray[:, coor]
    f = UnivariateSpline(z, x, k=k)
    return f


def transmission(truth_rays):
    success = (np.sum(np.all(truth_rays, axis=1))) / 2.0
    total = float(truth_rays.shape[0])
    return success / total
