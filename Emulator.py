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
input("WELCOME, ADVENTURER, TO OUR REALM!!!\n (Whenever you don't need to enter anything in, then just press ENTER to continue.)")
inputDebugMode = input("Turn on debug mode? Enter True or False: ")
if inputDebugMode == "False":
    debugMode = False
elif inputDebugMode == "True":
    debugMode = True
if debugMode == True:
    inputAutoStatConfig = input("Put in stats automatically? Enter True or False: ")
    if inputAutoStatConfig == "True":
        autoStatConfig = True
input("Now, let's begin your journey.\n ")

def rolechoice():
    global role
    print("\nChoose your role: warrior, mage or rogue.")
    role = input("Enter your role: ")
    #based on the roles
    if role == "warrior" or role == "rogue" or role == "mage":
        print("Great Choice!!!")
    if role=="warrior":
        print("You are a fearless Warrior, clad in heavy armor, with shield and sword in skilled hands.") #", marching toward the Fortress"
        print("(+1 to Strength)")
    elif role=="mage":
        #print("You are a master Thief, who is quick, clever, and silent, with hands skilled in locks and a mind sharp as any blade.")
        print("You are a Mage, an apprentice learning the art of the magic that flows through your world, knowledge heavy as your tome.")
        print("(+1 to Intelligence)")
    elif role=="rogue":
        print("You are a Rogue, who is silent but deadly with a sharp dagger no matter where you stand, and always four steps ahead.")
        print("(+1 to Dexterity)")
    else:
        input("Invalid option! Try again.")
        role = rolechoice()
    return role

role = rolechoice()

#stat configuration
def introStatConfig():
    input("First, to begin your story, we need to configure your stats.")
    input("Whatever class you choose already added +1 to one of them, which stacks with whatever you choose as your array.")
    input("While you can choose otherwise, it's recommended to have your main stat you use for your class be high for class specific options.")
    input("There's six to configure.")
    print("\nStrength(STR): Determines how physically strong you are.\nDexterity(DEX): Determines your flexibility, dodging, and sneaking ability.\nConstitution(CON): Determines how much your body can physically take, mainly health.")
    print("Wisdom(WIS): Determines how wise you are/how much conventional wisdom you have, or 'common sense'.\nIntelligence(INT): Determines how much you know, or 'book knowledge'.\nCharisma(CHA): Determines your social skills.")
    input("\nEverytime you make a decision, a die is rolled to see how effective it is.\nThese stats are modifiers that make you better or worse at certain skills.")
    input("You possess a unique set of trait values to distribute among your skills.\nUse each value wisely, once assigned, it cannot be used again [-1, 0, 1, 1, 2, and 2.]")

char_stats = Stats()
if autoStatConfig == False:
    introStatConfig()
    char_stats.inputStats()
    
if autoStatConfig == True:
    char_stats.autoStats()

#class based addition to stats
    if role == "warrior":
        char_stats.STR = char_stats.STR+1
    elif role == "mage":
        char_stats.INT = char_stats.INT+1
    elif role == "rogue":
        char_stats.DEX = char_stats.DEX+1
#beginning
def beginning(): #change pacing, add more description to environment
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

choiceA1 = A1(char_stats, debugMode, role)

if debugMode == False:
    beginning()
nexta1 = choiceA1.beginningchoice()
officala1 = choiceA1.beginningchoiceif()
#successful choices: afirebolt, abash, acall, alock, ateleport
#first choice split off

if officala1 == "afirebolt" or officala1 == "abash":
    choiceB1 = B1(char_stats, debugMode, role, officala1, choiceA1.a1BashFail, choiceA1.a1LockFail, choiceA1.a1CallFail)
    nextb1 = choiceB1.b1choice()
    officalb1 = choiceB1.b1choiceif()
if officala1 == "acall":
    choiceB2 = B2(char_stats, debugMode, role, choiceA1.a1BashFail, choiceA1.a1LockFail, choiceA1.a1CallFail)
    nextb2 = choiceB1.b2choice()
    officalb2 = choiceB1.b2choiceif()
