from PyQt5.QtWidgets import QPushButton, QTextEdit
from PyQt5.QtCore import pyqtSlot
import thread

class startBtn(QPushButton):

    def __init__(self, name, txtEditor):
        super(startBtn, self).__init__(name)
        self.clicked.connect(self.on_click)
        self.thread1 = thread.AThread()
        self.txtEditor = txtEditor

    @pyqtSlot()
    def on_click(self):
        if(self.text() == 'Start bot'):
            self.thread1.start()
            self.setText('Stop bot')
            self.txtEditor.append('Starting bot')
        elif(self.text() == 'Stop bot'):
            self.thread1.killthread()
            self.setText('Start bot')
            self.txtEditor.append('Stopping bot')


