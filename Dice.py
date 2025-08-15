import random

class Stats:
    role: str
    STR: int
    DEX: int
    CON: int
    INT: int
    WIS: int
    CHA: int

    
    def __init__(self):
        self.STR = 0
        self.DEX = 0
        self.CON = 0
        self.WIS = 0
        self.INT = 0
        self.CHA = 0

    def inputStats(self):
        available_values = [-1, 0, 1, 1, 2, 2]
        print("\033[36mYou possess a unique set of trait values to distribute among your skills.\nUse each value wisely, once assigned, it cannot be used again [-1, 0, 1, 1, 2, and 2.]\033[0m")
        
        for stat in ["Strength (STR)", "Dexterity (DEX)", "Constitution (CON)", "Wisdom (WIS)", "Intelligence (INT)", "Charisma (CHA)"]:
            while True:
                print(f"\n\033[33mAvailable values:\033[0m {available_values}")
                try:
                    val = int(input(f"\033[36mAssign a value to {stat}: \033[0m"))
                except ValueError:
                    print("\033[31mInvalid input! Please enter a number.\033[0m")
                    continue

                if val in available_values:
                    if "Strength" in stat:
                        self.STR = val
                    elif "Dexterity" in stat:
                        self.DEX = val
                    elif "Constitution" in stat:
                        self.CON = val
                    elif "Wisdom" in stat:
                        self.WIS = val
                    elif "Intelligence" in stat:
                        self.INT = val
                    elif "Charisma" in stat:
                        self.CHA = val
                    available_values.remove(val)
                    break
                else:
                    print("\033[31mInvalid choice! Pick from the available values only.\033[0m")
       
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
