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

import run
import bot


def startRun(refills):
    while(bot.imageIsFound('notEnoughEnergy.png') == False):
        print('A new run has started')
        runIsOver = False
        if(bot.imageIsFound('startBattleBtn.png')):
            pos = bot.locateImage('startBattleBtn.png')
            bot.clickImage(pos)

        while (runIsOver!=True):
            if(bot.imageIsFound('loseScreen.png')):
                print('player has died')
                run.playerDied()
                runIsOver = True
            elif(bot.imageIsFound('victoryScreen.png')):
                print('player has won')
                run.victoryScreen()
                runIsOver = True
            elif(bot.imageIsFound('reviveBtn.png')):
                print('player died')
                run.playerDied()

    if(bot.imageIsFound('notEnoughEnergy.png')):
        if(refills==True):
            run.noMoreEnergy()
        else:
            print('Refills has been deactivated.')



if __name__== "__main__":

    refillsWithCrystals = False

    startRun(refillsWithCrystals)

    print('The runs has been finished')