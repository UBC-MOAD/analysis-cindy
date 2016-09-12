from setuptools import setup

setup(
    name='ArcticTools',
    version='1.0',
    description='tools to plot/analyze Arctic',
    author='Cindy Yu',
    author_email='xiaoxiny@eos.ubc.ca',
    install_requires=[
    'matplotlib', 
    'basemap', 
    'netCDF4'],
    packages=['ArcticTools']
)
