from utils import *
from formats import * 
from struct import *

def search_cave(name, body, cave_size, file_offset, vaddr, infos, _bytes):
  null_count = 0
  size = len(body)

  for offset in xrange(size):
    byte = body[offset]
    check=False

    if byte in _bytes:
      null_count += 1
    else:
      check=True

    if offset == size - 1:
        check=True
        offset += 1

    if check:
      if null_count >= cave_size:
        print(color("{yellow}[*]{bold} New cave detected !{endc}"))
        print "  section_name: {}".format(name)
        print "  cave_begin:   0x{:08x}".format(file_offset + offset - null_count)
        print "  cave_end:     0x{:08x}".format(file_offset + offset)
        print "  cave_size:    0x{:08x} ({} bytes)".format(null_count,null_count)
        print "  vaddress:     0x{:08x}".format(vaddr + offset - null_count)
        print "  infos:        {}".format(infos)
        print
      null_count = 0


def parse_macho_flags(byte):
  ret = []

  if 0x1 & byte == 0x1: ret.append("READ")
  if 0x2 & byte == 0x2: ret.append("WRITE")
  if 0x4 & byte == 0x4: ret.append("EXECUTE")

  return ", ".join(ret)

def parse_sh_flags(byte):
  ret = []

  if 0x0000001 & byte == 0x0000001: ret.append("SHF_WRITE")
  if 0x0000002 & byte == 0x0000002: ret.append("SHF_ALLOC")
  if 0x0000004 & byte == 0x0000004: ret.append("SHF_EXECINSTR")
  if 0x0000010 & byte == 0x0000020: ret.append("SHF_MERGE")
  if 0x0000020 & byte == 0x0000020: ret.append("SHF_STRINGS")
  if 0x0000040 & byte == 0x0000040: ret.append("SHF_INFO_LINK")
  if 0x0000080 & byte == 0x0000080: ret.append("SHF_LINK_ORDER")
  if 0x0000100 & byte == 0x0000100: ret.append("SHF_OS_NONCONFORMING")
  if 0x0000200 & byte == 0x0000200: ret.append("SHF_GROUP")
  if 0x0000400 & byte == 0x0000400: ret.append("SHF_TLS")
  if 0xff00000 & byte == 0xff00000: ret.append("SHF_MASKOS")

  return ", ".join(ret)

def parse_pe_flags(byte):
  ret = []

  if 0x10000000 & byte == 0x10000000: ret.append("Shareable")
  if 0x20000000 & byte == 0x20000000: ret.append("Executable")
  if 0x40000000 & byte == 0x40000000: ret.append("Readable")
  if 0x80000000 & byte == 0x80000000: ret.append("Writeable")
  if 0x01000000 & byte == 0x01000000: ret.append("Contain extended relocation")
  if 0x02000000 & byte == 0x02000000: ret.append("Discardable as needed")
  if 0x04000000 & byte == 0x04000000: ret.append("Cant be cached")
  if 0x00001000 & byte == 0x00001000: ret.append("Contain COMDAT data")
  if 0x00000200 & byte == 0x00000200: ret.append("Contais comments or other infos")
  if 0x00000800 & byte == 0x00000800: ret.append("Wont become part of the image")
  if 0x00000020 & byte == 0x00000020: ret.append("Contain executable code")
  if 0x00000040 & byte == 0x00000040: ret.append("Contain initialized data")
  if 0x00000080 & byte == 0x00000080: ret.append("Contain uninitialized data")
  if 0x00000008 & byte == 0x00000008: ret.append("Shouldnt be padded to next boundary")

  return ", ".join(ret)

def search_pe(filename, cavesize, _bytes):
  g = MicrosoftPe.from_file(filename)

  if g.optional_hdr.std.format == MicrosoftPe.PeFormat.pe32:
    base_addr = g.optional_hdr.windows.image_base_32
  else:
    base_addr = g.optional_hdr.windows.image_base_64

  for section in g.sections:
    section_offset = section.pointer_to_raw_data
    infos = parse_pe_flags(section.characteristics)
    vaddr = section.virtual_address + base_addr

    '''
    Calculate difference between VirtualSize and RawSize
    If the RawSize is greater than VirtualSize the system will fill the difference with Zeros, so this space is an code cave
    '''
    body = section.body
    if section.size_of_raw_data > section.virtual_size:
        body += "\x00" * (section.size_of_raw_data - section.virtual_size) 
    search_cave(section.name, body, cavesize, section_offset, vaddr, infos, _bytes)

def search_macho(filename, cavesize, _bytes):
  g = MachO.from_file(filename)

  for command in g.load_commands:
    if command.type == MachO.LoadCommandType.segment_64:
      for section in command.body.sections:
        if isinstance(section.data, str):
          infos = "init: [{}], max: [{}]".format(parse_macho_flags(command.body.initprot), parse_macho_flags(command.body.maxprot))
          search_cave("{}.{}".format(section.seg_name, section.sect_name), section.data, cavesize, section.offset, section.addr, infos, _bytes)

def search_elf(filename, cavesize, _bytes):
  g = Elf.from_file(filename)

  for section in g.header.section_headers:
    infos = parse_sh_flags(section.flags)
    search_cave(section.name, section.body, cavesize, section.offset, section.addr, infos, _bytes)

def detect_type(filename, cavesize, _bytes):
  data = open(filename, "rb").read()

  mz    = "MZ"
  elf   = "\x7FELF"
  macho = pack("I", 0xfeedfacf)

  if   data[0x0:0x2] == mz:    search_pe(filename, cavesize, _bytes)
  elif data[0x0:0x4] == elf:   search_elf(filename, cavesize, _bytes)
  elif data[0x0:0x4] == macho: search_macho(filename, cavesize, _bytes)

def search(filename, cavesize, bytes_arg):
  print(color("{yellow}[*]{bold} Starting cave mining process...{endc}"))
  print(color("   {{bold}} Searching for bytes: {}...{{endc}}".format(", ".join(bytes_arg))))
  print

  _bytes = map(lambda e: chr(int(e, 16)), bytes_arg)

  detect_type(filename, parse_int(cavesize), _bytes)

  print(color("{yellow}[*]{bold} Mining finished.{endc}"))
