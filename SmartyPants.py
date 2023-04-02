# Importing the necessary libraries
import openai
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# Setting up speech recognition object
r = sr.Recognizer()
mic = sr.Microphone()

# Setting up the text to speech object
engine = pyttsx3.init()

# Setting up the OpenAI API client
# openai.api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = "<YOUR API TOKEN GOES HERE>"


# Analyse the command and creating a transcript
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        transcription = r.recognize_google(audio)
        return transcription
    except (sr.UnknownValueError, sr.RequestError):
        return None


def process_input():
    user_input = recognize_speech()
    print("You said:", user_input)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "user", "content": user_input}])

    answer = response["choices"][0]["message"]["content"]
    answer = answer.replace("\n", "")

    # Speak out response
    print("Friday:", answer)

    language = 'en'
    tts = gTTS(text=answer, lang=language)
    tts.save('output.mp3')
    playsound('output.mp3')


if __name__ == "__main__":
    process_input()
