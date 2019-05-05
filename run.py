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

def runesFound():
    if(bot.imageIsFound('6starsRune.png')):
        print('6* runes')

    else:
        pos = bot.locateImage('sell.png')
        bot.clickImage(pos)
        time.sleep(1)
        pos = bot.locateImage('yesBtn.png')
        bot.clickImage(pos)
        time.sleep(1)
        print('runes')

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