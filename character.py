from weapon import Wooden_Bow #HERO EQUIP HERE
from health_barold import HealthBar

class Character:
  def __init__(self, name: str, health: int) -> None:
    self.name = name
    self.health = health
    self.health_max = health
    self.weapon = Wooden_Bow #HERO EQUIP HERE
    
  def attack(self, target) -> None:
    target.health -= self.weapon.damage
    target.health = max(target.health, 0)
    target.health_bar.update()
    
    #ADD TEXT TO DAMAGE
    print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}!!") 
    
#HERO
class Hero(Character): #HERO EQUIPS IRON SWORD BY DEFAULT
  def __init__(self, name: str, health: int) -> None:
    #INHERIT THE CLASS CHARACTER ATTRIBUTES
    super().__init__(name=name, health=health)
    self.default_weapon = self.weapon
    self.health_bar = HealthBar(self, color='green2')
    
  def equip(self,weapon) -> None: #define HERO EQUIP
    self.weapon = weapon
    print(f"{self.name} equipped a(n) {self.weapon.name}!")
    
  def drop(self) -> None:
    print(f"{self.name} dropped the {self.weapon.name}!")
    self.weapon = self.default_weapon
    
#ENEMY   
class Enemy(Character): #ENEMY EQUIPS WEAPON
  def __init__(self, name: str, health: int, weapon,) -> None: #ENEMY WEARS WEAPON
    super().__init__(name=name, health=health)
    self.weapon = weapon
    self.health_bar = HealthBar(self, color='green2')