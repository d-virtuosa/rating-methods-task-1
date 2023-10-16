from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/plus', methods=['POST'])
def plus():
    data = request.get_json()
    if 'numbers' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    numbers = data['numbers']
    result = sum(numbers)
    return jsonify({'result': result})

@app.route('/minus', methods=['POST'])
def minus():
    data = request.get_json()
    if 'numbers' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    numbers = data['numbers']
    result = numbers[0] - sum(numbers[1:])
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    if 'numbers' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    numbers = data['numbers']
    result = 1
    for num in numbers:
        result *= num
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    if 'numbers' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    numbers = data['numbers']
    if 0 in numbers[1:]:
        return jsonify({'error': 'Cannot divide by zero'}), 400

    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host = "0.0.0.0")
