import os
import json
from block import Block, gen_genesis_block, convert_to_dict
from dataclasses import asdict

LEDGER_PATH = "./ledger.json"


def ledger_init():
    if not os.path.exists(LEDGER_PATH):
        genesis_block = gen_genesis_block()
        new_ledger = [
            {k: v for k, v in asdict(genesis_block).items()}
        ]
        with open(LEDGER_PATH, "w") as ledger:
            json.dump(new_ledger, ledger, indent=2)
            print("New ledger file created: ", new_ledger)
        ledger.close()


def ledger_append(block: Block):
    ledger_data = []
    with open(LEDGER_PATH, "r") as ledger:
        ledger_data = json.load(ledger)
    ledger_data.append(convert_to_dict(block))
    ledger.close()

    # TODO
    # Check the validity of `block`
    # Hint: `block.py` has `validate_block()` function
    # ...

    with open(LEDGER_PATH, "w") as ledger:
        json.dump(ledger_data, ledger, indent=2)
    ledger.close()


def get_latest_block():
    ledger_data = []
    with open(LEDGER_PATH, "r") as ledger:
        ledger_data = json.load(ledger)
    ledger.close()
    return ledger_data[-1]


# TODO
# def get_block(index: int):
