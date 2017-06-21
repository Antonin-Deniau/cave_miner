# CAVE MINER
This tools search for code cave in binaries (Elf, Mach-o, Pe), and inject code in them.

### Installation
/!\ Only work in python2.x /!\

```bash
pip install cave-miner
```

### Usage

```
> cave_miner --help
    /========\
   /    ||    \
        ||
        ||
        ||
   CAVE || MINER

Search for code cave in all binaries
Usage:
  cave_miner search [--size=<size>]
                  [--bytes=<bytes>]... <file_name>
  cave_miner inject <payload> <file_name> <address>

Options:
  -h --help        Show this help
  --version        Show the program version
  --size=<size>    The minimum size of the cave in bytes [default: 256]
  --bytes=<bytes>  The bytes used in the code cave [default: 0x00]
```

### Exemple

```
> cave_miner search ~/Downloads/putty.exe

    /========\
   /    ||    \
        ||
        ||
        ||
   CAVE || MINER

[*] Starting cave mining process...
    Searching for bytes: 0x00...

[*] New cave detected !
  section_name: .rdata
  cave_begin:   0x0009a314
  cave_end:     0x0009a418
  cave_size:    0x00000104
  vaddress:     0x0009b514
  infos:        Readable, Contain initialized data

[*] New cave detected !
  section_name: .rdata
  cave_begin:   0x0009a517
  cave_end:     0x0009a618
  cave_size:    0x00000101
  vaddress:     0x0009b717
  infos:        Readable, Contain initialized data

[*] New cave detected !
  section_name: .data
  cave_begin:   0x000a0ae5
  cave_end:     0x000a0c3c
  cave_size:    0x00000157
  vaddress:     0x000a20e5
  infos:        Readable, Writeable, Contain initialized data

[*] Mining finished.
```
