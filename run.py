'''
 This file will take care of every scenario case or a run.
 Lose, Win, refills are some of them.
'''

import time
import bot


#Used when victory and defeat screen appear.
longWaitTime = 2

mediumWaitTime = 1.1
#Used when we don't need to wait too long before clicking
shortWaitTime = 0.7
'''
 This procedure will be called when the player has failed a run.
 The program will then refuse to revive himself for 10 crystals and 
 start a new run.
'''
def playerDied():
    time.sleep(longWaitTime)
    pos = bot.locateImage('noBtn.png')
    bot.clickImage(pos)
    time.sleep(2)
    pos = bot.locateImage('loseScreen.png')
    bot.clickImage(pos)
    time.sleep(shortWaitTime)
    pos = bot.locateImage('prepareBtn.png')
    bot.clickImage(pos)
    time.sleep(shortWaitTime)

'''
 This procedure will be called when the player has finished a run.
 It will click on the victory screen, open the chest and get or sell the items.
'''
def victoryScreen():
    time.sleep(longWaitTime)
    pos = bot.locateImage('victoryScreen.png')
    bot.clickImage(pos)
    time.sleep(shortWaitTime)
    pos = bot.locateImage('chest.png')
    bot.clickImage(pos)
    print('chest')
    time.sleep(mediumWaitTime)
    if(bot.imageIsFound('okBtn.png')):
        pos = bot.locateImage('okBtn.png')
        bot.clickImage(pos)
    else:
        runesFound()
    time.sleep(shortWaitTime)
    pos = bot.locateImage('replay.png')
    bot.clickImage(pos)
    time.sleep(shortWaitTime)

def runesFound():
    if(bot.imageIsFound('6starsRune.png')):
        print('6* runes')
        pos = bot.locateImage('getRuneBtn.png')
        bot.clickImage(pos)
    else:
        pos = bot.locateImage('sell.png')
        bot.clickImage(pos)
        time.sleep(shortWaitTime)
        pos = bot.locateImage('yesBtn.png')
        bot.clickImage(pos)
        time.sleep(shortWaitTime)
        print('5* runes')

def refill():
    pos = bot.locateImage('shop.png')
    bot.clickImage(pos)
    time.sleep(shortWaitTime)
    pos = bot.locateImage('refillCrystals')
    bot.clickImage(pos)

def noMoreEnergy():
    return bot.imageIsFound('notEnoughEnergy.png')

def replay():
    pos = bot.locateImage('replay.png')
    bot.clickImage(pos)


def startRun():
    runIsDone = False
    print('run started')
    while(runIsDone == False):
        if(bot.imageIsFound('replay.png')):
            pos = bot.locateImage('replay.png')
            bot.clickImage(pos)
            time.sleep(shortWaitTime)
        elif(bot.imageIsFound('prepareBtn.png')):
            pos = bot.locateImage('prepareBtn.png')
            bot.clickImage(pos)
            time.sleep(shortWaitTime)
        elif(bot.imageIsFound('startBattleBtn.png')):
            print('Starting battle')
            pos = bot.locateImage('startBattleBtn.png')
            bot.clickImage(pos)
            time.sleep(shortWaitTime)
        elif(bot.imageIsFound('notEnoughEnergy.png')):
            runIsDone = True
        elif(bot.imageIsFound('victoryScreen.png')):
            victoryScreen()
        elif(bot.imageIsFound('reviveBtn.png')):
            playerDied()

