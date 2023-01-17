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
    ],
)
