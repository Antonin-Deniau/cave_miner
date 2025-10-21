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


def test_pe_parser():
    """Test PE parser with a real binary"""
    print("=" * 60)
    print("TEST 2: PE Parser")
    print("=" * 60)

    # Look for a PE binary (might not exist on Linux)
    pe_locations = [
        "/usr/share/wine/wine/notepad.exe",
        "/usr/lib/wine/notepad.exe",
    ]

    pe_binary = None
    for location in pe_locations:
        if os.path.exists(location):
            pe_binary = location
            break

    if not pe_binary:
        print("❌ SKIP: No PE binary found (expected on Linux)")
        print("   To test PE parser, provide a Windows .exe file\n")
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


def test_macho_parser():
    """Test Mach-O parser with a real binary"""
    print("=" * 60)
    print("TEST 3: Mach-O Parser")
    print("=" * 60)

    # Mach-O binaries are typically on macOS, won't exist on Linux
    macho_binary = "/bin/ls"  # Would be Mach-O on macOS

    # Check if it's actually a Mach-O file
    if os.path.exists(macho_binary):
        with open(macho_binary, 'rb') as f:
            magic = f.read(4)
            if magic == b'\xfe\xed\xfa\xcf' or magic == b'\xfe\xed\xfa\xce':
                is_macho = True
            else:
                is_macho = False
    else:
        is_macho = False

    if not is_macho:
        print("❌ SKIP: No Mach-O binary found (expected on non-macOS)")
        print("   To test Mach-O parser, provide a macOS binary\n")
        return None

    try:
        print(f"Testing with: {macho_binary}")
        macho = MachO.from_file(macho_binary)

        print(f"✓ Successfully parsed Mach-O binary")
        print(f"✓ Number of load commands: {len(macho.load_commands)}")

        # Display segments
        segment_count = 0
        for cmd in macho.load_commands:
            if cmd.type == MachO.LoadCommandType.segment_64:
                segment_count += 1
                if cmd.body and cmd.body.sections:
                    print(f"\nSegment {segment_count} sections:")
                    for section in cmd.body.sections[:3]:
                        print(f"  {section.seg_name}.{section.sect_name:20s} - addr: 0x{section.addr:08x}")

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
