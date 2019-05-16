'''
 This file will take care of every scenario case or a run.
 Lose, Win, refills are some of them.
'''

import time
import bot


#Used when victory and defeat screen appear.
longWaitTime = 1.9

mediumWaitTime = 1.1

#Used when we don't need to wait too long before clicking
shortWaitTime = 0.6

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
    bot.clickImage('rewardScreen.png', 0.1)
    bot.clickImage('chest.png', mediumWaitTime)

    if(bot.imageIsFound('okBtn.png')):
        bot.clickImage('okBtn.png', shortWaitTime)
    else:

        if(bot.imageIsFound('6starsRune.png') or bot.imageIsFound('legendRune.png')):
            bot.clickImage('getRuneBtn.png', shortWaitTime)
        elif(bot.imageIsFound('5starsRune.png')):
            bot.clickImage('sell.png', shortWaitTime)
            bot.clickImage('yesBtn.png', shortWaitTime)

    bot.clickImage('replay.png', shortWaitTime)

def refillWithCrystals():
    bot.clickImage('shopBtn.png', shortWaitTime)
    bot.clickImage('refillCrystals.png', shortWaitTime)
    bot.clickImage('yesRefillBtn.png', mediumWaitTime)
    bot.clickImage('okBtn.png', shortWaitTime)
    bot.clickImage('closeShop.png', shortWaitTime)
def noMoreEnergy():
    return bot.imageIsFound('notEnoughEnergy.png')


def startRun():

    runIsDone = False

    while(runIsDone == False):
        try:
            if(bot.imageIsFound('replay.png')):
                bot.clickImage('replay.png', shortWaitTime)
            elif(bot.imageIsFound('okBtn.png')):
                bot.clickImage('okBtn.png', shortWaitTime)
            elif(bot.imageIsFound('5starsRune.png')):
                bot.clickImage('sell.png', shortWaitTime)
                bot.clickImage('yesBtn.png', shortWaitTime)

            elif(bot.imageIsFound('prepareBtn.png')):
                bot.clickImage('prepareBtn.png', shortWaitTime)

            elif(bot.imageIsFound('startBattleBtn.png')):
                bot.clickImage('startBattleBtn.png', shortWaitTime)

            elif(bot.imageIsFound('notEnoughEnergy.png')):
                runIsDone = True

            elif(bot.imageIsFound('rewardScreen.png')):
                time.sleep(0)
                victoryScreen()

            elif(bot.imageIsFound('reviveBtn.png')):
                time.sleep(longWaitTime)
                playerDied()
        except:
            print("Exception raised.")

def faimonRun():
    while(noMoreEnergy()==False):
        try:
            if(bot.imageIsFound('replay.png')):
                bot.clickImage('replay.png', shortWaitTime)
            elif(bot.imageIsFound('okBtn.png')):
                bot.clickImage('okBtn.png', 0)
            elif(bot.imageIsFound('sell.png')):
                bot.clickImage('sell.png', 0)
                if(bot.imageIsFound('yesBtn.png')):
                    bot.clickImage('yesBtn.png', shortWaitTime)
            elif(bot.imageIsFound('rewardScreen.png')):
                bot.clickImage('rewardScreen.png', 0.1)
                bot.clickImage('chest.png', shortWaitTime)

        except:
            print("catch")