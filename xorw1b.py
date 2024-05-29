from argparse import ArgumentParser, RawTextHelpFormatter

def xorw1b(buf: bytes) -> bytes:
	x = buf[0]
	return bytes([b^x for b in buf[1:]])
	
	
def main():
	parser = ArgumentParser(
		description="""
		Ciphers the input buffer taking the first byte apart then xoring each byte using this first byte.
		Returns a '.xored' file containing the xored result, first byte removed.
		Overwrites the output file.
		""",
		formatter_class=RawTextHelpFormatter
	)
	parser.add_argument("filename", help="the input file containing the raw input buffer as bytes")
	args = parser.parse_args()
	
	with open(args.filename, mode="rb") as f:
		buf = f.read()
	outbuf = xorw1b(buf)
	with open(args.filename+".xored", mode="wb") as f:
		f.write(outbuf)	


if __name__=="__main__":
	main()