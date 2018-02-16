# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='clidye',
    version='0.0.1',
    description='Another Python Logging Module. Command line Dye. Pretty Print (and logging) for Python',
    long_description=long_description,
    author='Gilbert Montague',
    author_email='gilbert.i.montague@gmail.com',
    url='https://github.com/nerdgilbert/clidye',
    packages=find_packages(exclude=['docs', 'tests']),
    scripts=[path.join('bin', 'clidye')]
)
