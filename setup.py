# Get on making this package
from setuptools import find_packages

from numpy.distutils.core import setup, Extension

ext1 = Extension(name='transport',
                 sources=['secarlo/transport.f90'],
                 f2py_options=['--quiet'],
                )

ext2 = Extension(name='constraints',
                 sources=['secarlo/constraints.f90'],
                 f2py_options=['--quiet'],
                )

setup(name="SeCarlo",
      version="0.1.1",
      description="Use COSY maps to simulate SECAR",
      author="Caleb Marshall",
      packages=find_packages(),
      ext_modules=[ext1, ext2],
      include_package_data=True)
