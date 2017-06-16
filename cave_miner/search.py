from utils import *
from formats import * 
from struct import *

def search_cave(name, body, cave_size, file_offset):
  null_count = 0

  for offset in xrange(len(body)):
    byte = body[offset]

    if byte == "\x00":
      null_count += 1
    else:
      if null_count >= cave_size:
        print "{}[*]{} New cave detected !{}".format(Bcolors.YELLOW, Bcolors.BOLD, Bcolors.ENDC)
        print "  section_name: {}".format(name)
        print "  cave_begin:   0x{:08x}".format(file_offset + offset - null_count)
        print "  cave_end:     0x{:08x}".format(file_offset + offset)
        print "  cave_size:    0x{:08x}".format(null_count)
        print

      null_count = 0

def search_pe(filename, cavesize):
  g = MicrosoftPe.from_file(filename)

  for section in g.sections:
    section_offset = section.pointer_to_raw_data
    search_cave(section.name, section.body, cavesize, section_offset)

def search_macho(filename, cavesize):
  g = MachO.from_file(filename)

  for command in g.load_commands:
    if command.type == MachO.LoadCommandType.segment_64:
      for section in command.body.sections:
        if isinstance(section.data, str):
          search_cave("{}.{}".format(section.seg_name, section.sect_name), section.data, cavesize, section.offset)

def search_elf(filename, cavesize):
  g = Elf.from_file(filename)

  for section in g.header.section_headers:
    search_cave(section.name, section.body, cavesize, section.offset)

def detect_type(filename, cavesize):
  data = open(filename, "rb").read()

  mz    = "MZ"
  elf   = "\x7FELF"
  macho = pack("I", 0xfeedfacf)

  if   data[0x0:0x2] == mz:    search_pe(filename, cavesize)
  elif data[0x0:0x4] == elf:   search_elf(filename, cavesize)
  elif data[0x0:0x4] == macho: search_macho(filename, cavesize)

def search(filename, cavesize):
  print "{}[*]{} Starting cave mining process...{}".format(Bcolors.YELLOW, Bcolors.BOLD, Bcolors.ENDC)
  print

  detect_type(filename, parse_int(cavesize))

  print "{}[*]{} Mining finished.{}".format(Bcolors.YELLOW, Bcolors.BOLD, Bcolors.ENDC)
