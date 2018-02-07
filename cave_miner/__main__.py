# -*- coding: utf-8 -*-
"""Search for code cave in all binaries
Usage:
  cave_miner search [--size=<size>]
                    [--bytes=<bytes>]... <file_name>
  cave_miner inject <payload> <file_name> <address>

Options:
  -h --help        Show this help
  --version        Show the program version
  --size=<size>    The minimum size of the cave in bytes [default: 256]
  --bytes=<bytes>  The bytes used in the code cave [default: 0x00]
"""
from docopt import docopt
from . import *

def print_banner():
  banner = """
    /========\\
   /    ||    \\
        ||
        ||
        ||
   CAVE || MINER
  """
  banner = banner.replace('/', '{grey}/{endc}')
  banner = banner.replace('\\', '{grey}\\{endc}')
  banner = banner.replace('=', '{grey}={endc}')
  banner = banner.replace('||', '{green}||{endc}')

  print(color(banner))

def main():
  print_banner()
  args = docopt(__doc__, version='0.1')
  CONTINUE = True

  if args["search"] == True:
    CONTINUE = CONTINUE and test_file(args["<file_name>"])
    CONTINUE = CONTINUE and test_number(args["--size"])
    CONTINUE = CONTINUE and test_bytes(args["--bytes"])

    if CONTINUE: search(args["<file_name>"], args["--size"], args["--bytes"])

  elif args["inject"] == True:
    CONTINUE = CONTINUE and test_file(args["<payload>"])
    CONTINUE = CONTINUE and test_file(args["<file_name>"])
    CONTINUE = CONTINUE and test_number(args["<address>"])

    if CONTINUE: inject(args["<payload>"], args["<file_name>"], args["<address>"])

if __name__ == "__main__":
	main()