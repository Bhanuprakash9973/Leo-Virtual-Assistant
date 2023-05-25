# Leo-Virtual-Assistant

This is a Python script that implements a virtual assistant named "Leo" using various libraries and modules. Leo can perform a variety of tasks, including speech recognition, text-to-speech conversion, web browsing, playing YouTube videos, providing information, and controlling the mouse.

## Prerequisites
Before running the code, make sure you have the following Python libraries installed:
- speech_recognition
- pyttsx3
- pywhatkit
- datetime
- pyautogui
- socket
- webbrowser
- multiprocessing

You can install these libraries using the pip package manager:

pip install speechrecognition pyttsx3 pywhatkit datetime pyautogui socket webbrowser


## Usage
1. Run the script in a Python environment.
2. Make sure your computer has a working microphone for speech recognition.
3. Once the program is running, Leo will start listening for commands.
4. Speak your command after the prompt "listening...".
5. Leo will interpret your command and perform the appropriate action.

## Features
### Speech Recognition
Leo uses the `speech_recognition` library to recognize speech input from the user. It listens for voice commands and converts them into text.

### Text-to-Speech
Leo uses the `pyttsx3` library to convert text into speech. It utilizes the system's available voices and adjusts the speech rate for a more natural sound.

### Web Browsing
Leo can open web browsers and search the internet. It uses the `webbrowser` library to open Chrome or the default browser and performs web searches on Google.

### YouTube Playback
Leo can play YouTube videos. It uses the `pywhatkit` library to search and play videos on YouTube based on the user's command.

### Date and Time
Leo can provide the current date and time. It uses the `datetime` library to retrieve the current system time and formats it accordingly.

### Mouse Control
Leo can enable and disable mouse control. It uses the `pyautogui` library to scroll the mouse up or down based on the user's command. The mouse control feature runs in a separate process using the `multiprocessing` module.

### Information Retrieval
Leo can answer questions and provide information about various topics. It uses the `chatgpt` module to interact with a chatbot and obtain answers to user queries.

### Exiting the Program
To exit the program, simply say "cancel" or close the Python environment running the script.

## Command Examples
- "Hello": Leo greets the user.
- "Play [song name]": Leo plays the requested song on YouTube.
- "Time": Leo tells the current time.
- "Open Chrome": Leo opens the Google Chrome browser.
- "Open browser": Leo opens the default web browser.
- "Search for [query]": Leo performs a Google search for the given query.
- "Open WhatsApp": Leo opens WhatsApp Web.
- "Who is [person]": Leo provides information about the requested person.
- "Date": Leo tells the current date.
- "Scroll down": Leo scrolls the mouse down.
- "Scroll up": Leo scrolls the mouse up.
- "Enable mouse": Leo enables mouse control.
- "Disable mouse": Leo disables mouse control.
- "Joke": Leo tells a joke.
- "Cancel": Leo exits the program.

Note: These are just a few examples of the commands that Leo can understand and execute.

## Limitations
- Leo's speech recognition accuracy may vary depending on the microphone and the surrounding noise.
- Some commands may require an internet connection to function properly.
- The performance of the chatbot-based information retrieval depends on the available knowledge and training data.

## Disclaimer
This virtual assistant script is provided as-is, without any warranty or guarantee. Use it at your own risk.

Feel free to customize and enhance the functionality of the virtual assistant according to your needs and preferences.

If you have any questions or feedback, please don't hesitate to contact the developer.

Happy interacting with Leo!

