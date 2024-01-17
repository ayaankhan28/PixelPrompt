import keyboard
import pyperclip
from PIL import  ImageGrab
import gemini3
import sounddevice as sd
import soundfile as sf
from customtkinter import *

def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.png')


def analyze_image(image, query):

    description = gemini3.analyze(image, query)
    return description
def play_here():
    notification_sound_path = "noti.mp3"
    auddata, samra = sf.read(notification_sound_path)
    sd.play(auddata, samra)
    sd.wait()


description = ""
def get_input():
    def get_description():
        global description
        description = textbox.get("0.0", "end")
        print("Description:", description)
        app.destroy()

    app = CTk()
    app.title("MyAssist")
    app.geometry("400x300")

    label = CTkLabel(master=app, text="Ask me Anything", font=("Arial", 20, "bold"), text_color="#FFCC70")
    textbox = CTkTextbox(master=app, scrollbar_button_color="#FFCC70", corner_radius=16, border_color="#FFCC70",
                         border_width=2)
    btn = CTkButton(master=app, text="Ask", corner_radius=32, fg_color='#C850C0', hover_color="#4158D0",
                    command=get_description)
    btn.place(relx=0.5, rely=0.9, anchor=CENTER)
    label.place(relx=0.5, rely=0.1, anchor=CENTER)
    textbox.place(relx=0.5, rely=0.5, anchor=CENTER)

    app.mainloop()

while True:

    if keyboard.is_pressed('esc'):
        play_here()
        take_screenshot()

        get_input()

        print("Latest Description:", description)
        text = analyze_image('screenshot.png', description)
        pyperclip.copy(text)
        play_here()

