import cv2

from PIL import Image
import pytesseract as pyt
import pyperclip

import sqlite3
from sqlite3 import Error

# https://docs.python.org/3/library/sqlite3.html
# https://dev.to/video/introduction-to-text-detection-using-opencv-and-pytesseract-3he2
# https://github.com/madmaze/pytesseract
# https://github.com/UB-Mannheim/tesseract/wiki

# Read tesseract execuutable to run application
from sys import platform
if platform == "linux":
    print("linux")
elif platform == "darwin":
    print("osx")
elif platform == "win32":
    pyt.pytesseract.tesseract_cmd = (r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe')


def write_frames_from_video():
    '''
    This function reads the frames captured by the video frame and reads each frame for information. After that it should be saved inside a sqlite database.
    '''
    vidcap = cv2.VideoCapture('test_video.mp4')
    success, image = vidcap.read()
    count = 0
    while success:
        #cv2.imwrite("frames/frame%d.jpeg" % count, image) # save frame as jpeg
        success, image = vidcap.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cfg_filename = 'words'
        data = pyt.image_to_string(gray, lang=None, config=cfg_filename) #.lower() 
        print(data)
        #print('Read a new frame : ', success)
        count += 1


def write_frame_to_clipbord(image):
    '''
    This Method provides the possibvility to copy from a picture to the clipboard.
    '''
    cfg_filename = 'words'
    data = pyt.image_to_string(image, lang=None, config=cfg_filename) #.lower() 
    pyperclip.copy(data)    


def read_info_from_frame():  
    print(pyt.image_to_string(Image.open('frames\\frame0.jpeg')))


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"SQLite Version is: {sqlite3.version}")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


#if __name__ == '__main__':
#    #create_connection(r"sqlite.db")
#    write_frames_from_video()