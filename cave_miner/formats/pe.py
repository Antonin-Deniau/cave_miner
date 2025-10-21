"""PE format parser using lief library"""
import lief
from enum import IntEnum


class PeFormat(IntEnum):
    pe32 = 0
    pe32_plus = 1


class Std:
    def __init__(self, binary):
        self.format = PeFormat.pe32 if binary.optional_header.magic == lief.PE.PE_TYPE.PE32 else PeFormat.pe32_plus


class Windows:
    def __init__(self, binary):
        self.image_base_32 = binary.optional_header.imagebase
        self.image_base_64 = binary.optional_header.imagebase


class OptionalHeader:
    def __init__(self, binary):
        self.std = Std(binary)
        self.windows = Windows(binary)


class Section:
    def __init__(self, section):
        self._section = section
        self.name = section.name
        self.pointer_to_raw_data = section.pointerto_raw_data
        self.characteristics = section.characteristics
        self.virtual_address = section.virtual_address
        self.size_of_raw_data = section.sizeof_raw_data
        self.virtual_size = section.virtual_size
        self.body = bytes(section.content)


class Pe:
    PeFormat = PeFormat

    def __init__(self, binary):
        self.optional_hdr = OptionalHeader(binary)
        self.sections = [Section(section) for section in binary.sections]

    @classmethod
    def from_file(cls, filename):
        binary = lief.parse(filename)
        if binary is None or binary.format != lief.EXE_FORMATS.PE:
            raise ValueError(f"File {filename} is not a valid PE file")
        return cls(binary)
