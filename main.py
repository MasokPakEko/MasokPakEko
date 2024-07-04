from character import Hero, Enemy
from weapon import Fist, Iron_Bow, Sword_of_The_Ruler #CHANGE ENEMY EQUIP HERE

#HERO and ENEMY ATTRIBUTES
hero = Hero(name="Zidan", health=200)
hero.equip(Sword_of_The_Ruler)

enemy = Enemy(name="Abimanyu", health=200, weapon=Fist) #CHANGE ENEMY EQUIP HERE

while hero.health > 0 and enemy.health > 0:
      #loop continues while both characters are alive
  hero.attack(enemy)
  enemy.attack(hero)

  hero.health_bar.draw()
  enemy.health_bar.draw()
  
  input()

print("GAME OVER")
