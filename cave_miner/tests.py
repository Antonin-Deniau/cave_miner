import os.path
import re
from utils import *

def test_file(filename):
  res = os.path.isfile(filename)

  if not res: print(color("{{red}}*** File {} doesnt exist ***{{endc}}".format(filename)))
  return res

def test_number(number):
  pattern = re.compile("0[xX][0-9a-fA-F]+|\d+")
  res = pattern.match(number)

  if not res: print(color("{{red}}*** Number {} not valid ***{{endc}}".format(number)))
  return res

def test_bytes(args):
  res = True
  pattern = re.compile("0[xX][0-9a-fA-F]{1,2}")

  for b in args:
    res = res and pattern.match(b)
    if not res: print(color("{{red}}*** Byte {} not valid ***{{endc}}".format(b)))

  return res
