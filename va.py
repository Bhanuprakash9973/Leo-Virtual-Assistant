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


# talk(f'Hello, This is virtual Assistant for {hostname}')

def take_command():
    command = None
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'leo' in command:
                command = command.replace('leo', '')
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        talk('Exception occured!')
        print(message)
        pass
    return command


def execute(command):
    if 'hello' in command:
        wish_back = chatgpt.askgpt(command)
        talk(wish_back)
        print(wish_back)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'open chrome' in command:
        talk('opening Chrome')
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        url = 'https://www.google.com'
        webbrowser.get('chrome').open(url)
    elif 'open browser' in command:
        talk('Opening Your Default browser..')
        webbrowser.open('https://www.google.com', new=1)
    elif 'search' in command:
        task = command.replace('search for', "")
        url = f"https://www.google.com.tr/search?q={task}"
        talk(f'searching for {task}')
        webbrowser.open(url, new=1)
    elif 'open whatsapp' in command:
        talk('opening whatsapp web..')
        pywhatkit.open_web()
    elif 'who is' in command:
        info = chatgpt.askgpt(command)
        print(info)
        talk(info)
    elif 'date' in command:
        requestedDate = date1.get_date(command)
        print(requestedDate)
        talk(requestedDate)
    elif 'scroll down' in command:
        talk('scrolling down')
        pyautogui.scroll(-300)
    elif 'scroll up' in command:
        talk('scrolling up')
        pyautogui.scroll(300)
    elif 'enable mouse' in command:
        thread2 = multiprocessing.Process(target=take_command())
        thread1 = multiprocessing.Process(target=main.execute_mouse())
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
    elif 'disable mouse' in command:
        main.stop()
        # take_command()
    elif 'joke' in command:
        joke = chatgpt.askgpt(command)
        print(joke)
        talk(joke)
    elif 'cancel' in command:
        talk("Exiting the program...")
        exit()
    else:

        talk('Please say the command again.')


def start_leo():
    command1 = take_command()
    print(command1)
    execute(command=command1)


while True:
    start_leo()
