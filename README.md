# Sentiment Analysis API in Python

DoD:
* :heavy_check_mark: Working sentiment analysis API deployed on Docker and in the cloud
* :heavy_check_mark: Basic README on github with installation and usage instructions

TODOLIST:
* :heavy_check_mark: Build a simple Sentiment Analysis predictive model
* :heavy_check_mark: Build an API around the model
* :heavy_check_mark: Integrate the API with docker
* :heavy_check_mark: Deploy the docker image on the cloud

## Goal

This project's goal is to deploy a simple deep learning model for sentiment analysis as an API on the cloud.
* The model is built using [keras](https://keras.io/) with the [tensorflow](https://www.tensorflow.org/) backend
* The API is built using [flask](http://flask.pocoo.org/) and it's extension [restful_flask](https://flask-restful.readthedocs.io/en/latest/)
* The app is deployed on [Heroku](https://www.heroku.com/)

## Testing the app

To test the app (if it's still up and running when you're reading this!), run the following in the command line, specifying a sentence of your choice:
```
curl https://srbd-sentiment-v0.herokuapp.com -X PUT -d "data=This is fantastic !"
``` 
The API returns the predicted sentiment as well as its score, in JSON format:
```
{
  "score": "0.937636", 
  "sentiment": "Positive"
}
```

## Installation instructions (WORK IN PROGRESS)

### Building and running the docker image

Clone this repository locally and run the following command to create a docker image containing the app:

```{bash}
docker build -f Dockerfile -t sentiment-v0 .
```

To run the docker image, exposing port 8080 of the container onto port 6000 of the host:
```{bash}
## in interactive mode
docker run -it -p 6000:8080 sentiment-v0
## in detached mode
docker run -d -t -p 6000:8080 sentiment-v0
```
Note: The flask app will expose on port $PORT if the environment variable is defined, else on port 8080

### Calling the API

Example of API call when run locally on port 6000:
```
## hello-world (to check that the app is up and running)
curl localhost:6000
## get sentiment analysis
curl localhost:6000 -X PUT -d "data= I am totally in love with this !"
```

### Deploying on Heroku

[Follow these instructions](https://devcenter.heroku.com/articles/container-registry-and-runtime). Make sure beforehand to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)  

Remarks: 
* It can be useful to check out heroku logs to debug the app in case it's not working. Try the following command: ``` heroku logs --app name-of-your-app```
* On Heroku, the app is automatically binded on standard web ports (80 or 443), you therefore shouldn't specify any port in your API call.


## References
* [Dataset - First GOP Debate Twittea Sentimen (Kaggle)](https://www.kaggle.com/crowdflower/first-gop-debate-twitter-sentiment/data)
* [keras LSTM sentiment analysis (Kaggle kernel)](https://www.kaggle.com/ngyptr/lstm-sentiment-analysis-keras)
* [Flask Restful python library](https://flask-restful.readthedocs.io/en/latest/quickstart.html)
* [Deploying your keras model (Alon Burg)](https://medium.com/@burgalon/deploying-your-keras-model-35648f9dc5fb)
* [Miguel Grinberg's blog, excellent tutorials on building APIs in Python](https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful)
* [Building a Simple Rest API from a Keras model (Keras blog)](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html)
* [Issue on keras repo regarding using 'predict' asynchronously](https://github.com/keras-team/keras/issues/2397#issuecomment-254919212)
* [Deep Learning Docker Image](https://github.com/floydhub/dl-docker)
* [Keras - Tensorflow Docker Image](https://github.com/ivanvanderbyl/tensorflow-keras-docker/blob/master/Dockerfile)
* [Docker Deploys (heroku official doc)](https://devcenter.heroku.com/articles/container-registry-and-runtime) 

## Contributing

I Welcome all pull requests/suggestions/bug reports ! Feel free to drop an issue
