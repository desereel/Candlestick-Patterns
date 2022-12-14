import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

def assistant(audio):

	engine = pyttsx3.init()

	voices = engine.getProperty('voices')
	engine.setProperty('voices', voices[1].id)

	engine.say(audio)
	engine.runAndWait()

def greeting():
	
	assistant("Hello, I am your Virtual Assistant. How can I help you today")

def audio_input():

	aud = sr.Recognizer()
	with sr.Microphone() as source:
		print('listening and processing')
		aud.pause_threshold = 0.7
		audio = aud.listen(source)

	try:
		print("understanding")
		phrase = aud.recognize_google(audio, language='en-us')
		print("you said: ", phrase)
	
	except Exception as exp:
		
		print(exp)
		print("Can you please repeat that")
		return None

	return phrase

def theTime(self):

	time = str(datetime.datetime.now())
	print(time)
	hour = time[11:13]
	min = time[14:16]

	assistant(self, "The time right now is" + hour + "Hours and" + min + "Minutes")

def theDay():

	day = datetime.datetime.today().weekday() + 1

	Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

	if day in Day_dict.keys():
		weekday = Day_dict[day]

		print(weekday)
		assistant("its " + weekday)

def core_code():

	greeting()

	while True:
	
		phrase = audio_input().lower()
		if "open medium" in phrase:
			assistant("Opening Medium.com")
			webbrowser.open("www.medium.com")
			continue

		elif "open google" in phrase:
			assistant("Opening Google")
			webbrowser.open("www.google.com")
			continue

		elif "what day is it" in phrase:
			theDay()
			continue

		elif "what time is it" in phrase:
			theTime()
			continue

		elif "bye" in phrase:
			assistant("Exiting. Have a good day")
			exit()

		elif "from wikipedia" in phrase:
			assistant("Checking the wikipedia ")
			phrase = phrase.replace("wikipedia", "")
			result = wikipedia.summary(phrase, sentences=4)
			assistant("as per wikipedia")
			assistant(result)

		elif "what is your name" in phrase:
			assistant("I am your nameless virtual assistant")


if __name__ == '__main__':

	core_code()
