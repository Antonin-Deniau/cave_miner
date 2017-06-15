from setuptools import setup
setup(
  name = 'cave_miner',
  packages = ['cave_miner==0.3'], # this must be the same as the name above
  scripts = ['bin/cave_miner'],
  install_requires = ['docopt==0.6.2', 'kaitaistruct==0.7'],
  version = '0.3',
  description = 'Search for code cave in all binaries',
  author = 'DENIAU Antonin',
  author_email = 'antonin.deniau@protonmail.com',
  url = 'https://github.com/Antonin-Deniau/cave_miner', # use the URL to the github repo
  download_url = 'https://github.com/Antonin-Deniau/cave_miner/archive/0.3.tar.gz', # I'll explain this in a second
  keywords = ['code', 'cave', 'codecave', 'macho', 'mach-o', 'elf', 'pe'], # arbitrary keywords
  classifiers = [],
)

