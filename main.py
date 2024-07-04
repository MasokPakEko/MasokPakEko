import random


def roll():
  min_value = 1  #LEAST VALUE FROM A ROLL
  max_value = 6  #MOST VALUE FROM A ROLL
  #RANDINT MEANS INTEGER in RANDOM
  roll = random.randint(min_value, max_value)  #ROLL

  return roll  #CHANGE TURN


while True:  #INDENT IS SIMILAR TO MPORT, DEF, PRINT
  players = input("Enter The Number of Player(s) [2-4]: ")  #PLAYERS
  if players.isdigit():  #TELLS IF INPUT IS A DIGIT
    players = int(players)  #CONVERT STRING - INTEGER
    if 2 <= players <= 4:
      break  #EXIT TO WHILE TRUE, THUS REPEAT INPUT
    else:
      #LIMIT INPUT TO INTEGER BETWEEN 2-4
      print("MUST BE 2 - 4 PLAYERS, PLEASE!")
  else:
    #LIMIT IF INPUT IS FALSE (OTHER THAN INTEGER)
    print("INVALID INPUT!")

max_score = 30  #MAX SCORE

#PLAYERS' SCORE
#HOW TO READ IT > STORE A LIST STARTING WITH 0 FOR NUMBER OF PLAYERS
player_scores = [0 for _ in range(players)]

#print(players_scores) #CHECK THE LIST FOR PLAYERS

#AS LONG AS ANY PLAYER"S SCORE IS LESS THAN MAX SCORE, THE GAME IS ON.
while max(player_scores) < max_score:

  for player_idx in range(players):
    print("\nPLAYER NUMBER", player_idx + 1, "TURN HAS STARTED!")
    print("Your Total Score is:", player_scores[player_idx], "\n")
    current_score = 0  #INITIAL SCORE

    while True:
      should_roll = input("Would you like to roll (y)? ")
      #LOWERCASE "y" so that if instead the input is "Y", the player can roll still.
      if should_roll.lower() != "y":
        break

      value = roll()
      if value == 1:
        print("\nYOU ROLLED A 1! TURN DONE!\n")
        current_score = 0
        break
      else:
        current_score += value
        print("\nYOUR ROLLED A", value, "\n")

      print("Your Score is:", current_score)

    player_scores[player_idx] += current_score
    print("\nYOUR TOTAL SCORE IS:", player_scores[player_idx], "\n")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player Number", winning_idx + 1, "is the winner with a score of:",
      max_score)
