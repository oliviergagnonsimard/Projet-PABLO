import re

class Parse:

    def __init__(self,main):
        self.main = main


    def Identifier_infos(self):
        utg = ""
        utg_1 = ""
        utg_2 = ""
        lowjack = ""
        highjack = ""
        cutoff = ""
        button = ""


        stack_utg = ""
        stack_utg_1 = ""
        stack_utg_2 = ""
        stack_lowjack = ""
        stack_highjack = ""
        stack_cutoff = ""
        stack_smallblind = ""
        stack_bigblind = ""

        action = ""
        flop = ""
        turn = ""
        river = ""

        motif_1 = r'^Seat 1:[ABC]'


        smallblind = ":\sposts\ssmall\sblind"

        bigblind_motif = r".+:\sposts\sbig\sblind"

        bb = re.search(bigblind_motif, self.main)



    def recup_pseudo(self,chemin):
        for i in chemin:
            a = ""
            if i != ":":
                a += i
            else:
                pseudo = a




