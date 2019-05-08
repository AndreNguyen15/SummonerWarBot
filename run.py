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
    bot.clickImage('noBtn.png', longWaitTime)
    bot.clickImage('loseScreen.png', shortWaitTime)
    bot.clickImage('prepareBtn.png', shortWaitTime)

'''
 This procedure will be called when the player has finished a run.
 It will click on the victory screen, open the chest and get or sell the items.
'''
def victoryScreen():
    bot.clickImage('victoryScreen.png', shortWaitTime)
    bot.clickImage('chest.png', mediumWaitTime)

    if(bot.imageIsFound('okBtn.png')):
        bot.clickImage('okBtn.png', shortWaitTime)
    else:
        if(bot.imageIsFound('6starsRune.png')):
            bot.clickImage('getRuneBtn.png', shortWaitTime)
        else:
            bot.clickImage('sell.png', shortWaitTime)
            bot.clickImage('yesBtn.png', shortWaitTime)

    bot.clickImage('replay.png', shortWaitTime)

def refillWithCrystals():
    bot.clickImage('shop.png', shortWaitTime)
    bot.clickImage('refillCrystals.png', shortWaitTime)

def noMoreEnergy():
    return bot.imageIsFound('notEnoughEnergy.png')


def startRun():

    runIsDone = False

    while(runIsDone == False):

        if(bot.imageIsFound('replay.png')):
            bot.clickImage('replay.png', shortWaitTime)

        elif(bot.imageIsFound('prepareBtn.png')):
            bot.clickImage('prepareBtn.png', shortWaitTime)

        elif(bot.imageIsFound('startBattleBtn.png')):
            bot.clickImage('startBattleBtn.png', shortWaitTime)

        elif(bot.imageIsFound('notEnoughEnergy.png')):
            runIsDone = True

        elif(bot.imageIsFound('victoryScreen.png')):
            time.sleep(longWaitTime)
            victoryScreen()

        elif(bot.imageIsFound('reviveBtn.png')):
            time.sleep(longWaitTime)
            playerDied()

