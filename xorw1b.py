#!/usr/bin/python3

import sys
from argparse import ArgumentParser, RawTextHelpFormatter

ELF_MAGIC = b"\x7f\x45\x4c\x46"

def xorw1b(buf: bytes) -> bytes:  # XOR with 1st byte
	b = buf[0]
	return bytes([x^b for x in buf[1:]])
	
	
def process() -> int:
	parser = ArgumentParser(
		description="""
		Cipher the input buffer taking the first byte apart then xoring each byte using this first byte.
		Return a '.xored' file containing the xored result, first byte removed.
		Overwrites the output file.
		""",
		formatter_class=RawTextHelpFormatter
	)
	parser.add_argument("filename", help="the input file containing the raw input buffer as bytes")
	parser.add_argument("-o", "--output-file", action="store", help="specify the target filename, defaults to original filename postfixed with .xored extension")
	parser.add_argument("-e", "--ensure-elf", action="store_true", help="ensure result is an ELF executable")
	args = parser.parse_args()
	if args.output_file is None:
		args.output_file = args.filename+".xored"
	with open(args.filename, mode="rb") as f_in, open(args.output_file, mode="wb") as f_out:
		xored_buf = xorw1b(f_in.read())
		if args.ensure_elf:
			if xored_buf[:4] == ELF_MAGIC:
				print("Output buffer is an ELF executable")
			else:
				print("Output buffer is NOT an ELF executable")
				return 2
		f_out.write(xored_buf)
		print(f"Wrote {len(xored_buf)} bytes to {args.output_file}")
		return 0
	return 1


if __name__=="__main__":
	status: int = process()
	sys.exit(status)
