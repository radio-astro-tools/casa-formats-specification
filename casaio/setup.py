import numpy as np

from setuptools import setup
from Cython.Build import cythonize


setup(
    name="casaio",
    version="0.0.1",
    packages=["casaio"],
    package_dir={'casaio': 'src/casaio'},
    ext_modules=cythonize(
        module_list="src/casaio/tablestream/python/*.py"
    ),
    include_dirs=[np.get_include()],
    setup_requires=["cython>=0.29", "numpy"],  # Required for compilation

)