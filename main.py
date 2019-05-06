'''
Description : This is a bot that can be used to farm the dungeons.
It will search for specific image on the screen and click on them when found.

We import pyautogui to take care of the image search and click.
We import time to make the program wait on specific event.

IN NO CASE, can this program be sold or put on the internet without my
knowledge. (AKA, DONT SELL MY SHIT JEAN AUGUSTE AND DJO ALCIDOR)

@update : 5 may 2019
@author : André Nguyen
@special mention : Jackie Chao
'''

import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QTextEdit
import startPushButton

def createTxtEditor():
    textEditor = QTextEdit()
    textEditor.setReadOnly(True)
    textEditor.append('Le programme est prêt à être lancé')
    return textEditor

def createBtn(txtEditor):
    startbtn = startPushButton.startBtn('Start bot', txtEditor)
    return startbtn

def createLayout():
    layout = QVBoxLayout()
    txtEditor = createTxtEditor()
    layout.addWidget(createBtn(txtEditor))
    layout.addWidget(txtEditor)
    return layout

if __name__== "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = QWidget()
    window.setLayout(createLayout())
    window.show()
    app.exec_()
    print('The runs has been finished')
    sys.exit(app.exec_())

