"""Mach-O format parser using lief library"""
import lief
from enum import IntEnum


class LoadCommandType(IntEnum):
    segment_64 = 0x19


class Section:
    def __init__(self, section):
        self._section = section
        self.seg_name = section.segment_name
        self.sect_name = section.name
        self.offset = section.offset
        self.addr = section.virtual_address
        self.data = bytes(section.content)


class SegmentBody:
    def __init__(self, segment):
        self._segment = segment
        self.sections = [Section(section) for section in segment.sections]
        self.initprot = segment.init_protection
        self.maxprot = segment.max_protection


class LoadCommand:
    def __init__(self, segment):
        self._segment = segment
        # Check if this is a 64-bit segment
        if hasattr(segment, 'sections'):
            self.type = LoadCommandType.segment_64
            self.body = SegmentBody(segment)
        else:
            self.type = None
            self.body = None


class MachO:
    LoadCommandType = LoadCommandType

    def __init__(self, binary):
        self.load_commands = [
            LoadCommand(segment)
            for segment in binary.segments
        ]

    @classmethod
    def from_file(cls, filename):
        binary = lief.parse(filename)
        if binary is None or binary.format != lief.EXE_FORMATS.MACHO:
            raise ValueError(f"File {filename} is not a valid Mach-O file")
        return cls(binary)
