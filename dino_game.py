import pyautogui   
from PIL import Image, ImageGrab
import time
def hit(key):
    pyautogui.keyDown(key)
def dayn():
    for i in range(220, 290):
        for j in range(210, 227):
            if data[i, j] > 120:
                return True
            else:
                return False
    return False
def iscolide(data):
    '''
    if dayn()==True:
        for i in range(465, 578):
            for j in range(229, 260):
                if data[i, j] < 50:
                    hit("up")
                    return
    '''
    #if dayn()==False:
    if True:
        for i in range(465, 578):
            for j in range(229, 260):
                if data[i, j] > 140:
                    hit("up")
                    return
    return
if __name__ == "__main__":
    print("start in 2")
    time.sleep(1)
    print("start in 1")
    time.sleep(1)
    print("start in 0...started    ")
    # hit("up")
    # hit("up")
    # hit('up')
    while (1):
        image = ImageGrab.grab().convert('L')
        data = image.load()
        iscolide(data)
        #for i in range(200, 290):
        #    for j in range(200, 300):
        #        data[i, j] = 50
        #for i in range(465, 578):
        #    for j in range(229, 260):
        #        data[i, j] = 20
        #image.show()
        #break
