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
        self.x = np.array([p[0] for p in points])
        self.y = np.array([p[1] for p in points])
        self.calc_edges()

    def calc_edges(self):
        self.edges = []
        for i, ele in enumerate(self.points):
            p1 = ele
            p2 = self.points[(i + 1) % len(self.points)]
            self.edges.append((p1, p2))
        self.edges = np.asarray(self.edges, order='F')
        self.n = self.edges.shape[0]

    def check_bounds(self, x, y):
        xn = np.asarray([x]) if np.isscalar(x) else np.asarray(x)
        yn = np.asarray([y]) if np.isscalar(y) else np.asarray(y)
        inside = constraints.ray_casting_array(self.n, len(xn), self.edges, xn, yn)
        return inside

    def calc_center(self, x, y):
        """
        Centroid of a closed polygon.
        """
        signed_area = self.calc_area(x, y)

        # quicker to do one calculation since second part is shared
        xy = np.array([x, y])
        cent = np.dot(xy + np.roll(xy, 1, axis=1),
                      (x * np.roll(y, 1) - y * np.roll(x, 1)))
        cent = cent/(6.0 * signed_area) 
        return cent[0], cent[1]
        
    def calc_area(self, x, y):

        """
        Calculate the signed area of the polygon.

        A = 0.5 * SUM_0^N-1 (x_i y_{i+1} - x_{i+1} y_i)

        Where N is the number of vertices.

        See:
        https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates
        
        """

        # shift to maintain accuracy, just in case
        x_s = x - x.mean()
        y_s = y - y.mean()

        # using offset dot products
        correction = y_s[-1] * x_s[0] - x_s[-1] * y_s[0] 
        det_sum = np.dot(y_s[:-1], x_s[1:]) - np.dot(x_s[:-1], y_s[1:])
        return 0.5 * (det_sum + correction)

    def translate(self, x, y):

        """
        Shift the polygon points to the desired x and y values.
        The idea is to align the polygon center with the surveyed centers
        from the lattice file.
        """

        # first get the current center
        cent_x_init, cent_y_init = self.calc_center(self.x, self.y)
        # shift all points to the desired position, then remake the edges
        self.x = (self.x - cent_x_init ) + x
        self.y = (self.y - cent_y_init ) + y
        self.points = [(a, b) for a, b in zip(self.x, self.y)]
        self.calc_edges()

    def sort_points(self, x, y):
        cx, cy = self.calc_center(x, y)
        angles = []
        for p in self.points:
            # arctan2 goes y then x
            theta = np.arctan2(p[1]-cy, p[0]-cx)
            angles.append(theta)

        # now sort points
        self.points = [x for _, x in sorted(zip(angles, self.points))]
        self.x = np.array([p[0] for p in self.points])
        self.y = np.array([p[1] for p in self.points])
        self.calc_edges()
