from flask import Flask
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'week_2_block_structure')))
# from block import block
from get_block import ledger.py

app = Flask(__name__)

@app.route('/get_block/<block_number>')
def get_block(block_number) -> str:
    return f"Hello! This is Flask for /get_block route. blocknumeber: {block_number}"

@app.route('/ledger_append')
def ledger_append() -> str:
    return "Hello! This is Flask for /ledger_append route."

@app.route('/get_last_block')
def get_last_block() -> str:
    return "Hello! This is Flask for /get_last_block route."

# TODO
# ledger.py 에 있는 함수들 호출할 수 있도록 하기
### [!] get_block
### [ ] get_latest_block
### [ ] ledger_append

# TODO
# block.py 에 있는 함수 중
### [ ] gen_block_header
### [ ] gen_block_data
### [ ] gen_block

if __name__ == '__main__':
    app.run(debug=True)


