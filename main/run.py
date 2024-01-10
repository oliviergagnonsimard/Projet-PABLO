import os

class Bot:
    DEFAULTPATH = "C:/Program Files (x86)/PokerStars/PokerStarsUpdate.exe"
    
    def __init__(self):
        pass

    def DemanderEmplacementPokerStars(self):
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
        print("Ouverture de pokerstars")
        os.startfile(path)


bot = Bot()

bot.DemanderEmplacementPokerStars()