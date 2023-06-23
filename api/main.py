#   IMPORT GENERAL MODULE
from flask import Flask
from flask import request
from flask import jsonify

#   IMPORTING TEXT PREDICTION FUNCTION
from analyze.analyzer import predict

#   INIT FLASK APPLICATION
app = Flask(__name__)

#   Considering the complexity and future requirements of api
#   It stores the text to be analyzed
class TextRequest:
    def __init__(self, text):
        self.text = text

#   ROOT PATH OF API
@app.route('/')
def index():
    """
    Route handler for the root endpoint.
    Returns instruction to run the api with 'Sentimental Analyze API is running' message.
    """

    return ("Sentimental Analyze API is running....\n\n \
            Please make a post request with text in json format\n\n \
            { 'text': 'Your text to analyze' }")

#   ANALYZE PATH OF API, WHICH ONLY ALLOW POST REQUEST AS REQUIREMENTS SAYS
@app.route('/analyze', methods=['POST'])
def analyze_text():
    """
    Route handler for the '/analyze' endpoint.
    Accepts a POST request with JSON data containing a 'text' field.
    Calls the 'predict' function to analyze the text and returns the result as JSON.
    """
    try:
        # Retrieve JSON data from the request
        data = request.get_json()
        
        # Create a TextRequest object with the text from the JSON data
        text_request = TextRequest(data['text'])

        # Call the 'predict' function to analyze the text
        result = predict(text_request.text)

        # Return the result as JSON
        return jsonify({ 'sentiment': result })
    
    except KeyError:
        error_response = {"error": "Invalid Request"}
        return jsonify(error_response), 400

    except Exception as e:
        error_response = {"error": "Internal Server Error"}
        return jsonify(error_response), 500

# RUNNING THE APPLICATION
if __name__ == '__main__':
    app.run()
