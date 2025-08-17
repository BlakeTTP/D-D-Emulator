import random

class Player:
    def __init__(self, role):
        self.role = role
        self.skills = []
        if role == "warrior":
            self.name = "Warrior of Light"
            self.stamina = 150
            self.attack = 15
            self.defence = 10
        elif role == "mage":
            self.name = "Mage of Flames"
            self.stamina = 120
            self.attack = 12
            self.defence = 8
        elif role == "rogue":
            self.name = "Rogue Of Shadow"
            self.stamina = 100
            self.attack = 10
            self.defence = 6

        self.max_stamina = self.stamina
        self.is_defending = False
        self.is_invisible = False
        self.next_turn_bonus = 1  # for rogue sneak damage
        self.inventory = {"potion": 2}  # 2 healing potions


class Enemy:
    def __init__(self, name, stamina, attack, defence):
        self.name = name
        self.stamina = stamina
        self.attack = attack
        self.defence = defence
        self.is_defending = False
        self.dazed = False


def battle(player, enemies):
    turn = 1
    while player.stamina > 0 and any(e.stamina > 0 for e in enemies):
        print(f"\n--- Turn {turn} ---")
        print(f"{player.name}: {player.stamina} HP")
        for i, e in enumerate(enemies, start=1):
            if e.stamina > 0:
                status = f"{e.name}: {e.stamina} HP"
                status += " (Defending)" if e.is_defending else " (Not defending)"
                if e.dazed:
                    status += " (Dazed)"
                print(f"Enemy {i} - {status}")

        # reset defending each turn
        player.is_defending = False

        # Player options
        choice = input("\nOptions:\n- attack\n- defend\n- item\n- skill\nType your choice: ").strip().lower()

        if choice == "defend":
            player.is_defending = True
            print(f"{player.name} is defending and will take half damage this turn!")

        elif choice == "attack":
            target_index = int(input("Attack which enemy? (number): ")) - 1
            if 0 <= target_index < len(enemies) and enemies[target_index].stamina > 0:
                target = enemies[target_index]
                damage = max(0, player.attack * player.next_turn_bonus - target.defence)
                if target.is_defending:
                    damage //= 2
                target.stamina -= damage
                print(f"{player.name} attacks {target.name} for {damage} damage!")
                player.next_turn_bonus = 1  # reset rogue sneak bonus

        elif choice == "item":
            if player.inventory["potion"] > 0:
                heal = 10
                player.stamina = min(player.max_stamina, player.stamina + heal)
                player.inventory["potion"] -= 1
                print(f"You used a potion and healed {heal} HP! ({player.inventory['potion']} left)")
            else:
                print("No potions left!")

        elif choice == "skill":
            if player.role == "rogue":
                player.is_invisible = True
                player.next_turn_bonus = 2
                print(f"{player.name} vanishes in shadows (next attack 2x damage, cannot be hit this turn).")
            elif player.role == "mage":
                target_index = int(input("Cast spell on which enemy? (number): ")) - 1
                if 0 <= target_index < len(enemies) and enemies[target_index].stamina > 0:
                    damage = random.randint(10, 25)
                    enemies[target_index].stamina -= damage
                    print(f"{player.name} casts a spell on {enemies[target_index].name} for {damage} damage!")
            elif player.role == "warrior":
                target_index = int(input("Bash which enemy? (number): ")) - 1
                if 0 <= target_index < len(enemies) and enemies[target_index].stamina > 0:
                    damage = random.randint(5, 10)
                    enemies[target_index].stamina -= damage
                    # chance to daze
                    if random.random() < 0.3:
                        enemies[target_index].dazed = True
                        print(f"{player.name} bashes {enemies[target_index].name} for {damage} damage and dazes them!")
                    else:
                        print(f"{player.name} bashes {enemies[target_index].name} for {damage} damage!")

        # Enemies' turn
        for e in enemies:
            if e.stamina > 0 and not e.dazed:
                if not player.is_invisible:
                    dmg = max(0, e.attack - player.defence)
                    if player.is_defending:
                        dmg //= 2
                    player.stamina -= dmg
                    print(f"{e.name} attacks {player.name} for {dmg} damage!")
                else:
                    print(f"{e.name} tries to attack, but {player.name} is invisible!")
            e.is_defending = random.choice([True, False])  # enemies sometimes defend
            e.dazed = False  # reset daze after skipping one turn

        # End turn
        player.is_invisible = False
        turn += 1

    # Battle result
    if player.stamina <= 0:
        print("\nYou were defeated...")
    else:
        print("\nAll enemies defeated! You win!")

    




    
    
    




    
