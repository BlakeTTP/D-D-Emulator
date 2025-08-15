from Dice import Stats
from Dice import die
from EmulatorA1 import A1

class B2:
    def __init__(self, char_stats, debugMode, role, officialA1, a1BashFail, a1LockFail, a1CallFail):
        self.char_stats = char_stats
        self.debugMode = debugMode
        self.role = role
        self.officialA1 = officialA1
        self.a1BashFail = a1BashFail
        self.a1LockFail = a1LockFail
        self.a1CallFail = a1CallFail
        #changable
        self.phealth = self.char_stats.CON + 10
        self.haveItems = True
        self.check = 0
        self.bfightHaveAdvantage = False
        self.bfightHaveDisadvantage = False

        self.hasLootedRoom = False
        self.hasLootedGuard = False

    def b2choice(self):
        input("Temporary text! Mention grabbing the tools. Options:")
        print("\nLeave the room: 'leave'")
        if self.hasLootedRoom == False:
            print("Look around for loot - 'loot'")
        if self.officialA1 == "acall" and self.hasLootedGuard == False:
            print("Loot the guard - 'loot guard'")
        if self.officialA1 == "acall" and self.hasLootedGuard == False and self.role == "rogue":
            print("Disguise yourself as the guard - 'disguise'")
        self.nextb2 = input("\nWhat do you want to do? Enter: ")
        return self.nextb2


    def b2choiceif(self):
        if self.nextb2 == "loot":
            pass
