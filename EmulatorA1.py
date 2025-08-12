from Dice import Stats
from Dice import die

class A1:
    a1bashfail = False
    a1lockfail = False
    a1callfail = False
    nexta1 = ""
    check = 0
    officala1 = ""
    def __init__(self, char_stats, debugMode, role):
        self.char_stats = char_stats
        self.debugMode = debugMode
        self.role = role
    
    #beginning choice
    def beginningchoice(self):
        input("The door doesn't seem too sturdy. The lock also appears to be relatively weak...")
        input("You could try:")
        if self.role == "warrior" and self.a1bashfail == False:
            print("Bashing the door down - 'bash'")
        elif self.role == "mage":
            print("\nUsing magic to break out - 'cast' (This will use up one of your three spells)")
        elif self.role == "rogue" and self.a1lockfail == False:
            print("Lockpicking the door - 'lock'")
        if self.a1callfail == False:
            print("Calling out for a guard to trick - 'call'")
        if self.role == "warrior" and self.a1bashfail == True and self.a1callfail == True:
            input("You've already tried bashing the door, and tricking the guard didn't work.")
            input("You slump down in your cell, awaiting rescue.")
            input("GAME OVER! Try again!")
            exit()
        if self.role == "rogue" and self.a1lockfail == True and self.a1callfail == True:
            input("You've already tried lockpicking the door, and tricking the guard didn't work.")
            input("You slump down in your cell, awaiting rescue.")
            input("GAME OVER! Try again!")
            exit()
        self.nexta1 = input("\nWhat do you want to do? Enter: ")
        return self.nexta1
    def beginningchoiceif(self):
        #warrior
        if self.nexta1 == "bash" and self.a1bashfail == False:
            input("You attempt to bash the door down! Strength check!")
            check = die.rollSTR(self.char_stats)
            if check >= 6:
                input("You passed the check! The door's hinges creak loudly as the rotting wood crashes down.")
                input("You confidently step outside, resoundly stepping on the shards of the door.")
                return "abash"
            elif check < 6:
                input("You failed the check! Try something else!")
                self.a1bashfail = True
                self.nexta1 = self.beginningchoice()
                self.officala1 = self.beginningchoiceif() 
        elif self.nexta1 == "bash" and self.a1bashfail == True:
            print("You already failed that option! Try a different one.") 
            self.nexta1 = self.beginningchoice()
            self.officala1 = self.beginningchoiceif()
                
        #mage
        elif self.nexta1 == "cast": #add description for spells
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
                self.nexta1 == self.beginningchoice()
                self.officala1 = self.beginningchoiceif()

            elif spell_choice == "3" or spell_choice == "teleport spark" and "Teleport Spark" not in used_spells:
                used_spells.append("Teleport Spark")
                input("You teleport through the bars and appear on the other side of the door!")
                return "ateleport"

            else:
                print("Invalid choice or you already used a spell.")
                input("Try again!")
                self.nexta1 == self.beginningchoice()
                self.officala1 = self.beginningchoiceif()
        #rogue
        elif self.nexta1 == "lock" and self.a1lockfail == False:
            input("You take out your hair pin, letting your hair down for a bit.")
            input("You crouch, checking if there's any guards watching you.")
            input("All clear.")
            input("You attempt to pick the lock...")
            print("Dexterity check!!!")
            check = die.rollDEX(self.char_stats)
            if check >= 7:
                input("Success! The lock clicks open. You silently slip out of your cell.")
                return "alock"
            elif check < 7:
                input("As you attempt to push it in, you push too far in the wrong direction as you hear the wrong click.")
                input("You retract the pin, now broken in two.")
                input("You failed the check! Try something else!")
                self.a1lockfail = True
                self.nexta1 == self.beginningchoice()
                self.officala1 = self.beginningchoiceif()
        elif self.nexta1 == "lock" and self.a1lockfail == True:
            print("You already failed that option! Try a different one.") 
            self.nexta1 = self.beginningchoice()
            self.officala1 = self.beginningchoiceif()

        #general - call
        elif self.nexta1 == "call" and self.a1callfail == False:
            print("You cry out, pretending to be scared.")
            input("Footsteps approach quickly...")
            input("A hulking guard looms over you, but any intimidation factor is lost alongside the crumbs falling from his face, as he takes another bite into his sandwich.")
            input("'Hey, damsel.'")
            input("(What does he mean by THAT?)")
            input("Well, anyway.")
            input("Roll to attempt to trick the guard! Charisma check!")
            check = die.rollCHA(self.char_stats)
            if check >= 6:
                input("You passed the check! You're pretty sure he thinks you're 'defenseless' as a 'damsel in distress'.")
                input("You lean into the act. 'Oh no, I don't know what to do anymore! The wound on my leg might get infected, if only I could see a doctor!'")
                input("The guard rolls his eyes. 'What, do you want someone to look at it or something?")
                print("It's not like you're going to die before the hero gets here.'")
                input("(So they're using you as bait, huh...) 'I'm not sure I can make it!'")
                input("(For dramatic effect, as you sit on the cold murky ground, you clutch your leg to your chest.)")
                input("The guard sighs. 'Damn damsel already making my life difficult...' He mutters to himself.")
                input("He starts getting his keys out for the door. As the key slots in, the door swings open as you lunge for him!")
                input("'Wh- you little-!' he yells in the struggle, as you press your boot against his head as you grasp for the keys.")
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
                self.a1callfail = True
                self.nexta1 = self.beginningchoice()
                self.officala1 = self.beginningchoiceif()
        elif self.nexta1 == "call" and self.a1callfail == True:
            print("You already failed that option! Try a different one.") 
            self.nexta1 = self.beginningchoice()
            self.officala1 = self.beginningchoiceif()
        else:
            input("Invalid option! Try again.")
            self.nexta1 = self.beginningchoice()
            self.officala1 = self.beginningchoiceif()



        