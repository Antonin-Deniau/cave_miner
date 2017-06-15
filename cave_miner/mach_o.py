# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import array
import struct
import zlib
from enum import Enum
from pkg_resources import parse_version

from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class MachO(KaitaiStruct):

    class LoadCommandType(Enum):
        segment = 1
        symtab = 2
        symseg = 3
        thread = 4
        unix_thread = 5
        load_fvm_lib = 6
        id_fvm_lib = 7
        ident = 8
        fvm_file = 9
        prepage = 10
        dysymtab = 11
        load_dylib = 12
        id_dylib = 13
        load_dylinker = 14
        id_dylinker = 15
        prebound_dylib = 16
        routines = 17
        sub_framework = 18
        sub_umbrella = 19
        sub_client = 20
        sub_library = 21
        twolevel_hints = 22
        prebind_cksum = 23
        segment_64 = 25
        routines_64 = 26
        uuid = 27
        code_signature = 29
        segment_split_info = 30
        lazy_load_dylib = 32
        encryption_info = 33
        dyld_info = 34
        load_upward_dylib = 35
        version_min_macosx = 36
        version_min_iphoneos = 37
        function_starts = 38
        dyld_environment = 39
        main = 40
        data_in_code = 41
        source_version = 42
        dylib_code_sign_drs = 43
        encryption_info_64 = 44
        linker_option = 45
        linker_optimization_hint = 46
        version_min_tvos = 47
        version_min_watchos = 48
        req_dyld = 2147483648
        load_weak_dylib = 2147483672
        rpath = 2147483676
        reexport_dylib = 2147483679
        dyld_info_only = 2147483682
        main2 = 2147483688

    class MachoFlags(Enum):
        no_undefs = 1
        incr_link = 2
        dyld_link = 4
        bind_at_load = 8
        prebound = 16
        split_segs = 32
        lazy_init = 64
        two_level = 128
        force_flat = 256
        no_multi_defs = 512
        no_fix_prebinding = 1024
        prebindable = 2048
        all_mods_bound = 4096
        subsections_via_symbols = 8192
        canonical = 16384
        weak_defines = 32768
        binds_to_weak = 65536
        allow_stack_execution = 131072
        root_safe = 262144
        setuid_safe = 524288
        no_reexported_dylibs = 1048576
        pie = 2097152
        dead_strippable_dylib = 4194304
        has_tlv_descriptors = 8388608
        no_heap_execution = 16777216
        app_extension_safe = 33554432

    class MagicType(Enum):
        fat_le = 3199925962
        fat_be = 3405691582
        macho_le_x86 = 3472551422
        macho_le_x64 = 3489328638
        macho_be_x86 = 4277009102
        macho_be_x64 = 4277009103

    class FileType(Enum):
        object = 1
        execute = 2
        fvmlib = 3
        core = 4
        preload = 5
        dylib = 6
        dylinker = 7
        bundle = 8
        dylib_stub = 9
        dsym = 10
        kext_bundle = 11

    class CpuType(Enum):
        vax = 1
        romp = 2
        ns32032 = 4
        ns32332 = 5
        i386 = 7
        mips = 8
        ns32532 = 9
        hppa = 11
        arm = 12
        mc88000 = 13
        sparc = 14
        i860 = 15
        i860_little = 16
        rs6000 = 17
        powerpc = 18
        abi64 = 16777216
        x86_64 = 16777223
        powerpc64 = 16777234
        any = 4294967295
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.magic = self._root.MagicType(self._io.read_u4be())
        self.header = self._root.MachHeader(self._io, self, self._root)
        self.load_commands = [None] * (self.header.ncmds)
        for i in range(self.header.ncmds):
            self.load_commands[i] = self._root.LoadCommand(self._io, self, self._root)


    class RpathCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.path_offset = self._io.read_u4le()
            self.path = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")


    class Uleb128(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.b1 = self._io.read_u1()
            if (self.b1 & 128) != 0:
                self.b2 = self._io.read_u1()

            if (self.b2 & 128) != 0:
                self.b3 = self._io.read_u1()

            if (self.b3 & 128) != 0:
                self.b4 = self._io.read_u1()

            if (self.b4 & 128) != 0:
                self.b5 = self._io.read_u1()

            if (self.b5 & 128) != 0:
                self.b6 = self._io.read_u1()

            if (self.b6 & 128) != 0:
                self.b7 = self._io.read_u1()

            if (self.b7 & 128) != 0:
                self.b8 = self._io.read_u1()

            if (self.b8 & 128) != 0:
                self.b9 = self._io.read_u1()

            if (self.b9 & 128) != 0:
                self.b10 = self._io.read_u1()


        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = (((self.b1 % 128) << 0) + (0 if (self.b1 & 128) == 0 else (((self.b2 % 128) << 7) + (0 if (self.b2 & 128) == 0 else (((self.b3 % 128) << 14) + (0 if (self.b3 & 128) == 0 else (((self.b4 % 128) << 21) + (0 if (self.b4 & 128) == 0 else (((self.b5 % 128) << 28) + (0 if (self.b5 & 128) == 0 else (((self.b6 % 128) << 35) + (0 if (self.b6 & 128) == 0 else (((self.b7 % 128) << 42) + (0 if (self.b7 & 128) == 0 else (((self.b8 % 128) << 49) + (0 if (self.b8 & 128) == 0 else (((self.b9 % 128) << 56) + (0 if (self.b8 & 128) == 0 else ((self.b10 % 128) << 63)))))))))))))))))))
            return self._m_value if hasattr(self, '_m_value') else None


    class SourceVersionCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.version = self._io.read_u8le()


    class CsBlob(KaitaiStruct):

        class CsMagic(Enum):
            blob_wrapper = 4208855809
            requirement = 4208856064
            requirements = 4208856065
            code_directory = 4208856066
            embedded_signature = 4208856256
            detached_signature = 4208856257
            entitlement = 4208882033
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.magic = self._root.CsBlob.CsMagic(self._io.read_u4be())
            self.length = self._io.read_u4be()
            _on = self.magic
            if _on == self._root.CsBlob.CsMagic.detached_signature:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.SuperBlob(io, self, self._root)
            elif _on == self._root.CsBlob.CsMagic.embedded_signature:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.SuperBlob(io, self, self._root)
            elif _on == self._root.CsBlob.CsMagic.entitlement:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.Entitlement(io, self, self._root)
            elif _on == self._root.CsBlob.CsMagic.blob_wrapper:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.BlobWrapper(io, self, self._root)
            elif _on == self._root.CsBlob.CsMagic.requirement:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.Requirement(io, self, self._root)
            elif _on == self._root.CsBlob.CsMagic.code_directory:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.CodeDirectory(io, self, self._root)
            elif _on == self._root.CsBlob.CsMagic.requirements:
                self._raw_body = self._io.read_bytes((self.length - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CsBlob.Entitlements(io, self, self._root)
            else:
                self.body = self._io.read_bytes((self.length - 8))

        class Entitlement(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.data = self._io.read_bytes_full()


        class CodeDirectory(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.version = self._io.read_u4be()
                self.flags = self._io.read_u4be()
                self.hash_offset = self._io.read_u4be()
                self.ident_offset = self._io.read_u4be()
                self.n_special_slots = self._io.read_u4be()
                self.n_code_slots = self._io.read_u4be()
                self.code_limit = self._io.read_u4be()
                self.hash_size = self._io.read_u1()
                self.hash_type = self._io.read_u1()
                self.spare1 = self._io.read_u1()
                self.page_size = self._io.read_u1()
                self.spare2 = self._io.read_u4be()
                if self.version >= 131328:
                    self.scatter_offset = self._io.read_u4be()

                if self.version >= 131584:
                    self.team_id_offset = self._io.read_u4be()


            @property
            def ident(self):
                if hasattr(self, '_m_ident'):
                    return self._m_ident if hasattr(self, '_m_ident') else None

                _pos = self._io.pos()
                self._io.seek((self.ident_offset - 8))
                self._m_ident = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")
                self._io.seek(_pos)
                return self._m_ident if hasattr(self, '_m_ident') else None

            @property
            def team_id(self):
                if hasattr(self, '_m_team_id'):
                    return self._m_team_id if hasattr(self, '_m_team_id') else None

                _pos = self._io.pos()
                self._io.seek((self.team_id_offset - 8))
                self._m_team_id = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")
                self._io.seek(_pos)
                return self._m_team_id if hasattr(self, '_m_team_id') else None

            @property
            def hashes(self):
                if hasattr(self, '_m_hashes'):
                    return self._m_hashes if hasattr(self, '_m_hashes') else None

                _pos = self._io.pos()
                self._io.seek(((self.hash_offset - 8) - (self.hash_size * self.n_special_slots)))
                self._m_hashes = [None] * ((self.n_special_slots + self.n_code_slots))
                for i in range((self.n_special_slots + self.n_code_slots)):
                    self._m_hashes[i] = self._io.read_bytes(self.hash_size)

                self._io.seek(_pos)
                return self._m_hashes if hasattr(self, '_m_hashes') else None


        class EntitlementsBlobIndex(KaitaiStruct):

            class RequirementType(Enum):
                host = 1
                guest = 2
                designated = 3
                library = 4
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.type = self._root.CsBlob.EntitlementsBlobIndex.RequirementType(self._io.read_u4be())
                self.offset = self._io.read_u4be()

            @property
            def value(self):
                if hasattr(self, '_m_value'):
                    return self._m_value if hasattr(self, '_m_value') else None

                _pos = self._io.pos()
                self._io.seek((self.offset - 8))
                self._m_value = self._root.CsBlob(self._io, self, self._root)
                self._io.seek(_pos)
                return self._m_value if hasattr(self, '_m_value') else None


        class Data(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.length = self._io.read_u4be()
                self.value = self._io.read_bytes(self.length)
                self.padding = self._io.read_bytes((4 - (self.length & 3)))


        class SuperBlob(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.count = self._io.read_u4be()
                self.blobs = [None] * (self.count)
                for i in range(self.count):
                    self.blobs[i] = self._root.CsBlob.BlobIndex(self._io, self, self._root)



        class Expr(KaitaiStruct):

            class OpEnum(Enum):
                false = 0
                true = 1
                ident = 2
                apple_anchor = 3
                anchor_hash = 4
                info_key_value = 5
                and_op = 6
                or_op = 7
                cd_hash = 8
                not_op = 9
                info_key_field = 10
                cert_field = 11
                trusted_cert = 12
                trusted_certs = 13
                cert_generic = 14
                apple_generic_anchor = 15
                entitlement_field = 16

            class CertSlot(Enum):
                left_cert = 0
                anchor_cert = 4294967295
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.op = self._root.CsBlob.Expr.OpEnum(self._io.read_u4be())
                _on = self.op
                if _on == self._root.CsBlob.Expr.OpEnum.cert_generic:
                    self.data = self._root.CsBlob.Expr.CertGenericExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.apple_generic_anchor:
                    self.data = self._root.CsBlob.Expr.AppleGenericAnchorExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.info_key_field:
                    self.data = self._root.CsBlob.Expr.InfoKeyFieldExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.and_op:
                    self.data = self._root.CsBlob.Expr.AndExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.anchor_hash:
                    self.data = self._root.CsBlob.Expr.AnchorHashExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.info_key_value:
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.or_op:
                    self.data = self._root.CsBlob.Expr.OrExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.trusted_cert:
                    self.data = self._root.CsBlob.Expr.CertSlotExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.not_op:
                    self.data = self._root.CsBlob.Expr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.ident:
                    self.data = self._root.CsBlob.Expr.IdentExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.cert_field:
                    self.data = self._root.CsBlob.Expr.CertFieldExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.entitlement_field:
                    self.data = self._root.CsBlob.Expr.EntitlementFieldExpr(self._io, self, self._root)
                elif _on == self._root.CsBlob.Expr.OpEnum.cd_hash:
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)

            class InfoKeyFieldExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)
                    self.match = self._root.CsBlob.Match(self._io, self, self._root)


            class CertSlotExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.value = self._root.CsBlob.Expr.CertSlot(self._io.read_u4be())


            class CertGenericExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.cert_slot = self._root.CsBlob.Expr.CertSlot(self._io.read_u4be())
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)
                    self.match = self._root.CsBlob.Match(self._io, self, self._root)


            class IdentExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.identifier = self._root.CsBlob.Data(self._io, self, self._root)


            class CertFieldExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.cert_slot = self._root.CsBlob.Expr.CertSlot(self._io.read_u4be())
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)
                    self.match = self._root.CsBlob.Match(self._io, self, self._root)


            class AnchorHashExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.cert_slot = self._root.CsBlob.Expr.CertSlot(self._io.read_u4be())
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)


            class AppleGenericAnchorExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self

                @property
                def value(self):
                    if hasattr(self, '_m_value'):
                        return self._m_value if hasattr(self, '_m_value') else None

                    self._m_value = u"anchor apple generic"
                    return self._m_value if hasattr(self, '_m_value') else None


            class EntitlementFieldExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)
                    self.match = self._root.CsBlob.Match(self._io, self, self._root)


            class AndExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.left = self._root.CsBlob.Expr(self._io, self, self._root)
                    self.right = self._root.CsBlob.Expr(self._io, self, self._root)


            class OrExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.left = self._root.CsBlob.Expr(self._io, self, self._root)
                    self.right = self._root.CsBlob.Expr(self._io, self, self._root)



        class BlobIndex(KaitaiStruct):

            class CsslotType(Enum):
                code_directory = 0
                info_slot = 1
                requirements = 2
                resource_dir = 3
                application = 4
                entitlements = 5
                alternate_code_directories = 4096
                signature_slot = 65536
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.type = self._root.CsBlob.BlobIndex.CsslotType(self._io.read_u4be())
                self.offset = self._io.read_u4be()

            @property
            def blob(self):
                if hasattr(self, '_m_blob'):
                    return self._m_blob if hasattr(self, '_m_blob') else None

                io = self._parent._io
                _pos = io.pos()
                io.seek((self.offset - 8))
                self._raw__m_blob = io.read_bytes_full()
                io = KaitaiStream(BytesIO(self._raw__m_blob))
                self._m_blob = self._root.CsBlob(io, self, self._root)
                io.seek(_pos)
                return self._m_blob if hasattr(self, '_m_blob') else None


        class Match(KaitaiStruct):

            class Op(Enum):
                exists = 0
                equal = 1
                contains = 2
                begins_with = 3
                ends_with = 4
                less_than = 5
                greater_than = 6
                less_equal = 7
                greater_equal = 8
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.match_op = self._root.CsBlob.Match.Op(self._io.read_u4be())
                if self.match_op != self._root.CsBlob.Match.Op.exists:
                    self.data = self._root.CsBlob.Data(self._io, self, self._root)



        class Requirement(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.kind = self._io.read_u4be()
                self.expr = self._root.CsBlob.Expr(self._io, self, self._root)


        class BlobWrapper(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.data = self._io.read_bytes_full()


        class Entitlements(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.count = self._io.read_u4be()
                self.items = [None] * (self.count)
                for i in range(self.count):
                    self.items[i] = self._root.CsBlob.EntitlementsBlobIndex(self._io, self, self._root)




    class SegmentCommand64(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.segname = (KaitaiStream.bytes_strip_right(self._io.read_bytes(16), 0)).decode(u"ascii")
            self.vmaddr = self._io.read_u8le()
            self.vmsize = self._io.read_u8le()
            self.fileoff = self._io.read_u8le()
            self.filesize = self._io.read_u8le()
            self.maxprot = self._io.read_u4le()
            self.initprot = self._io.read_u4le()
            self.nsects = self._io.read_u4le()
            self.flags = self._io.read_u4le()
            self.sections = [None] * (self.nsects)
            for i in range(self.nsects):
                self.sections[i] = self._root.SegmentCommand64.Section64(self._io, self, self._root)


        class Section64(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.sect_name = (KaitaiStream.bytes_strip_right(self._io.read_bytes(16), 0)).decode(u"ascii")
                self.seg_name = (KaitaiStream.bytes_strip_right(self._io.read_bytes(16), 0)).decode(u"ascii")
                self.addr = self._io.read_u8le()
                self.size = self._io.read_u8le()
                self.offset = self._io.read_u4le()
                self.align = self._io.read_u4le()
                self.reloff = self._io.read_u4le()
                self.nreloc = self._io.read_u4le()
                self.flags = self._io.read_u4le()
                self.reserved1 = self._io.read_u4le()
                self.reserved2 = self._io.read_u4le()
                self.reserved3 = self._io.read_u4le()

            class CfStringList(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.items = []
                    while not self._io.is_eof():
                        self.items.append(self._root.SegmentCommand64.Section64.CfString(self._io, self, self._root))



            class CfString(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.isa = self._io.read_u8le()
                    self.info = self._io.read_u8le()
                    self.data = self._io.read_u8le()
                    self.length = self._io.read_u8le()


            class EhFrameItem(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.length = self._io.read_u4le()
                    if self.length == 4294967295:
                        self.length64 = self._io.read_u8le()

                    self.id = self._io.read_u4le()
                    if self.length > 0:
                        _on = self.id
                        if _on == 0:
                            self._raw_body = self._io.read_bytes((self.length - 4))
                            io = KaitaiStream(BytesIO(self._raw_body))
                            self.body = self._root.SegmentCommand64.Section64.EhFrameItem.Cie(io, self, self._root)
                        else:
                            self.body = self._io.read_bytes((self.length - 4))


                class CharChain(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self.chr = self._io.read_u1()
                        if self.chr != 0:
                            self.next = self._root.SegmentCommand64.Section64.EhFrameItem.CharChain(self._io, self, self._root)



                class Cie(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self.version = self._io.read_u1()
                        self.aug_str = self._root.SegmentCommand64.Section64.EhFrameItem.CharChain(self._io, self, self._root)
                        self.code_alignment_factor = self._root.Uleb128(self._io, self, self._root)
                        self.data_alignment_factor = self._root.Uleb128(self._io, self, self._root)
                        self.return_address_register = self._io.read_u1()
                        if self.aug_str.chr == 122:
                            self.augmentation = self._root.SegmentCommand64.Section64.EhFrameItem.AugmentationEntry(self._io, self, self._root)



                class AugmentationEntry(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self.length = self._root.Uleb128(self._io, self, self._root)
                        if self._parent.aug_str.next.chr == 82:
                            self.fde_pointer_encoding = self._io.read_u1()




            class EhFrame(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.items = []
                    while not self._io.is_eof():
                        self.items.append(self._root.SegmentCommand64.Section64.EhFrameItem(self._io, self, self._root))



            class PointerList(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.items = []
                    while not self._io.is_eof():
                        self.items.append(self._io.read_u8le())



            class StringList(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.strings = []
                    while not self._io.is_eof():
                        self.strings.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ascii"))



            @property
            def data(self):
                if hasattr(self, '_m_data'):
                    return self._m_data if hasattr(self, '_m_data') else None

                io = self._root._io
                _pos = io.pos()
                io.seek(self.offset)
                _on = self.sect_name
                if _on == u"__objc_nlclslist":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.PointerList(io, self, self._root)
                elif _on == u"__objc_methname":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.StringList(io, self, self._root)
                elif _on == u"__nl_symbol_ptr":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.PointerList(io, self, self._root)
                elif _on == u"__la_symbol_ptr":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.PointerList(io, self, self._root)
                elif _on == u"__objc_selrefs":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.PointerList(io, self, self._root)
                elif _on == u"__cstring":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.StringList(io, self, self._root)
                elif _on == u"__objc_classlist":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.PointerList(io, self, self._root)
                elif _on == u"__objc_protolist":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.PointerList(io, self, self._root)
                elif _on == u"__objc_imageinfo":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.PointerList(io, self, self._root)
                elif _on == u"__objc_methtype":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.StringList(io, self, self._root)
                elif _on == u"__cfstring":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.CfStringList(io, self, self._root)
                elif _on == u"__objc_classrefs":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.PointerList(io, self, self._root)
                elif _on == u"__objc_protorefs":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.PointerList(io, self, self._root)
                elif _on == u"__objc_classname":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.StringList(io, self, self._root)
                elif _on == u"__got":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.PointerList(io, self, self._root)
                elif _on == u"__eh_frame":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.EhFrame(io, self, self._root)
                elif _on == u"__objc_superrefs":
                    self._raw__m_data = io.read_bytes(self.size)
                    io = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = self._root.SegmentCommand64.Section64.PointerList(io, self, self._root)
                else:
                    self._m_data = io.read_bytes(self.size)
                io.seek(_pos)
                return self._m_data if hasattr(self, '_m_data') else None



    class DysymtabCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.i_local_sym = self._io.read_u4le()
            self.n_local_sym = self._io.read_u4le()
            self.i_ext_def_sym = self._io.read_u4le()
            self.n_ext_def_sym = self._io.read_u4le()
            self.i_undef_sym = self._io.read_u4le()
            self.n_undef_sym = self._io.read_u4le()
            self.toc_off = self._io.read_u4le()
            self.n_toc = self._io.read_u4le()
            self.mod_tab_off = self._io.read_u4le()
            self.n_mod_tab = self._io.read_u4le()
            self.ext_ref_sym_off = self._io.read_u4le()
            self.n_ext_ref_syms = self._io.read_u4le()
            self.indirect_sym_off = self._io.read_u4le()
            self.n_indirect_syms = self._io.read_u4le()
            self.ext_rel_off = self._io.read_u4le()
            self.n_ext_rel = self._io.read_u4le()
            self.loc_rel_off = self._io.read_u4le()
            self.n_loc_rel = self._io.read_u4le()

        @property
        def indirect_symbols(self):
            if hasattr(self, '_m_indirect_symbols'):
                return self._m_indirect_symbols if hasattr(self, '_m_indirect_symbols') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.indirect_sym_off)
            self._m_indirect_symbols = [None] * (self.n_indirect_syms)
            for i in range(self.n_indirect_syms):
                self._m_indirect_symbols[i] = io.read_u4le()

            io.seek(_pos)
            return self._m_indirect_symbols if hasattr(self, '_m_indirect_symbols') else None


    class MachHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.cputype = self._root.CpuType(self._io.read_u4le())
            self.cpusubtype = self._io.read_u4le()
            self.filetype = self._root.FileType(self._io.read_u4le())
            self.ncmds = self._io.read_u4le()
            self.sizeofcmds = self._io.read_u4le()
            self.flags = self._io.read_u4le()
            if  ((self._root.magic == self._root.MagicType.macho_be_x64) or (self._root.magic == self._root.MagicType.macho_le_x64)) :
                self.reserved = self._io.read_u4le()



    class LinkeditDataCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.data_off = self._io.read_u4le()
            self.data_size = self._io.read_u4le()


    class Version(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.p1 = self._io.read_u1()
            self.minor = self._io.read_u1()
            self.major = self._io.read_u1()
            self.release = self._io.read_u1()


    class CodeSignatureCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.data_off = self._io.read_u4le()
            self.data_size = self._io.read_u4le()

        @property
        def code_signature(self):
            if hasattr(self, '_m_code_signature'):
                return self._m_code_signature if hasattr(self, '_m_code_signature') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.data_off)
            self._raw__m_code_signature = io.read_bytes(self.data_size)
            io = KaitaiStream(BytesIO(self._raw__m_code_signature))
            self._m_code_signature = self._root.CsBlob(io, self, self._root)
            io.seek(_pos)
            return self._m_code_signature if hasattr(self, '_m_code_signature') else None


    class DyldInfoCommand(KaitaiStruct):

        class BindOpcode(Enum):
            done = 0
            set_dylib_ordinal_immediate = 16
            set_dylib_ordinal_uleb = 32
            set_dylib_special_immediate = 48
            set_symbol_trailing_flags_immediate = 64
            set_type_immediate = 80
            set_append_sleb = 96
            set_segment_and_offset_uleb = 112
            add_address_uleb = 128
            do_bind = 144
            do_bind_add_address_uleb = 160
            do_bind_add_address_immediate_scaled = 176
            do_bind_uleb_times_skipping_uleb = 192
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.rebase_off = self._io.read_u4le()
            self.rebase_size = self._io.read_u4le()
            self.bind_off = self._io.read_u4le()
            self.bind_size = self._io.read_u4le()
            self.weak_bind_off = self._io.read_u4le()
            self.weak_bind_size = self._io.read_u4le()
            self.lazy_bind_off = self._io.read_u4le()
            self.lazy_bind_size = self._io.read_u4le()
            self.export_off = self._io.read_u4le()
            self.export_size = self._io.read_u4le()

        class BindItem(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.opcode_and_immediate = self._io.read_u1()
                if  ((self.opcode == self._root.DyldInfoCommand.BindOpcode.set_dylib_ordinal_uleb) or (self.opcode == self._root.DyldInfoCommand.BindOpcode.set_append_sleb) or (self.opcode == self._root.DyldInfoCommand.BindOpcode.set_segment_and_offset_uleb) or (self.opcode == self._root.DyldInfoCommand.BindOpcode.add_address_uleb) or (self.opcode == self._root.DyldInfoCommand.BindOpcode.do_bind_add_address_uleb) or (self.opcode == self._root.DyldInfoCommand.BindOpcode.do_bind_uleb_times_skipping_uleb)) :
                    self.uleb = self._root.Uleb128(self._io, self, self._root)

                if self.opcode == self._root.DyldInfoCommand.BindOpcode.do_bind_uleb_times_skipping_uleb:
                    self.skip = self._root.Uleb128(self._io, self, self._root)

                if self.opcode == self._root.DyldInfoCommand.BindOpcode.set_symbol_trailing_flags_immediate:
                    self.symbol = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")


            @property
            def opcode(self):
                if hasattr(self, '_m_opcode'):
                    return self._m_opcode if hasattr(self, '_m_opcode') else None

                self._m_opcode = self._root.DyldInfoCommand.BindOpcode((self.opcode_and_immediate & 240))
                return self._m_opcode if hasattr(self, '_m_opcode') else None

            @property
            def immediate(self):
                if hasattr(self, '_m_immediate'):
                    return self._m_immediate if hasattr(self, '_m_immediate') else None

                self._m_immediate = (self.opcode_and_immediate & 15)
                return self._m_immediate if hasattr(self, '_m_immediate') else None


        class RebaseData(KaitaiStruct):

            class Opcode(Enum):
                done = 0
                set_type_immediate = 16
                set_segment_and_offset_uleb = 32
                add_address_uleb = 48
                add_address_immediate_scaled = 64
                do_rebase_immediate_times = 80
                do_rebase_uleb_times = 96
                do_rebase_add_address_uleb = 112
                do_rebase_uleb_times_skipping_uleb = 128
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.items = []
                while True:
                    _ = self._root.DyldInfoCommand.RebaseData.RebaseItem(self._io, self, self._root)
                    self.items.append(_)
                    if _.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.done:
                        break

            class RebaseItem(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.opcode_and_immediate = self._io.read_u1()
                    if  ((self.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.set_segment_and_offset_uleb) or (self.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.add_address_uleb) or (self.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.do_rebase_uleb_times) or (self.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.do_rebase_add_address_uleb) or (self.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.do_rebase_uleb_times_skipping_uleb)) :
                        self.uleb = self._root.Uleb128(self._io, self, self._root)

                    if self.opcode == self._root.DyldInfoCommand.RebaseData.Opcode.do_rebase_uleb_times_skipping_uleb:
                        self.skip = self._root.Uleb128(self._io, self, self._root)


                @property
                def opcode(self):
                    if hasattr(self, '_m_opcode'):
                        return self._m_opcode if hasattr(self, '_m_opcode') else None

                    self._m_opcode = self._root.DyldInfoCommand.RebaseData.Opcode((self.opcode_and_immediate & 240))
                    return self._m_opcode if hasattr(self, '_m_opcode') else None

                @property
                def immediate(self):
                    if hasattr(self, '_m_immediate'):
                        return self._m_immediate if hasattr(self, '_m_immediate') else None

                    self._m_immediate = (self.opcode_and_immediate & 15)
                    return self._m_immediate if hasattr(self, '_m_immediate') else None



        class ExportNode(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.terminal_size = self._root.Uleb128(self._io, self, self._root)
                self.children_count = self._io.read_u1()
                self.children = [None] * (self.children_count)
                for i in range(self.children_count):
                    self.children[i] = self._root.DyldInfoCommand.ExportNode.Child(self._io, self, self._root)

                self.terminal = self._io.read_bytes(self.terminal_size.value)

            class Child(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
                    self.node_offset = self._root.Uleb128(self._io, self, self._root)

                @property
                def value(self):
                    if hasattr(self, '_m_value'):
                        return self._m_value if hasattr(self, '_m_value') else None

                    _pos = self._io.pos()
                    self._io.seek(self.node_offset.value)
                    self._m_value = self._root.DyldInfoCommand.ExportNode(self._io, self, self._root)
                    self._io.seek(_pos)
                    return self._m_value if hasattr(self, '_m_value') else None



        class BindData(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.items = []
                while True:
                    _ = self._root.DyldInfoCommand.BindItem(self._io, self, self._root)
                    self.items.append(_)
                    if _.opcode == self._root.DyldInfoCommand.BindOpcode.done:
                        break


        class LazyBindData(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.items = []
                while not self._io.is_eof():
                    self.items.append(self._root.DyldInfoCommand.BindItem(self._io, self, self._root))



        @property
        def rebase(self):
            if hasattr(self, '_m_rebase'):
                return self._m_rebase if hasattr(self, '_m_rebase') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.rebase_off)
            self._raw__m_rebase = io.read_bytes(self.rebase_size)
            io = KaitaiStream(BytesIO(self._raw__m_rebase))
            self._m_rebase = self._root.DyldInfoCommand.RebaseData(io, self, self._root)
            io.seek(_pos)
            return self._m_rebase if hasattr(self, '_m_rebase') else None

        @property
        def bind(self):
            if hasattr(self, '_m_bind'):
                return self._m_bind if hasattr(self, '_m_bind') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.bind_off)
            self._raw__m_bind = io.read_bytes(self.bind_size)
            io = KaitaiStream(BytesIO(self._raw__m_bind))
            self._m_bind = self._root.DyldInfoCommand.BindData(io, self, self._root)
            io.seek(_pos)
            return self._m_bind if hasattr(self, '_m_bind') else None

        @property
        def lazy_bind(self):
            if hasattr(self, '_m_lazy_bind'):
                return self._m_lazy_bind if hasattr(self, '_m_lazy_bind') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.lazy_bind_off)
            self._raw__m_lazy_bind = io.read_bytes(self.lazy_bind_size)
            io = KaitaiStream(BytesIO(self._raw__m_lazy_bind))
            self._m_lazy_bind = self._root.DyldInfoCommand.LazyBindData(io, self, self._root)
            io.seek(_pos)
            return self._m_lazy_bind if hasattr(self, '_m_lazy_bind') else None

        @property
        def exports(self):
            if hasattr(self, '_m_exports'):
                return self._m_exports if hasattr(self, '_m_exports') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.export_off)
            self._raw__m_exports = io.read_bytes(self.export_size)
            io = KaitaiStream(BytesIO(self._raw__m_exports))
            self._m_exports = self._root.DyldInfoCommand.ExportNode(io, self, self._root)
            io.seek(_pos)
            return self._m_exports if hasattr(self, '_m_exports') else None


    class DylinkerCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.name = self._root.LcStr(self._io, self, self._root)


    class DylibCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.name_offset = self._io.read_u4le()
            self.timestamp = self._io.read_u4le()
            self.current_version = self._io.read_u4le()
            self.compatibility_version = self._io.read_u4le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")


    class LcStr(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.length = self._io.read_u4le()
            self.value = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")


    class LoadCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.type = self._root.LoadCommandType(self._io.read_u4le())
            self.size = self._io.read_u4le()
            _on = self.type
            if _on == self._root.LoadCommandType.rpath:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.RpathCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.source_version:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.SourceVersionCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.load_dylinker:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DylinkerCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.symtab:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.SymtabCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.main:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.EntryPointCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.function_starts:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.LinkeditDataCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.version_min_macosx:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.VersionMinCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.data_in_code:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.LinkeditDataCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.uuid:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.UuidCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.dyld_info_only:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DyldInfoCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.code_signature:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.CodeSignatureCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.dysymtab:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DysymtabCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.load_dylib:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.DylibCommand(io, self, self._root)
            elif _on == self._root.LoadCommandType.segment_64:
                self._raw_body = self._io.read_bytes((self.size - 8))
                io = KaitaiStream(BytesIO(self._raw_body))
                self.body = self._root.SegmentCommand64(io, self, self._root)
            else:
                self.body = self._io.read_bytes((self.size - 8))


    class UuidCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.uuid = self._io.read_bytes(16)


    class SymtabCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.sym_off = self._io.read_u4le()
            self.n_syms = self._io.read_u4le()
            self.str_off = self._io.read_u4le()
            self.str_size = self._io.read_u4le()

        class StrTable(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.unknown = self._io.read_u4le()
                self.items = []
                while True:
                    _ = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
                    self.items.append(_)
                    if _ == u"":
                        break


        class Nlist64(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.un = self._io.read_u4le()
                self.type = self._io.read_u1()
                self.sect = self._io.read_u1()
                self.desc = self._io.read_u2le()
                self.value = self._io.read_u8le()


        @property
        def symbols(self):
            if hasattr(self, '_m_symbols'):
                return self._m_symbols if hasattr(self, '_m_symbols') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.sym_off)
            self._m_symbols = [None] * (self.n_syms)
            for i in range(self.n_syms):
                self._m_symbols[i] = self._root.SymtabCommand.Nlist64(io, self, self._root)

            io.seek(_pos)
            return self._m_symbols if hasattr(self, '_m_symbols') else None

        @property
        def strs(self):
            if hasattr(self, '_m_strs'):
                return self._m_strs if hasattr(self, '_m_strs') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.str_off)
            self._raw__m_strs = io.read_bytes(self.str_size)
            io = KaitaiStream(BytesIO(self._raw__m_strs))
            self._m_strs = self._root.SymtabCommand.StrTable(io, self, self._root)
            io.seek(_pos)
            return self._m_strs if hasattr(self, '_m_strs') else None


    class VersionMinCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.version = self._root.Version(self._io, self, self._root)
            self.reserved = self._root.Version(self._io, self, self._root)


    class EntryPointCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.entry_off = self._io.read_u8le()
            self.stack_size = self._io.read_u8le()



