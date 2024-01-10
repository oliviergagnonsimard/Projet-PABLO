import re

class Parse:

    def __init__(self,main):
        self.main = main
        self.nombre_joueur = self.nombre_joueur()
        self.num_seat_bb = ''
    def identifier_infos(self):
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

        smallblind_info = re.search(r".+:\sposts\ssmall\sblind", self.main).group()
        bigblind_info = re.search(r".+:\sposts\sbig\sblind", self.main).group()
        smallblind = self.recup_pseudo_avant(smallblind_info)
        bigblind = self.recup_pseudo_avant(bigblind_info)
        self.recherche_seat_bb(bigblind)
        for i in range(int(self.nombre_joueur)):
            pseudo = re.search(r"Seat \d+: \w+", self.main).group()
            pseudo = self.recup_pseudo_apres(pseudo)
            self.recherche_position(int(self.num_seat_bb),pseudo)
    def recup_pseudo_avant(self, infos):
        a = ""
        for i in infos:
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
    def recup_stack_joueur(self,joueur):
        a = re.search(r"^Seat \d: andy_keiv \(\$\d\.\d+ in chips\)",self.main)

    def recherche_seat_bb(self,bigblind_pseudo):

      #  try:
        g = re.compile(fr"^Seat \d: {bigblind_pseudo}")
        info = re.search(g, self.main)
        info2 = info.group()
        self.num_seat_bb = info[6]
       # except AttributeError:
         #   print("a")

    def recherche_position(self,num_seat_bb,pseudo):
       # if re.search(r"^Table '\w+ \w+' 6-max",self.main):
       for i in range(int(self.nombre_joueur)):
            no_seat = int(re.search(fr"^ Seat \w:{pseudo}",self.main).group()[6])
            if no_seat == num_seat_bb+(self.nombre_joueur-2) or no_seat == num_seat_bb-(self.nombre_joueur-4):
                button = pseudo
            elif no_seat == num_seat_bb+(self.nombre_joueur-3) or no_seat == num_seat_bb-(self.nombre_joueur-3):
                cutoff = pseudo
            elif no_seat == num_seat_bb+(self.nombre_joueur-4) or no_seat == num_seat_bb-(self.nombre_joueur-2):
                highjack = pseudo
            elif no_seat == num_seat_bb+(self.nombre_joueur-5) or no_seat == num_seat_bb-(self.nombre_joueur-1):
                lowjack = pseudo
    def nombre_joueur(self):
        occurrences_joueurs = re.findall(re.compile(r'Seat \d+: '), self.main)
        return len(occurrences_joueurs)/2

P = Parse(main="""PokerStars Hand #248175750958:  Hold'em No Limit ($0.01/$0.02 USD) - 2024/01/09 19:32:13 ET
Table 'Alhena III' 6-max Seat #5 is the button
Seat 1: andy_keiv ($1.97 in chips)
Seat 2: RReyesJ ($1.41 in chips)
Seat 3: ULISSES 222 ($1.69 in chips)
Seat 5: altazorchile ($1.58 in chips)
Seat 6: PokerBoss2639 ($2.07 in chips)
PokerBoss2639: posts small blind $0.01
andy_keiv: posts big blind $0.02
*** HOLE CARDS ***
RReyesJ: folds
ULISSES 222: folds
altazorchile: calls $0.02
PokerBoss2639: folds
andy_keiv: checks
*** FLOP *** [6c Th 2c]
andy_keiv: checks
altazorchile: checks
*** TURN *** [6c Th 2c] [2d]
Zeydn13 joins the table at seat #4
andy_keiv: bets $0.03
altazorchile: calls $0.03
*** RIVER *** [6c Th 2c 2d] [7d]
ULISSES 222 leaves the table
andy_keiv: checks
altazorchile: checks
*** SHOW DOWN ***
andy_keiv: shows [8d Qs] (a pair of Deuces)
altazorchile: shows [5d 6d] (two pair, Sixes and Deuces)
altazorchile collected $0.11 from pot
*** SUMMARY ***
Total pot $0.11 | Rake $0
Board [6c Th 2c 2d 7d]
Seat 1: andy_keiv (big blind) showed [8d Qs] and lost with a pair of Deuces
Seat 2: RReyesJ folded before Flop (didn't bet)
Seat 3: ULISSES 222 folded before Flop (didn't bet)
Seat 5: altazorchile (button) showed [5d 6d] and won ($0.11) with two pair, Sixes and Deuces
Seat 6: PokerBoss2639 (small blind) folded before Flop""")
P.identifier_infos()
