# Week2
## Block Structure
- Block Header
    - Version
    - Timestamp
    - Index
    - Previous Hash (sha256)
    - Merkle Root Hash
- Block Data
    - Msg

## Funcitons
- `ledger.py`
    - *ledger_init()*
    - *ledger_append(block: Block)*
    - *get_latest_block*
- `block.py`
    - *convert_to_dict(block: Block)*
    - *gen_genesis_block()*
    - *gen_block_header()*
    - *gen_block_data(msg: bytes)*
    - *gen_block(header: BlockHeader, data: BlockData) -> Block*
    - *validate_block(block: Block)*
    - *gen_block_hash(previous_block_header: BlockHeader)*
    - *gen_merkle_root(data: bytes) -> bytes*

## Test
- run `test.py` will create a new `ledger.json` file.
```bash
$ python3 test.py
New ledger file created:  [{'Header': {'version': '1', 'timestamp': '1705367949566172000',
'index': 0, 'previous_hash': '000000000000000000000000000000000000000000000000000000000000
0000', 'merkle_hash': 'cd413729e479ad0065c8270dc1c113d86ead1857f8f769f7333abc49434c5e82'},
'Data': {'msg': 'Gensis Block'}}]
```

- `ledger.json` contains the blocks information
```json
[
  {
    "Header": {
      "version": "1",
      "timestamp": "1705367949566172000",
      "index": 0,
      "previous_hash": "0000000000000000000000000000000000000000000000000000000000000000",
      "merkle_hash": "cd413729e479ad0065c8270dc1c113d86ead1857f8f769f7333abc49434c5e82"
    },
    "Data": {
      "msg": "Gensis Block"
    }
  }
]
```

- you can append the block run `test.py` again
```
$ python3 test.py
Input your msg>> Hello World!
```

- `ledger.json` updated
```json
[
  {
    "Header": {
      "version": "1",
      "timestamp": "1705367949566172000",
      "index": 0,
      "previous_hash": "0000000000000000000000000000000000000000000000000000000000000000",
      "merkle_hash": "cd413729e479ad0065c8270dc1c113d86ead1857f8f769f7333abc49434c5e82"
    },
    "Data": {
      "msg": "Gensis Block"
    }
  },
  {
    "Header": {
      "version": "1",
      "timestamp": "1705368144748889000",
      "index": 1,
      "previous_hash": "a6b8321b8aaacc11bb308620c906d9175de31ee9a894660c13c9fec433ee40e2",
      "merkle_hash": "fe75e33a23f0d8a14cbd71f5d2c664b73d467a00aa1f7c132aab1a0bfa3f8f50"
    },
    "Data": {
      "msg": "Hello World!"
    }
  }
]
```
