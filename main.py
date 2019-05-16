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


if __name__== "__main__":
    '''
    app.setStyle('Fusion')
    window = QWidget()
    window.setLayout(createLayout())
    window.show()
    app.exec_()
    '''
    print("What would you like to do? Select by entering the number.")

    userInput = 0
    refillWithCrystals = input("Do you want to refill with crystals? y/n")

    while(userInput != "3"):
        userInput = input("1 : Farm dungeons\n 2 : Farm Faimon\n 3 : Quit\n")
        if(userInput == "1"):
            print("Bot is now farming dungeon.")
            while(run.noMoreEnergy()==False):
                run.startRun()
                if(refillWithCrystals == "y" and run.noMoreEnergy()==True):
                    run.refillWithCrystals()
        elif(userInput == "2"):
            print("Starting bot to farm faimon.")
            while(run.noMoreEnergy()==False):
                run.faimonRun()
        elif(userInput == "3"):
            print("Quitting.")
        else:
            print("Unknown value, please enter 1 or 2 to select an option.")