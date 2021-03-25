import pyautogui   
from PIL import Image, ImageGrab
import time
# x,y = pyautogui.position()
x,y = 910,261
x2,y2 = 880,248
w, h = 80, 1
w2, h2 = 80, 1
def start():
    print("start in 2")
    time.sleep(1)
    print("start in 1")
    time.sleep(1)
    print("start in 0...started    ")
def checking():
    for i in range(x, x+w):
       for j in range(y, y+h):
           data[i, j] = 0
    image.show()
def checking2():
    for i in range(x2, x2+w2):
       for j in range(y2, y2+h2):
           data[i, j] = 0
    image.show()
   
def hit(key):
    pyautogui.keyDown(key)
    time.sleep(0.5)
    pyautogui.keyUp("down")
def iscolide(data):
    for i in range(x, x+w):
        for j in range(y, y+h):
            if data[i, j] <  100:
                # hit("up")
                hit("up")
                return
    for i in range(x2, x2+w2):
        for j in range(y2, y2+h2):
            if data[i, j] <  100:
                hit("down")
                return
    

start()
while (1):
    image = ImageGrab.grab().convert('L')
    data = image.load()
    iscolide(data)

# checking...
    checking()
    # checking2()
    # break
