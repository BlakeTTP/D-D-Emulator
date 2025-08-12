import random
from EmulatorA1 import A1
from Dice import Stats
from Dice import die
autoStatConfig = False

#beginning part/decription of skills
input("WELCOME, ADVENTURER, TO OUR REALM!!!\n (Whenever you don't need to enter anything in, then just press ENTER to continue.)")
inputDebugMode = input("Turn on debug mode? Enter True or False: ")
if inputDebugMode == "False":
    debugMode = False
if inputDebugMode == "True":
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

a1bashfail = False
a1lockfail = False
a1callfail = False
check = 0
phealth = char_stats.CON + 10
haveItems = False

#successful choices: afirebolt, abash
def b1choice():
    input("As the door breaking resounds through the empty air, you hear a pair of footsteps rapidly approaching.")
    input("Guards are coming! You quickly glance around your surroundings, looking for options.")
    input("Your stuff is but only a few meters away, but could take up precious seconds...")
    print("You could:")
    print("Grab your stuff and fight them! - 'fight'")
    print("Try to run away! - 'run'")
    print("Try to grab your stuff, and THEN run - 'grab'") #harder to pass check, but otherwise you don't get stuff as a variable later on
    if role == "mage":
        print("Cast a spell - 'cast'")
    b1 = input("\nWhat do you want to do? Enter: ")
    return b1

bfightHaveAdvantage = False
bfightHaveDisadvantage = False

def bfight():
    global phealth
def brun():
    global haveItems
    global check
    if haveItems == False:
        input("You take a longing look towards your stuff, but decide it's not worth the risk.")
        input("...It'd be pretty hard to go back for it later.")
        input("Either way, you decide to run for it!")
        input("Roll to evade the guards!")
        check = die.rollDEX(char_stats)
        if check > 5:
            input("You start running, and find a room off the main path.")
            input("Right as the guards round the corner,")
    if haveItems == True:
        input("You take a glance towards the connecting corridor, and grab your stuff!")

def b1choiceif():
    global check
    global nextb1
    global officalb1
    global haveItems
    if nextb1 == "fight":
        input("You quickly lunge for your stuff, and take inventory of it.")
        if role == "warrior":
            input("It's your trusty sword and shield!")
            input("You quickly wrap the sheath around your waist as you reveal your blade.")
            input("As you see the guards rapidly approaching, you slide your shield onto your arm, ready in battle stance.")
            bfight()
        elif role == "mage":
            input("It's your beloved tome!")
            input("As you snap it open with one hand, your handwriting, scrawling from page to page, is revealed.")
            input("As you see the guards rapidly approaching, you refresh yourself on your new spell, ready.")
            #learn thorny vines
            bfight()
        elif role == "rogue":
            input("It's your sharpened dagger and lockpicking tools!")
            if nexta1 == "call" and A1.a1lockfail == False:
                input("Thank goodness you didn't have to use that hair pin.")
                input("You'd be quite disappointed if it broke.")
            elif nexta1 == "lock":
                input("Thank goodness your hair pin worked!")
                input("You'd be quite disappointed if it broke.")
            elif a1lockfail == True:
                input("...It's sad you got them back only after your hair pin broke.")
                input("You quite liked it!")
                input("However, it did serve its use as a backup lockpick. Ah well.")
            input("Either way, you spin your dagger around, slotting perfectly in your hand as you crouch behind the wall.")
            input("You're ready.")
            bfight()
    elif nextb1 == "run":
        brun()
    elif nextb1 == "grab":
        haveItems = True
        brun()
    else:
        input("Invalid option. Try again!")
        nextb1 = b1choice()
        officalb1 = b1choiceif()

choiceA1 = A1(char_stats, debugMode, role)

if debugMode == False:
    introStatConfig()
    beginning()
nexta1 = choiceA1.beginningchoice()
officala1 = choiceA1.beginningchoiceif()
#successful choices: afirebolt, abash, acall, alock, ateleport
#first choice split off
if officala1 == "afirebolt" or officala1 == "abash":
    nextb1 = b1choice()
    officalb1 = b1choiceif()
#if officala1 = "acall"
#    nextb2 = b2choice()
#    officalb2 = b2choiceif()
