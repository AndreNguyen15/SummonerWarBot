import pyautogui

'''
 This method will find the image on the screen and return its
 x and y positions. It will be used to move the mouse to the positions of
 the image.

 @return : x and y coordinates
'''
def locateImage(imageName):
    positions = pyautogui.locateOnScreen(imageName, confidence=0.9)
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
    positions = pyautogui.locateOnScreen(imageName, confidence=0.9)
    if(positions!=None):
        isFound = True
    return isFound

'''
 Click at the coordinates given.
 
 @param pos : The position of the image that must be clicked.
'''
def clickImage(pos):
    pyautogui.click(pos[0], pos[1])