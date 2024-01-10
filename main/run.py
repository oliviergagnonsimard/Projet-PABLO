import os
import pyautogui
import time

class Bot:
    DEFAULTPATH = "C:/Program Files (x86)/PokerStars/PokerStarsUpdate.exe"
    
    def __init__(self):
        pass

    def _run(self, first_spot = (750, 250), nbTables = 21, durée = 8):
        bot = Bot()
        bot.DemanderEmplacementPokerstars()
        time.sleep(10)
        bot.AccéderAuCompte()
        time.sleep(5)
        bot.DescendreEnBas(first_spot[0], first_spot[1], durée)
        bot.OuvrirTables(nbTables)

    def DemanderEmplacementPokerstars(self):
        bot = Bot()
        print("current default path: ""C:\Program Files (x86)\PokerStars\PokerStarsUpdate.exe""")
        answer = input("Would you like to use the default path to pokerstars? (y/n) ")
        if answer == "y":
            self.path = self.DEFAULTPATH
            bot.OuvrirPokerstars(self.path)
            return
        self.path = input("Where is pokerstars installed? (.exe) : ")
        bot.OuvrirPokerstars(self.path)


    def OuvrirPokerstars(self, path):
        print("Opening pokerstars")
        os.startfile(path)


    def AccéderAuCompte(self):
        print("Accessing account")
        Bot.press("enter")

    def DescendreEnBas(self, x, y, durée):
        Bot.click(x, y)
        start_time = time.time()
        while time.time() - start_time < durée:
            print("test")
            pyautogui.keyDown("Down")
        pyautogui.keyUp("Down")
        Bot.press("up")

    def OuvrirTables(self, nbTables):
        for _ in range(nbTables):
            Bot.press("enter")
            time.sleep(0.5)

            pyautogui.keyDown("alt")
            time.sleep(0.3)
            Bot.press("tab")
            pyautogui.keyUp("alt")
            time.sleep(0.3)

            Bot.press("up")
        pass

    @staticmethod
    def click(x, y):
        pyautogui.click(x, y)
    @staticmethod
    def press(touche):
        pyautogui.press(touche)

bot = Bot()
bot._run(nbTables=5)
# Pokerstars autorise jusqu'à 21 tables observés à la fois.