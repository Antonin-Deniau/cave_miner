# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import struct


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Elf(KaitaiStruct):

    class Endian(Enum):
        le = 1
        be = 2

    class ShType(Enum):
        null_type = 0
        progbits = 1
        symtab = 2
        strtab = 3
        rela = 4
        hash = 5
        dynamic = 6
        note = 7
        nobits = 8
        rel = 9
        shlib = 10
        dynsym = 11
        init_array = 14
        fini_array = 15
        preinit_array = 16
        group = 17
        symtab_shndx = 18
        sunw_capchain = 1879048175
        sunw_capinfo = 1879048176
        sunw_symsort = 1879048177
        sunw_tlssort = 1879048178
        sunw_ldynsym = 1879048179
        sunw_dof = 1879048180
        sunw_cap = 1879048181
        sunw_signature = 1879048182
        sunw_annotate = 1879048183
        sunw_debugstr = 1879048184
        sunw_debug = 1879048185
        sunw_move = 1879048186
        sunw_comdat = 1879048187
        sunw_syminfo = 1879048188
        sunw_verdef = 1879048189
        sunw_verneed = 1879048190
        sunw_versym = 1879048191
        sparc_gotdata = 1879048192
        amd64_unwind = 1879048193

    class OsAbi(Enum):
        system_v = 0
        hp_ux = 1
        netbsd = 2
        gnu = 3
        solaris = 6
        aix = 7
        irix = 8
        freebsd = 9
        tru64 = 10
        modesto = 11
        openbsd = 12
        openvms = 13
        nsk = 14
        aros = 15
        fenixos = 16
        cloudabi = 17
        openvos = 18

    class Machine(Enum):
        not_set = 0
        sparc = 2
        x86 = 3
        mips = 8
        powerpc = 20
        arm = 40
        superh = 42
        ia_64 = 50
        x86_64 = 62
        aarch64 = 183

    class Bits(Enum):
        b32 = 1
        b64 = 2

    class PhType(Enum):
        null_type = 0
        load = 1
        dynamic = 2
        interp = 3
        note = 4
        shlib = 5
        phdr = 6
        tls = 7
        gnu_eh_frame = 1685382480
        gnu_stack = 1685382481
        hios = 1879048191

    class ObjType(Enum):
        relocatable = 1
        executable = 2
        shared = 3
        core = 4
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.ensure_fixed_contents(struct.pack('4b', 127, 69, 76, 70))
        self.bits = self._root.Bits(self._io.read_u1())
        self.endian = self._root.Endian(self._io.read_u1())
        self.ei_version = self._io.read_u1()
        self.abi = self._root.OsAbi(self._io.read_u1())
        self.abi_version = self._io.read_u1()
        self.pad = self._io.read_bytes(7)
        self.header = self._root.EndianElf(self._io, self, self._root)

    class EndianElf(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            _on = self._root.endian
            if _on == self._root.Endian.le:
                self._is_le = True
            elif _on == self._root.Endian.be:
                self._is_le = False

            if self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()
            else:
                raise Exception("Unable to decide endianness")

        def _read_le(self):
            self.e_type = self._root.ObjType(self._io.read_u2le())
            self.machine = self._root.Machine(self._io.read_u2le())
            self.e_version = self._io.read_u4le()
            _on = self._root.bits
            if _on == self._root.Bits.b32:
                self.entry_point = self._io.read_u4le()
            elif _on == self._root.Bits.b64:
                self.entry_point = self._io.read_u8le()
            _on = self._root.bits
            if _on == self._root.Bits.b32:
                self.program_header_offset = self._io.read_u4le()
            elif _on == self._root.Bits.b64:
                self.program_header_offset = self._io.read_u8le()
            _on = self._root.bits
            if _on == self._root.Bits.b32:
                self.section_header_offset = self._io.read_u4le()
            elif _on == self._root.Bits.b64:
                self.section_header_offset = self._io.read_u8le()
            self.flags = self._io.read_bytes(4)
            self.e_ehsize = self._io.read_u2le()
            self.program_header_entry_size = self._io.read_u2le()
            self.qty_program_header = self._io.read_u2le()
            self.section_header_entry_size = self._io.read_u2le()
            self.qty_section_header = self._io.read_u2le()
            self.section_names_idx = self._io.read_u2le()

        def _read_be(self):
            self.e_type = self._root.ObjType(self._io.read_u2be())
            self.machine = self._root.Machine(self._io.read_u2be())
            self.e_version = self._io.read_u4be()
            _on = self._root.bits
            if _on == self._root.Bits.b32:
                self.entry_point = self._io.read_u4be()
            elif _on == self._root.Bits.b64:
                self.entry_point = self._io.read_u8be()
            _on = self._root.bits
            if _on == self._root.Bits.b32:
                self.program_header_offset = self._io.read_u4be()
            elif _on == self._root.Bits.b64:
                self.program_header_offset = self._io.read_u8be()
            _on = self._root.bits
            if _on == self._root.Bits.b32:
                self.section_header_offset = self._io.read_u4be()
            elif _on == self._root.Bits.b64:
                self.section_header_offset = self._io.read_u8be()
            self.flags = self._io.read_bytes(4)
            self.e_ehsize = self._io.read_u2be()
            self.program_header_entry_size = self._io.read_u2be()
            self.qty_program_header = self._io.read_u2be()
            self.section_header_entry_size = self._io.read_u2be()
            self.qty_section_header = self._io.read_u2be()
            self.section_names_idx = self._io.read_u2be()

        class ProgramHeader(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le

                if self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()
                else:
                    raise Exception("Unable to decide endianness")

            def _read_le(self):
                self.type = self._root.PhType(self._io.read_u4le())
                if self._root.bits == self._root.Bits.b64:
                    self.flags64 = self._io.read_u4le()

                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.offset = self._io.read_u4le()
                elif _on == self._root.Bits.b64:
                    self.offset = self._io.read_u8le()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.vaddr = self._io.read_u4le()
                elif _on == self._root.Bits.b64:
                    self.vaddr = self._io.read_u8le()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.paddr = self._io.read_u4le()
                elif _on == self._root.Bits.b64:
                    self.paddr = self._io.read_u8le()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.filesz = self._io.read_u4le()
                elif _on == self._root.Bits.b64:
                    self.filesz = self._io.read_u8le()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.memsz = self._io.read_u4le()
                elif _on == self._root.Bits.b64:
                    self.memsz = self._io.read_u8le()
                if self._root.bits == self._root.Bits.b32:
                    self.flags32 = self._io.read_u4le()

                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.align = self._io.read_u4le()
                elif _on == self._root.Bits.b64:
                    self.align = self._io.read_u8le()

            def _read_be(self):
                self.type = self._root.PhType(self._io.read_u4be())
                if self._root.bits == self._root.Bits.b64:
                    self.flags64 = self._io.read_u4be()

                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.offset = self._io.read_u4be()
                elif _on == self._root.Bits.b64:
                    self.offset = self._io.read_u8be()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.vaddr = self._io.read_u4be()
                elif _on == self._root.Bits.b64:
                    self.vaddr = self._io.read_u8be()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.paddr = self._io.read_u4be()
                elif _on == self._root.Bits.b64:
                    self.paddr = self._io.read_u8be()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.filesz = self._io.read_u4be()
                elif _on == self._root.Bits.b64:
                    self.filesz = self._io.read_u8be()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.memsz = self._io.read_u4be()
                elif _on == self._root.Bits.b64:
                    self.memsz = self._io.read_u8be()
                if self._root.bits == self._root.Bits.b32:
                    self.flags32 = self._io.read_u4be()

                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.align = self._io.read_u4be()
                elif _on == self._root.Bits.b64:
                    self.align = self._io.read_u8be()


        class SectionHeader(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le

                if self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()
                else:
                    raise Exception("Unable to decide endianness")

            def _read_le(self):
                self.name_offset = self._io.read_u4le()
                self.type = self._root.ShType(self._io.read_u4le())
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.flags = self._io.read_u4le()
                elif _on == self._root.Bits.b64:
                    self.flags = self._io.read_u8le()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.addr = self._io.read_u4le()
                elif _on == self._root.Bits.b64:
                    self.addr = self._io.read_u8le()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.offset = self._io.read_u4le()
                elif _on == self._root.Bits.b64:
                    self.offset = self._io.read_u8le()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.size = self._io.read_u4le()
                elif _on == self._root.Bits.b64:
                    self.size = self._io.read_u8le()
                self.linked_section_idx = self._io.read_u4le()
                self.info = self._io.read_bytes(4)
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.align = self._io.read_u4le()
                elif _on == self._root.Bits.b64:
                    self.align = self._io.read_u8le()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.entry_size = self._io.read_u4le()
                elif _on == self._root.Bits.b64:
                    self.entry_size = self._io.read_u8le()

            def _read_be(self):
                self.name_offset = self._io.read_u4be()
                self.type = self._root.ShType(self._io.read_u4be())
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.flags = self._io.read_u4be()
                elif _on == self._root.Bits.b64:
                    self.flags = self._io.read_u8be()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.addr = self._io.read_u4be()
                elif _on == self._root.Bits.b64:
                    self.addr = self._io.read_u8be()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.offset = self._io.read_u4be()
                elif _on == self._root.Bits.b64:
                    self.offset = self._io.read_u8be()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.size = self._io.read_u4be()
                elif _on == self._root.Bits.b64:
                    self.size = self._io.read_u8be()
                self.linked_section_idx = self._io.read_u4be()
                self.info = self._io.read_bytes(4)
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.align = self._io.read_u4be()
                elif _on == self._root.Bits.b64:
                    self.align = self._io.read_u8be()
                _on = self._root.bits
                if _on == self._root.Bits.b32:
                    self.entry_size = self._io.read_u4be()
                elif _on == self._root.Bits.b64:
                    self.entry_size = self._io.read_u8be()

            @property
            def body(self):
                if hasattr(self, '_m_body'):
                    return self._m_body if hasattr(self, '_m_body') else None

                io = self._root._io
                _pos = io.pos()
                io.seek(self.offset)
                if self._is_le:
                    self._m_body = io.read_bytes(self.size)
                else:
                    self._m_body = io.read_bytes(self.size)
                io.seek(_pos)
                return self._m_body if hasattr(self, '_m_body') else None

            @property
            def name(self):
                if hasattr(self, '_m_name'):
                    return self._m_name if hasattr(self, '_m_name') else None

                io = self._root.header.strings._io
                _pos = io.pos()
                io.seek(self.name_offset)
                if self._is_le:
                    self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
                else:
                    self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
                io.seek(_pos)
                return self._m_name if hasattr(self, '_m_name') else None


        class StringsStruct(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le

                if self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()
                else:
                    raise Exception("Unable to decide endianness")

            def _read_le(self):
                self.entries = []
                while not self._io.is_eof():
                    self.entries.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII"))


            def _read_be(self):
                self.entries = []
                while not self._io.is_eof():
                    self.entries.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII"))



        @property
        def program_headers(self):
            if hasattr(self, '_m_program_headers'):
                return self._m_program_headers if hasattr(self, '_m_program_headers') else None

            _pos = self._io.pos()
            self._io.seek(self.program_header_offset)
            if self._is_le:
                self._raw__m_program_headers = [None] * (self.qty_program_header)
                self._m_program_headers = [None] * (self.qty_program_header)
                for i in range(self.qty_program_header):
                    self._raw__m_program_headers[i] = self._io.read_bytes(self.program_header_entry_size)
                    io = KaitaiStream(BytesIO(self._raw__m_program_headers[i]))
                    self._m_program_headers[i] = self._root.EndianElf.ProgramHeader(io, self, self._root, self._is_le)

            else:
                self._raw__m_program_headers = [None] * (self.qty_program_header)
                self._m_program_headers = [None] * (self.qty_program_header)
                for i in range(self.qty_program_header):
                    self._raw__m_program_headers[i] = self._io.read_bytes(self.program_header_entry_size)
                    io = KaitaiStream(BytesIO(self._raw__m_program_headers[i]))
                    self._m_program_headers[i] = self._root.EndianElf.ProgramHeader(io, self, self._root, self._is_le)

            self._io.seek(_pos)
            return self._m_program_headers if hasattr(self, '_m_program_headers') else None

        @property
        def section_headers(self):
            if hasattr(self, '_m_section_headers'):
                return self._m_section_headers if hasattr(self, '_m_section_headers') else None

            _pos = self._io.pos()
            self._io.seek(self.section_header_offset)
            if self._is_le:
                self._raw__m_section_headers = [None] * (self.qty_section_header)
                self._m_section_headers = [None] * (self.qty_section_header)
                for i in range(self.qty_section_header):
                    self._raw__m_section_headers[i] = self._io.read_bytes(self.section_header_entry_size)
                    io = KaitaiStream(BytesIO(self._raw__m_section_headers[i]))
                    self._m_section_headers[i] = self._root.EndianElf.SectionHeader(io, self, self._root, self._is_le)

            else:
                self._raw__m_section_headers = [None] * (self.qty_section_header)
                self._m_section_headers = [None] * (self.qty_section_header)
                for i in range(self.qty_section_header):
                    self._raw__m_section_headers[i] = self._io.read_bytes(self.section_header_entry_size)
                    io = KaitaiStream(BytesIO(self._raw__m_section_headers[i]))
                    self._m_section_headers[i] = self._root.EndianElf.SectionHeader(io, self, self._root, self._is_le)

            self._io.seek(_pos)
            return self._m_section_headers if hasattr(self, '_m_section_headers') else None

        @property
        def strings(self):
            if hasattr(self, '_m_strings'):
                return self._m_strings if hasattr(self, '_m_strings') else None

            _pos = self._io.pos()
            self._io.seek(self.section_headers[self.section_names_idx].offset)
            if self._is_le:
                self._raw__m_strings = self._io.read_bytes(self.section_headers[self.section_names_idx].size)
                io = KaitaiStream(BytesIO(self._raw__m_strings))
                self._m_strings = self._root.EndianElf.StringsStruct(io, self, self._root, self._is_le)
            else:
                self._raw__m_strings = self._io.read_bytes(self.section_headers[self.section_names_idx].size)
                io = KaitaiStream(BytesIO(self._raw__m_strings))
                self._m_strings = self._root.EndianElf.StringsStruct(io, self, self._root, self._is_le)
            self._io.seek(_pos)
            return self._m_strings if hasattr(self, '_m_strings') else None



