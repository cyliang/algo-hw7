# vim: set syntax=python filetype=python:

import msgpack

with open("../input.txt", "wb") as output_file:
	msgpack.pack(6, output_file)
	msgpack.pack([1, 1, 1], output_file)
	msgpack.pack([10, 20], output_file)
	msgpack.pack([3, 6, 10, 9, 2], output_file)
	msgpack.pack([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], output_file)
	msgpack.pack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], output_file)
	msgpack.pack([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], output_file)
