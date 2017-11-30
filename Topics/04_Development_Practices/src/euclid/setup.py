# Always prefer setuptools over distutils
from setuptools import setup

setup(
    name='euclid',      version='0.0.1',
    description='Euclid greatest common denominator (GCD) library',
    long_description="....",
    url='https://github.com/gdanezis/Design_and_Professional_Skills',
    author='George Danezis, University College London',
    author_email='g.danezis@ucl.ac.uk',
    license='BSD',

    packages=['euclid'],          # The package directories
    install_requires=['pytest==3.3.0'],  # Dependencies

    entry_points={                # Entry function
        'console_scripts': ['euclid=euclid:main'] },
)