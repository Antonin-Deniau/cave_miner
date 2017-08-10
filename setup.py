from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cave_miner',
    version='1.8.0',
    description='Search for code cave in all binaries',
    long_description=long_description,
    url='https://github.com/Antonin-Deniau/cave_miner',
    author='DENIAU Antonin',
    author_email='antonin.deniau@protonmail.com',
    license='GNU General Public License v3 or later (GPLv3+)',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='codecave hacking injection',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['docopt==0.6.2', 'kaitaistruct==0.7'],

    extras_require={},

    entry_points={
      'console_scripts': [
        'cave_miner=cave_miner.main:main',
      ],
    },
)
