from . import elements
from . import geometry
import pkg_resources
import pandas as pd
import numpy as np

# Geometry and optical elements defined in csv file
beam_pipes = pkg_resources.resource_filename("secarlo", "data/beam_pipes.csv")

df = pd.read_csv(
    beam_pipes, keep_default_na=False, sep="\s*,\s*", engine="python"
)


def produce_points(filename, unit="in"):

    """CSV file with X and Y points

    :param filename: path to file
    :param unit: inches by default, so convert to meters
    :returns: list of tuples -> (x, y)

    """

    data = pd.read_csv(filename)
    points = [(x * 0.0254, y * 0.0254) for x, y in zip(data["X"], data["Y"])]
    return points


def produce_radius(filename, unit="in"):
    """Read file that has the radius defined

    :param filename:
    :param unit:
    :returns:

    """
    data = pd.read_csv(filename)
    r = data.iloc[0].to_numpy()[0] * 0.0254
    return r


def produce_rectangle(filename, unit="in"):
    """Place holder function for now

    :param filename:
    :param unit:
    :returns: np.inf

    """
    print("Rectangle input is not implemented at this time!")
    return np.inf, np.inf


def create_geometry_case(geo_type, geo_file):
    """

    :param geo_type: string that defines type of object
    :param geo_file: path to file with info
    :returns: geometry.Geometry object

    """
    if geo_type == "points":
        p = produce_points(geo_file)
        geo_obj = geometry.Polygon2D(p)
        # make sure they are centered
        geo_obj.sort_points()
        geo_obj.translate(0.0, 0.0)
        # switch x and y if they are rotated, all chambers
        # are larger in x than y
        if max(geo_obj.y) > max(geo_obj.x):
            p = [(y, x) for x, y in zip(geo_obj.x, geo_obj.y)]
            geo_obj = geometry.Polygon2D(p)
            geo_obj.sort_points()
            geo_obj.translate(0.0, 0.0)

    elif geo_type == "circle":
        r = produce_radius(geo_file)
        geo_obj = geometry.Circle(r)

    elif geo_type == "rectangle":
        x_lim, y_lim = produce_rectangle(geo_file)
        geo_obj = geometry.Rectangle(x_lim, y_lim)

    else:
        geo_obj = geometry.Geometry()

    return geo_obj


def build_secar(df, maps_dir):
    secar = elements.BeamLine()
    # build the maps and the z positions
    for f, z, n in zip(df["file"], df["Z"], df["NAME"]):
        secar.add_element(
            maps_dir + f,
            z,
            name=str(n),
        )
    secar.create_z_array()

    # now set up the constraints

    geometry_dir = pkg_resources.resource_filename("secarlo", "data")
    geometry_dir += "/"

    for ele, start_type, start_file, end_type, end_file in zip(
        secar.elements,
        df["begin_geo"],
        df["begin_file"],
        df["end_geo"],
        df["end_file"],
    ):
        if start_type:
            start_obj = create_geometry_case(
                start_type, geometry_dir + start_file
            )
            ele.set_start_constraint(start_obj)
        if end_type:
            end_obj = create_geometry_case(end_type, geometry_dir + end_file)
            ele.set_end_constraint(end_obj)

    return secar


def build_a_n(df=df):
    maps_dir = pkg_resources.resource_filename("secarlo", "a_n_maps")
    maps_dir += "/"
    secar = build_secar(df, maps_dir)
    return secar


def build_p_g(df=df):
    maps_dir = pkg_resources.resource_filename("secarlo", "p_g_maps")
    maps_dir += "/"
    secar = build_secar(df, maps_dir)
    return secar
