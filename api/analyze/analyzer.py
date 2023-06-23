# Import the SetFitModel class from the setfit module
from setfit import SetFitModel  

# Import the threading module for asynchronous loading of the model
import threading  

MODEL_PATH = "dumps/saved_model_v1"  # Path to the saved model
CLASSES = ['negative', 'positive']  # List of sentiment classes

def load_model():
	"""
    Load the pre-trained model from the saved model path.
    """
	print("\n\n----------> Loading the Model\n\n")
	model = SetFitModel.from_pretrained(MODEL_PATH)     # Load the model from the saved model path
	print("\n\n----------> Model Loaded Successfully\n\n")
	return model

# Global variable to store the loaded model
model = None


def load_model_async():
	"""
    Asynchronously load the model in a separate thread.
    """
	global model
	model = load_model()

# Start loading the model asynchronously
model_loading_thread = threading.Thread(target=load_model_async)
model_loading_thread.start()

def predict(text):
	"""
	Predict the sentiment of the given text using the loaded model.
	"""

	# Perform prediction using the loaded model
	pred = model([text])  

	# Get the predicted sentiment as a numeric value
	pred = pred[0].item()  

	# Map the numeric value to the corresponding sentiment class
	return CLASSES[pred]  