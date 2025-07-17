from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data or 'operation' not in data:
        return jsonify({'error': 'Missing any parameters'})

    a = data['a']
    b = data['b']
    op = data['operation']

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return jsonify({'error': 'Input must be numbers'})

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            return jsonify({'error': 'Cannot divide by 0'})
        result = a / b
    else:
        return jsonify({'error': 'Invalid operation'})

    return jsonify({'result': result})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
