"""Search for code cave in all binaries
Usage:
  cave_miner search [--size=<size>]
                    [--bytes=<bytes>]... <file_name>
  cave_miner inject <payload> <file_name> <address>

Options:
  -h --help        Show this help
  --version        Show the program version
  --size=<size>    The minimum size of the cave in bytes [default: 256]
  --bytes=<bytes>  The bytes used in the code cave [default: 0x00]
"""

from docopt import docopt
from .utils import color
from .tests import test_file, test_number, test_bytes
from .search import search
from .inject import inject

BANNER = """
  /========\\
  /    ||    \\
      ||
      ||
      ||
  CAVE || MINER
"""
BANNER = BANNER.replace("/", "{grey}/{endc}")
BANNER = BANNER.replace("\\", "{grey}\\{endc}")
BANNER = BANNER.replace("=", "{grey}={endc}")
BANNER = BANNER.replace("||", "{green}||{endc}")


def main():
    print(color(BANNER))

    args = docopt(__doc__, version="cave_miner 2.0.0")

    if args["search"]:
        ok = test_file(args["<file_name>"])
        ok = ok and test_number(args["--size"])
        ok = ok and test_bytes(args["--bytes"])

        if ok:
            search(args["<file_name>"], args["--size"], args["--bytes"])

    elif args["inject"]:
        ok = test_file(args["<payload>"])
        ok = ok and test_file(args["<file_name>"])
        ok = ok and test_number(args["<address>"])

        if ok:
            inject(args["<payload>"], args["<file_name>"], args["<address>"])


if __name__ == "__main__":
    main()
