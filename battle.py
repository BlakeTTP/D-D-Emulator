import random
from Dice import Stats
from Dice import die
from EmulatorA1 import A1
from EmulatorB1 import B1
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
    elif role == "rogue"
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


    
