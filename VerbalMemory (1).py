from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import time
import pyscreenshot
import pyautogui
import os

time.sleep(4)
wordList = []

while True:
    print("starting the loop")
    # im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))
    image = pyscreenshot.grab(bbox=(550, 480, 1200, 600))
    
    image.save(r"C:\Users\16178\Documents\gunk.png")

    # To view the screenshot
    #image.show()

    img = r"C:\Users\16178\Documents\gunk.png"


    text = pytesseract.image_to_string(Image.open(img))

    if not wordList:
        print("list was empty")
        pyautogui.click(x=1000, y=650)
        wordList.append(text)

    if any(thing in text for thing in wordList):
        
        print("seen")
        pyautogui.click(x=900, y=650)
            

    else:
        print("new")
        pyautogui.click(x=1000, y=650)
        wordList.append(text)
        
            
    os.remove(r"C:\Users\16178\Documents\gunk.png")
    time.sleep(0.1)
