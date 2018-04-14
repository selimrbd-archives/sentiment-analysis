# Sentiment Analysis API in Python

DoD:
* Working sentiment analysis API deployed on Docker and in the cloud
* Basic README on github with installation and usage instructions

TODOLIST:

* :heavy_check_mark: Build a simple Sentiment Analysis predictive model
* :heavy_check_mark: Build an API around the model
* :white_check_mark: Integrate the API with docker
* :white_check_mark: Deploy the docker image on the cloud


### Instructions

**WORK IN PROGRESS**

Example of API call:
```
curl localhost:5000 -X PUT -d "data= This is fantastic !"
```

#### docker

Build a docker image called keras-1 from the Dockerfile
```
docker build -f Dockerfile -t keras-1 .
```
Run the docker image, exposing port 5000 of the container onto port 6000 of the host
```
docker run -it keras-1 -port 6000:5000
```


### References
* [Dataset - First GOP Debate Twittea Sentimen (Kaggle)](https://www.kaggle.com/crowdflower/first-gop-debate-twitter-sentiment/data)
* [keras LSTM sentiment analysis (Kaggle kernel)](https://www.kaggle.com/ngyptr/lstm-sentiment-analysis-keras)
* [Flask Restful python library](https://flask-restful.readthedocs.io/en/latest/quickstart.html)
* [Miguel Grinberg's blog, excellent tutorials on building APIs in Python](https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful)
* [Building a Simple Rest API from a Keras model (Keras blog)](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html)
* [Issue on keras repo regarding using 'predict' asynchronously](https://github.com/keras-team/keras/issues/2397#issuecomment-254919212)
* [Deep Learning Docker Image](https://github.com/floydhub/dl-docker)
* [Keras - Tensorflow Docker Image](https://github.com/ivanvanderbyl/tensorflow-keras-docker/blob/master/Dockerfile)
 
