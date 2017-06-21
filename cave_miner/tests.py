import os.path
import re

def test_file(filename):
  res = os.path.isfile(filename)

  if not res: print "{r}*** File {filename} doesnt exist ***{e}".format(filename=filename, r=Bcolors.RED, e=Bcolors.ENDC)
  return res

def test_number(number):
  pattern = re.compile("0[xX][0-9a-fA-F]+|\d+")
  res = pattern.match(number)

  if not res: print "{r}*** Number {number} not valid ***{e}".format(number=number, r=Bcolors.RED, e=Bcolors.ENDC)
  return res

def test_bytes(args):
  res = True
  pattern = re.compile("0[xX][0-9a-fA-F]{1,2}")

  for b in args:
    res = res and pattern.match(b)
    if not res: print "{r}*** Byte {byte} not valid ***{e}".format(byte=b, r=Bcolors.RED, e=Bcolors.ENDC)

  return res
