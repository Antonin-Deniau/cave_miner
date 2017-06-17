# -*- coding: utf-8 -*-
"""Search for code cave in all binaries
Usage:
  cave_miner search [--size=<size>] <file_name>
  cave_miner inject <payload> <file_name> <address>

Options:
  -h --help      Show this help
  --version      Show the program version
  --size=<size>  The minimum size of the cave in bytes [default: 256]
"""
from docopt import docopt
import os.path
from cave_miner import *
import re

def print_banner():
  print """
    {gy}/========\{e}
   {gy}/{e}    {gn}||{e}    {gy}\{e}
        {gn}||{e}
        {gn}||{e}
        {gn}||{e}
   CAVE {gn}||{e} MINER
  """.format(gy=Bcolors.GREY, gn=Bcolors.GREEN, e=Bcolors.ENDC)

def test_file(filename):
  res = os.path.isfile(filename)

  if not res: print "{r}*** File {filename} doesnt exist ***{e}".format(filename=filename, r=Bcolors.RED, e=Bcolors.ENDC)
  return res

def test_number(number):
  pattern = re.compile("0[xX][0-9a-fA-F]+|\d+")
  res = pattern.match(number)

  if not res: print "{r}*** Number {number} not valid ***{e}".format(number=number, r=Bcolors.RED, e=Bcolors.ENDC)
  return res

def main():
  print_banner()
  args = docopt(__doc__, version='0.1')
  CONTINUE = True

  if args["search"] == True:
    CONTINUE = CONTINUE and test_file(args["<file_name>"])
    CONTINUE = CONTINUE and test_number(args["--size"])

    if CONTINUE: search(args["<file_name>"], args["--size"])

  elif args["inject"] == True:
    CONTINUE = CONTINUE and test_file(args["<payload>"])
    CONTINUE = CONTINUE and test_file(args["<file_name>"])
    CONTINUE = CONTINUE and test_number(args["<address>"])

    if CONTINUE: inject(args["<payload>"], args["<file_name>"], args["<address>"])
