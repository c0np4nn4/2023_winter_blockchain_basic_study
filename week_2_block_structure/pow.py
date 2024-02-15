from block import gen_block_hash, gen_block_header, gen_merkle_root
from block import BlockHeader
from time import time_ns

version = str(1)
timestamp = str(time_ns())
index = 0
previous_hash = "0" * 64
merkle_hash = gen_merkle_root("pow".encode()).hex()

block_header = gen_block_header(
    version, timestamp, index, previous_hash, merkle_hash
)

hash = gen_block_hash(block_header)

print(hash)

while True:
    # ...
# ..
