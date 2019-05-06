import sys
import time
import run

from PyQt5.QtCore import (QCoreApplication, QThread)

class AThread(QThread):

    def __init__(self,parent=None):
        super(AThread, self).__init__(parent)
        self.setTerminationEnabled(True)

    def run(self):
        refills = False
        self.start(run.startRun(refills))

    def killthread(self):
        self.terminate()
        self.wait()
        print('The thread has stopped')