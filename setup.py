from setuptools import setup
setup(
  name = 'cave_miner',
  packages = ['cave_miner', 'cave_miner.formats'],
  entry_points={
    'console_scripts': [
      'cave_miner=cave_miner.main:main',
    ],
  },
  install_requires = ['docopt==0.6.2', 'kaitaistruct==0.7'],
  version = '1.6',
  description = 'Search for code cave in all binaries',
  author = 'DENIAU Antonin',
  author_email = 'antonin.deniau@protonmail.com',
  url = 'https://github.com/Antonin-Deniau/cave_miner',
  keywords = ['code', 'cave', 'codecave', 'macho', 'mach-o', 'elf', 'pe'],
  classifiers = [],
)

