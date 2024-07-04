# ------------ imports ------------
import os

# ------------ setup ------------
os.system("")


# ------------ class setup ------------
# ------------ OLD SETUP 25 length of HEALTHBAR ----------
class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier1: str = "<" # HP=0
    barrier2: str = ">" # HP=MAX
    colors: dict = {"red": "\033[1;31m",
                    "purple": "\33[95m",
                    "blue": "\33[34m",
                    "blue2": "\33[36m",
                    "blue3": "\33[96m",
                    "darkcyan": '\033[36m',#DARKER BLUE
                    "green": "\033[92m",
                    "green2": "\033[32m",#DARKER GREEN
                    "brown": "\33[33m",
                    "yellow": "\33[93m",
                    "grey": "\33[37m",
                    "cyan": '\033[96m',
                    "bold": '\033[1m',#APPEARS DEFAULT
                    "underline": '\033[4m',#APPEARS DEFAULT
                    "default": "\033[0m"
                   }

    def __init__(self,
                 entity,
                 length: int = 25, #LENGTH HEALTHBAR
                 is_colored: bool = True,
                 color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health
        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]

    #UPDATE means The Remaining Bar Value matches the Draw.
    def update(self) -> None:
        self.current_value = self.entity.health
        
    #DRAW means number of Turn(s) the Battle happens.
    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        health_percentage = (self.current_value / self.max_value) * 100

    # Color logic of % on line 51. INDENTATION SENSITIVE
        if health_percentage <= 20:
            self.color = self.colors["red"]
        elif health_percentage <= 50:
            self.color = self.colors["yellow"]
        else:
            self.color = self.colors["green2"]

    #CALL THE HEALTHBAR    
        print(f"{self.entity.name}'s Health: {self.entity.health}/{self.entity.health_max}")
        print(f"{self.barrier1}" #HP = 0
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier2}") #HP = MAX