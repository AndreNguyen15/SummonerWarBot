import pyautogui
import time

'''
 This method will find the image on the screen and return its
 x and y positions. It will be used to move the mouse to the positions of
 the image.

 @return : x and y coordinates
'''
def locateImage(imageName):
    positions = pyautogui.locateOnScreen(imageName, confidence=0.8)
    x = positions[0]
    y = positions[1]
    return x, y

'''
 Search the image on the screen. The confidence parameter is a value between
 0 to 1 that takes into account our level of tolerance for the image
 we want to find and the one found on the screen.
 
 @return : boolean value
'''
def imageIsFound(imageName):
    isFound = False
    positions = pyautogui.locateOnScreen(imageName, confidence=0.8)
    if(positions != None):
        isFound = True
    return isFound

'''
 Click at the coordinates given.
 
 @param imageName : The name of the image that must be clicked
 @param waitTime : The amount amount of time the program must wait after 
                clicking
'''
def clickImage(imageName, waitTime):
    pos = locateImage(imageName)
    pyautogui.click(pos[0], pos[1])
    time.sleep(waitTime)
