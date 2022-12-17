from datetime import datetime
from logging import exception
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import requests
API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
headers = {"Authorization": "Bearer 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"}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


class Voice:
   def speak(audio):
      engine.say(audio)
      engine.runAndWait()

   def wishMe():
      Voice.speak("What is your Name?")
      name = Ask.takeCommand();
      hour = int(datetime.now().hour)
      if hour >= 0 and hour < 12:
         Voice.speak(f"Good Morning {name}!")
      elif hour >= 12 and hour <= 18:
         Voice.speak(f"Good Afternoon {name}!")
      else:
         Voice.speak(f"Good Evening {name}!")

      Voice.speak(
          f"I here to help you  {name} to sumarized your stuff from Paragaraph to your voice ")
      print(
          f"I here to help you  {name} to sumarized your stuff from Paragaraph to your voice ")


class Ask():
   def takeCommand():
      r = sr.Recognizer()
      with sr.Microphone() as source:
         print("Listening....")
         r.pause_threshold = 1
         audio = r.listen(source)

      try:
         print("Recognizing...")
         query = r.recognize_google(audio, language='en-in')
         print(f"User said: {query}\n")

      except Exception as E:
         # print(e)
         print("Say that again please...")
         Voice.speak("Say that again please...")
         return "None"
      return query


class process():
	
	def question():
		def query(payload):
			response = requests.post(API_URL, headers=headers, json=payload)
			return response.json()
		Voice.speak(f"Please Enter 1 To sumbit data in written format and 2 to submit data in voice format ")

		a = int(input("Please Enter 1 To sumbit data in written format and 2 to submit data in voice format "))
		if a ==1:
			minl = int(input("Please Enter the Minimum Length of sumarized paragraphs you would like to have"))
			maxl = int(input("Please Enter the Maximium Length of sumarized paragraphs you would like to have"))
			data = input("Enter the data which you wanted to sumarized ")

			output = query({
					"inputs": data,
               "parameters":{
                  "min_length":minl,
                  "max_length":maxl,
               }
				})
			Voice.speak(output)
			print(output)
		if a == 2:
			print("Speak now")
			data = Ask.takeCommand()

			output = query({
					"inputs": data,
				})
			Voice.speak(output)
			print(output)			


if __name__ == "__main__": 
   Voice.wishMe()
   process.question()