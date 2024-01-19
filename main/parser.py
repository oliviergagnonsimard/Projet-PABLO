import re

class Parse:

    def __init__(self,main):
        self.main = main
        self.nombre_joueur = self.nombre_joueur()
        self.num_seat_bb = ''
    def identifier_infos(self):

        #action = ""
        #flop = ""
        #turn = ""
        #river = ""

        #motif_1 = r'Seat \w: andy_keiv'

        smallblind_info = re.search(r".+:\sposts\ssmall\sblind", self.main).group()
        bigblind_info = re.search(r".+:\sposts\sbig\sblind", self.main).group()
        self.smallblind = self.recup_pseudo_avant(smallblind_info)
        self.bigblind = self.recup_pseudo_avant(bigblind_info)
        self.recherche_seat_bb(self.bigblind)
        b=0
        for _ in range(int(self.nombre_joueur)+1):
            b+=1
            try:
                pseudo = re.search(fr"Seat {b}: \w+", self.main).group()
                pseudo = self.recup_pseudo_apres(pseudo)
                self.recherche_position(int(self.num_seat_bb),pseudo)
                self.recup_stack_joueur(pseudo)
            except AttributeError:
                pass
        print("a")
    def recup_pseudo_avant(self, infos):
        a = ""
        for i in infos:
            if i != ":":
                a += i
            else:
                return a
    def recup_pseudo_apres(self, infos):
        b = 0
        for i in infos:
            if i != ":":
                b+=1
            else:
                return infos[b+2:]
    def recup_stack_joueur(self,joueur):
        stack = re.search(fr"Seat \d: {joueur} \(\$\d\.\d+ in chips\)",self.main).group()

        if self.bigblind == joueur:
            self.stack_bigblind = float(re.search(r"\$\d\.\d+",stack).group()[1:])/0.02
        elif self.smallblind == joueur:
            self.stack_smallblind = float(re.search(r"\$\d\.\d+",stack).group()[1:])/0.02
        elif self.cutoff == joueur:
            self.stack_cutoff = float(re.search(r"\$\d\.\d+",stack).group()[1:])/0.02
        elif self.highjack == joueur:
            self.stack_highjack = float(re.search(r"\$\d\.\d+",stack).group()[1:])/0.02
        elif self.lowjack == joueur:
            self.stack_lowjack = float(re.search(r"\$\d\.\d+",stack).group()[1:])/0.02
        elif self.button == joueur:
            self.stack_button = float(re.search(r"\$\d\.\d+",stack).group()[1:])/0.02

    def recherche_seat_bb(self,bigblind_pseudo):
        motif = fr"Seat \d: {re.escape(bigblind_pseudo)}"
        match = re.search(motif, self.main)
        info2 = match.group()
        self.num_seat_bb = info2[5]


    def recherche_position(self,num_seat_bb,pseudo):
       # if re.search(r"^Table '\w+ \w+' 6-max",self.main):

        no_seat = int(re.search(fr"Seat \w: {pseudo}",self.main).group()[5])
        if no_seat == num_seat_bb+(self.nombre_joueur-2) or no_seat == num_seat_bb-(self.nombre_joueur-4):
            self.button = pseudo
        elif no_seat == num_seat_bb+(self.nombre_joueur-3) or no_seat == num_seat_bb-(self.nombre_joueur-3):
            self.cutoff = pseudo
        elif no_seat == num_seat_bb+(self.nombre_joueur-4) or no_seat == num_seat_bb-(self.nombre_joueur-2):
            self.highjack = pseudo
        elif no_seat == num_seat_bb+(self.nombre_joueur-5) or no_seat == num_seat_bb-(self.nombre_joueur-1):
            self.lowjack = pseudo
    def nombre_joueur(self):
        occurrences_joueurs = re.findall(re.compile(r'Seat \d+: '), self.main)
        return len(occurrences_joueurs)/2

P = Parse(main="""PokerStars Hand #248211475345:  Hold'em No Limit ($0.01/$0.02 USD) - 2024/01/11 15:33:49 ET
Table 'Albertine II' 6-max Seat #2 is the button
Seat 1: BeSmartNFold ($8.41 in chips) 
Seat 2: Muszkli299 ($2 in chips) 
Seat 3: LongRanges ($2.31 in chips) 
Seat 4: Alek$win ($2 in chips) 
Seat 5: Marwizy ($8.12 in chips) 
Seat 6: Nema.H.B ($2.14 in chips) 
LongRanges: posts small blind $0.01
Alek$win: posts big blind $0.02
*** HOLE CARDS ***
Marwizy: raises $0.02 to $0.04
Nema.H.B: raises $0.08 to $0.12
BeSmartNFold: calls $0.12
Muszkli299: calls $0.12
LongRanges: raises $0.24 to $0.36
Alek$win: folds 
Marwizy: calls $0.32
Nema.H.B: calls $0.24
BeSmartNFold: calls $0.24
Muszkli299: calls $0.24
*** FLOP *** [9h 7s Ks]
LongRanges: bets $0.58
Marwizy: calls $0.58
Nema.H.B: folds 
BeSmartNFold: folds 
Muszkli299: folds 
*** TURN *** [9h 7s Ks] [Ac]
LongRanges: checks 
Marwizy: bets $1.44
LongRanges: calls $1.37 and is all-in
Uncalled bet ($0.07) returned to Marwizy
*** RIVER *** [9h 7s Ks Ac] [6s]
*** SHOW DOWN ***
LongRanges: shows [Ts Kh] (a pair of Kings)
Marwizy: shows [5h Ah] (a pair of Aces)
Marwizy collected $5.52 from pot
*** SUMMARY ***
<<<<<<< HEAD
Total pot $0.11 | Rake $0
Board [6c Th 2c 2d 7d]
Seat 1: andy_keiv (big blind) showed [8d Qs] and lost with a pair of Deuces
Seat 2: RReyesJ folded before Flop (didn't bet)
Seat 3: ULISSES 222 folded before Flop (didn't bet)
Seat 5: altazorchile (button) showed [5d 6d] and won ($0.11) with two pair, Sixes and Deuces
Seat 6: PokerBoss2639 (small blind) folded before Flop""")
P.identifier_infos()
=======
Total pot $5.72 | Rake $0.20 
Board [9h 7s Ks Ac 6s]
Seat 1: BeSmartNFold folded on the Flop
Seat 2: Muszkli299 (button) folded on the Flop
Seat 3: LongRanges (small blind) showed [Ts Kh] and lost with a pair of Kings
Seat 4: Alek$win (big blind) folded before Flop
Seat 5: Marwizy showed [5h Ah] and won ($5.52) with a pair of Aces
Seat 6: Nema.H.B folded on the Flop
""")
# P = Parse(main="""PokerStars Hand #248175750958:  Hold'em No Limit ($0.01/$0.02 USD) - 2024/01/09 19:32:13 ET
# Table 'Alhena III' 6-max Seat #5 is the button
# Seat 1: andy_keiv ($1.97 in chips)
# Seat 2: RReyesJ ($1.41 in chips)
# Seat 3: ULISSES 222 ($1.69 in chips)
# Seat 5: altazorchile ($1.58 in chips)
# Seat 6: PokerBoss2639 ($2.07 in chips)
# PokerBoss2639: posts small blind $0.01
# andy_keiv: posts big blind $0.02
# *** HOLE CARDS ***
# RReyesJ: folds
# ULISSES 222: folds
# altazorchile: calls $0.02
# PokerBoss2639: folds
# andy_keiv: checks
# *** FLOP *** [6c Th 2c]
# andy_keiv: checks
# altazorchile: checks
# *** TURN *** [6c Th 2c] [2d]
# Zeydn13 joins the table at seat #4
# andy_keiv: bets $0.03
# altazorchile: calls $0.03
# *** RIVER *** [6c Th 2c 2d] [7d]
# ULISSES 222 leaves the table
# andy_keiv: checks
# altazorchile: checks
# *** SHOW DOWN ***
# andy_keiv: shows [8d Qs] (a pair of Deuces)
# altazorchile: shows [5d 6d] (two pair, Sixes and Deuces)
# altazorchile collected $0.11 from pot
# *** SUMMARY ***
# Total pot $0.11 | Rake $0
# Board [6c Th 2c 2d 7d]
# Seat 1: andy_keiv (big blind) showed [8d Qs] and lost with a pair of Deuces
# Seat 2: RReyesJ folded before Flop (didn't bet)
# Seat 3: ULISSES 222 folded before Flop (didn't bet)
# Seat 5: altazorchile (button) showed [5d 6d] and won ($0.11) with two pair, Sixes and Deuces
# Seat 6: PokerBoss2639 (small blind) folded before Flop""")
P.identifier_infos()
>>>>>>> 4d0e0f92c7022d3560a5daf5370afebe3621005a
