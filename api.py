from flask import Flask, request, jsonify
from currency_converter import extract_currency, extract_number

app = Flask(__name__)


@app.route('/', methods=['GET'])
def parse_amount():
    input_currency = request.args.get('currency')
    input_amount = request.args.get('amount')
    return jsonify({
        'currency': extract_currency(input_currency),
        'amount': extract_number(input_amount)
    })