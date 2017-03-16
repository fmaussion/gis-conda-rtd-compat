"""Setup file for the test package.

   Adapted from the Python Packaging Authority template and also from xarray's.
"""

from setuptools import setup, find_packages  # Always prefer setuptools
from codecs import open  # To use a consistent encoding

MAJOR = 0
MINOR = 0
MICRO = 1
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)
QUALIFIER = ''

DISTNAME = 'gis-conda-rtd-compat'
LICENSE = 'Public Domain'
AUTHOR = 'Fabien Maussion'
AUTHOR_EMAIL = 'fabien.maussion@uibk.ac.at'
URL = 'http://gis-conda-rtd-compat.readthedocs.io'
CLASSIFIERS = []

DESCRIPTION = 'Test epository for doc builds'
with open('README.md') as file:
    LONG_DESCRIPTION = file.read()

# code to extract and write the version copied from pandas
FULLVERSION = VERSION

setup(
    # Project info
    name=DISTNAME,
    version=FULLVERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    # The project's main homepage.
    url=URL,
    # Author details
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    # License
    license=LICENSE,
    classifiers=CLASSIFIERS,
    # What does your project relate to?
    keywords=[],
    # Find packages automatically
    packages=find_packages(exclude=['docs']),
    # Decided not to let pip install the dependencies, this is too brutal
    install_requires=[],
    # additional groups of dependencies here (e.g. development dependencies).
    extras_require={},
    # data files that need to be installed
    package_data={},
    # Old
    data_files=[],
    # Executable scripts
    entry_points={},
)
