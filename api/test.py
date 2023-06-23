import requests

url = "http://127.0.0.1:5000"

test_set = [
    {"text": "It is a wonderful day today", "sentiment": 'positive'},
    {"text": "I absolutely love this movie", "sentiment": 'positive'},
    {"text": "He didnot like the watch", "sentiment": 'negative'},
    {"text": "I was expecting more from this", "sentiment": 'negative'},
]

text = "It is a wonderful day today"

for set in test_set:
	text = set['text']
	y = set['sentiment']
	result = requests.post(f'{url}/analyze', json={'text': text})
	pred = result.json()['sentiment']
	correct = y == pred
	assert correct
	print(f"({correct}) - {result.json()['sentiment']}: {text}")
print(" ------ All Tests passed ------ ")