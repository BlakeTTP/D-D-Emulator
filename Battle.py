class Player:
  def __init__(self,role):
    self.role = role
    self.skills= []
    if role == "warrior":
      self.name = "Warrior of Light"
      self.stamina= 150
      self.attack = 15
      self.defence= 10
    elif role == "mage":
      self.name = "Mage of Flames"
      self.stamina = 120
      self.attack = 12
      self.defence = 8
    elif role == "rogue":
      self.name= "Rogue Of Shadow"
      self.stamina= 100
      self.attack= 10
      self.defence= 6

class Enemy :
  def __init__(self):
    self.name= "Dragon"
    self.stamina= 110
    self.attack= 9
    self.defence = 4


def battle(player,enemy):
   #enemy stamina
    damage_to_enemy = player.attack - enemy.defence
    if damage_to_enemy<0:
      damage_to_enemy =0 
    enemy.stamina -= damage_to_enemy 
    print(f"{player.name} attacks {enemy.name} for {damage_to_enemy} damage!")
    print(f"{enemy.name} now has {enemy.stamina}stamina left")

  #player stamina
    damage_to_player = enemy.attack - player.defence
    if damage_to_player<0:
      damage_to_player =0 
    player.stamina -= damage_to_player 
    print(f"{enemy.name} attacks {player.name} for {damage_to_player} damage!")
    print(f"{player.name} now has {player.stamina}stamina left")

    
    
    




    
