from flask import Flask, jsonify, request
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def test():
	print("hi hello")



if __name__ == '__main__':

	app.run(debug = True)
