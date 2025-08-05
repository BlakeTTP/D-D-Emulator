import random
#random.randint(1, 6)
#random.randint(1, 20)

#beginning part/decription of skills
input("(Whenever you don't need to enter anything in, then just press ENTER to continue.)")
#input("(As well, answer everything in all lowercase, and no typos.)")
input("Now, lets begin your journey.")
print("\nChoose your role:warrior, theif or rogue.")
role = input("Enter your role:")
print("Great Choice!!!")

#based on the roles
if role=="warrior":
    print("\n You are a fearless Warrior, clad in heavy armor, with shield and sword in hand, marching toward the Fortress.")
elif role=="theif":
    print("You are a master Thief, who is quick, clever, and silent, with hands skilled in locks and a mind sharp as any blade.")
elif role=="rogue":
    print("You are a Rogue, who is silent but deadly since you are a sharp dagger no matter where you stand, and always four steps ahead.")


input("First, to begin your story, we need to configure your stats.")
input("There's six to configure.")
print("Strength(STR): Determines how physically strong you are.")
input("Dexterity(DEX): Determines your flexibility, dodging, and sneaking ability.")
input("Constitution(CON): Determines how much your body can physically take, mainly health.")
input("Wisdom(WIS): Determines how wise you are/how much conventional wisdom you have, or 'common sense'.")
input("Intelligence(INT): Determines how much you know, or 'book knowledge'.")
input("Charisma(CHA): Determines your social skills.")
input("Everytime you make a decision, a die is rolled to see how effective it is.")
input("These stats are modifiers that make you better or worse at certain skills.")
input("The array you're allowed to use is -1, 0, 1, 1, 2, and 3.")
STR = int (input("Enter your strength: "))
DEX = int (input("Enter your dexterity: "))
CON = int (input("Enter your constitution: "))
WIS = int (input("Enter your wisdom: "))
INT = int (input("Enter your intelligence: "))
CHA = int (input("Enter your charisma: "))

#STR roll function
def rollSTR():
    roll = random.randint(1,20)
    print("You rolled a "+str(roll)+"!")
    check = roll+STR
    if STR > 0:
        print("+"+str(STR)+" = "+str(check)+" overall!")
        return check
    if STR < 0:
        print(str(STR)+" = "+str(check)+" overall!")
        return check
    

answer1 = input("testcheck1: enter yes no or maybe: ")
if answer1 == "yes":
    input("you said yes!")
    a1 = 1
    input("since you said yes, this thing happens! roll for strength!")
    check = rollSTR()
    if check >= 9:
        input("you passed the check! insert good job here!")
    if check <= 9:
        input("you failed the check! rip")

if answer1 == "no":
    input("you said no!")
    a1 = 2

if answer1 == "maybe":
    input("you said maybe!")
    a1 = 3

