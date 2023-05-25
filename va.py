import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyautogui
import socket
import webbrowser
import multiprocessing

import chatgpt
import date1
import main

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

hostname = socket.gethostname()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'leo' in command:
                command = command.replace('leo', '')
            return command
    except sr.UnknownValueError:
        talk('Sorry, I didn\'t catch that. Please try again.')
    except sr.RequestError:
        talk('Sorry, I\'m currently unable to process your request. Please try again later.')


def execute_command(command):
    if 'hello' in command:
        wish_back = chatgpt.askgpt(command)
        talk(wish_back)
        print(wish_back)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + current_time)
    elif 'open chrome' in command:
        talk('Opening Chrome')
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        url = 'https://www.google.com'
        webbrowser.get('chrome').open(url)
    elif 'open browser' in command:
        talk('Opening your default browser')
        webbrowser.open('https://www.google.com', new=1)
    elif 'search' in command:
        query = command.replace('search for', '')
        url = f"https://www.google.com.tr/search?q={query}"
        talk(f'Searching for {query}')
        webbrowser.open(url, new=1)
    elif 'open whatsapp' in command:
        talk('Opening WhatsApp Web')
        pywhatkit.open_web()
    elif 'who is' in command:
        info = chatgpt.askgpt(command)
        print(info)
        talk(info)
    elif 'date' in command:
        requested_date = date1.get_date(command)
        print(requested_date)
        talk(requested_date)
    elif 'scroll down' in command:
        talk('Scrolling down')
        pyautogui.scroll(-300)
    elif 'scroll up' in command:
        talk('Scrolling up')
        pyautogui.scroll(300)
    elif 'enable mouse' in command:
        process_mouse_control()
    elif 'disable mouse' in command:
        main.stop()
    elif 'joke' in command:
        joke = chatgpt.askgpt(command)
        print(joke)
        talk(joke)
    elif 'cancel' in command:
        talk("Exiting the program...")
        exit()
    else:
        talk('Please say the command again.')


def process_mouse_control():
    process1 = multiprocessing.Process(target=take_command)
    process2 = multiprocessing.Process(target=main.execute_mouse)
    process1.start()
    process2.start()
    process1.join()
    process2.join()


def start_leo():
    while True:
        command = take_command()
        print(command)
        execute_command(command)


if __name__ == '__main__':
    talk(f'Hello, This is virtual assistant for {hostname}')
    start_leo()
