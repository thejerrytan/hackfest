from flask import Flask
import flask
from recommender import get_rec_for_x

app = Flask(__name__)

@app.route('/')
def index():
	return "hello world"

@app.route('/recommend/<item>')
def rec_item(item):
	return flask.jsonify(**get_rec_for_x(item))