import textwrap
import time

import google.generativeai as genai
import numpy as np




genai.configure(api_key='******')

#####################TO CHECK AVAILABLE MODELS
"""for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)"""

########################################################################## FOR TEXT TO TEXT

"""model = genai.GenerativeModel('gemini-pro')


response = model.generate_content("give me 5 points to start youtube channel")
print(response.text)"""
#############FOR ANSWERSS IN CHUNKS
"""for chunk in response:
  print(chunk.text)
  print("_"*80)"""
##############################################################################
############################################################################## FOR  IMAGE TO TEXT

import PIL.Image
def analyze(path,query):
    img = PIL.Image.open(f"{path}")

    a = time.time()
    model = genai.GenerativeModel('gemini-pro-vision')

    response = model.generate_content([f"{query}",img])
    b = time.time()

    return response.text
############################################################################## FOR CHATTING

"""model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
while True:

    prompt = input("Enter your question: ")
    a = time.time()
    if(prompt == "exit"):
        break
    else:
        response = chat.send_message(f"{prompt}")
        output=chat.history
        ##print(output)
        print(response.text)
        b = time.time()
        #speech.speak(response.text)

        print("Response Time: "+str(round(b-a))+" sec")"""
#speechV2.speak(output)



"""


"""