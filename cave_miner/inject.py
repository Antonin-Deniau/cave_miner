from utils import *

def inject(payload_name, file_name, straddr):
  print "{}[*]{} Starting injection into binary...{}".format(Bcolors.YELLOW, Bcolors.BOLD, Bcolors.ENDC)
  print
  addr = parse_int(straddr)

  payload = open(payload_name, "rb").read()
  vic = open(file_name, "rb").read()

  res = vic[:addr] + payload + vic[addr + len(payload):]

  f = open("{}.mod".format(file_name), "w")
  f.write(res)
  f.close()

  print "{}[*]{} Injection finished.{}".format(Bcolors.YELLOW, Bcolors.BOLD, Bcolors.ENDC)
