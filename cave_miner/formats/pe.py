# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Pe(KaitaiStruct):
    """
    .. seealso::
       Source - https://learn.microsoft.com/en-us/windows/win32/debug/pe-format
    """

    class PeFormat(Enum):
        rom_image = 263
        pe32 = 267
        pe32_plus = 523
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.mz = Pe.MzPlaceholder(self._io, self, self._root)

    class CertificateEntry(KaitaiStruct):
        """
        .. seealso::
           Source - https://learn.microsoft.com/en-us/windows/win32/debug/pe-format#the-attribute-certificate-table-image-only
        """

        class CertificateRevision(Enum):
            revision_1_0 = 256
            revision_2_0 = 512

        class CertificateTypeEnum(Enum):
            x509 = 1
            pkcs_signed_data = 2
            reserved_1 = 3
            ts_stack_signed = 4
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = self._io.read_u4le()
            self.revision = KaitaiStream.resolve_enum(Pe.CertificateEntry.CertificateRevision, self._io.read_u2le())
            self.certificate_type = KaitaiStream.resolve_enum(Pe.CertificateEntry.CertificateTypeEnum, self._io.read_u2le())
            self.certificate_bytes = self._io.read_bytes((self.length - 8))


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
            windows_boot_application = 16
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self._parent.std.format == Pe.PeFormat.pe32:
                self.image_base_32 = self._io.read_u4le()

            if self._parent.std.format == Pe.PeFormat.pe32_plus:
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
            self.subsystem = KaitaiStream.resolve_enum(Pe.OptionalHeaderWindows.SubsystemEnum, self._io.read_u2le())
            self.dll_characteristics = self._io.read_u2le()
            if self._parent.std.format == Pe.PeFormat.pe32:
                self.size_of_stack_reserve_32 = self._io.read_u4le()

            if self._parent.std.format == Pe.PeFormat.pe32_plus:
                self.size_of_stack_reserve_64 = self._io.read_u8le()

            if self._parent.std.format == Pe.PeFormat.pe32:
                self.size_of_stack_commit_32 = self._io.read_u4le()

            if self._parent.std.format == Pe.PeFormat.pe32_plus:
                self.size_of_stack_commit_64 = self._io.read_u8le()

            if self._parent.std.format == Pe.PeFormat.pe32:
                self.size_of_heap_reserve_32 = self._io.read_u4le()

            if self._parent.std.format == Pe.PeFormat.pe32_plus:
                self.size_of_heap_reserve_64 = self._io.read_u8le()

            if self._parent.std.format == Pe.PeFormat.pe32:
                self.size_of_heap_commit_32 = self._io.read_u4le()

            if self._parent.std.format == Pe.PeFormat.pe32_plus:
                self.size_of_heap_commit_64 = self._io.read_u8le()

            self.loader_flags = self._io.read_u4le()
            self.number_of_rva_and_sizes = self._io.read_u4le()


    class OptionalHeaderDataDirs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.export_table = Pe.DataDir(self._io, self, self._root)
            self.import_table = Pe.DataDir(self._io, self, self._root)
            self.resource_table = Pe.DataDir(self._io, self, self._root)
            self.exception_table = Pe.DataDir(self._io, self, self._root)
            self.certificate_table = Pe.DataDir(self._io, self, self._root)
            self.base_relocation_table = Pe.DataDir(self._io, self, self._root)
            self.debug = Pe.DataDir(self._io, self, self._root)
            self.architecture = Pe.DataDir(self._io, self, self._root)
            self.global_ptr = Pe.DataDir(self._io, self, self._root)
            self.tls_table = Pe.DataDir(self._io, self, self._root)
            self.load_config_table = Pe.DataDir(self._io, self, self._root)
            self.bound_import = Pe.DataDir(self._io, self, self._root)
            self.iat = Pe.DataDir(self._io, self, self._root)
            self.delay_import_descriptor = Pe.DataDir(self._io, self, self._root)
            self.clr_runtime_header = Pe.DataDir(self._io, self, self._root)


    class DataDir(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.virtual_address = self._io.read_u4le()
            self.size = self._io.read_u4le()


    class CoffSymbol(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_name_annoying = self._io.read_bytes(8)
            _io__raw_name_annoying = KaitaiStream(BytesIO(self._raw_name_annoying))
            self.name_annoying = Pe.Annoyingstring(_io__raw_name_annoying, self, self._root)
            self.value = self._io.read_u4le()
            self.section_number = self._io.read_u2le()
            self.type = self._io.read_u2le()
            self.storage_class = self._io.read_u1()
            self.number_of_aux_symbols = self._io.read_u1()

        @property
        def section(self):
            if hasattr(self, '_m_section'):
                return self._m_section

            self._m_section = self._root.pe.sections[(self.section_number - 1)]
            return getattr(self, '_m_section', None)

        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            _pos = self._io.pos()
            self._io.seek((self.section.pointer_to_raw_data + self.value))
            self._m_data = self._io.read_bytes(1)
            self._io.seek(_pos)
            return getattr(self, '_m_data', None)


    class PeHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pe_signature = self._io.read_bytes(4)
            if not self.pe_signature == b"\x50\x45\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x50\x45\x00\x00", self.pe_signature, self._io, u"/types/pe_header/seq/0")
            self.coff_hdr = Pe.CoffHeader(self._io, self, self._root)
            self._raw_optional_hdr = self._io.read_bytes(self.coff_hdr.size_of_optional_header)
            _io__raw_optional_hdr = KaitaiStream(BytesIO(self._raw_optional_hdr))
            self.optional_hdr = Pe.OptionalHeader(_io__raw_optional_hdr, self, self._root)
            self.sections = []
            for i in range(self.coff_hdr.number_of_sections):
                self.sections.append(Pe.Section(self._io, self, self._root))


        @property
        def certificate_table(self):
            if hasattr(self, '_m_certificate_table'):
                return self._m_certificate_table

            if self.optional_hdr.data_dirs.certificate_table.virtual_address != 0:
                _pos = self._io.pos()
                self._io.seek(self.optional_hdr.data_dirs.certificate_table.virtual_address)
                self._raw__m_certificate_table = self._io.read_bytes(self.optional_hdr.data_dirs.certificate_table.size)
                _io__raw__m_certificate_table = KaitaiStream(BytesIO(self._raw__m_certificate_table))
                self._m_certificate_table = Pe.CertificateTable(_io__raw__m_certificate_table, self, self._root)
                self._io.seek(_pos)

            return getattr(self, '_m_certificate_table', None)


    class OptionalHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.std = Pe.OptionalHeaderStd(self._io, self, self._root)
            self.windows = Pe.OptionalHeaderWindows(self._io, self, self._root)
            self.data_dirs = Pe.OptionalHeaderDataDirs(self._io, self, self._root)


    class Section(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
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
                return self._m_body

            _pos = self._io.pos()
            self._io.seek(self.pointer_to_raw_data)
            self._m_body = self._io.read_bytes(self.size_of_raw_data)
            self._io.seek(_pos)
            return getattr(self, '_m_body', None)


    class CertificateTable(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.items = []
            i = 0
            while not self._io.is_eof():
                self.items.append(Pe.CertificateEntry(self._io, self, self._root))
                i += 1



    class MzPlaceholder(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(2)
            if not self.magic == b"\x4D\x5A":
                raise kaitaistruct.ValidationNotEqualError(b"\x4D\x5A", self.magic, self._io, u"/types/mz_placeholder/seq/0")
            self.data1 = self._io.read_bytes(58)
            self.ofs_pe = self._io.read_u4le()


    class OptionalHeaderStd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.format = KaitaiStream.resolve_enum(Pe.PeFormat, self._io.read_u2le())
            self.major_linker_version = self._io.read_u1()
            self.minor_linker_version = self._io.read_u1()
            self.size_of_code = self._io.read_u4le()
            self.size_of_initialized_data = self._io.read_u4le()
            self.size_of_uninitialized_data = self._io.read_u4le()
            self.address_of_entry_point = self._io.read_u4le()
            self.base_of_code = self._io.read_u4le()
            if self.format == Pe.PeFormat.pe32:
                self.base_of_data = self._io.read_u4le()



    class CoffHeader(KaitaiStruct):
        """
        .. seealso::
           3.3. COFF File Header (Object and Image)
        """

        class MachineType(Enum):
            unknown = 0
            i386 = 332
            r4000 = 358
            wce_mips_v2 = 361
            alpha = 388
            sh3 = 418
            sh3_dsp = 419
            sh4 = 422
            sh5 = 424
            arm = 448
            thumb = 450
            arm_nt = 452
            am33 = 467
            powerpc = 496
            powerpc_fp = 497
            ia64 = 512
            mips16 = 614
            alpha64_or_axp64 = 644
            mips_fpu = 870
            mips16_fpu = 1126
            ebc = 3772
            riscv32 = 20530
            riscv64 = 20580
            riscv128 = 20776
            loongarch32 = 25138
            loongarch64 = 25188
            amd64 = 34404
            m32r = 36929
            arm64 = 43620
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.machine = KaitaiStream.resolve_enum(Pe.CoffHeader.MachineType, self._io.read_u2le())
            self.number_of_sections = self._io.read_u2le()
            self.time_date_stamp = self._io.read_u4le()
            self.pointer_to_symbol_table = self._io.read_u4le()
            self.number_of_symbols = self._io.read_u4le()
            self.size_of_optional_header = self._io.read_u2le()
            self.characteristics = self._io.read_u2le()

        @property
        def symbol_table_size(self):
            if hasattr(self, '_m_symbol_table_size'):
                return self._m_symbol_table_size

            self._m_symbol_table_size = (self.number_of_symbols * 18)
            return getattr(self, '_m_symbol_table_size', None)

        @property
        def symbol_name_table_offset(self):
            if hasattr(self, '_m_symbol_name_table_offset'):
                return self._m_symbol_name_table_offset

            self._m_symbol_name_table_offset = (self.pointer_to_symbol_table + self.symbol_table_size)
            return getattr(self, '_m_symbol_name_table_offset', None)

        @property
        def symbol_name_table_size(self):
            if hasattr(self, '_m_symbol_name_table_size'):
                return self._m_symbol_name_table_size

            _pos = self._io.pos()
            self._io.seek(self.symbol_name_table_offset)
            self._m_symbol_name_table_size = self._io.read_u4le()
            self._io.seek(_pos)
            return getattr(self, '_m_symbol_name_table_size', None)

        @property
        def symbol_table(self):
            if hasattr(self, '_m_symbol_table'):
                return self._m_symbol_table

            _pos = self._io.pos()
            self._io.seek(self.pointer_to_symbol_table)
            self._m_symbol_table = []
            for i in range(self.number_of_symbols):
                self._m_symbol_table.append(Pe.CoffSymbol(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_symbol_table', None)


    class Annoyingstring(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

        @property
        def name_from_offset(self):
            if hasattr(self, '_m_name_from_offset'):
                return self._m_name_from_offset

            if self.name_zeroes == 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(((self._parent._parent.symbol_name_table_offset + self.name_offset) if self.name_zeroes == 0 else 0))
                self._m_name_from_offset = (io.read_bytes_term(0, False, True, False)).decode(u"ascii")
                io.seek(_pos)

            return getattr(self, '_m_name_from_offset', None)

        @property
        def name_offset(self):
            if hasattr(self, '_m_name_offset'):
                return self._m_name_offset

            _pos = self._io.pos()
            self._io.seek(4)
            self._m_name_offset = self._io.read_u4le()
            self._io.seek(_pos)
            return getattr(self, '_m_name_offset', None)

        @property
        def name(self):
            if hasattr(self, '_m_name'):
                return self._m_name

            self._m_name = (self.name_from_offset if self.name_zeroes == 0 else self.name_from_short)
            return getattr(self, '_m_name', None)

        @property
        def name_zeroes(self):
            if hasattr(self, '_m_name_zeroes'):
                return self._m_name_zeroes

            _pos = self._io.pos()
            self._io.seek(0)
            self._m_name_zeroes = self._io.read_u4le()
            self._io.seek(_pos)
            return getattr(self, '_m_name_zeroes', None)

        @property
        def name_from_short(self):
            if hasattr(self, '_m_name_from_short'):
                return self._m_name_from_short

            if self.name_zeroes != 0:
                _pos = self._io.pos()
                self._io.seek(0)
                self._m_name_from_short = (self._io.read_bytes_term(0, False, True, False)).decode(u"ascii")
                self._io.seek(_pos)

            return getattr(self, '_m_name_from_short', None)


    @property
    def pe(self):
        if hasattr(self, '_m_pe'):
            return self._m_pe

        _pos = self._io.pos()
        self._io.seek(self.mz.ofs_pe)
        self._m_pe = Pe.PeHeader(self._io, self, self._root)
        self._io.seek(_pos)
        return getattr(self, '_m_pe', None)


