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
        if self.debugMode == False:
            input("Treading lightly, you slip unnoticed up to the table across from your cell.")
            if self.role == "warrior":
                input("Your hands glide over your sword and shield.")
                input("You slide the art of metallurgy into its sheath and protective gear against your arm, back where it belongs.")
            if self.role == "mage":
                input("Your hands glide over your tome, worn and aged with every flicker from your pens.")
                input("You slot the tome back against your body, familiar weight settling against you.")
            if self.role == "rogue":
                input("Your hands glide over your lockpicking tools and dagger.")
                input("Dagger held curved perfectly to suit your hand, you slot the tools against your body, back where they belong.")
            input("Despite it being only a short span of time since being parted from your belongings, you can say with certainty- ")
            input("You missed this.")
            input("Now that you’re reunited though, you have bigger priorities.")
            input("You look around the room surrounding your cell.")
        input("You could try to: ")
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
