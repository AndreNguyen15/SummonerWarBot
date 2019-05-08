import sys
import time
import run

from PyQt5.QtCore import (QCoreApplication, QThread)

class AThread(QThread):

    def __init__(self,parent=None):
        super(AThread, self).__init__(parent)
        self.setTerminationEnabled(True)
        self.isDone = False

    def run(self):
        self.start(self.task())
        self.isDone = False

    def task(self):
        refills = False
        while(self.isDone == False):
            run.startRun(refills)
    def killthread(self):
        self.isDone = True
        self.terminate()
        self.wait()