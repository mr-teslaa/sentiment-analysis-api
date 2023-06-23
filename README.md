# Sentiment Analysis API

The Sentiment Analysis API is a Flask-based API that provides sentiment analysis functionality using a pre-trained model. The API allows users to send a text query and receive the predicted sentiment as a response. We need you use larger model for more accurate result. 

I am using FLASK web framework to build this API.
#### FLASK
  - To run flask server. Go to `api` directory and run `main.py` file
  ```bash
  cd api
  python main.py
  ```
  
## Features
- Accepts POST requests at `/analyze` endpoint.
- Performs sentiment analysis on the provided text using a pre-trained machine learning model.
- I also trained with a dataset for better result. We can add any other large model to train that in future.
- Returns the sentiment analysis result as a JSON response.
- Handles errors gracefully and provides appropriate error responses.
- Supports asynchronous processing for improved scalability and performance.
- Train this model with custom dataset or large dataset on training directory
- The `test.py` file includes automated tests for the API endpoints. I am not using any testing framework like `pytest` as it is so simple. Instead I am using the `requests` library to send requests to the running API server and compares the responses with the expected results.
- Follows industry-standard coding best practices and style guidelines.

## Installation
To set up the project locally, follow these steps:

1. Ensure you have Python 3.7 or higher installed on your machine.

2. Clone the repository:
```bash
  git clone https://github.com/mr-teslaa/sentiment-analysis-api
```

3. Navigate to the project directory:
```bash
  cd sentiment-analysis-api
```

4. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
```

5. Activate the virtual environment:
- On Windows:
```bash
  venv\Scripts\activate
```
- On macOS/Linux:
```bash
  source venv/bin/activate
```

6. For train the model go to training directory and run the jupyter notebook
```bash
cd training
```

7. For running api, go to api directory
```bash
cd api
```

8. Install the project dependencies:
```bash
  pip install -r requirements.txt
```

9. For simplicity, I already train small ammount of data, you can load them from dumps directory. We can add more large dataset in `training` directory in future if needed.

10. Start the API server:

- Enable debugging mode, and restart server automatically when code changes
```bash
set FLASK_APP=main
set FLASK_DEBUG=1
flask run
```
- **Instead of that**, you can also simply run the API server with python. But you have to close and run the server every single time you have made any changes
```shell
python main.py
```

11. Access the API using the following endpoints:
### `/`

- HTTP Method: `GET`
- Description: Route handler for the root endpoint. Returns instruction to run the api with 'Sentimental Analyze API is running' message.
- Response: 
```
Sentimental Analyze API is running....
Please make a post request with text in json format
{ 'text': 'Your text to analyze' }
```

### `/analyze`

- HTTP Method: `POST`
- Description: Route handler for the '/analyze' endpoint. Accepts a POST request with JSON data containing a 'text' field. Calls the 'predict' function to analyze the text and returns the result as JSON.
- Request Body:

```json
{
  "text": "It is a wonderful day today"
}
```

- Response:

```json
{
  "sentiment": "positive"
}
```

## Loading the Model

- The sentiment analysis model is loaded using the `SetFitModel` class from the `setfit` library.
- The model is loaded asynchronously using a separate thread to avoid blocking the main execution.

## Sentiment Prediction

The `predict()` function in `analyzer.py` takes a text input and uses the loaded model to predict the sentiment. The predicted sentiment is returned as the output.

## Automated Testing

- The `test.py` file includes automated tests for the API endpoints.
- It uses the `requests` library to send requests to the running API server and compares the responses with the expected results.

1. Make sure your api is running or you can run using the comman
```shell
python main.py
```
2. To run the automated tests, execute the following command:

```shell
python test.py
```

## Training the Model

**0. Training Methods:** We are using 2 methods for trainings
- Simple
- Complex

**Complex:**
- It is implemented using pytorch.
- We are loading the amazon product reviews dataset, since it contains many rows and can be loaded and manipulated easity.
- Then we have created our own pipeline for preprocessing and loading the data for model.
- Model is then trained in epochs, validated and saved.
- Use this if you want to control the flow, manipulate the epochs or the data pipeline.

**Simple:**
- It uses the default methods provided by setfit library.
- We used that twitter airline dataset for training, as it is in format directly compatable with our setfit training procedure.
- We just need to provide the data and model as parameters and it takes care of the processing, pipeline and training.
- This method makes the code easier, but not the most efficient and also you cannot change much of the trainig process.
- Use this method when you don't want to get into the details and just want to get the model trained.

**1. Importing the Required Libraries:** The necessary libraries are imported to use the functionalities required for training the model.

**2. Loading the Twitter Airline Sentiment Dataset:** The `load_dataset` function from the `datasets` library is used to load the Twitter Airline Sentiment dataset. This dataset contains text data along with corresponding sentiment labels. We have also used `bittlingmayer/amazonreviews` data set form here https://www.kaggle.com/datasets/bittlingmayer/amazonreviews

**3. Loading the Pre-trained Model:** The `SetFitModel` class from the `setfit` library is used to load a pre-trained sentiment analysis model. The `from_pretrained` method is called with the appropriate model name, such as "StatsGary/setfit-ft-sentinent-eval", to load the specific model.

**4. Training the Model:** The `SetFitTrainer` class from the `setfit` library is used to train the sentiment analysis model. The `model` parameter is set to the loaded pre-trained model. The `train_dataset` parameter is set to the training subset of the loaded dataset. The `loss_class` parameter is set to `CosineSimilarityLoss` from the `sentence_transformers.losses` module, which specifies the loss function to use during training. The `metric` parameter is set to "accuracy" to evaluate the model's performance. Other parameters such as `batch_size`, `num_iterations`, `num_epochs`, and `column_mapping` are also specified to configure the training process.

**5. Training and Evaluation:** The `trainer.train()` method is called to start the training process. The model is trained using the specified dataset and configuration. After training, the `trainer.evaluate()` method is called to evaluate the model's performance and compute the metrics.

**6. Saving the Model:** The trained model is saved using the `_save_pretrained` method of the `model` object. The `save_directory` parameter specifies the directory where the model will be saved, such as "./output/".
