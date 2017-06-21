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
from cave_miner import *

def print_banner():
  print """
    {gy}/========\{e}
   {gy}/{e}    {gn}||{e}    {gy}\{e}
        {gn}||{e}
        {gn}||{e}
        {gn}||{e}
   CAVE {gn}||{e} MINER
  """.format(gy=Bcolors.GREY, gn=Bcolors.GREEN, e=Bcolors.ENDC)

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
