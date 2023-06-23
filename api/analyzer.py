from setfit import SetFitModel
import threading

MODEL_PATH = "dumps/saved_model_v1"
CLASSES = ['negative', 'positive']

def load_model():
	print("\n\n----------> Loading the Model\n\n")
	model = SetFitModel.from_pretrained(MODEL_PATH)
	print("\n\n----------> Model Loaded Successfully\n\n")
	return model

model = None

def load_model_async():
    global model
    model = load_model()

# Start loading the model asynchronously
model_loading_thread = threading.Thread(target=load_model_async)
model_loading_thread.start()

def predict(text):
	pred = model([text])
	pred = pred[0].item()
	return CLASSES[pred]