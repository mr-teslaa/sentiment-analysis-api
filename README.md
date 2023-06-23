# Sentiment Analysis API

The Sentiment Analysis API is a Flask-based web application that provides sentiment analysis functionality using a pre-trained model. The API allows users to send a text query and receive the predicted sentiment as a response.

## Installation


## Usage

1. Install the dependencies:

```shell
pip install -r requirements.txt
```

2. Start the API server:

```shell
python main.py
```

3. Access the API using the following endpoints:

### `/`

- HTTP Method: GET
- Description: Home endpoint to check if the API is running.
- Response: "Hello, world!"

### `/analyze`

- HTTP Method: POST
- Description: Analyzes the sentiment of a given text.
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

1. **Importing the Required Libraries:** The necessary libraries are imported to use the functionalities required for training the model.

2. **Loading the Twitter Airline Sentiment Dataset:** The `load_dataset` function from the `datasets` library is used to load the Twitter Airline Sentiment dataset. This dataset contains text data along with corresponding sentiment labels.

3. **Loading the Pre-trained Model:** The `SetFitModel` class from the `setfit` library is used to load a pre-trained sentiment analysis model. The `from_pretrained` method is called with the appropriate model name, such as "StatsGary/setfit-ft-sentinent-eval", to load the specific model.

4. **Training the Model:** The `SetFitTrainer` class from the `setfit` library is used to train the sentiment analysis model. The `model` parameter is set to the loaded pre-trained model. The `train_dataset` parameter is set to the training subset of the loaded dataset. The `loss_class` parameter is set to `CosineSimilarityLoss` from the `sentence_transformers.losses` module, which specifies the loss function to use during training. The `metric` parameter is set to "accuracy" to evaluate the model's performance. Other parameters such as `batch_size`, `num_iterations`, `num_epochs`, and `column_mapping` are also specified to configure the training process.

5. **Training and Evaluation:** The `trainer.train()` method is called to start the training process. The model is trained using the specified dataset and configuration. After training, the `trainer.evaluate()` method is called to evaluate the model's performance and compute the metrics.

6. **Saving the Model:** The trained model is saved using the `_save_pretrained` method of the `model` object. The `save_directory` parameter specifies the directory where the model will be saved, such as "./output/".
