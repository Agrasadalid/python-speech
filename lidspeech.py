import pyttsx3
import speech_recognition as sr
import pyjokes

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
            return ""
        except sr.RequestError as e:
            print(f"Couldn't request results from Google Speech Recognition service: {e}")
            return ""

        except:
            pass
            command = "No Mic"
            print(command)
            return command

def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

def main():
    speak("Hello! I'm here to tell you jokes. Just say 'tell me a joke' to hear one.")
    while True:
        command = listen()
        if "tell me a joke" in command:
            tell_joke()
        elif "thank you" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
