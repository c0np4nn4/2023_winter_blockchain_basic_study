from time import time_ns
from hashlib import sha256
from block import (
    gen_merkle_root,
    gen_block_header,
    gen_block_data,
    gen_block,
    gen_block_hash,
    BlockHeader,
)
from ledger import (
    ledger_init,
    ledger_append,
    get_latest_block,
    LEDGER_PATH,
)
from dacite import from_dict
import os

# 1. Init ledger
if not os.path.exists(LEDGER_PATH):
    ledger_init()

else:
    latest_block = get_latest_block()
    latest_block_header = latest_block["Header"]
    latest_block_data = latest_block["Data"]

    # 2. generate new block
    # block data
    msg = input("Input your msg>> ")

    # block header
    version = str(1)
    timestamp = str(time_ns())
    index = latest_block_header["index"] + 1
    previous_hash = gen_block_hash(
        from_dict(data_class=BlockHeader, data=latest_block_header)
    )
    merkle_hash = gen_merkle_root(msg.encode()).hex()
    block_header = gen_block_header(
        version, timestamp, index, previous_hash, merkle_hash
    )
    block_data = gen_block_data(msg)
    block = gen_block(block_header, block_data)

    # append ledger
    ledger_append(block)
