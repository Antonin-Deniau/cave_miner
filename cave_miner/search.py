from struct import pack

from .utils import color, parse_int
from .formats import MachO, Pe, Elf


def search_cave(name, body, cave_size, file_offset, vaddr, infos, _bytes):
    null_count = 0
    size = len(body)

    for offset in range(size):
        byte = body[offset]
        check = False

        if byte in _bytes:
            null_count += 1
        else:
            check = True

        if offset == size - 1:
            check = True
            offset += 1

        if check:
            if null_count >= cave_size:
                print(color("{yellow}[*]{bold} New cave detected !{endc}"))
                print("  section_name: {}".format(name))
                print(
                    "  cave_begin:   0x{:08x}".format(file_offset + offset - null_count)
                )
                print("  cave_end:     0x{:08x}".format(file_offset + offset))
                print(
                    "  cave_size:    0x{:08x} ({} bytes)".format(null_count, null_count)
                )
                print("  vaddress:     0x{:08x}".format(vaddr + offset - null_count))
                print("  infos:        {}".format(infos))
                print()
            null_count = 0


def parse_macho_flags(prot):
    ret = []

    if prot.read:
        ret.append("READ")
    if prot.write:
        ret.append("WRITE")
    if prot.execute:
        ret.append("EXECUTE")

    return ", ".join(ret)


def parse_sh_flags(byte):
    ret = []

    if 0x0000001 & byte == 0x0000001:
        ret.append("SHF_WRITE")
    if 0x0000002 & byte == 0x0000002:
        ret.append("SHF_ALLOC")
    if 0x0000004 & byte == 0x0000004:
        ret.append("SHF_EXECINSTR")
    if 0x0000010 & byte == 0x0000020:
        ret.append("SHF_MERGE")
    if 0x0000020 & byte == 0x0000020:
        ret.append("SHF_STRINGS")
    if 0x0000040 & byte == 0x0000040:
        ret.append("SHF_INFO_LINK")
    if 0x0000080 & byte == 0x0000080:
        ret.append("SHF_LINK_ORDER")
    if 0x0000100 & byte == 0x0000100:
        ret.append("SHF_OS_NONCONFORMING")
    if 0x0000200 & byte == 0x0000200:
        ret.append("SHF_GROUP")
    if 0x0000400 & byte == 0x0000400:
        ret.append("SHF_TLS")
    if 0xFF00000 & byte == 0xFF00000:
        ret.append("SHF_MASKOS")

    return ", ".join(ret)


def parse_pe_flags(byte):
    ret = []

    if 0x10000000 & byte == 0x10000000:
        ret.append("Shareable")
    if 0x20000000 & byte == 0x20000000:
        ret.append("Executable")
    if 0x40000000 & byte == 0x40000000:
        ret.append("Readable")
    if 0x80000000 & byte == 0x80000000:
        ret.append("Writeable")
    if 0x01000000 & byte == 0x01000000:
        ret.append("Contain extended relocation")
    if 0x02000000 & byte == 0x02000000:
        ret.append("Discardable as needed")
    if 0x04000000 & byte == 0x04000000:
        ret.append("Cant be cached")
    if 0x00001000 & byte == 0x00001000:
        ret.append("Contain COMDAT data")
    if 0x00000200 & byte == 0x00000200:
        ret.append("Contais comments or other infos")
    if 0x00000800 & byte == 0x00000800:
        ret.append("Wont become part of the image")
    if 0x00000020 & byte == 0x00000020:
        ret.append("Contain executable code")
    if 0x00000040 & byte == 0x00000040:
        ret.append("Contain initialized data")
    if 0x00000080 & byte == 0x00000080:
        ret.append("Contain uninitialized data")
    if 0x00000008 & byte == 0x00000008:
        ret.append("Shouldnt be padded to next boundary")

    return ", ".join(ret)


def search_pe(filename, cavesize, _bytes):
    g = Pe.from_file(filename)
    pe = g.pe

    if pe.optional_hdr.std.format == Pe.PeFormat.pe32:
        base_addr = pe.optional_hdr.windows.image_base_32
    else:
        base_addr = pe.optional_hdr.windows.image_base_64

    for section in pe.sections:
        section_offset = section.pointer_to_raw_data
        infos = parse_pe_flags(section.characteristics)
        vaddr = section.virtual_address + base_addr

        # section.body already holds the full size_of_raw_data bytes stored on
        # disk. When size_of_raw_data > virtual_size, the trailing slack is zero
        # padding present in the file, so it is included here and shows up as a
        # cave on its own.
        body = section.body
        search_cave(section.name, body, cavesize, section_offset, vaddr, infos, _bytes)


def search_macho(filename, cavesize, _bytes):
    g = MachO.from_file(filename)
    data = open(filename, "rb").read()

    for command in g.load_commands:
        if command.type == MachO.LoadCommandType.segment_64:
            infos = "init: [{}], max: [{}]".format(
                parse_macho_flags(command.body.initprot),
                parse_macho_flags(command.body.maxprot),
            )
            for section in command.body.sections:
                # zerofill sections (e.g. __bss) hold no bytes in the file
                if section.offset == 0 or section.size == 0:
                    continue

                body = data[section.offset : section.offset + section.size]
                search_cave(
                    "{}.{}".format(section.seg_name, section.sect_name),
                    body,
                    cavesize,
                    section.offset,
                    section.addr,
                    infos,
                    _bytes,
                )


def search_elf(filename, cavesize, _bytes):
    g = Elf.from_file(filename)
    data = open(filename, "rb").read()

    for section in g.header.section_headers:
        # nobits sections (e.g. .bss) occupy no space in the file
        if section.type == Elf.ShType.nobits:
            continue

        infos = parse_sh_flags(section.flags)
        body = data[section.ofs_body : section.ofs_body + section.len_body]

        search_cave(
            section.name,
            body,
            cavesize,
            section.ofs_body,
            section.addr,
            infos,
            _bytes,
        )


def detect_type(filename, cavesize, _bytes):
    data = open(filename, "rb").read()

    mz = "MZ".encode("ascii")
    elf = "\x7FELF".encode("ascii")
    macho = pack("I", 0xFEEDFACF)

    if data[0x0:0x2] == mz:
        search_pe(filename, cavesize, _bytes)
    elif data[0x0:0x4] == elf:
        search_elf(filename, cavesize, _bytes)
    elif data[0x0:0x4] == macho:
        search_macho(filename, cavesize, _bytes)
    else:
        raise Exception("Unable to detect filetype")


def search(filename, cavesize, bytes_arg):
    print(color("{yellow}[*]{bold} Starting cave mining process...{endc}"))
    print(
        color(
            "   {{bold}} Searching for bytes: {}...{{endc}}".format(
                ", ".join(bytes_arg)
            )
        )
    )
    print()

    _bytes = [int(e, 16) for e in bytes_arg]

    detect_type(filename, parse_int(cavesize), _bytes)

    print(color("{yellow}[*]{bold} Mining finished.{endc}"))
