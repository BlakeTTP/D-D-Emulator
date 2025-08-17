import random

class Player:
    def __init__(self, role):
        self.role = role.lower()
        self.skills = []
        if self.role == "warrior":
            self.name = "Warrior of Light"
            self.stamina = 150
            self.attack = 15
            self.defence = 10
        elif self.role == "mage":
            self.name = "Mage of Flames"
            self.stamina = 120
            self.attack = 12
            self.defence = 8
            self.spells = 3   # mage has limited spell casts
        elif self.role == "rogue":
            self.name = "Rogue of Shadows"
            self.stamina = 100
            self.attack = 10
            self.defence = 6

        # status trackers
        self.sneak_ready = False   # rogue double-damage next turn
        self.is_dazed = False      # player dazed (if enemy had effect, optional)

class Enemy:
    def __init__(self):
        self.name = "Dragon"
        self.stamina = 110
        self.attack = 9
        self.defence = 4
        self.is_dazed = False      # enemy can be dazed

def battle(player, enemy):
    turn = 1
    print(f"\n⚔️ Battle Start: {player.name} vs {enemy.name} ⚔️\n")

    while player.stamina > 0 and enemy.stamina > 0:
        print(f"\n--- Turn {turn} ---")

        # Player's turn
        if not player.is_dazed:  
            action = input(f"\nChoose your action ({player.role}): [attack / special] ").lower()

            if action == "attack":
                damage = max(0, player.attack - enemy.defence)
                if player.sneak_ready:   # Rogue sneak bonus
                    damage *= 2
                    print("💥 Sneak attack deals double damage!")
                    player.sneak_ready = False
                enemy.stamina -= damage
                print(f"{player.name} attacks {enemy.name} for {damage} damage!")

            elif action == "special":
                if player.role == "rogue":
                    print("🌀 You vanish into the shadows... (No damage taken this turn, double damage next turn)")
                    player.sneak_ready = True

                elif player.role == "mage":
                    if player.spells > 0:
                        spell_damage = random.randint(15, 25)
                        enemy.stamina -= spell_damage
                        player.spells -= 1
                        print(f"🔥 {player.name} casts Firebolt! It hits {enemy.name} for {spell_damage} damage!")
                    else:
                        print("❌ No spells left! You attack normally instead.")
                        damage = max(0, player.attack - enemy.defence)
                        enemy.stamina -= damage
                        print(f"{player.name} attacks {enemy.name} for {damage} damage!")

                elif player.role == "warrior":
                    damage = max(0, (player.attack // 2) - enemy.defence)
                    enemy.stamina -= damage
                    print(f"🛡️ {player.name} bashes {enemy.name} for {damage} damage!")
                    if random.random() < 0.3:  # 30% chance
                        enemy.is_dazed = True
                        print(f"💫 {enemy.name} is Dazed and will skip their next turn!")

            else:
                print("Invalid action! You miss your chance to attack.")

        else:
            print(f"{player.name} is dazed and skips this turn!")
            player.is_dazed = False  # recover next turn

        # Check if enemy is defeated
        if enemy.stamina <= 0:
            print(f"\n✅ {enemy.name} has fallen! {player.name} wins! ✅")
            break

        # Enemy's turn
        if not enemy.is_dazed:
            damage = max(0, enemy.attack - player.defence)
            if not player.sneak_ready:  # Rogue is invisible if sneak_ready
                player.stamina -= damage
                print(f"{enemy.name} attacks {player.name} for {damage} damage!")
            else:
                print(f"{enemy.name} swings blindly but misses the invisible Rogue!")
        else:
            print(f"{enemy.name} is dazed and skips their turn!")
            enemy.is_dazed = False  # recover

        # Check if player is defeated
        if player.stamina <= 0:
            print(f"\n❌ {player.name} has fallen! {enemy.name} wins! ❌")
            break

        # Status update
        print(f"{player.name} Stamina: {player.stamina} | {enemy.name} Stamina: {enemy.stamina}")
        turn += 1
