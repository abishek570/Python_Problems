## COMPRESSION AND DECOMPRESSION OF A STRING

import zlib

inp = "Hello Roshika, I'm John and I'm in love with you!!!"

compress = zlib.compress(inp.encode())

decompress = zlib.decompress(compress).decode()

print(inp)
print(compress)
print(decompress)