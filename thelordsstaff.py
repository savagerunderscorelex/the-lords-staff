import random
class Player():
    damage = 10
    health = 16
    money = 100
    weapon = "Fists"

def choose():
    option = input("What do you want to do? (1: Scour/ 2: Search for the Lord's Staff in the Maze/3: Go to Shop/4: Check Your Stats)")
    if option == "1":
        winnings = random.randrange(1,120)
        print("You got " + str(winnings) + " moneys!")
        Player.money += winnings
    elif option == "4":
        print(f"Your money: {Player.money}")
        print(f"Your health: {Player.health}")
        print(f"Your current damage: {Player.damage}")
        print(f"Your current weapon: {Player.weapon}")
    choose()


print("Welcome to The Lord's Staff! Enter 1 to start the game.")
enter = input("Enter the Game:")
if enter == "1":
    print("You spawn in a fantasy city, with witches in crooked hats speeding on their brooms over you, and stone trolls hobbling past you. "
    "You don’t know who you are, where you came from, or what made you come here. " 
    "But you have this overwhelming feeling of heading on a journey to find something. A special something. The Lord’s Staff.")

choose()

input_weaponshop = 1

if input_weaponshop == "Sword":
    weapon = "Sword"
    damage = 20


    