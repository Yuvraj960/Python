# Snake Water Gun Game
"""
1 for Snake
-1 for Water
0 for Gun

"""
import random
computer_choice = random.choice(["s", "w", "g"])
# computer = -1
your_choice = input("Enter your choice (s, w, g): ")
gameDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = gameDict[your_choice]
computer = gameDict[computer_choice]

print(f"You Chose {reverseDict[you]} and Computer Chose {reverseDict[computer]}")

if computer == you:
    print("It's a Draw")
elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
    print("You lose")
elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
    print("You win")
else:
    print("Something went wrong")