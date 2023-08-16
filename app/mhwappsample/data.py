from flask import Flask, jsonify

app = Flask(__name__)

# Sample Python function to get data
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return data

@app.route('/api/data', methods=['GET'])
def get_data_api():
    data = get_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run()
