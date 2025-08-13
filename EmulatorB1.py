from Dice import Stats
from Dice import die
from EmulatorA1 import A1
class B1:
    def __init__(self, char_stats, debugMode, role, officalA1, a1BashFail, a1LockFail, a1CallFail):
        self.char_stats = char_stats
        self.debugMode = debugMode
        self.role = role
        self.officialA1 = officalA1
        self.a1BashFail = a1BashFail
        self.a1LockFail = a1LockFail
        self.a1CallFail = a1CallFail
        #changable
        self.phealth = self.char_stats.CON + 10
        self.haveItems = False
        self.check = 0
        self.bfightHaveAdvantage = False
        self.bfightHaveDisadvantage = False

    #successful choices: afirebolt, abash
    def b1choice(self):
        #char_stats = self.char_stats
        #debugMode = self.debugMode
        #role = self.role
        #officialA1 = self.officialA1
        #a1BashFail = self.a1BashFail
        #a1LockFail = self.a1LockFail
        #a1CallFail = self.a1CallFail
        input("As the door breaking resounds through the empty air, you hear a pair of footsteps rapidly approaching.")
        input("Guards are coming! You quickly glance around your surroundings, looking for options.")
        input("Your stuff is but only a few meters away, but could take up precious seconds...")
        print("You could:")
        print("Grab your stuff and fight them! - 'fight'")
        print("Try to run away! - 'run'")
        print("Try to grab your stuff, and THEN run - 'grab'") #harder to pass check, but otherwise you don't get stuff as a variable later on
        if self.role == "mage":
            print("Cast a spell - 'cast'")
        self.nextb1 = input("\nWhat do you want to do? Enter: ")
        return self.nextb1
    def bfight(self):
        #pasting the battle code here
    def brun(self):
        if self.haveItems == False:
            input("You take a longing look towards your stuff, but decide it's not worth the risk.")
            input("...It'd be pretty hard to go back for it later.")
            input("Either way, you decide to run for it!")
            input("Roll to evade the guards!")
            self.check = die.rollDEX(self.char_stats)
            if self.check > 5:
                input("You start running, and find a room off the main path.")
                input("Right as the guards round the corner, you slip in.")
                input("You put a hand over your mouth, muffling any breathing.")
                input("You don't dare close your eyes.")
                input("...silence.")
                input("It seems the coast is clear! (You passed the check!)")
        if self.haveItems == True:
            input("You take a glance towards the connecting corridor, and grab your stuff!")

    def b1choiceif(self):
        if self.nextb1 == "fight":
            input("You quickly lunge for your stuff, and take inventory of it.")
            if self.role == "warrior":
                input("It's your trusty sword and shield!")
                input("You quickly wrap the sheath around your waist as you reveal your blade.")
                input("As you see the guards rapidly approaching, you slide your shield onto your arm, ready in battle stance.")
                self.bfight()
            elif self.role == "mage":
                input("It's your beloved tome!")
                input("As you snap it open with one hand, your handwriting, scrawling from page to page, is revealed.")
                input("As you see the guards rapidly approaching, you refresh yourself on your new spell, ready.")
                #learn thorny vines
                self.bfight()
            elif self.role == "rogue":
                input("It's your sharpened dagger and lockpicking tools!")
                if self.officialA1 == "call" and self.a1LockFail == False:
                    input("Thank goodness you didn't have to use that hair pin.")
                    input("You'd be quite disappointed if it broke.")
                elif self.officialA1 == "lock":
                    input("Thank goodness your hair pin worked!")
                    input("You'd be quite disappointed if it broke.")
                elif self.a1LockFail == True:
                    input("...It's sad you got them back only after your hair pin broke.")
                    input("You quite liked it!")
                    input("However, it did serve its use as a backup lockpick. Ah well.")
                input("Either way, you spin your dagger around, slotting perfectly in your hand as you crouch behind the wall.")
                input("You're ready.")
                self.bfight()   #caalling the battle code
        elif self.nextb1 == "run":
            self.brun()
        elif self.nextb1 == "grab":
            self.haveItems = True
            self.brun()
        else:
            input("Invalid option. Try again!")
            self.nextb1 = self.b1choice()
            self.officalb1 = self.b1choiceif()







"""
import random
from Dice import Stats
from Dice import die
from EmulatorA1 import A1
from EmulatorB1 import B1
class Player:
  def __init__(self,role):
    self.role = role
    self.skills= []
    if role == "warrior":
      self.name = "Warrior of Light"
      self.stamina= 150
      self.attack = 15
      self.defence= 10
    elif role == "mage":
      self.name = "Mage of Flames"
      self.stamina = 120
      self.attack = 12
      self.defence = 8
    elif role == "rogue"
      self.name= "Rogue Of Shadow"
      self.stamina= 100
      self.attack= 10
      self.defence= 6

class Enemy :
  def __init__(self):
    self.name= "Dragon"
    self.stamina= 110
    self.attack= 9
    self.defence = 4

def battle(player,enemy):
    damage_to_enemy = player.attack - enemy.defence
    if damage_to_enemy<0:
      damage_to_enemy =0 
    enemy.stamina -= damage_to_enemy 
    print(f"{player.name} attacks {enemy.name} for {damage_to_enemy} damage!")
    print(f"{enemy.name} now has {enemy.stamina}stamina left")
   
    damage_to_player = enemy.attack - player.defence
    if damage_to_player<0:
      damage_to_player =0 
    player.stamina -= damage_to_player 
    print(f"{enemy.name} attacks {player.name} for {damage_to_player} damage!")
    print(f"{player.name} now has {player.stamina}stamina left")
"""
    
    
    


    
