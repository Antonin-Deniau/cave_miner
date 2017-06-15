# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import array
import struct
import zlib
from enum import Enum
from pkg_resources import parse_version

from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class MicrosoftPe(KaitaiStruct):

    class PeFormat(Enum):
        rom_image = 263
        pe32 = 267
        pe32_plus = 523
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.mz1 = self._root.MzPlaceholder(self._io, self, self._root)
        self.mz2 = self._io.read_bytes((self.mz1.header_size - 64))
        self.pe_signature = self._io.ensure_fixed_contents(struct.pack('4b', 80, 69, 0, 0))
        self.coff_hdr = self._root.CoffHeader(self._io, self, self._root)
        self._raw_optional_hdr = self._io.read_bytes(self.coff_hdr.size_of_optional_header)
        io = KaitaiStream(BytesIO(self._raw_optional_hdr))
        self.optional_hdr = self._root.OptionalHeader(io, self, self._root)
        self.sections = [None] * (self.coff_hdr.number_of_sections)
        for i in range(self.coff_hdr.number_of_sections):
            self.sections[i] = self._root.Section(self._io, self, self._root)


    class OptionalHeaderWindows(KaitaiStruct):

        class SubsystemEnum(Enum):
            unknown = 0
            native = 1
            windows_gui = 2
            windows_cui = 3
            posix_cui = 7
            windows_ce_gui = 9
            efi_application = 10
            efi_boot_service_driver = 11
            efi_runtime_driver = 12
            efi_rom = 13
            xbox = 14
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            if self._parent.std.format == self._root.PeFormat.pe32:
                self.image_base_32 = self._io.read_u4le()

            if self._parent.std.format == self._root.PeFormat.pe32_plus:
                self.image_base_64 = self._io.read_u8le()

            self.section_alignment = self._io.read_u4le()
            self.file_alignment = self._io.read_u4le()
            self.major_operating_system_version = self._io.read_u2le()
            self.minor_operating_system_version = self._io.read_u2le()
            self.major_image_version = self._io.read_u2le()
            self.minor_image_version = self._io.read_u2le()
            self.major_subsystem_version = self._io.read_u2le()
            self.minor_subsystem_version = self._io.read_u2le()
            self.win32_version_value = self._io.read_u4le()
            self.size_of_image = self._io.read_u4le()
            self.size_of_headers = self._io.read_u4le()
            self.check_sum = self._io.read_u4le()
            self.subsystem = self._root.OptionalHeaderWindows.SubsystemEnum(self._io.read_u2le())
            self.dll_characteristics = self._io.read_u2le()
            if self._parent.std.format == self._root.PeFormat.pe32:
                self.size_of_stack_reserve_32 = self._io.read_u4le()

            if self._parent.std.format == self._root.PeFormat.pe32_plus:
                self.size_of_stack_reserve_64 = self._io.read_u8le()

            if self._parent.std.format == self._root.PeFormat.pe32:
                self.size_of_stack_commit_32 = self._io.read_u4le()

            if self._parent.std.format == self._root.PeFormat.pe32_plus:
                self.size_of_stack_commit_64 = self._io.read_u8le()

            if self._parent.std.format == self._root.PeFormat.pe32:
                self.size_of_heap_reserve_32 = self._io.read_u4le()

            if self._parent.std.format == self._root.PeFormat.pe32_plus:
                self.size_of_heap_reserve_64 = self._io.read_u8le()

            if self._parent.std.format == self._root.PeFormat.pe32:
                self.size_of_heap_commit_32 = self._io.read_u4le()

            if self._parent.std.format == self._root.PeFormat.pe32_plus:
                self.size_of_heap_commit_64 = self._io.read_u8le()

            self.loader_flags = self._io.read_u4le()
            self.number_of_rva_and_sizes = self._io.read_u4le()


    class OptionalHeaderDataDirs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.export_table = self._root.DataDir(self._io, self, self._root)
            self.import_table = self._root.DataDir(self._io, self, self._root)
            self.resource_table = self._root.DataDir(self._io, self, self._root)
            self.exception_table = self._root.DataDir(self._io, self, self._root)
            self.certificate_table = self._root.DataDir(self._io, self, self._root)
            self.base_relocation_table = self._root.DataDir(self._io, self, self._root)
            self.debug = self._root.DataDir(self._io, self, self._root)
            self.architecture = self._root.DataDir(self._io, self, self._root)
            self.global_ptr = self._root.DataDir(self._io, self, self._root)
            self.tls_table = self._root.DataDir(self._io, self, self._root)
            self.load_config_table = self._root.DataDir(self._io, self, self._root)
            self.bound_import = self._root.DataDir(self._io, self, self._root)
            self.iat = self._root.DataDir(self._io, self, self._root)
            self.delay_import_descriptor = self._root.DataDir(self._io, self, self._root)
            self.clr_runtime_header = self._root.DataDir(self._io, self, self._root)


    class DataDir(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.virtual_address = self._io.read_u4le()
            self.size = self._io.read_u4le()


    class OptionalHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.std = self._root.OptionalHeaderStd(self._io, self, self._root)
            self.windows = self._root.OptionalHeaderWindows(self._io, self, self._root)
            self.data_dirs = self._root.OptionalHeaderDataDirs(self._io, self, self._root)


    class Section(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.name = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 0)).decode(u"UTF-8")
            self.virtual_size = self._io.read_u4le()
            self.virtual_address = self._io.read_u4le()
            self.size_of_raw_data = self._io.read_u4le()
            self.pointer_to_raw_data = self._io.read_u4le()
            self.pointer_to_relocations = self._io.read_u4le()
            self.pointer_to_linenumbers = self._io.read_u4le()
            self.number_of_relocations = self._io.read_u2le()
            self.number_of_linenumbers = self._io.read_u2le()
            self.characteristics = self._io.read_u4le()

        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body if hasattr(self, '_m_body') else None

            _pos = self._io.pos()
            self._io.seek(self.pointer_to_raw_data)
            self._m_body = self._io.read_bytes(self.size_of_raw_data)
            self._io.seek(_pos)
            return self._m_body if hasattr(self, '_m_body') else None


    class MzPlaceholder(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.magic = self._io.ensure_fixed_contents(struct.pack('2b', 77, 90))
            self.data1 = self._io.read_bytes(58)
            self.header_size = self._io.read_u4le()


    class OptionalHeaderStd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.format = self._root.PeFormat(self._io.read_u2le())
            self.major_linker_version = self._io.read_u1()
            self.minor_linker_version = self._io.read_u1()
            self.size_of_code = self._io.read_u4le()
            self.size_of_initialized_data = self._io.read_u4le()
            self.size_of_uninitialized_data = self._io.read_u4le()
            self.address_of_entry_point = self._io.read_u4le()
            self.base_of_code = self._io.read_u4le()
            if self.format == self._root.PeFormat.pe32:
                self.base_of_data = self._io.read_u4le()



    class CoffHeader(KaitaiStruct):

        class MachineType(Enum):
            unknown = 0
            i386 = 332
            r4000 = 358
            wcemipsv2 = 361
            sh3 = 418
            sh3dsp = 419
            sh4 = 422
            sh5 = 424
            arm = 448
            thumb = 450
            armnt = 452
            am33 = 467
            powerpc = 496
            powerpcfp = 497
            ia64 = 512
            mips16 = 614
            mipsfpu = 870
            mipsfpu16 = 1126
            ebc = 3772
            riscv32 = 20530
            riscv64 = 20580
            riscv128 = 20776
            amd64 = 34404
            m32r = 36929
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.machine = self._root.CoffHeader.MachineType(self._io.read_u2le())
            self.number_of_sections = self._io.read_u2le()
            self.time_date_stamp = self._io.read_u4le()
            self.pointer_to_symbol_table = self._io.read_u4le()
            self.number_of_symbols = self._io.read_u4le()
            self.size_of_optional_header = self._io.read_u2le()
            self.characteristics = self._io.read_u2le()



