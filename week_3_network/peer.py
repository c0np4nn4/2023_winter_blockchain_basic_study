from flask import Flask

app = Flask(__name__)

@app.route('/get_block')
def hello() -> str:
    return "Hello! This is Flask!";

# @app.route('/ledger_append')
# def hello() -> str:
#     return "Hello! This is Flask!";

# @app.route('/get_last_block')
# def hello() -> str:
#     return "Hello! This is Flask!";

app.run()

