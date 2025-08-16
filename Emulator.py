import random
from Dice import Stats
from Dice import die
from EmulatorA1 import A1
from EmulatorB1 import B1
from EmulatorB2 import B2

"""
to-do:
-add turn-based fight mechanics
-rewrite a lot
-add spell descriptions
-add "you passed/failed the check!" to the end of description instead of beginning

"""



autoStatConfig = False

#beginning part/decription of skills
input("\033[1;34mWELCOME 🙏, ADVENTURER, TO OUR REALM!!!\033[0m\n (Whenever you don't need to enter anything in, then just press ENTER to continue.)")

while True:
     inputDebugMode = input("Turn on debug mode? \033[1mEnter\033[0m \033[32mTrue\033[0m or \033[31mFalse\033[0m: ")
     if inputDebugMode.lower() == "false":
         debugMode = False
         autoStatConfig = False 
         break
     elif inputDebugMode.lower() == "true":
         debugMode = True
         break
     else:
         print("Invalid input. Please Enter either TRUE or FALSE :")

while True:         
    if debugMode:
        inputAutoStatConfig = input("Put in stats automatically? \033[1mEnter\033[0m \033[32mTrue\033[0m or \033[31mFalse\033[0m: ")
        if inputAutoStatConfig.lower() == "true":
            autoStatConfig = True
            break
        elif inputAutoStatConfig.lower() == "false":
            autoStatConfig = False
            break
        else:
            print("Invalid input. Please Enter TRUE or False")
    else:
        break
input("\n\n\033[92mNow, let's begin your journey.\033[0m\n ")

def rolechoice():
    global role
    while True:
        print("\n\033[1mChoose your role:\033[0m \033[33mWarrior,\033[36m Mage \033[0mor \033[35mRogue.\033[0m")
        role = input("\033[1mEnter your role:\033[0m ").strip().lower()

        if role == "warrior":
            print("Great Choice!!!")
            print("You are a fearless Warrior🤺, clad in heavy armor 𐂫, with shield 🛡️ and sword 🗡️ in skilled hands.")
            print("(\033[32m+1 to Strength\033[0m)")
            break
        elif role == "mage":
            print("Great Choice!!!")
            print("You are a Mage, an apprentice learning the art of the magic that flows through your world, knowledge heavy as your tome.")
            print("(\033[32m+1 to Intelligence\033[0m)")
            break
        elif role == "rogue":
            print("Great Choice!!!")
            print("You are a Rogue, who is silent but deadly with a sharp dagger no matter where you stand, and always four steps ahead.")
            print("(\033[32m+1 to Dexterity\033[0m)")
            break
        else:
            print("\033[31mInvalid option! Try again.\033[0m")
    return role

role = rolechoice()

#stat configuration
def introStatConfig():
    input("\033[1mFirst, to begin your story, we need to configure your stats.\033[0m")
    input("Whatever class you choose already added \033[32m+1\033[0m to one of them, which stacks with whatever you choose as your array.")
    input("While you can choose otherwise, it's \033[36mrecommended\033[0m to have your main stat you use for your class be high for class specific options.")
    input("There's \033[1;33msix\033[0m to configure.")
    print("\n\033[33mStrength(STR)\033[0m: \033[36mDetermines how physically strong you are.\033[0m\n\033[33mDexterity(DEX)\033[0m: \033[36mDetermines your flexibility, dodging, and sneaking ability.\033[0m\n\033[33mConstitution(CON)\033[0m: \033[36mDetermines how much your body can physically take, mainly health.\033[0m")
    print("\033[33mWisdom(WIS)\033[0m: \033[36mDetermines how wise you are/how much conventional wisdom you have, or 'common sense'.\033[0m\n\033[33mIntelligence(INT)\033[0m: \033[36mDetermines how much you know, or 'book knowledge'.\033[0m\n\033[33mCharisma(CHA)\033[0m: \033[36mDetermines your social skills.\033[0m")
    input("\nEverytime you make a decision, a \033[1;33mdie\033[0m is rolled to see how effective it is.\nThese stats are modifiers that make you better or worse at certain skills.")
    input("You possess a unique set of trait values to distribute among your skills.\nUse each value wisely, once assigned, it cannot be used again \033[1;32m[-1, 0, 1, 1, 2, and 2.]\033[0m")

char_stats = Stats()
if autoStatConfig == False:
    introStatConfig()
    char_stats.inputStats()
    
if autoStatConfig == True:
    char_stats.autoStats()

#class based addition to stats
    if role == "Warrior":
        char_stats.STR = char_stats.STR+1
    elif role == "Mage":
        char_stats.INT = char_stats.INT+1
    elif role == "Rogue":
        char_stats.DEX = char_stats.DEX+1
#beginning
def beginning(): #change pacing, add more description to environment
    input("\033[34mYou find yourself lying on the ground, and the first thing you're aware of is the migraine blooming through your skull.\033[0m")
    input("\033[31mWhat, did someone hit y- oh.")
    input("Someone did.\033[0m") #beat moment
    input("\033[36mFirst things first.\033[0m") #beat moment
    input("You were in the village, training like usual.")
    if role == "Warrior":
        input("\033[32mUnder the watchful eye of your mentor, you were attempting a new battle stance against some test dummies.\033[0m")
        input("Exhausted, having sheathed your weapon away, you decided a break would renew your energy.")
    elif role == "Mage":
        input("\033[35mSpellbook sprawled uncomfortably close to the edge of your desk, arms raised, you were practicing a new spell.\033[0m")
        input("You weren't having much luck with it. Deciding on a break, you slotted it within your robe as you opened your door.")
    elif role == "Rogue":
        input("\033[90mOpened locks were strewn about as you sat at the center of them crosslegged, them radiating outwards from you like a fractal.\033[0m")
        input("As you finally picked the last one, marking the 50th, you decided a celebratory break was in order.")
    input("Shielding your eyes from the sunlight, you went for a walk towards the nearest bakery for a fresh loaf of bread.")
    input("Seeing a commotion around a fallen cart, and people already crowding it, you ended up taking a shortcut by ducking along a dark alley.")
    input("\033[36mThat's when it happened.\033[0m") #beat moment
    input("Moving sluggishly from exhaustion, reflexes slowed despite yourself, you ended up kidnapped.")
    input("\033[31mBy amateurs, too.\033[0m") #beat moment
    input("As you pat yourself down, you find your stuff only a few meters away.")
    input("Behind bars, yes, but only a few meters.")
    input("\033[36mIf- no, WHEN you get out, you could get your stuff back.\033[0m") #beat moment

choiceA1 = A1(char_stats, debugMode, role)

if debugMode == False:
    beginning()
nexta1 = choiceA1.beginningchoice()
officiala1 = choiceA1.beginningchoiceif()
#successful choices: afirebolt, abash, acall, alock, ateleport
#first choice split off

if officiala1 == "afirebolt" or officiala1 == "abash":
    choiceB1 = B1(char_stats, debugMode, role, officiala1, choiceA1.a1BashFail, choiceA1.a1LockFail, choiceA1.a1CallFail)
    nextb1 = choiceB1.b1choice()
    officialb1 = choiceB1.b1choiceif()
if officiala1 == "acall" or officiala1 == "alock" or officiala1 == "ateleport":
    choiceB2 = B2(char_stats, debugMode, role, officiala1, choiceA1.a1BashFail, choiceA1.a1LockFail, choiceA1.a1CallFail)
    nextb2 = choiceB2.b2choice()
    officialb2 = choiceB2.b2choiceif()



