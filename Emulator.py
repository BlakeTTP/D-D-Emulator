import random
#random.randint(1, 6)
#random.randint(1, 20)

#beginning part/decription of skills
input("(Whenever you don't need to enter anything in, then just press ENTER to continue.)")
input("Now, let's begin your journey.")
print("\nChoose your role: warrior, mage or rogue.")
role = input("Enter your role: ")
print("Great Choice!!!")

#based on the roles
if role=="warrior":
    print("You are a fearless Warrior, clad in heavy armor, with shield and sword in hand, marching toward the Fortress.") #", marching toward the Fortress"
    print("(+1 to Strength)")
elif role=="mage":
    #print("You are a master Thief, who is quick, clever, and silent, with hands skilled in locks and a mind sharp as any blade.")
    print("You are a Mage, an apprentice learning the art of the magic that flows through your world, knowledge heavy as your tome.")
    print("(+1 to Intelligence)")
elif role=="rogue":
    print("You are a Rogue, who is silent but deadly since you are a sharp dagger no matter where you stand, and always four steps ahead.")
    print("(+1 to Dexterity)")

#stat configuration
input("First, to begin your story, we need to configure your stats.")
input("Whatever class you choose already added +1 to one of them, which stacks with whatever you choose as your array.")
input("While you can choose otherwise, it's recommended to have your main stat you use for your class be high for class specific options.")
input("There's six to configure.")
input("Strength(STR): Determines how physically strong you are.")
input("Dexterity(DEX): Determines your flexibility, dodging, and sneaking ability.")
input("Constitution(CON): Determines how much your body can physically take, mainly health.")
input("Wisdom(WIS): Determines how wise you are/how much conventional wisdom you have, or 'common sense'.")
input("Intelligence(INT): Determines how much you know, or 'book knowledge'.")
input("Charisma(CHA): Determines your social skills.")
input("Everytime you make a decision, a die is rolled to see how effective it is.")
input("These stats are modifiers that make you better or worse at certain skills.")
input("The array you're allowed to use is -1, 0, 1, 1, 2, and 2.")
input("That means you can use each number once, for each stat.")
STR = int (input("\nEnter your strength: "))
DEX = int (input("Enter your dexterity: "))
CON = int (input("Enter your constitution: "))
WIS = int (input("Enter your wisdom: "))
INT = int (input("Enter your intelligence: "))
CHA = int (input("Enter your charisma: "))

#class based addition to stats
if role == "warrior":
    STR = STR+1
elif role == "mage":
    INT = INT+1
elif role == "rogue":
    DEX = DEX+1

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

#DEX roll function
def rollDEX():
    roll = random.randint(1,20)
    print("You rolled a "+str(roll)+"!")
    check = roll+DEX
    if DEX > 0:
        print("+"+str(DEX)+" = "+str(check)+" overall!")
        return check
    if DEX < 0:
        print(str(DEX)+" = "+str(check)+" overall!")
        return check
    
#CON roll function
def rollCON():
    roll = random.randint(1,20)
    print("You rolled a "+str(roll)+"!")
    check = roll+CON
    if CON > 0:
        print("+"+str(CON)+" = "+str(check)+" overall!")
        return check
    if CON < 0:
        print(str(CON)+" = "+str(check)+" overall!")
        return check

#WIS roll function
def rollWIS():
    roll = random.randint(1,20)
    print("You rolled a "+str(roll)+"!")
    check = roll+WIS
    if WIS > 0:
        print("+"+str(WIS)+" = "+str(check)+" overall!")
        return check
    if WIS < 0:
        print(str(WIS)+" = "+str(check)+" overall!")
        return check
    
#INT roll function
def rollINT():
    roll = random.randint(1,20)
    print("You rolled a "+str(roll)+"!")
    check = roll+INT
    if INT > 0:
        print("+"+str(INT)+" = "+str(check)+" overall!")
        return check
    if INT < 0:
        print(str(INT)+" = "+str(check)+" overall!")
        return check

#CHA roll function
def rollCHA():
    roll = random.randint(1,20)
    print("You rolled a "+str(roll)+"!")
    check = roll+CHA
    if CHA > 0:
        print("+"+str(CHA)+" = "+str(check)+" overall!")
        return check
    if CHA < 0:
        print(str(CHA)+" = "+str(check)+" overall!")
        return check
    
#beginning
def beginning():
    input("You find yourself lying on the ground, and the first thing you're aware of is the migraine blooming through your skull.")
    input("What, did someone hit y- oh. Someone did.")
    input("First things first.")
    input("You were in the village, training like usual.")
    if role == "warrior":
        input("Under the watchful eye of your mentor, you were attempting a new battle stance against some test dummies.")
        input("Exhausted, having sheathed your weapon away, you decided a break would renew your energy.")
    elif role == "mage":
        input("Spellbook sprawled uncomfortably close to the edge of your desk, arms raised, you were practicing a new spell.")
        input("You weren't having much luck with it. Deciding on a break, you slotted it within your robe as you opened your door.")
    elif role == "rogue":
        input("Opened locks were strewn about as you sat at the center of them crosslegged, them radiating outwards from you like a fractal.")
        input("As you finally picked the last one, marking the 50th, you decided a celebratory break was in order.")
    input("Shielding your eyes from the sunlight, you went for a walk towards the nearest bakery for a fresh loaf of bread.")
    input("Seeing a commotion around a fallen cart, and people already crowding it, you ended up taking a shortcut by ducking along a dark alley.")
    input("That's when it happened.")
    input("Moving sluggishly from exhaustion, reflexes slowed despite yourself, you ended up kidnapped.")
    input("By amateurs, too. As you pat yourself down, you find your stuff only a few meters away.")
    input("Behind bars, yes, but only a few meters. If- no, WHEN you get out, you could get your stuff back.")
#beginning choice
def beginningchoice():
    input("The door doesn't seem too sturdy. The lock also appears to be relatively weak...")
    input("You could try:")
    if role == "warrior":
        input("Bashing the door down - 'bash'")
    elif role == "mage":
        input ("Using magic to grab your tome - 'cast' (This will use up one of your three spells)")
    elif role == "rogue":
        input("Lockpicking the door - 'lock'")
    input("Calling out for a guard to trick - 'call'")
    a1 = input("What do you want to do? Enter: ")
    return a1

beginning()
nexta1 = beginningchoice()
if nexta1 == "bash":
    input("You attempt to bash the door down! Strength check!")
    check = rollSTR()
    if check >= 6:
        input("You passed the check! The door's hinges creak loudly as the rotting wood crashes down.")
    if check < 6:
        input("you failed the check! rip")

    
"""answer1 = input("testcheck1: enter yes no or maybe: ")
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
    a1 = 3"""

