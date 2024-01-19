import os
import pyautogui
import time
import pygetwindow as gw

# WIN+UP (fullscreen)
class Bot:
    DEFAULTPATH = "C:/Program Files (x86)/PokerStars/PokerStarsUpdate.exe"
    
    def __init__(self):
        pass

    def _run(self, first_spot = (750, 250), nbTables = 21, durée = 8):
        self.DemanderEmplacementPokerstars()
        time.sleep(10)
        self.AccéderAuCompte()
        time.sleep(6)
        self.DescendreEnBas(first_spot[0], first_spot[1], durée)
        self.OuvrirTables(nbTables)
        self.OuvrirHistorique()

    def DemanderEmplacementPokerstars(self):
        print("current default path: ""C:\Program Files (x86)\PokerStars\PokerStarsUpdate.exe""")
        answer = input("Would you like to use the default path to pokerstars? (y/n) ")
        if answer == "y":
            self.path = self.DEFAULTPATH
            self.OuvrirPokerstars(self.path)
            return
        self.path = input("Where is pokerstars installed? (.exe) : ")
        self.OuvrirPokerstars(self.path)


    def OuvrirPokerstars(self, path):
        print("Opening pokerstars")
        os.startfile(path)


    def AccéderAuCompte(self):
        print("Accessing account")
        Bot.press("enter")

    def DescendreEnBas(self, x, y, durée):
        Bot.click(x, y)
        for _ in range(75):
            Bot.press("down")
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

    def OuvrirHistorique(self):
        pyautogui.keyDown("alt")
        time.sleep(0.3)
        Bot.press("tab")
        time.sleep(0.3)
        Bot.press("tab")
        pyautogui.keyUp("alt")
        time.sleep(0.3)

        pyautogui.keyDown("win")
        time.sleep(0.3)
        pyautogui.press("up")
        time.sleep(0.3)
        pyautogui.keyUp("win")

        time.sleep(2)

        self.click(250, 870)
        time.sleep(1)
        self.click(720, self.get_window_size("PokerStars Lobby")[1] * 0.89)

    #89%
    def get_window_size(self, title):
        window = gw.getWindowsWithTitle(title)[0]
        return window.width, window.height



    @staticmethod
    def click(x, y):
        pyautogui.click(x, y)

    @staticmethod
    def press(touche):
        pyautogui.press(touche)

bot = Bot()
bot._run(nbTables=5)
# Pokerstars autorise jusqu'à 21 tables observés à la fois.