import random
from colorama import Fore, Style
class Stats:
    role: str
    STR: int
    DEX: int
    CON: int
    INT: int
    WIS: int
    CHA: int

    def inputStats(self):
        self.STR = int (input(Fore.RED+"\nEnter your strength: "+ Style.RESET_ALL ))
        self.DEX = int (input(Fore.GREEN+ "Enter your dexterity: "+Style.RESET_ALL))
        self.CON = int (input(Fore.PURPLE+ "Enter your constitution: "+Style.RESET_ALL))
        self.WIS = int (input("Enter your wisdom: "))
        self.INT = int (input(Fore.ORANGE+"Enter your intelligence: "+Style.RESET_ALL))
        self.CHA = int (input(Fore.BLUE+ "Enter your charisma: "+Style.RESET_ALL))
    def autoStats(self):
        self.STR = 1
        self.DEX = 1
        self.CON = 1
        self.WIS = 1
        self.INT = 1
        self.CHA = 1


class die:

    #STR roll function
    def rollSTR(Emulator):
        roll = random.randint(1,20)
        print("You rolled a "+str(roll)+"!")
        check = roll+Emulator.STR
        if Emulator.STR > 0:
            print("+"+str(Emulator.STR)+" = "+str(check)+" overall!")
            return check
        if Emulator.STR < 0:
            print(str(Emulator.STR)+" = "+str(check)+" overall!")
            return check

    #DEX roll function
    def rollDEX(Emulator):
        roll = random.randint(1,20)
        print("You rolled a "+str(roll)+"!")
        check = roll+Emulator.DEX
        if Emulator.DEX > 0:
            print("+"+str(Emulator.DEX)+" = "+str(check)+" overall!")
            return check
        if Emulator.DEX < 0:
            print(str(Emulator.DEX)+" = "+str(check)+" overall!")
            return check
        
    #CON roll function
    def rollCON(Emulator):
        roll = random.randint(1,20)
        print("You rolled a "+str(roll)+"!")
        check = roll+Emulator.CON
        if Emulator.CON > 0:
            print("+"+str(Emulator.CON)+" = "+str(check)+" overall!")
            return check
        if Emulator.CON < 0:
            print(str(Emulator.CON)+" = "+str(check)+" overall!")
            return check

    #WIS roll function
    def rollWIS(Emulator):
        roll = random.randint(1,20)
        print("You rolled a "+str(roll)+"!")
        check = roll+Emulator.WIS
        if Emulator.WIS > 0:
            print("+"+str(Emulator.WIS)+" = "+str(check)+" overall!")
            return check
        if Emulator.WIS < 0:
            print(str(Emulator.WIS)+" = "+str(check)+" overall!")
            return check
        
    #INT roll function
    def rollINT(Emulator):
        roll = random.randint(1,20)
        print("You rolled a "+str(roll)+"!")
        check = roll+Emulator.INT
        if Emulator.INT > 0:
            print("+"+str(Emulator.INT)+" = "+str(check)+" overall!")
            return check
        if Emulator.INT < 0:
            print(str(Emulator.INT)+" = "+str(check)+" overall!")
            return check

    #CHA roll function
    def rollCHA(Emulator):
        roll = random.randint(1,20)
        print("You rolled a "+str(roll)+"!")
        check = roll+Emulator.CHA
        if Emulator.CHA > 0:
            print("+"+str(Emulator.CHA)+" = "+str(check)+" overall!")
            return check
        if Emulator.CHA < 0:
            print(str(Emulator.CHA)+" = "+str(check)+" overall!")
            return check
