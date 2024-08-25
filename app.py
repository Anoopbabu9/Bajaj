from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the BFHL Application!"

@app.route('/bfhl', methods=['POST'])
def bfhl():
    # Replace this with your actual logic
    return jsonify({"status": "success", "message": "API is working!"})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
