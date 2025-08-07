import random

#random.randint(1, 6)
#random.randint(1, 20)

#beginning part/decription of skills
input("WELCOME, ADVENTURER, TO OUR RELEAM!!!\n (Whenever you don't need to enter anything in, then just press ENTER to continue.)")
input("Now, let's begin your journey.\n ")
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
print("\nStrength(STR): Determines how physically strong you are.\nDexterity(DEX): Determines your flexibility, dodging, and sneaking ability.\nConstitution(CON): Determines how much your body can physically take, mainly health.")
#input("Dexterity(DEX): Determines your flexibility, dodging, and sneaking ability.")
#input("Constitution(CON): Determines how much your body can physically take, mainly health.")
print("Wisdom(WIS): Determines how wise you are/how much conventional wisdom you have, or 'common sense'.\nIntelligence(INT): Determines how much you know, or 'book knowledge'.\nCharisma(CHA): Determines your social skills.")
#input("Intelligence(INT): Determines how much you know, or 'book knowledge'.")
#input("Charisma(CHA): Determines your social skills.")
input("\nEverytime you make a decision, a die is rolled to see how effective it is.\nThese stats are modifiers that make you better or worse at certain skills.")
#input("These stats are modifiers that make you better or worse at certain skills.")
input("You possess a unique set of trait values to distribute among your skills.\nUse each value wisely, once assigned, it cannot be used again [-1, 0, 1, 1, 2, and 2.]")
#input("That means you can use each number once, for each stat.")
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

a1bashfail = False
a1lockfail = False
a1callfail = False
check = 0

#beginning choice
def beginningchoice():
    input("The door doesn't seem too sturdy. The lock also appears to be relatively weak...")
    input("You could try:")
    if role == "warrior" and a1bashfail == False:
        print("Bashing the door down - 'bash'")
    elif role == "mage":
         print("\nUsing magic to grab your tome - 'cast' (This will use up one of your three spells)")
    elif role == "rogue" and a1lockfail == False:
        print("Lockpicking the door - 'lock'")
    if a1callfail == False:
        print("Calling out for a guard to trick - 'call'")
    if role == "warrior" and a1bashfail == True and a1callfail == True:
        input("You've already tried bashing the door, and tricking the guard didn't work.")
        input("You slump down in your cell, awaiting rescue.")
        input("GAME OVER! Try again!")
        exit()
    if role == "rogue" and a1lockfail == True and a1callfail == True:
        input("You've already tried lockpicking the door, and tricking the guard didn't work.")
        input("You slump down in your cell, awaiting rescue.")
        input("GAME OVER! Try again!")
        exit()
    a1 = input("\nWhat do you want to do? Enter: ")
    return a1


def beginningchoiceif():
    #warrior
    global nexta1
    global a1bashfail
    global a1lockfail
    global a1callfail
    global check

    if nexta1 == "bash" and a1bashfail == False:
        input("You attempt to bash the door down! Strength check!")
        check = rollSTR()
        if check >= 6:
            input("You passed the check! The door's hinges creak loudly as the rotting wood crashes down.")
            input("You confidently step outside, resoundly stepping on the shards of the door.")
            return "abash"
        elif check < 6:
            input("You failed the check! Try something else!")
            a1bashfail = True
            nexta1 = beginningchoice()
            beginningchoiceif() 
    if nexta1 == "bash" and a1bashfail == True:
        print("You already failed that option! Try a different one.") 
        nexta1 = beginningchoice()
        beginningchoiceif()
              
    #mage
    elif nexta1 == "cast":
        spells = ["Firebolt", "Frost Shield", "Teleport Spark"]
        used_spells = []
        print("Choose a spell to cast:")
        for i, spell in enumerate(spells):
            print(f"{i+1}. {spell}")

        spell_choice = input("Enter the spell number (1-3): ")

        if spell_choice == "1" or spell_choice == "firebolt" and "Firebolt" not in used_spells:
            used_spells.append("Firebolt")
            input("You cast Firebolt! The door bursts into flames and collapses.")
            input("As the flames flicker, you carefully step over the decimated door.")
            return "afirebolt"

        elif spell_choice == "2" or spell_choice == "frost shield" and "Frost Shield" not in used_spells:
            used_spells.append("Frost Shield")
            print("You cast Frost Shield! A magical barrier surrounds you.")
            input("...")
            input("Since you're trying to get out and nothing's trying to get in, there's nothing it can really do.")
            input("Try again!")
            #print(used_spells) Btw the used spells doesn't work for some weird reason - to do later
            nexta1 == beginningchoice()
            beginningchoiceif()

        elif spell_choice == "3" or spell_choice == "teleport spark" and "Teleport Spark" not in used_spells:
            used_spells.append("Teleport Spark")
            input("You teleport through the crack in the wall and appear on the other side of the door!")
            return "ateleport"

        else:
            print("Invalid choice or you already used a spell.")
            input("Try again!")
            nexta1 == beginningchoice()
            beginningchoiceif()
    #rogue
    elif nexta1 == "lock" and a1lockfail == False:
        input("You take out your hair pin, letting your hair down for a bit.")
        input("You crouch, checking if there's any guards watching you.")
        input("All clear.")
        input("You attempt to pick the lock...")
        print("Dexterity check!!!")
        check = rollDEX()
        if check >= 7:
            input("Success! The lock clicks open. You silently slip out of your cell.")
            return "alock"
        elif check < 7:
            input("As you attempt to push it in, you push too far in the wrong direction as you hear the wrong click.")
            input("You retract the pin, now broken in two.")
            input("You failed the check! Try something else!")
            a1lockfail = True
            nexta1 == beginningchoice()
            beginningchoiceif()
    elif nexta1 == "lock" and a1lockfail == True:
        print("You already failed that option! Try a different one.") 
        nexta1 = beginningchoice()
        beginningchoiceif()

    #general - call
    elif nexta1 == "call" and a1callfail == False:
        print("You cry out, pretending to be scared.")
        input("Footsteps approach quickly...")
        input("A hulking guard looms over you, but any intimidation factor is lost alongside the crumbs falling from his face, as he takes another bite into his sandwich.")
        input("'Hey, damsel.'")
        input("(What does he mean by THAT?)")
        input("Well, anyway.")
        input("Roll to attempt to trick the guard! Charisma check!")
        check = rollCHA()
        if check >= 6:
            input("You passed the check! You're pretty sure he thinks you're 'defenseless' as a 'damsel in distress'.")
            input("You lean into the act. 'Oh no, I don't know what to do anymore! The wound on my leg might get infected, if only I could see a doctor!'")
            input("The guard rolls his eyes. 'What, do you want someone to look at it or something?")
            print("It's not like you're going to die before the hero gets here.'")
            input("(So they're using you as bait, huh...) 'I'm not sure I can make it!'")
            input("(For dramatic effect, as you sit on the cold murky ground, you clutch your leg to your chest.)")
            input("The guard sighs. 'Damn damsel already making my life difficult...' He mutters to himself.")
            input("He starts getting his keys out for the door. As the key slots in, the door swings open as you lunge for him!")
            input("'Wh- I thought you were injured!' he yells in the struggle, as you press your boot against his head as you grasp for the keys.")
            input("Got them!")
            input("As you kick the guard one final time, he falls unconcious as you brush yourself off. Man. You can't believe how easy that was.")
            input("The sandwich remains disgarded as you step out the cell.")
            return "acall"
        elif check < 6:
            input("You decide to act defenseless. 'Ow, my knee really hurts!'")
            input("He raises his eyebrows at you disbelievingly. 'Yeah, sure, sure.'")
            input("He leans slightly towards the cell. 'Cry about it.'")
            input("The guard turns around, and right as he's about to walk away, he stops.")
            input("'Don't call me unless there's something real.' He continues walking away, along with the keys.")
            input("You failed the check! Try something else.")
            a1callfail = True
            nexta1 = beginningchoice()
            beginningchoiceif() 
    elif nexta1 == "call" and a1callfail == True:
        print("You already failed that option! Try a different one.") 
        nexta1 = beginningchoice()
        beginningchoiceif()

#successful choices: afirebolt, abash
def b1choice():
    input("As the door breaking resounds through the empty air, you hear footsteps rapidly approaching.")
    print("guard comes etc etc (fill in rest later)")
    print("You could:")
    print("Fight them! - 'fight'")
    print("Try to run away - 'run'")
    print("Try to grab your stuff, and THEN run - 'grab'") #harder to pass check, but otherwise you don't get stuff as a variable later on
    if role == "mage":
        print("Cast a spell - 'cast'")
    b1 = input("\nWhat do you want to do? Enter: ")
    return b1
def b1choiceif():
    global check
    global nextb1


beginning()
nexta1 = beginningchoice()
officala1 = beginningchoiceif()
#successful choices: afirebolt, abash, acall, alock, ateleport
#first choice split off
#if officala1 == "afirebolt" or "abash":
#    nextb1 = b1choice()
#    officalb1 = b1choiceif()
#if officala1 = "acall"
#    nextb2 = b2choice()
#    officalb2 = b2choiceif()





