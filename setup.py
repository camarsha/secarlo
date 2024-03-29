# Get on making this package
from setuptools import find_packages
from numpy.distutils.core import setup, Extension

ext1 = Extension(
    name="transport",
    sources=["secarlo/transport.f90"],
    f2py_options=["--quiet"],
)

ext2 = Extension(
    name="constraints",
    sources=["secarlo/constraints.f90"],
    f2py_options=["--quiet"],
)

setup(
    name="SeCarlo",
    version="0.1.1",
    description="Use COSY maps to simulate SECAR",
    author="Caleb Marshall",
    packages=find_packages(),
    ext_modules=[ext1, ext2],
    include_package_data=True,
    data_files=[
        ("secarlo/data/", ["secarlo/data/beam_pipes.csv"]),
        ("secarlo/data/", ["secarlo/data/q5_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/B6_entrance.csv"]),
        ("secarlo/data/", ["secarlo/data/B4_exit.csv"]),
        ("secarlo/data/", ["secarlo/data/q6_q7.csv"]),
        ("secarlo/data/", ["secarlo/data/q12_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/q8_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/q14_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/B2_entrance.csv"]),
        ("secarlo/data/", ["secarlo/data/q1_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/Hex2.csv"]),
        ("secarlo/data/", ["secarlo/data/B3_exit.csv"]),
        ("secarlo/data/", ["secarlo/data/B4_entrance.csv"]),
        ("secarlo/data/", ["secarlo/data/pipes_after_b2.csv"]),
        ("secarlo/data/", ["secarlo/data/q10_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/hex1_q3_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/q2_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/Hex3.csv"]),
        ("secarlo/data/", ["secarlo/data/q13_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/q9_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/B3_entrance.csv"]),
        ("secarlo/data/", ["secarlo/data/q4_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/dl_21.csv"]),
        ("secarlo/data/", ["secarlo/data/q15_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/beam_pipes.csv"]),
        ("secarlo/data/", ["secarlo/data/oct1.csv"]),
        ("secarlo/data/", ["secarlo/data/q11_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/ic_window.csv"]),
        ("secarlo/data/", ["secarlo/data/dl29_chamber.csv"]),
        ("secarlo/data/", ["secarlo/data/6_way_crosses.csv"]),
        ("secarlo/data/", ["secarlo/data/B7_entrance.csv"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.30"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.31"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.32"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.33"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.34"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.35"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.36"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.37"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.38"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.39"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.40"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.41"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.42"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.43"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.44"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.45"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.46"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.47"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.48"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.49"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.50"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.51"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.52"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.53"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.54"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.55"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.56"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.57"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.58"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.59"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.60"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.61"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.62"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.63"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.64"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.65"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.66"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.67"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.68"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.69"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.70"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.71"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.72"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.73"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.74"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.75"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.76"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.77"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.78"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.79"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.80"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.81"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.82"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.83"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.84"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.85"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.86"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.87"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.88"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.89"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.90"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.91"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.92"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.93"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.94"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.95"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.96"]),
        ("secarlo/p_g_maps", ["secarlo/p_g_maps/fort.97"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.30"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.31"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.32"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.33"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.34"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.35"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.36"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.37"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.38"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.39"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.40"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.41"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.42"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.43"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.44"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.45"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.46"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.47"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.48"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.49"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.50"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.51"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.52"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.53"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.54"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.55"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.56"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.57"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.58"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.59"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.60"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.61"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.62"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.63"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.64"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.65"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.66"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.67"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.68"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.69"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.70"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.71"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.72"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.73"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.74"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.75"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.76"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.77"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.78"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.79"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.80"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.81"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.82"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.83"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.84"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.85"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.86"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.87"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.88"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.89"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.90"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.91"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.92"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.93"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.94"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.95"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.96"]),
        ("secarlo/a_n_maps", ["secarlo/a_n_maps/fort.97"]),
    ],
)
