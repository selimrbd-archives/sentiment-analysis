#!/home/selim/DS/python/anaconda3/bin/python
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import pickle
import numpy as np
import sys
import keras
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences


path_model  = './cfg/model_sentiment_v1.h5'
path_config = './cfg/config.pkl'

model  = None
config = None
graph  = None

def load_model():
	"""load ML model and configuration"""
	global model, config, graph
	model  = keras.models.load_model(path_model)
	graph  = tf.get_default_graph()
	config = pickle.load(open(path_config, 'rb'))

def prepare_datapoint(text):
	text = [text] if type(text) == np.str else text
	tokenizer = config['tokenizer']['tokenizer']
	text = tokenizer.texts_to_sequences(text)
	text = pad_sequences(text, maxlen     = config['tokenizer']['token_maxlen'],
                                   padding    = config['tokenizer']['padding_type'],
                                   truncating = config['tokenizer']['truncating_type'],
                                   value      = config['tokenizer']['padding_value'])
	return(text)
	
## helper function
def predict_sentiment(text):
	ret = dict()
	text = prepare_datapoint(text)
	global graph
	with graph.as_default():
		sentiment = model.predict(text,batch_size=1,verbose = 0)[0]
	argmax_sent = np.argmax(sentiment)
	ret['sentiment'] = 'Positive' if  argmax_sent == 1 else 'Negative'
	ret['score']     = str(sentiment[argmax_sent])
	return(ret)


## API
app = Flask(__name__)
api = Api(app)

class PredictSentiment(Resource):
	def put(self):
		text = request.form['data']
		ret  = predict_sentiment(text)
		return(jsonify(ret))


api.add_resource(PredictSentiment, '/')

if __name__ == '__main__':
	print(("* Loading Keras model and Flask starting server..."
		"please wait until server has fully started"))
	load_model()
	app.run(debug = True)
