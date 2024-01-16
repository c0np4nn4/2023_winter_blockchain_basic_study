from dataclasses import dataclass, asdict
from typing import assert_type
from hashlib import sha256
from pymerkle import InmemoryTree as MerkleTree
from time import time_ns


@dataclass
class BlockHeader:
    version: str
    timestamp: str
    index: int
    previous_hash: str
    merkle_hash: str


@dataclass
class BlockData:
    msg: str


@dataclass
class Block:
    Header: BlockHeader
    Data: BlockData


def convert_to_dict(block: Block):
    return {k: v for k, v in asdict(block).items()}


def gen_genesis_block():
    # block data
    msg = "Gensis Block"

    # block header
    version = str(1)
    timestamp = str(time_ns())
    index = 0
    previous_hash = "0" * 64
    merkle_hash = gen_merkle_root(msg.encode()).hex()

    # header
    block_header = gen_block_header(
        version, timestamp, index, previous_hash, merkle_hash
    )

    # data
    block_data = gen_block_data(msg)
    block = gen_block(block_header, block_data)

    return block


def gen_block_header(
    version: str,
    timestamp: str,
    index: int,
    previous_hash: str,
    merkle_hash: str,
):
    return BlockHeader(
        version, timestamp, index, previous_hash, merkle_hash
    )


def gen_block_data(msg: str):
    return BlockData(msg)


def gen_block(header: BlockHeader, data: BlockData) -> Block:
    block = Block(header, data)
    return block


def validate_block(block: Block):
    # type checking
    assert_type(block.Header.version, str)
    assert_type(block.Header.timestamp, str)
    assert_type(block.Header.index, int)
    assert_type(block.Header.previous_hash, str)
    assert_type(block.Header.merkle_hash, str)
    assert_type(block.Data.msg, str)


def gen_block_hash(previous_block_header: BlockHeader):
    header_data = ""
    header_data += previous_block_header.version
    header_data += previous_block_header.timestamp
    header_data += str(previous_block_header.index)
    header_data += str(previous_block_header.previous_hash)
    header_data += str(previous_block_header.merkle_hash)
    return sha256(header_data.encode()).digest().hex()


def gen_merkle_root(data: bytes) -> bytes:
    tree = MerkleTree(algorithm="sha256")
    tree.append_entry(data)
    return tree.get_state()
