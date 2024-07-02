#!/usr/bin/python3

from pathlib import Path
from binascii import unhexlify
from argparse import ArgumentParser


def xor_buf(buf, key):
    kl = len(key)
    abuf = bytearray(buf)
    for i in range(len(abuf)):
        abuf[i] ^= key[i % kl]
    return bytes(abuf)


def xor_fp(fp, key):
    data = fp.read_bytes()
    xdata = xor_buf(data, key)
    fp.write_bytes(xdata)


if __name__ == "__main__":
    parser = ArgumentParser(description="xor file with key")
    parser.add_argument("filename", help="input file")
    parser.add_argument("-k", "--key", required=True, help="Secret key")
    args = parser.parse_args()
    xor_fp(Path(args.filename), unhexlify(args.key))
