from utils import *

def inject(payload_name, file_name, straddr):
  print "{}[*]{} Starting injection into binary...{}".format(Bcolors.YELLOW, Bcolors.BOLD, Bcolors.ENDC)
  print

  addr = parse_int(straddr)
  payload = open(payload_name, "rb").read()
  original = open(file_name, "rb").read()

  modified_data = original[:addr] + payload + original[addr+len(payload):]

  modified_file = open("{}.mod".format(file_name),"w") 
   
  modified_file.write(modified_data)
  modified_file.close() 

  print "{}[*]{} Injection finished.{}".format(Bcolors.YELLOW, Bcolors.BOLD, Bcolors.ENDC)
