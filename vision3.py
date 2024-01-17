import cv2
import keyboard
import pyautogui
import pyperclip
from PIL import Image, ImageGrab
import Listen
import gemini3
import sounddevice as sd
import soundfile as sf
from customtkinter import *
import pystray
from pystray import Icon, Menu, MenuItem
import tkinter as tk

# Function to take a screenshot
def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.png')

# Function to analyze image using your AI model
def analyze_image(image, query):
    # Your code to process the image and get a description
    # Replace this with your actual AI model integration
    description = gemini3.analyze(image, query)
    return description

# Function to play notification sound
def play_here():
    notification_sound_path = "noti.mp3"
    auddata, samra = sf.read(notification_sound_path)
    sd.play(auddata, samra)
    sd.wait()

# Function to get user input using customtkinter

description = ""
def get_input():


    def get_description():
        global description
        description = textbox.get("0.0", "end")
        print("Description:", description)
        app.destroy()

    # Create a custom tkinter window
    app = CTk()
    app.title("MyAssist")
    app.geometry("400x300")

    # Create UI components
    label = CTkLabel(master=app, text="Ask me Anything", font=("Arial", 20, "bold"), text_color="#FFCC70")
    textbox = CTkTextbox(master=app, scrollbar_button_color="#FFCC70", corner_radius=16, border_color="#FFCC70",
                         border_width=2)
    btn = CTkButton(master=app, text="Ask", corner_radius=32, fg_color='#C850C0', hover_color="#4158D0",
                    command=get_description)
    btn.place(relx=0.5, rely=0.9, anchor=CENTER)
    label.place(relx=0.5, rely=0.1, anchor=CENTER)
    textbox.place(relx=0.5, rely=0.5, anchor=CENTER)

    app.mainloop()

# Function to get description and close the window


# Main loop
while True:
    # Capture frame-by-frame
    if keyboard.is_pressed('esc'):
        play_here()
        take_screenshot()

        # Get user input using customtkinter
        get_input()

        print("Latest Description:", description)
        text = analyze_image('screenshot.png', description)

        # Write the text
        #pyautogui.write(text)
        pyperclip.copy(text)

        # Play notification sound
        play_here()

"""
import cv2
import keyboard
import pyautogui
import pyperclip
from PIL import Image, ImageGrab
import Listen
import gemini3
import sounddevice as sd
import soundfile as sf
from customtkinter import *
import pystray
from pystray import Icon, Menu, MenuItem
import tkinter as tk
def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.png')
# Function to analyze image using your AI model
def analyze_image(image,query):
    # Your code to process the image and get a description
    # Replace this with your actual AI model integration
    description = gemini3.anaylyze(image,query)
    return description
def playhere():
    notification_sound_path = "noti.mp3"
    auddata, samra = sf.read(notification_sound_path)
    sd.play(auddata, samra)
    sd.wait()


import speechV2

# Open the camera

position = (5, 50)
font_size = 0.7
font_color = (0, 0, 255)
font_thickness = 2
text = "data"

description=""
def getdes():
    description = textbox.get("0.0", "end")
    print(description)
    app.destroy()

while True:
    # Capture frame-by-frame



    # Save the frame to the specified path

    if keyboard.is_pressed('esc'):
        playhere()
        take_screenshot()








        app = CTk()
        app.title("MyAssist")
        app.geometry("400x300")
        label = CTkLabel(master=app, text="Ask me Anything", font=("Arial", 20, "bold"), text_color="#FFCC70")
        textbox = CTkTextbox(master=app, scrollbar_button_color="#FFCC70", corner_radius=16, border_color="#FFCC70",
                             border_width=2)
        btn = CTkButton(master=app, text="Ask", corner_radius=32, fg_color='#C850C0', hover_color="#4158D0",
                        command=getdes)
        btn.place(relx=0.5, rely=0.9, anchor=CENTER)
        label.place(relx=0.5, rely=0.1, anchor=CENTER)
        textbox.place(relx=0.5, rely=0.5, anchor=CENTER)

        app.mainloop()


        print("latest",description)
        text = analyze_image('screenshot.png',description)

        #speechV2.speak(text)
        pyautogui.write(text)
        #pyperclip.copy(text)
        playhere()
         #There are 5 fingers in the photo. The person is holding their hand up with their palm facing the camera.


"""