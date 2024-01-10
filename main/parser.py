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

        motif_1 = r'^Seat \w: andy_keiv'

        smallblind_info = re.search(r":\sposts\ssmall\sblind", self.main).group()
        bigblind_info = re.search(r".+:\sposts\sbig\sblind", self.main).group()
        smallblind = self.recup_pseudo_avant(smallblind_info)
        bigblind = self.recup_pseudo_avant(bigblind_info)
        self.recherche_seat_bb(bigblind)

    def recup_pseudo_avant(self, infos):
        for i in infos:
            a = ""
            if i != ":":
                a += i
            else:
                return a
    def recup_pseudo_apres(self, infos):
        for i in infos:
            b = 0
            if i != ":":
                b+=1
            else:
                return infos[b+1:]
    def recherche_seat_bb(self,bigblind_pseudo):
        info = re.search(fr"^ Seat \w: {bigblind_pseudo}",self.main).group()
        self.num_seat_bb = info[6]

    def recherche_position(self,num_seat_bb,pseudo):
        if re.search(r"^Table '\w+ \w+' 6-max",self.main):
            no_seat = int(re.search(fr"^ Seat \w:{pseudo}",self.main).group()[6])
            if no_seat == num_seat_bb+1 or no_seat == num_seat_bb-5:
                lowjack = pseudo
            elif no_seat == num_seat_bb+2 or no_seat == num_seat_bb-4:
                highjack = pseudo
            elif no_seat == num_seat_bb+3 or no_seat == num_seat_bb-3:
                cutoff = pseudo
            elif no_seat == num_seat_bb+4 or no_seat == num_seat_bb-2:
                button = pseudo
        if re.search(r"^Table '\w+ \w+' 9-max",self.main):
            pass









