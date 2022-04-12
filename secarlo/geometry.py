import numpy as np
import constraints
import matplotlib.pyplot as plt

class Polygon2D():

    """
    Class that builds 2d polygons and can
    check if points are within the bounded area.
    """
    def __init__(self, points):
        self.points = points
        self.make_edges()

    def make_edges(self):

        self.edges = []
        for i, ele in enumerate(self.points):
            p1 = ele
            p2 = self.points[(i + 1) % len(self.points)]
            self.edges.append((p1, p2))
        self.edges = np.asarray(self.edges)
        self.n = self.edges.shape[0]

    def check_bounds(self, x, y):
        xn = np.asarray([x]) if np.isscalar(x) else np.asarray(x)
        yn = np.asarray([y]) if np.isscalar(y) else np.asarray(y)
        inside = constraints.ray_casting_array(self.n, len(xn), self.edges, xn, yn)
        return inside

