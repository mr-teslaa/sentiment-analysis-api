from flask import Flask, request, jsonify
from analyzer import predict

app = Flask(__name__)

class TextRequest:
    def __init__(self, text):
        self.text = text

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    text_request = TextRequest(data['text'])
    result = predict(text_request.text)
    return jsonify({
        'sentiment': result
    })

if __name__ == '__main__':
    app.run()
