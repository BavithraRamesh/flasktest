from flask import Flask, jsonify, request
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)


@app.route('/start', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):
		command = input("Shall we start")
		print(command)
		if 'start' in command:
			r = sr.Recognizer()
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source, duration=1)
			print("Listening.......")
			audio = r.listen(source)
			try:
				print("Recognizing.............")
				text = r.recognize_google(audio, language='en-in')
				text = text.lower()
				print(f"User said : {text}\n")
				say(text)
			except Exception as e:
				print(e)
				print("can not recognize your voice")
				return "None"
			return text



def say(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    engine.setProperty('rate', 175)
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    engine.say(text)
    engine.runAndWait()





if __name__ == '__main__':

	app.run(debug = True)
