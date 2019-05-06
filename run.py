'''
 This file will take care of every scenario case or a run.
 Lose, Win, refills are some of them.
'''

import time
import bot
'''
 This procedure will be called when the player has failed a run.
 The program will then refuse to revive himself for 10 crystals and 
 start a new run.
'''
def playerDied():
    time.sleep(2)
    pos = bot.locateImage('noBtn.png')
    bot.clickImage(pos)
    time.sleep(1)
    pos = bot.locateImage('loseScreen.png')
    bot.clickImage(pos)
    time.sleep(0.5)
    pos = bot.locateImage('prepareBtn.png')
    bot.clickImage(pos)
    time.sleep(1)
    pos = bot.locateImage('startBattleBtn.png')
    bot.clickImage(pos)

'''
 This procedure will be called when the player has finished a run.
 It will click on the victory screen, open the chest and get or sell the items.
'''
def victoryScreen():
    time.sleep(2)
    pos = bot.locateImage('victoryScreen.png')
    bot.clickImage(pos)
    print('victory')
    time.sleep(1)
    pos = bot.locateImage('chest.png')
    bot.clickImage(pos)
    print('chest')
    time.sleep(1)
    if(bot.imageIsFound('okBtn.png')):
        pos = bot.locateImage('okBtn.png')
        bot.clickImage(pos)
        time.sleep(1)
        print('reawrd')
    else:
        runesFound()
    time.sleep(1)
    pos = bot.locateImage('replay.png')
    bot.clickImage(pos)
    time.sleep(1)

def runesFound():
    if(bot.imageIsFound('6starsRune.png')):
        print('6* runes')
        pos = bot.locateImage('getRuneBtn.png')
        bot.clickImage(pos)
    else:
        pos = bot.locateImage('sell.png')
        bot.clickImage(pos)
        time.sleep(1)
        pos = bot.locateImage('yesBtn.png')
        bot.clickImage(pos)
        time.sleep(1)
        print('5* runes')

def refill():
    pos = bot.locateImage('shop.png')
    bot.clickImage(pos)
    time.sleep(1)
    pos = bot.locateImage('refillCrystals')
    bot.clickImage(pos)

def noMoreEnergy():
    print('no energy left.')

def replay():
    pos = bot.locateImage('replay.png')
    bot.clickImage(pos)

def stopRun():
    exit()

def startRun(refills):
    print('A new run has started')
    runIsOver = False
    if(bot.imageIsFound('startBattleBtn.png')):
        pos = bot.locateImage('startBattleBtn.png')
        bot.clickImage(pos)

    while (runIsOver!=True):
        if(bot.imageIsFound('victoryScreen.png')):
            print('player has won')
            victoryScreen()
            runIsOver = True
        elif(bot.imageIsFound('reviveBtn.png')):
            print('player died')
            playerDied()
            runIsOver = True

    if(bot.imageIsFound('notEnoughEnergy.png')):
        if(refills==True):
            noMoreEnergy()
        else:
            print('Refills has been deactivated.')