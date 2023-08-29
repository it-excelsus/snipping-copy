import easyocr
import pyperclip
import numpy as np

def image_to_clipboard(screenshot_image):
    screenshot_np_array = np.array(screenshot_image) 
    reader = easyocr.Reader(['en','de','tr'], gpu=False) # this needs to run only once to load the model into memory
    result = reader.readtext(screenshot_np_array, detail=0)
    scaned_text = ''.join(result)
    print(scaned_text)
    pyperclip.copy(scaned_text)