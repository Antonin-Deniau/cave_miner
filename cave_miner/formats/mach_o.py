# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from cave_miner.formats import asn1_der
class MachO(KaitaiStruct):
    """
    .. seealso::
       Source - https://www.stonedcoder.org/~kd/lib/MachORuntime.pdf
    
    
    .. seealso::
       Source - https://opensource.apple.com/source/python_modules/python_modules-43/Modules/macholib-1.5.1/macholib-1.5.1.tar.gz
    
    
    .. seealso::
       Source - https://github.com/comex/cs/blob/07a88f9/macho_cs.py
    
    
    .. seealso::
       Source - https://opensource.apple.com/source/Security/Security-55471/libsecurity_codesigning/requirements.grammar.auto.html
    
    
    .. seealso::
       Source - https://github.com/apple/darwin-xnu/blob/xnu-2782.40.9/bsd/sys/codesign.h
    
    
    .. seealso::
       Source - https://opensource.apple.com/source/dyld/dyld-852/src/ImageLoaderMachO.cpp.auto.html
    
    
    .. seealso::
       Source - https://opensource.apple.com/source/dyld/dyld-852/src/ImageLoaderMachOCompressed.cpp.auto.html
    """

    class MagicType(Enum):
        macho_le_x86 = 3472551422
        macho_le_x64 = 3489328638
        macho_be_x86 = 4277009102
        macho_be_x64 = 4277009103

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
        arm64 = 16777228
        powerpc64 = 16777234
        any = 4294967295

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
        version_min_macosx = 36
        version_min_iphoneos = 37
        function_starts = 38
        dyld_environment = 39
        data_in_code = 41
        source_version = 42
        dylib_code_sign_drs = 43
        encryption_info_64 = 44
        linker_option = 45
        linker_optimization_hint = 46
        version_min_tvos = 47
        version_min_watchos = 48
        build_version = 50
        req_dyld = 2147483648
        load_weak_dylib = 2147483672
        rpath = 2147483676
        reexport_dylib = 2147483679
        dyld_info_only = 2147483682
        load_upward_dylib = 2147483683
        main = 2147483688
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = KaitaiStream.resolve_enum(MachO.MagicType, self._io.read_u4be())
        self.header = MachO.MachHeader(self._io, self, self._root)
        self.load_commands = []
        for i in range(self.header.ncmds):
            self.load_commands.append(MachO.LoadCommand(self._io, self, self._root))


    class RpathCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.path_offset = self._io.read_u4le()
            self.path = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")


    class Uleb128(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
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
                return self._m_value

            self._m_value = (((self.b1 % 128) << 0) + (0 if (self.b1 & 128) == 0 else (((self.b2 % 128) << 7) + (0 if (self.b2 & 128) == 0 else (((self.b3 % 128) << 14) + (0 if (self.b3 & 128) == 0 else (((self.b4 % 128) << 21) + (0 if (self.b4 & 128) == 0 else (((self.b5 % 128) << 28) + (0 if (self.b5 & 128) == 0 else (((self.b6 % 128) << 35) + (0 if (self.b6 & 128) == 0 else (((self.b7 % 128) << 42) + (0 if (self.b7 & 128) == 0 else (((self.b8 % 128) << 49) + (0 if (self.b8 & 128) == 0 else (((self.b9 % 128) << 56) + (0 if (self.b8 & 128) == 0 else ((self.b10 % 128) << 63)))))))))))))))))))
            return getattr(self, '_m_value', None)


    class SourceVersionCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_u8le()


    class CsBlob(KaitaiStruct):

        class CsMagic(Enum):
            blob_wrapper = 4208855809
            requirement = 4208856064
            requirements = 4208856065
            code_directory = 4208856066
            embedded_signature = 4208856256
            detached_signature = 4208856257
            entitlements = 4208882033
            der_entitlements = 4208882034
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = KaitaiStream.resolve_enum(MachO.CsBlob.CsMagic, self._io.read_u4be())
            self.length = self._io.read_u4be()
            _on = self.magic
            if _on == MachO.CsBlob.CsMagic.requirement:
                self._raw_body = self._io.read_bytes((self.length - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.CsBlob.Requirement(_io__raw_body, self, self._root)
            elif _on == MachO.CsBlob.CsMagic.code_directory:
                self._raw_body = self._io.read_bytes((self.length - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.CsBlob.CodeDirectory(_io__raw_body, self, self._root)
            elif _on == MachO.CsBlob.CsMagic.requirements:
                self._raw_body = self._io.read_bytes((self.length - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.CsBlob.Requirements(_io__raw_body, self, self._root)
            elif _on == MachO.CsBlob.CsMagic.blob_wrapper:
                self._raw_body = self._io.read_bytes((self.length - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.CsBlob.BlobWrapper(_io__raw_body, self, self._root)
            elif _on == MachO.CsBlob.CsMagic.embedded_signature:
                self._raw_body = self._io.read_bytes((self.length - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.CsBlob.SuperBlob(_io__raw_body, self, self._root)
            elif _on == MachO.CsBlob.CsMagic.entitlements:
                self._raw_body = self._io.read_bytes((self.length - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.CsBlob.Entitlements(_io__raw_body, self, self._root)
            elif _on == MachO.CsBlob.CsMagic.detached_signature:
                self._raw_body = self._io.read_bytes((self.length - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.CsBlob.SuperBlob(_io__raw_body, self, self._root)
            elif _on == MachO.CsBlob.CsMagic.der_entitlements:
                self._raw_body = self._io.read_bytes((self.length - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = asn1_der.Asn1Der(_io__raw_body)
            else:
                self.body = self._io.read_bytes((self.length - 8))

        class CodeDirectory(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
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
                    return self._m_ident

                _pos = self._io.pos()
                self._io.seek((self.ident_offset - 8))
                self._m_ident = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")
                self._io.seek(_pos)
                return getattr(self, '_m_ident', None)

            @property
            def team_id(self):
                if hasattr(self, '_m_team_id'):
                    return self._m_team_id

                _pos = self._io.pos()
                self._io.seek((self.team_id_offset - 8))
                self._m_team_id = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")
                self._io.seek(_pos)
                return getattr(self, '_m_team_id', None)

            @property
            def hashes(self):
                if hasattr(self, '_m_hashes'):
                    return self._m_hashes

                _pos = self._io.pos()
                self._io.seek(((self.hash_offset - 8) - (self.hash_size * self.n_special_slots)))
                self._m_hashes = []
                for i in range((self.n_special_slots + self.n_code_slots)):
                    self._m_hashes.append(self._io.read_bytes(self.hash_size))

                self._io.seek(_pos)
                return getattr(self, '_m_hashes', None)


        class Data(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.length = self._io.read_u4be()
                self.value = self._io.read_bytes(self.length)
                self.padding = self._io.read_bytes((-(self.length) % 4))


        class SuperBlob(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.count = self._io.read_u4be()
                self.blobs = []
                for i in range(self.count):
                    self.blobs.append(MachO.CsBlob.BlobIndex(self._io, self, self._root))



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
                self._read()

            def _read(self):
                self.op = KaitaiStream.resolve_enum(MachO.CsBlob.Expr.OpEnum, self._io.read_u4be())
                _on = self.op
                if _on == MachO.CsBlob.Expr.OpEnum.ident:
                    self.data = MachO.CsBlob.Expr.IdentExpr(self._io, self, self._root)
                elif _on == MachO.CsBlob.Expr.OpEnum.or_op:
                    self.data = MachO.CsBlob.Expr.OrExpr(self._io, self, self._root)
                elif _on == MachO.CsBlob.Expr.OpEnum.info_key_value:
                    self.data = MachO.CsBlob.Data(self._io, self, self._root)
                elif _on == MachO.CsBlob.Expr.OpEnum.anchor_hash:
                    self.data = MachO.CsBlob.Expr.AnchorHashExpr(self._io, self, self._root)
                elif _on == MachO.CsBlob.Expr.OpEnum.info_key_field:
                    self.data = MachO.CsBlob.Expr.InfoKeyFieldExpr(self._io, self, self._root)
                elif _on == MachO.CsBlob.Expr.OpEnum.not_op:
                    self.data = MachO.CsBlob.Expr(self._io, self, self._root)
                elif _on == MachO.CsBlob.Expr.OpEnum.entitlement_field:
                    self.data = MachO.CsBlob.Expr.EntitlementFieldExpr(self._io, self, self._root)
                elif _on == MachO.CsBlob.Expr.OpEnum.trusted_cert:
                    self.data = MachO.CsBlob.Expr.CertSlotExpr(self._io, self, self._root)
                elif _on == MachO.CsBlob.Expr.OpEnum.and_op:
                    self.data = MachO.CsBlob.Expr.AndExpr(self._io, self, self._root)
                elif _on == MachO.CsBlob.Expr.OpEnum.cert_generic:
                    self.data = MachO.CsBlob.Expr.CertGenericExpr(self._io, self, self._root)
                elif _on == MachO.CsBlob.Expr.OpEnum.cert_field:
                    self.data = MachO.CsBlob.Expr.CertFieldExpr(self._io, self, self._root)
                elif _on == MachO.CsBlob.Expr.OpEnum.cd_hash:
                    self.data = MachO.CsBlob.Data(self._io, self, self._root)
                elif _on == MachO.CsBlob.Expr.OpEnum.apple_generic_anchor:
                    self.data = MachO.CsBlob.Expr.AppleGenericAnchorExpr(self._io, self, self._root)

            class InfoKeyFieldExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.data = MachO.CsBlob.Data(self._io, self, self._root)
                    self.match = MachO.CsBlob.Match(self._io, self, self._root)


            class CertSlotExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.value = KaitaiStream.resolve_enum(MachO.CsBlob.Expr.CertSlot, self._io.read_u4be())


            class CertGenericExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.cert_slot = KaitaiStream.resolve_enum(MachO.CsBlob.Expr.CertSlot, self._io.read_u4be())
                    self.data = MachO.CsBlob.Data(self._io, self, self._root)
                    self.match = MachO.CsBlob.Match(self._io, self, self._root)


            class IdentExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.identifier = MachO.CsBlob.Data(self._io, self, self._root)


            class CertFieldExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.cert_slot = KaitaiStream.resolve_enum(MachO.CsBlob.Expr.CertSlot, self._io.read_u4be())
                    self.data = MachO.CsBlob.Data(self._io, self, self._root)
                    self.match = MachO.CsBlob.Match(self._io, self, self._root)


            class AnchorHashExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.cert_slot = KaitaiStream.resolve_enum(MachO.CsBlob.Expr.CertSlot, self._io.read_u4be())
                    self.data = MachO.CsBlob.Data(self._io, self, self._root)


            class AppleGenericAnchorExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    pass

                @property
                def value(self):
                    if hasattr(self, '_m_value'):
                        return self._m_value

                    self._m_value = u"anchor apple generic"
                    return getattr(self, '_m_value', None)


            class EntitlementFieldExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.data = MachO.CsBlob.Data(self._io, self, self._root)
                    self.match = MachO.CsBlob.Match(self._io, self, self._root)


            class AndExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.left = MachO.CsBlob.Expr(self._io, self, self._root)
                    self.right = MachO.CsBlob.Expr(self._io, self, self._root)


            class OrExpr(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.left = MachO.CsBlob.Expr(self._io, self, self._root)
                    self.right = MachO.CsBlob.Expr(self._io, self, self._root)



        class BlobIndex(KaitaiStruct):

            class CsslotType(Enum):
                code_directory = 0
                info_slot = 1
                requirements = 2
                resource_dir = 3
                application = 4
                entitlements = 5
                der_entitlements = 7
                alternate_code_directories = 4096
                signature_slot = 65536
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.type = KaitaiStream.resolve_enum(MachO.CsBlob.BlobIndex.CsslotType, self._io.read_u4be())
                self.offset = self._io.read_u4be()

            @property
            def blob(self):
                if hasattr(self, '_m_blob'):
                    return self._m_blob

                io = self._parent._io
                _pos = io.pos()
                io.seek((self.offset - 8))
                self._raw__m_blob = io.read_bytes_full()
                _io__raw__m_blob = KaitaiStream(BytesIO(self._raw__m_blob))
                self._m_blob = MachO.CsBlob(_io__raw__m_blob, self, self._root)
                io.seek(_pos)
                return getattr(self, '_m_blob', None)


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
                self._read()

            def _read(self):
                self.match_op = KaitaiStream.resolve_enum(MachO.CsBlob.Match.Op, self._io.read_u4be())
                if self.match_op != MachO.CsBlob.Match.Op.exists:
                    self.data = MachO.CsBlob.Data(self._io, self, self._root)



        class Requirement(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.kind = self._io.read_u4be()
                self.expr = MachO.CsBlob.Expr(self._io, self, self._root)


        class Requirements(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.count = self._io.read_u4be()
                self.items = []
                for i in range(self.count):
                    self.items.append(MachO.CsBlob.RequirementsBlobIndex(self._io, self, self._root))



        class BlobWrapper(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.data = self._io.read_bytes_full()


        class Entitlements(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.data = self._io.read_bytes_full()


        class RequirementsBlobIndex(KaitaiStruct):

            class RequirementType(Enum):
                host = 1
                guest = 2
                designated = 3
                library = 4
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.type = KaitaiStream.resolve_enum(MachO.CsBlob.RequirementsBlobIndex.RequirementType, self._io.read_u4be())
                self.offset = self._io.read_u4be()

            @property
            def value(self):
                if hasattr(self, '_m_value'):
                    return self._m_value

                _pos = self._io.pos()
                self._io.seek((self.offset - 8))
                self._m_value = MachO.CsBlob(self._io, self, self._root)
                self._io.seek(_pos)
                return getattr(self, '_m_value', None)



    class BuildVersionCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.platform = self._io.read_u4le()
            self.minos = self._io.read_u4le()
            self.sdk = self._io.read_u4le()
            self.ntools = self._io.read_u4le()
            self.tools = []
            for i in range(self.ntools):
                self.tools.append(MachO.BuildVersionCommand.BuildToolVersion(self._io, self, self._root))


        class BuildToolVersion(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.tool = self._io.read_u4le()
                self.version = self._io.read_u4le()



    class RoutinesCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.init_address = self._io.read_u4le()
            self.init_module = self._io.read_u4le()
            self.reserved = self._io.read_bytes(24)


    class MachoFlags(KaitaiStruct):
        def __init__(self, value, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.value = value
            self._read()

        def _read(self):
            pass

        @property
        def subsections_via_symbols(self):
            """safe to divide up the sections into sub-sections via symbols for dead code stripping."""
            if hasattr(self, '_m_subsections_via_symbols'):
                return self._m_subsections_via_symbols

            self._m_subsections_via_symbols = (self.value & 8192) != 0
            return getattr(self, '_m_subsections_via_symbols', None)

        @property
        def dead_strippable_dylib(self):
            if hasattr(self, '_m_dead_strippable_dylib'):
                return self._m_dead_strippable_dylib

            self._m_dead_strippable_dylib = (self.value & 4194304) != 0
            return getattr(self, '_m_dead_strippable_dylib', None)

        @property
        def weak_defines(self):
            """the final linked image contains external weak symbols."""
            if hasattr(self, '_m_weak_defines'):
                return self._m_weak_defines

            self._m_weak_defines = (self.value & 32768) != 0
            return getattr(self, '_m_weak_defines', None)

        @property
        def prebound(self):
            """the file has its dynamic undefined references prebound."""
            if hasattr(self, '_m_prebound'):
                return self._m_prebound

            self._m_prebound = (self.value & 16) != 0
            return getattr(self, '_m_prebound', None)

        @property
        def all_mods_bound(self):
            """indicates that this binary binds to all two-level namespace modules of its dependent libraries. only used when MH_PREBINDABLE and MH_TWOLEVEL are both set."""
            if hasattr(self, '_m_all_mods_bound'):
                return self._m_all_mods_bound

            self._m_all_mods_bound = (self.value & 4096) != 0
            return getattr(self, '_m_all_mods_bound', None)

        @property
        def has_tlv_descriptors(self):
            if hasattr(self, '_m_has_tlv_descriptors'):
                return self._m_has_tlv_descriptors

            self._m_has_tlv_descriptors = (self.value & 8388608) != 0
            return getattr(self, '_m_has_tlv_descriptors', None)

        @property
        def force_flat(self):
            """the executable is forcing all images to use flat name space bindings."""
            if hasattr(self, '_m_force_flat'):
                return self._m_force_flat

            self._m_force_flat = (self.value & 256) != 0
            return getattr(self, '_m_force_flat', None)

        @property
        def root_safe(self):
            """When this bit is set, the binary declares it is safe for use in processes with uid zero."""
            if hasattr(self, '_m_root_safe'):
                return self._m_root_safe

            self._m_root_safe = (self.value & 262144) != 0
            return getattr(self, '_m_root_safe', None)

        @property
        def no_undefs(self):
            """the object file has no undefined references."""
            if hasattr(self, '_m_no_undefs'):
                return self._m_no_undefs

            self._m_no_undefs = (self.value & 1) != 0
            return getattr(self, '_m_no_undefs', None)

        @property
        def setuid_safe(self):
            """When this bit is set, the binary declares it is safe for use in processes when issetugid() is true."""
            if hasattr(self, '_m_setuid_safe'):
                return self._m_setuid_safe

            self._m_setuid_safe = (self.value & 524288) != 0
            return getattr(self, '_m_setuid_safe', None)

        @property
        def no_heap_execution(self):
            if hasattr(self, '_m_no_heap_execution'):
                return self._m_no_heap_execution

            self._m_no_heap_execution = (self.value & 16777216) != 0
            return getattr(self, '_m_no_heap_execution', None)

        @property
        def no_reexported_dylibs(self):
            """When this bit is set on a dylib, the static linker does not need to examine dependent dylibs to see if any are re-exported."""
            if hasattr(self, '_m_no_reexported_dylibs'):
                return self._m_no_reexported_dylibs

            self._m_no_reexported_dylibs = (self.value & 1048576) != 0
            return getattr(self, '_m_no_reexported_dylibs', None)

        @property
        def no_multi_defs(self):
            """this umbrella guarantees no multiple defintions of symbols in its sub-images so the two-level namespace hints can always be used."""
            if hasattr(self, '_m_no_multi_defs'):
                return self._m_no_multi_defs

            self._m_no_multi_defs = (self.value & 512) != 0
            return getattr(self, '_m_no_multi_defs', None)

        @property
        def app_extension_safe(self):
            if hasattr(self, '_m_app_extension_safe'):
                return self._m_app_extension_safe

            self._m_app_extension_safe = (self.value & 33554432) != 0
            return getattr(self, '_m_app_extension_safe', None)

        @property
        def prebindable(self):
            """the binary is not prebound but can have its prebinding redone. only used when MH_PREBOUND is not set."""
            if hasattr(self, '_m_prebindable'):
                return self._m_prebindable

            self._m_prebindable = (self.value & 2048) != 0
            return getattr(self, '_m_prebindable', None)

        @property
        def incr_link(self):
            """the object file is the output of an incremental link against a base file and can't be link edited again."""
            if hasattr(self, '_m_incr_link'):
                return self._m_incr_link

            self._m_incr_link = (self.value & 2) != 0
            return getattr(self, '_m_incr_link', None)

        @property
        def bind_at_load(self):
            """the object file's undefined references are bound by the dynamic linker when loaded."""
            if hasattr(self, '_m_bind_at_load'):
                return self._m_bind_at_load

            self._m_bind_at_load = (self.value & 8) != 0
            return getattr(self, '_m_bind_at_load', None)

        @property
        def canonical(self):
            """the binary has been canonicalized via the unprebind operation."""
            if hasattr(self, '_m_canonical'):
                return self._m_canonical

            self._m_canonical = (self.value & 16384) != 0
            return getattr(self, '_m_canonical', None)

        @property
        def two_level(self):
            """the image is using two-level name space bindings."""
            if hasattr(self, '_m_two_level'):
                return self._m_two_level

            self._m_two_level = (self.value & 128) != 0
            return getattr(self, '_m_two_level', None)

        @property
        def split_segs(self):
            """the file has its read-only and read-write segments split."""
            if hasattr(self, '_m_split_segs'):
                return self._m_split_segs

            self._m_split_segs = (self.value & 32) != 0
            return getattr(self, '_m_split_segs', None)

        @property
        def lazy_init(self):
            """the shared library init routine is to be run lazily via catching memory faults to its writeable segments (obsolete)."""
            if hasattr(self, '_m_lazy_init'):
                return self._m_lazy_init

            self._m_lazy_init = (self.value & 64) != 0
            return getattr(self, '_m_lazy_init', None)

        @property
        def allow_stack_execution(self):
            """When this bit is set, all stacks in the task will be given stack execution privilege.  Only used in MH_EXECUTE filetypes."""
            if hasattr(self, '_m_allow_stack_execution'):
                return self._m_allow_stack_execution

            self._m_allow_stack_execution = (self.value & 131072) != 0
            return getattr(self, '_m_allow_stack_execution', None)

        @property
        def binds_to_weak(self):
            """the final linked image uses weak symbols."""
            if hasattr(self, '_m_binds_to_weak'):
                return self._m_binds_to_weak

            self._m_binds_to_weak = (self.value & 65536) != 0
            return getattr(self, '_m_binds_to_weak', None)

        @property
        def no_fix_prebinding(self):
            """do not have dyld notify the prebinding agent about this executable."""
            if hasattr(self, '_m_no_fix_prebinding'):
                return self._m_no_fix_prebinding

            self._m_no_fix_prebinding = (self.value & 1024) != 0
            return getattr(self, '_m_no_fix_prebinding', None)

        @property
        def dyld_link(self):
            """the object file is input for the dynamic linker and can't be staticly link edited again."""
            if hasattr(self, '_m_dyld_link'):
                return self._m_dyld_link

            self._m_dyld_link = (self.value & 4) != 0
            return getattr(self, '_m_dyld_link', None)

        @property
        def pie(self):
            """When this bit is set, the OS will load the main executable at a random address. Only used in MH_EXECUTE filetypes."""
            if hasattr(self, '_m_pie'):
                return self._m_pie

            self._m_pie = (self.value & 2097152) != 0
            return getattr(self, '_m_pie', None)


    class RoutinesCommand64(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.init_address = self._io.read_u8le()
            self.init_module = self._io.read_u8le()
            self.reserved = self._io.read_bytes(48)


    class LinkerOptionCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_strings = self._io.read_u4le()
            self.strings = []
            for i in range(self.num_strings):
                self.strings.append((self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8"))



    class SegmentCommand64(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.segname = (KaitaiStream.bytes_strip_right(self._io.read_bytes(16), 0)).decode(u"ascii")
            self.vmaddr = self._io.read_u8le()
            self.vmsize = self._io.read_u8le()
            self.fileoff = self._io.read_u8le()
            self.filesize = self._io.read_u8le()
            self.maxprot = MachO.VmProt(self._io, self, self._root)
            self.initprot = MachO.VmProt(self._io, self, self._root)
            self.nsects = self._io.read_u4le()
            self.flags = self._io.read_u4le()
            self.sections = []
            for i in range(self.nsects):
                self.sections.append(MachO.SegmentCommand64.Section64(self._io, self, self._root))


        class Section64(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
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
                    self._read()

                def _read(self):
                    self.items = []
                    i = 0
                    while not self._io.is_eof():
                        self.items.append(MachO.SegmentCommand64.Section64.CfString(self._io, self, self._root))
                        i += 1



            class CfString(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.isa = self._io.read_u8le()
                    self.info = self._io.read_u8le()
                    self.data = self._io.read_u8le()
                    self.length = self._io.read_u8le()


            class EhFrameItem(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.length = self._io.read_u4le()
                    if self.length == 4294967295:
                        self.length64 = self._io.read_u8le()

                    self.id = self._io.read_u4le()
                    if self.length > 0:
                        _on = self.id
                        if _on == 0:
                            self._raw_body = self._io.read_bytes((self.length - 4))
                            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                            self.body = MachO.SegmentCommand64.Section64.EhFrameItem.Cie(_io__raw_body, self, self._root)
                        else:
                            self.body = self._io.read_bytes((self.length - 4))


                class CharChain(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.chr = self._io.read_u1()
                        if self.chr != 0:
                            self.next = MachO.SegmentCommand64.Section64.EhFrameItem.CharChain(self._io, self, self._root)



                class Cie(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.version = self._io.read_u1()
                        self.aug_str = MachO.SegmentCommand64.Section64.EhFrameItem.CharChain(self._io, self, self._root)
                        self.code_alignment_factor = MachO.Uleb128(self._io, self, self._root)
                        self.data_alignment_factor = MachO.Uleb128(self._io, self, self._root)
                        self.return_address_register = self._io.read_u1()
                        if self.aug_str.chr == 122:
                            self.augmentation = MachO.SegmentCommand64.Section64.EhFrameItem.AugmentationEntry(self._io, self, self._root)



                class AugmentationEntry(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.length = MachO.Uleb128(self._io, self, self._root)
                        if self._parent.aug_str.next.chr == 82:
                            self.fde_pointer_encoding = self._io.read_u1()




            class EhFrame(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.items = []
                    i = 0
                    while not self._io.is_eof():
                        self.items.append(MachO.SegmentCommand64.Section64.EhFrameItem(self._io, self, self._root))
                        i += 1



            class PointerList(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.items = []
                    i = 0
                    while not self._io.is_eof():
                        self.items.append(self._io.read_u8le())
                        i += 1



            class StringList(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.strings = []
                    i = 0
                    while not self._io.is_eof():
                        self.strings.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ascii"))
                        i += 1



            @property
            def data(self):
                if hasattr(self, '_m_data'):
                    return self._m_data

                io = self._root._io
                _pos = io.pos()
                io.seek(self.offset)
                _on = self.sect_name
                if _on == u"__objc_nlclslist":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.PointerList(_io__raw__m_data, self, self._root)
                elif _on == u"__objc_methname":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.StringList(_io__raw__m_data, self, self._root)
                elif _on == u"__nl_symbol_ptr":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.PointerList(_io__raw__m_data, self, self._root)
                elif _on == u"__la_symbol_ptr":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.PointerList(_io__raw__m_data, self, self._root)
                elif _on == u"__objc_selrefs":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.PointerList(_io__raw__m_data, self, self._root)
                elif _on == u"__cstring":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.StringList(_io__raw__m_data, self, self._root)
                elif _on == u"__objc_classlist":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.PointerList(_io__raw__m_data, self, self._root)
                elif _on == u"__objc_protolist":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.PointerList(_io__raw__m_data, self, self._root)
                elif _on == u"__objc_imageinfo":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.PointerList(_io__raw__m_data, self, self._root)
                elif _on == u"__objc_methtype":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.StringList(_io__raw__m_data, self, self._root)
                elif _on == u"__cfstring":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.CfStringList(_io__raw__m_data, self, self._root)
                elif _on == u"__objc_classrefs":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.PointerList(_io__raw__m_data, self, self._root)
                elif _on == u"__objc_protorefs":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.PointerList(_io__raw__m_data, self, self._root)
                elif _on == u"__objc_classname":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.StringList(_io__raw__m_data, self, self._root)
                elif _on == u"__got":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.PointerList(_io__raw__m_data, self, self._root)
                elif _on == u"__eh_frame":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.EhFrame(_io__raw__m_data, self, self._root)
                elif _on == u"__objc_superrefs":
                    self._raw__m_data = io.read_bytes(self.size)
                    _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                    self._m_data = MachO.SegmentCommand64.Section64.PointerList(_io__raw__m_data, self, self._root)
                else:
                    self._m_data = io.read_bytes(self.size)
                io.seek(_pos)
                return getattr(self, '_m_data', None)



    class VmProt(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.strip_read = self._io.read_bits_int_be(1) != 0
            self.is_mask = self._io.read_bits_int_be(1) != 0
            self.reserved0 = self._io.read_bits_int_be(1) != 0
            self.copy = self._io.read_bits_int_be(1) != 0
            self.no_change = self._io.read_bits_int_be(1) != 0
            self.execute = self._io.read_bits_int_be(1) != 0
            self.write = self._io.read_bits_int_be(1) != 0
            self.read = self._io.read_bits_int_be(1) != 0
            self.reserved1 = self._io.read_bits_int_be(24)


    class DysymtabCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
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
                return self._m_indirect_symbols

            io = self._root._io
            _pos = io.pos()
            io.seek(self.indirect_sym_off)
            self._m_indirect_symbols = []
            for i in range(self.n_indirect_syms):
                self._m_indirect_symbols.append(io.read_u4le())

            io.seek(_pos)
            return getattr(self, '_m_indirect_symbols', None)


    class MachHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cputype = KaitaiStream.resolve_enum(MachO.CpuType, self._io.read_u4le())
            self.cpusubtype = self._io.read_u4le()
            self.filetype = KaitaiStream.resolve_enum(MachO.FileType, self._io.read_u4le())
            self.ncmds = self._io.read_u4le()
            self.sizeofcmds = self._io.read_u4le()
            self.flags = self._io.read_u4le()
            if  ((self._root.magic == MachO.MagicType.macho_be_x64) or (self._root.magic == MachO.MagicType.macho_le_x64)) :
                self.reserved = self._io.read_u4le()


        @property
        def flags_obj(self):
            if hasattr(self, '_m_flags_obj'):
                return self._m_flags_obj

            self._m_flags_obj = MachO.MachoFlags(self.flags, self._io, self, self._root)
            return getattr(self, '_m_flags_obj', None)


    class LinkeditDataCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data_off = self._io.read_u4le()
            self.data_size = self._io.read_u4le()


    class SubCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = MachO.LcStr(self._io, self, self._root)


    class TwolevelHintsCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.offset = self._io.read_u4le()
            self.num_hints = self._io.read_u4le()


    class Version(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.p1 = self._io.read_u1()
            self.minor = self._io.read_u1()
            self.major = self._io.read_u1()
            self.release = self._io.read_u1()


    class EncryptionInfoCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cryptoff = self._io.read_u4le()
            self.cryptsize = self._io.read_u4le()
            self.cryptid = self._io.read_u4le()
            if  ((self._root.magic == MachO.MagicType.macho_be_x64) or (self._root.magic == MachO.MagicType.macho_le_x64)) :
                self.pad = self._io.read_u4le()



    class CodeSignatureCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data_off = self._io.read_u4le()
            self.data_size = self._io.read_u4le()

        @property
        def code_signature(self):
            if hasattr(self, '_m_code_signature'):
                return self._m_code_signature

            io = self._root._io
            _pos = io.pos()
            io.seek(self.data_off)
            self._raw__m_code_signature = io.read_bytes(self.data_size)
            _io__raw__m_code_signature = KaitaiStream(BytesIO(self._raw__m_code_signature))
            self._m_code_signature = MachO.CsBlob(_io__raw__m_code_signature, self, self._root)
            io.seek(_pos)
            return getattr(self, '_m_code_signature', None)


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
            self._read()

        def _read(self):
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
                self._read()

            def _read(self):
                self.items = []
                i = 0
                while True:
                    _ = MachO.DyldInfoCommand.RebaseData.RebaseItem(self._io, self, self._root)
                    self.items.append(_)
                    if _.opcode == MachO.DyldInfoCommand.RebaseData.Opcode.done:
                        break
                    i += 1

            class RebaseItem(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.opcode_and_immediate = self._io.read_u1()
                    if  ((self.opcode == MachO.DyldInfoCommand.RebaseData.Opcode.set_segment_and_offset_uleb) or (self.opcode == MachO.DyldInfoCommand.RebaseData.Opcode.add_address_uleb) or (self.opcode == MachO.DyldInfoCommand.RebaseData.Opcode.do_rebase_uleb_times) or (self.opcode == MachO.DyldInfoCommand.RebaseData.Opcode.do_rebase_add_address_uleb) or (self.opcode == MachO.DyldInfoCommand.RebaseData.Opcode.do_rebase_uleb_times_skipping_uleb)) :
                        self.uleb = MachO.Uleb128(self._io, self, self._root)

                    if self.opcode == MachO.DyldInfoCommand.RebaseData.Opcode.do_rebase_uleb_times_skipping_uleb:
                        self.skip = MachO.Uleb128(self._io, self, self._root)


                @property
                def opcode(self):
                    if hasattr(self, '_m_opcode'):
                        return self._m_opcode

                    self._m_opcode = KaitaiStream.resolve_enum(MachO.DyldInfoCommand.RebaseData.Opcode, (self.opcode_and_immediate & 240))
                    return getattr(self, '_m_opcode', None)

                @property
                def immediate(self):
                    if hasattr(self, '_m_immediate'):
                        return self._m_immediate

                    self._m_immediate = (self.opcode_and_immediate & 15)
                    return getattr(self, '_m_immediate', None)



        class BindItem(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.opcode_and_immediate = self._io.read_u1()
                if  ((self.opcode == MachO.DyldInfoCommand.BindOpcode.set_dylib_ordinal_uleb) or (self.opcode == MachO.DyldInfoCommand.BindOpcode.set_append_sleb) or (self.opcode == MachO.DyldInfoCommand.BindOpcode.set_segment_and_offset_uleb) or (self.opcode == MachO.DyldInfoCommand.BindOpcode.add_address_uleb) or (self.opcode == MachO.DyldInfoCommand.BindOpcode.do_bind_add_address_uleb) or (self.opcode == MachO.DyldInfoCommand.BindOpcode.do_bind_uleb_times_skipping_uleb)) :
                    self.uleb = MachO.Uleb128(self._io, self, self._root)

                if self.opcode == MachO.DyldInfoCommand.BindOpcode.do_bind_uleb_times_skipping_uleb:
                    self.skip = MachO.Uleb128(self._io, self, self._root)

                if self.opcode == MachO.DyldInfoCommand.BindOpcode.set_symbol_trailing_flags_immediate:
                    self.symbol = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")


            @property
            def opcode(self):
                if hasattr(self, '_m_opcode'):
                    return self._m_opcode

                self._m_opcode = KaitaiStream.resolve_enum(MachO.DyldInfoCommand.BindOpcode, (self.opcode_and_immediate & 240))
                return getattr(self, '_m_opcode', None)

            @property
            def immediate(self):
                if hasattr(self, '_m_immediate'):
                    return self._m_immediate

                self._m_immediate = (self.opcode_and_immediate & 15)
                return getattr(self, '_m_immediate', None)


        class BindData(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.items = []
                i = 0
                while not self._io.is_eof():
                    self.items.append(MachO.DyldInfoCommand.BindItem(self._io, self, self._root))
                    i += 1



        class ExportNode(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.terminal_size = MachO.Uleb128(self._io, self, self._root)
                self.children_count = self._io.read_u1()
                self.children = []
                for i in range(self.children_count):
                    self.children.append(MachO.DyldInfoCommand.ExportNode.Child(self._io, self, self._root))

                self.terminal = self._io.read_bytes(self.terminal_size.value)

            class Child(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
                    self.node_offset = MachO.Uleb128(self._io, self, self._root)

                @property
                def value(self):
                    if hasattr(self, '_m_value'):
                        return self._m_value

                    _pos = self._io.pos()
                    self._io.seek(self.node_offset.value)
                    self._m_value = MachO.DyldInfoCommand.ExportNode(self._io, self, self._root)
                    self._io.seek(_pos)
                    return getattr(self, '_m_value', None)



        @property
        def bind(self):
            if hasattr(self, '_m_bind'):
                return self._m_bind

            if self.bind_size != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.bind_off)
                self._raw__m_bind = io.read_bytes(self.bind_size)
                _io__raw__m_bind = KaitaiStream(BytesIO(self._raw__m_bind))
                self._m_bind = MachO.DyldInfoCommand.BindData(_io__raw__m_bind, self, self._root)
                io.seek(_pos)

            return getattr(self, '_m_bind', None)

        @property
        def exports(self):
            if hasattr(self, '_m_exports'):
                return self._m_exports

            if self.export_size != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.export_off)
                self._raw__m_exports = io.read_bytes(self.export_size)
                _io__raw__m_exports = KaitaiStream(BytesIO(self._raw__m_exports))
                self._m_exports = MachO.DyldInfoCommand.ExportNode(_io__raw__m_exports, self, self._root)
                io.seek(_pos)

            return getattr(self, '_m_exports', None)

        @property
        def weak_bind(self):
            if hasattr(self, '_m_weak_bind'):
                return self._m_weak_bind

            if self.weak_bind_size != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.weak_bind_off)
                self._raw__m_weak_bind = io.read_bytes(self.weak_bind_size)
                _io__raw__m_weak_bind = KaitaiStream(BytesIO(self._raw__m_weak_bind))
                self._m_weak_bind = MachO.DyldInfoCommand.BindData(_io__raw__m_weak_bind, self, self._root)
                io.seek(_pos)

            return getattr(self, '_m_weak_bind', None)

        @property
        def rebase(self):
            if hasattr(self, '_m_rebase'):
                return self._m_rebase

            if self.rebase_size != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.rebase_off)
                self._raw__m_rebase = io.read_bytes(self.rebase_size)
                _io__raw__m_rebase = KaitaiStream(BytesIO(self._raw__m_rebase))
                self._m_rebase = MachO.DyldInfoCommand.RebaseData(_io__raw__m_rebase, self, self._root)
                io.seek(_pos)

            return getattr(self, '_m_rebase', None)

        @property
        def lazy_bind(self):
            if hasattr(self, '_m_lazy_bind'):
                return self._m_lazy_bind

            if self.lazy_bind_size != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.lazy_bind_off)
                self._raw__m_lazy_bind = io.read_bytes(self.lazy_bind_size)
                _io__raw__m_lazy_bind = KaitaiStream(BytesIO(self._raw__m_lazy_bind))
                self._m_lazy_bind = MachO.DyldInfoCommand.BindData(_io__raw__m_lazy_bind, self, self._root)
                io.seek(_pos)

            return getattr(self, '_m_lazy_bind', None)


    class DylinkerCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = MachO.LcStr(self._io, self, self._root)


    class DylibCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name_offset = self._io.read_u4le()
            self.timestamp = self._io.read_u4le()
            self.current_version = self._io.read_u4le()
            self.compatibility_version = self._io.read_u4le()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")


    class SegmentCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.segname = (KaitaiStream.bytes_strip_right(self._io.read_bytes(16), 0)).decode(u"ascii")
            self.vmaddr = self._io.read_u4le()
            self.vmsize = self._io.read_u4le()
            self.fileoff = self._io.read_u4le()
            self.filesize = self._io.read_u4le()
            self.maxprot = MachO.VmProt(self._io, self, self._root)
            self.initprot = MachO.VmProt(self._io, self, self._root)
            self.nsects = self._io.read_u4le()
            self.flags = self._io.read_u4le()
            self.sections = []
            for i in range(self.nsects):
                self.sections.append(MachO.SegmentCommand.Section(self._io, self, self._root))


        class Section(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.sect_name = (KaitaiStream.bytes_strip_right(self._io.read_bytes(16), 0)).decode(u"ascii")
                self.seg_name = (KaitaiStream.bytes_strip_right(self._io.read_bytes(16), 0)).decode(u"ascii")
                self.addr = self._io.read_u4le()
                self.size = self._io.read_u4le()
                self.offset = self._io.read_u4le()
                self.align = self._io.read_u4le()
                self.reloff = self._io.read_u4le()
                self.nreloc = self._io.read_u4le()
                self.flags = self._io.read_u4le()
                self.reserved1 = self._io.read_u4le()
                self.reserved2 = self._io.read_u4le()

            @property
            def data(self):
                if hasattr(self, '_m_data'):
                    return self._m_data

                io = self._root._io
                _pos = io.pos()
                io.seek(self.offset)
                self._m_data = io.read_bytes(self.size)
                io.seek(_pos)
                return getattr(self, '_m_data', None)



    class LcStr(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = self._io.read_u4le()
            self.value = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")


    class LoadCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(MachO.LoadCommandType, self._io.read_u4le())
            self.size = self._io.read_u4le()
            _on = self.type
            if _on == MachO.LoadCommandType.id_dylinker:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.DylinkerCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.reexport_dylib:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.DylibCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.build_version:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.BuildVersionCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.source_version:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.SourceVersionCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.function_starts:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.LinkeditDataCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.rpath:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.RpathCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.sub_framework:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.SubCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.routines:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.RoutinesCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.sub_library:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.SubCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.dyld_info_only:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.DyldInfoCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.dyld_environment:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.DylinkerCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.load_dylinker:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.DylinkerCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.segment_split_info:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.LinkeditDataCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.main:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.EntryPointCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.load_dylib:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.DylibCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.encryption_info:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.EncryptionInfoCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.dysymtab:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.DysymtabCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.twolevel_hints:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.TwolevelHintsCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.encryption_info_64:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.EncryptionInfoCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.linker_option:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.LinkerOptionCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.dyld_info:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.DyldInfoCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.version_min_tvos:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.VersionMinCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.load_upward_dylib:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.DylibCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.segment_64:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.SegmentCommand64(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.segment:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.SegmentCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.sub_umbrella:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.SubCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.version_min_watchos:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.VersionMinCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.routines_64:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.RoutinesCommand64(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.id_dylib:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.DylibCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.sub_client:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.SubCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.dylib_code_sign_drs:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.LinkeditDataCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.symtab:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.SymtabCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.linker_optimization_hint:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.LinkeditDataCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.data_in_code:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.LinkeditDataCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.code_signature:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.CodeSignatureCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.version_min_iphoneos:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.VersionMinCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.load_weak_dylib:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.DylibCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.lazy_load_dylib:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.DylibCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.uuid:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.UuidCommand(_io__raw_body, self, self._root)
            elif _on == MachO.LoadCommandType.version_min_macosx:
                self._raw_body = self._io.read_bytes((self.size - 8))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MachO.VersionMinCommand(_io__raw_body, self, self._root)
            else:
                self.body = self._io.read_bytes((self.size - 8))


    class UuidCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.uuid = self._io.read_bytes(16)


    class SymtabCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sym_off = self._io.read_u4le()
            self.n_syms = self._io.read_u4le()
            self.str_off = self._io.read_u4le()
            self.str_size = self._io.read_u4le()

        class StrTable(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.unknown = self._io.read_u4le()
                self.items = []
                i = 0
                while True:
                    _ = (self._io.read_bytes_term(0, False, True, False)).decode(u"utf-8")
                    self.items.append(_)
                    if _ == u"":
                        break
                    i += 1


        class Nlist64(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.un = self._io.read_u4le()
                self.type = self._io.read_u1()
                self.sect = self._io.read_u1()
                self.desc = self._io.read_u2le()
                self.value = self._io.read_u8le()

            @property
            def name(self):
                if hasattr(self, '_m_name'):
                    return self._m_name

                if self.un != 0:
                    _pos = self._io.pos()
                    self._io.seek((self._parent.str_off + self.un))
                    self._m_name = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")
                    self._io.seek(_pos)

                return getattr(self, '_m_name', None)


        class Nlist(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.un = self._io.read_u4le()
                self.type = self._io.read_u1()
                self.sect = self._io.read_u1()
                self.desc = self._io.read_u2le()
                self.value = self._io.read_u4le()

            @property
            def name(self):
                if hasattr(self, '_m_name'):
                    return self._m_name

                if self.un != 0:
                    _pos = self._io.pos()
                    self._io.seek((self._parent.str_off + self.un))
                    self._m_name = (self._io.read_bytes_term(0, False, True, True)).decode(u"utf-8")
                    self._io.seek(_pos)

                return getattr(self, '_m_name', None)


        @property
        def symbols(self):
            if hasattr(self, '_m_symbols'):
                return self._m_symbols

            io = self._root._io
            _pos = io.pos()
            io.seek(self.sym_off)
            self._m_symbols = []
            for i in range(self.n_syms):
                _on = self._root.magic
                if _on == MachO.MagicType.macho_le_x64:
                    self._m_symbols.append(MachO.SymtabCommand.Nlist64(io, self, self._root))
                elif _on == MachO.MagicType.macho_be_x64:
                    self._m_symbols.append(MachO.SymtabCommand.Nlist64(io, self, self._root))
                elif _on == MachO.MagicType.macho_le_x86:
                    self._m_symbols.append(MachO.SymtabCommand.Nlist(io, self, self._root))
                elif _on == MachO.MagicType.macho_be_x86:
                    self._m_symbols.append(MachO.SymtabCommand.Nlist(io, self, self._root))

            io.seek(_pos)
            return getattr(self, '_m_symbols', None)

        @property
        def strs(self):
            if hasattr(self, '_m_strs'):
                return self._m_strs

            io = self._root._io
            _pos = io.pos()
            io.seek(self.str_off)
            self._raw__m_strs = io.read_bytes(self.str_size)
            _io__raw__m_strs = KaitaiStream(BytesIO(self._raw__m_strs))
            self._m_strs = MachO.SymtabCommand.StrTable(_io__raw__m_strs, self, self._root)
            io.seek(_pos)
            return getattr(self, '_m_strs', None)


    class VersionMinCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = MachO.Version(self._io, self, self._root)
            self.sdk = MachO.Version(self._io, self, self._root)


    class EntryPointCommand(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entry_off = self._io.read_u8le()
            self.stack_size = self._io.read_u8le()



