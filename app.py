from flask import Flask, request, jsonify

app = Flask(__name__)

# 모델 로드
model = tf.keras.models.load_model('model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['input']])
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run()
