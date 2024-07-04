class weapon:
  def __init__(self, name: str, type: str, damage: int) -> None:
    self.name = name
    self.type = type
    self.damage = damage

#LIST OF WEAPONS
Fist = weapon(name="Fist", type="Fist", damage=1)
Wooden_Sword = weapon(name="Wooden Sword", type="1hSword", damage=2)
Iron_Sword = weapon(name="Iron Sword", type="1hSword", damage=3)
Wooden_Bow = weapon(name="Wooden Bow", type="Bow", damage=2)
Iron_Bow = weapon(name="Iron Bow", type="Bow", damage=3)
Sword_of_The_Ruler = weapon(name="Ruler", type="1hSword", damage=10)
Defender = weapon(name="Defender", type="2hSword", damage=-5)
