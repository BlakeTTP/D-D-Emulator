from Dice import Stats
from Dice import die
from EmulatorA1 import A1

class B2:
    def __init__(self, char_stats, debugMode, role, a1BashFail, a1LockFail, a1CallFail):
        self.char_stats = char_stats
        self.debugMode = debugMode
        self.role = role
        self.a1BashFail = a1BashFail
        self.a1LockFail = a1LockFail
        self.a1CallFail = a1CallFail
        #changable
        self.phealth = self.char_stats.CON + 10
        self.haveItems = True
        self.check = 0
        self.bfightHaveAdvantage = False
        self.bfightHaveDisadvantage = False
    def b2choice(self):
        input(" ")
    def b2choiceif(self):
        input(" ")
