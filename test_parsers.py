#!/usr/bin/env python3
"""Test script to verify binary format parsers"""

import sys
import os

# Add the cave_miner directory to the path
sys.path.insert(0, '/home/user/cave_miner')

from cave_miner.formats import Elf, Pe, MachO


def test_elf_parser():
    """Test ELF parser with a real binary"""
    print("=" * 60)
    print("TEST 1: ELF Parser")
    print("=" * 60)

    # Find an ELF binary
    elf_binary = "/bin/ls"

    if not os.path.exists(elf_binary):
        print(f"❌ SKIP: {elf_binary} not found")
        return False

    try:
        print(f"Testing with: {elf_binary}")
        elf = Elf.from_file(elf_binary)

        print(f"✓ Successfully parsed ELF binary")
        print(f"✓ Number of sections: {len(elf.header.section_headers)}")

        # Display some sections
        print("\nFirst 5 sections:")
        for i, section in enumerate(elf.header.section_headers[:5]):
            print(f"  [{i}] {section.name:20s} - addr: 0x{section.addr:08x}, offset: 0x{section.ofs_body:08x}, size: {len(section.body)} bytes")

        print("✅ ELF parser test PASSED\n")
        return True

    except Exception as e:
        print(f"❌ ELF parser test FAILED: {e}\n")
        import traceback
        traceback.print_exc()
        return False


def create_pe_binary(filepath):
    """Create a PE binary using MinGW cross-compiler if available"""
    import subprocess
    import tempfile

    # Check if mingw is available
    try:
        result = subprocess.run(['which', 'x86_64-w64-mingw32-gcc'],
                              capture_output=True, text=True)
        if result.returncode != 0:
            return None
    except:
        return None

    # Create a simple C program
    with tempfile.NamedTemporaryFile(mode='w', suffix='.c', delete=False) as f:
        f.write("""
#include <stdio.h>
int main() {
    printf("Test PE binary\\n");
    return 0;
}
""")
        c_file = f.name

    try:
        # Compile with MinGW
        result = subprocess.run(
            ['x86_64-w64-mingw32-gcc', c_file, '-o', filepath],
            capture_output=True, text=True, timeout=10
        )
        os.unlink(c_file)

        if result.returncode == 0 and os.path.exists(filepath):
            return filepath
        return None
    except:
        if os.path.exists(c_file):
            os.unlink(c_file)
        return None


def test_pe_parser():
    """Test PE parser with a real binary"""
    print("=" * 60)
    print("TEST 2: PE Parser")
    print("=" * 60)

    # Look for existing PE binaries
    pe_locations = [
        "/tmp/test.exe",
        "/usr/share/wine/wine/notepad.exe",
        "/usr/lib/wine/notepad.exe",
    ]

    pe_binary = None
    for location in pe_locations:
        if os.path.exists(location):
            pe_binary = location
            break

    # If no PE binary found, try to create one
    if not pe_binary:
        print("No existing PE binary found, attempting to create one...")
        pe_binary = create_pe_binary("/tmp/test_pe_created.exe")
        if pe_binary:
            print(f"✓ Created test PE binary at {pe_binary}")
        else:
            print("❌ SKIP: Cannot create PE binary (MinGW not available)")
            print("   Install gcc-mingw-w64-x86-64 to enable PE testing\n")
            return None

    try:
        print(f"Testing with: {pe_binary}")
        pe = Pe.from_file(pe_binary)

        print(f"✓ Successfully parsed PE binary")
        print(f"✓ Format: {'PE32' if pe.optional_hdr.std.format == Pe.PeFormat.pe32 else 'PE32+'}")
        print(f"✓ Number of sections: {len(pe.sections)}")
        print(f"✓ Image base: 0x{pe.optional_hdr.windows.image_base_32:08x}")

        # Display sections
        print("\nSections:")
        for section in pe.sections:
            print(f"  {section.name:10s} - vaddr: 0x{section.virtual_address:08x}, raw: 0x{section.pointer_to_raw_data:08x}, size: {section.size_of_raw_data} bytes")

        print("✅ PE parser test PASSED\n")
        return True

    except Exception as e:
        print(f"❌ PE parser test FAILED: {e}\n")
        import traceback
        traceback.print_exc()
        return False


def create_minimal_macho(filepath):
    """Create a minimal valid Mach-O binary with sections for testing"""
    import struct

    # Mach-O 64-bit constants
    MH_MAGIC_64 = 0xFEEDFACF
    CPU_TYPE_X86_64 = 0x01000007
    CPU_SUBTYPE_X86_64_ALL = 0x00000003
    MH_EXECUTE = 0x00000002
    LC_SEGMENT_64 = 0x19
    SECTION_64_SIZE = 80

    data = bytearray()

    # Mach-O header (32 bytes)
    data += struct.pack('<I', MH_MAGIC_64)
    data += struct.pack('<I', CPU_TYPE_X86_64)
    data += struct.pack('<I', CPU_SUBTYPE_X86_64_ALL)
    data += struct.pack('<I', MH_EXECUTE)
    data += struct.pack('<I', 1)  # ncmds
    data += struct.pack('<I', 72 + (2 * SECTION_64_SIZE))  # sizeofcmds
    data += struct.pack('<I', 0)  # flags
    data += struct.pack('<I', 0)  # reserved

    # LC_SEGMENT_64 command
    data += struct.pack('<I', LC_SEGMENT_64)
    data += struct.pack('<I', 72 + (2 * SECTION_64_SIZE))
    data += b'__TEXT\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    data += struct.pack('<Q', 0x100000000)  # vmaddr
    data += struct.pack('<Q', 0x1000)  # vmsize
    data += struct.pack('<Q', 0)  # fileoff
    data += struct.pack('<Q', 0x1000)  # filesize
    data += struct.pack('<I', 7)  # maxprot
    data += struct.pack('<I', 5)  # initprot
    data += struct.pack('<I', 2)  # nsects - 2 sections
    data += struct.pack('<I', 0)  # flags

    # Section 1: __text
    data += b'__text\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    data += b'__TEXT\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    data += struct.pack('<Q', 0x100000000)
    data += struct.pack('<Q', 0x100)
    data += struct.pack('<I', 0x100)
    data += struct.pack('<I', 4)
    data += struct.pack('<I', 0)
    data += struct.pack('<I', 0)
    data += struct.pack('<I', 0x80000400)
    data += struct.pack('<I', 0)
    data += struct.pack('<I', 0)
    data += struct.pack('<I', 0)

    # Section 2: __const
    data += b'__const\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    data += b'__TEXT\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    data += struct.pack('<Q', 0x100000100)
    data += struct.pack('<Q', 0x50)
    data += struct.pack('<I', 0x200)
    data += struct.pack('<I', 3)
    data += struct.pack('<I', 0)
    data += struct.pack('<I', 0)
    data += struct.pack('<I', 0)
    data += struct.pack('<I', 0)
    data += struct.pack('<I', 0)
    data += struct.pack('<I', 0)

    # Pad and add section data
    current_size = len(data)
    data += b'\x00' * (0x100 - current_size)
    # __text section: some code then padding
    data += b'\x90' * 0x50  # Some NOP instructions
    data += b'\x00' * 0xB0  # Large null byte area (176 bytes)
    # __const section: some data then padding
    data += b'Mach-O test data\x00'
    data += b'\x00' * 0x40  # Large null byte area (64 bytes)
    data += b'\x00' * (0x1000 - len(data))

    with open(filepath, 'wb') as f:
        f.write(data)

    return filepath


def test_macho_parser():
    """Test Mach-O parser with a real binary"""
    print("=" * 60)
    print("TEST 3: Mach-O Parser")
    print("=" * 60)

    # Try to find an existing Mach-O binary
    macho_binary = None
    test_paths = ["/bin/ls", "/usr/bin/file"]

    for path in test_paths:
        if os.path.exists(path):
            with open(path, 'rb') as f:
                magic = f.read(4)
                if magic == b'\xfe\xed\xfa\xcf' or magic == b'\xfe\xed\xfa\xce':
                    macho_binary = path
                    break

    # If no Mach-O binary found, create a minimal one
    if not macho_binary:
        print("No native Mach-O binary found, creating test binary...")
        macho_binary = "/tmp/test_macho"
        create_minimal_macho(macho_binary)
        print(f"✓ Created test Mach-O binary at {macho_binary}")

    try:
        print(f"Testing with: {macho_binary}")
        macho = MachO.from_file(macho_binary)

        print(f"✓ Successfully parsed Mach-O binary")
        print(f"✓ Number of load commands: {len(macho.load_commands)}")

        # Display segments and sections
        segment_count = 0
        total_sections = 0
        for cmd in macho.load_commands:
            if cmd.type == MachO.LoadCommandType.segment_64:
                segment_count += 1
                if cmd.body and cmd.body.sections:
                    total_sections += len(cmd.body.sections)
                    print(f"\nSegment {segment_count} - {len(cmd.body.sections)} section(s):")
                    for i, section in enumerate(cmd.body.sections):
                        print(f"  [{i}] {section.seg_name}.{section.sect_name:20s} - addr: 0x{section.addr:016x}, offset: 0x{section.offset:08x}, size: {len(section.data)} bytes")

        print(f"\n✓ Total sections found: {total_sections}")
        print("✅ Mach-O parser test PASSED\n")
        return True

    except Exception as e:
        print(f"❌ Mach-O parser test FAILED: {e}\n")
        import traceback
        traceback.print_exc()
        return False


def test_import():
    """Test that parsers can be imported"""
    print("=" * 60)
    print("TEST 0: Import Test")
    print("=" * 60)

    try:
        from cave_miner.formats import Elf, Pe, MachO
        print("✓ Successfully imported Elf")
        print("✓ Successfully imported Pe")
        print("✓ Successfully imported MachO")
        print("✅ Import test PASSED\n")
        return True
    except Exception as e:
        print(f"❌ Import test FAILED: {e}\n")
        import traceback
        traceback.print_exc()
        return False


def main():
    print("\n" + "=" * 60)
    print("CAVE MINER - Binary Format Parser Tests")
    print("=" * 60 + "\n")

    results = []

    # Test imports
    results.append(("Import", test_import()))

    # Test parsers
    results.append(("ELF Parser", test_elf_parser()))
    results.append(("PE Parser", test_pe_parser()))
    results.append(("Mach-O Parser", test_macho_parser()))

    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    passed = sum(1 for _, result in results if result is True)
    failed = sum(1 for _, result in results if result is False)
    skipped = sum(1 for _, result in results if result is None)

    for name, result in results:
        if result is True:
            status = "✅ PASSED"
        elif result is False:
            status = "❌ FAILED"
        else:
            status = "⊝ SKIPPED"
        print(f"{status}: {name}")

    print(f"\nTotal: {passed} passed, {failed} failed, {skipped} skipped")
    print("=" * 60 + "\n")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
