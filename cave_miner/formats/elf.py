"""ELF format parser using lief library"""
import lief


class SectionHeader:
    def __init__(self, section):
        self._section = section
        self.name = section.name
        self.flags = section.flags
        self.addr = section.virtual_address
        self.ofs_body = section.offset
        self.body = bytes(section.content)


class Header:
    def __init__(self, binary):
        self.section_headers = [
            SectionHeader(section)
            for section in binary.sections
        ]


class Elf:
    def __init__(self, binary):
        self.header = Header(binary)

    @classmethod
    def from_file(cls, filename):
        binary = lief.parse(filename)
        if binary is None or binary.format != lief.EXE_FORMATS.ELF:
            raise ValueError(f"File {filename} is not a valid ELF file")
        return cls(binary)
