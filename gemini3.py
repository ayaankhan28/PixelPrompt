import textwrap
import time
import google.generativeai as genai
import numpy as np
genai.configure(api_key='******')
import PIL.Image
def analyze(path,query):
    img = PIL.Image.open(f"{path}")
    a = time.time()
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([f"{query}",img])
    b = time.time()
    return response.text
