import requests

# Set the base URL for the API
url = "http://127.0.0.1:5000"

# Define a test set with sample text and expected sentiment
test_set = [
    {"text": "It is a wonderful day today", "sentiment": 'positive'},
    {"text": "I absolutely love this movie", "sentiment": 'positive'},
    {"text": "He did not like the watch", "sentiment": 'negative'},
    {"text": "I was expecting more from this", "sentiment": 'negative'},
]

# Iterate through the test set
for test in test_set:
    # Extract the text and expected sentiment from the test data
    text = test['text']
    expected_sentiment = test['sentiment']
    
    # Send a POST request to the /analyze endpoint of the API with the text data
    result = requests.post(f'{url}/analyze', json={'text': text})
    
    # Extract the predicted sentiment from the response JSON
    predicted_sentiment = result.json()['sentiment']
    
    # Compare the predicted sentiment with the expected sentiment
    is_correct = expected_sentiment == predicted_sentiment
    
    # Print the test result
    print(f"({is_correct}) - Predicted sentiment: {predicted_sentiment} | Text: {text}")
    
    # Assert that the predicted sentiment matches the expected sentiment
    assert is_correct

# Print a confirmation message when all tests pass
print(" ------ All tests passed ------ ")
