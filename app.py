from flask import Flask, request, jsonify
from src.processor import *

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = ProcessorFood.predict(data['image'])
    return jsonify({'result': prediction})

if __name__ == '__main__':
    app.run()
