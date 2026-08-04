from .utils import color, parse_int


def inject(payload_name: str, file_name: str, straddr: str) -> None:
    print(color("{yellow}[*]{bold} Starting injection into binary...{endc}"))
    print()
    addr = parse_int(straddr)

    payload = open(payload_name, "rb").read()
    vic = open(file_name, "rb").read()

    res = vic[:addr] + payload + vic[addr + len(payload) :]

    f = open("{}.mod".format(file_name), "wb")
    f.write(res)
    f.close()

    print(color("{yellow}[*]{bold} Injection finished.{endc}"))
