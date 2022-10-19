from . import elements
from . import geometry
import pkg_resources
import pandas as pd

# Geometry and optical elements defined in csv file
beam_pipes = pkg_resources.resource_filename("secarlo", "data/beam_pipes.csv")

df = pd.read_csv(beam_pipes)


def build_secar(df, maps_dir):
    secar = elements.BeamLine()
    for f, z, n in zip(df["file"], df["Z"], df["NAME"]):
        secar.add_element(
            maps_dir + f,
            z,
            name=str(n),
        )

    secar.create_z_array()
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
