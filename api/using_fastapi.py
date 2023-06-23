from fastapi import FastAPI
from pydantic import BaseModel
from analyzer import predict

app = FastAPI()

class TextRequest(BaseModel):
	text: str

@app.get("/")
def index():
	return "Hello, world!"

@app.post("/analyze")
def analyze_text(text_request: TextRequest):
	text = text_request.text
	result = predict(text)
	return {
		"sentiment": result
	}