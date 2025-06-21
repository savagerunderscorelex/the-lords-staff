import random
"""
TODO: 
Add function to select name
Finish inventory select function
begin on maze code, figure out monsters, directions, etc. 
Finish adding comments as well

"""

# Initializing variables, Player class, Weapon Class + instances, and functions for gameplay
# Standalone variables
shop_choice = 0

#Classes
class Weapon():
    def __init__(self, damage, name, cost):
        self.damage = damage
        self.name = name
        self.cost = cost
    def __str__(self):
        return f"{self.damage}, {self.name}, {self.cost}"
    
class Player():
    health = 100 # Player's HP, doesn't increase, but can be healed by buying potions
    money = 50 # Base money, can be increased through "Scouring"
    health_potions = 0 # Health Potions that can be used to recover a player's health
    player_weapon = Weapon(10, "Fists", 0) # Starter weapon + base damage, decided to have both in one variable
    bag = [] # Initializing bag, so that players can purchase multiple weapons

bag = Player.bag
# Tests
Player.bag.append("Fists")
print(*Player.bag)
#------------------------------------ 

# Weapons and their stats: Damage, Name, and shop Cost
stick = Weapon(15, "Stick", 300)
wooden_sword = Weapon(20, "Wooden Sword", 500)
bow = Weapon(30, "Bow", 700)
metal_sword = Weapon(40, "Metal Sword", 1000)
dragonblade = Weapon(200, "Dragonblade", 7000)
# ------------------------------------------------

def add_weapon(bag, shop_choice):
    bag.append(shop_choice)
    print(f"You just bought {shop_choice}!")
    
print(Player.player_weapon)
def maze():
    x = 1
    """
    This might not stay a function, it's just a placeholder for the options. Still planning out how the maze will work.
    """
def purchasing(): # Function for buying things at the shop
    print(" ")
    print(f"Wares: \nStick ({stick.cost} coins)\nWooden Sword ({wooden_sword.cost} coins)\nBow (700 coins)\nMetal Sword ({metal_sword.cost} coins)\nDragonblade ({dragonblade.cost} coins), ")
    while 1 == 1: # Loop of buying things in shop
        shop_choice = input("What would you like to buy?: ")
        if shop_choice == "Nothing":
            print("Have a nice day!")
            break # Leaves the shop
        elif shop_choice == "Stick":
            if bag.count(shop_choice) > 0: # If the player already has this item in their bag, they're kicked out of the shop teehee
                print("You already have this item.")
                break
            else: 
                if Player.money >= stick.cost: 
                    confirmation = input("Are you sure?")
                    if confirmation == "Yes":
                        add_weapon(bag, shop_choice)
                        Player.money -= stick.cost
                        Player.player_weapon = stick
                        print("You just bought the Stick (15 damage)")
                        print("You've equipped the Stick.")
                        purchasing()
                    elif confirmation == "No":
                        print("\"Look around, then! Maybe you'll find something else you like,\" the boy says.")
                        continue
                else:
                    print("You don't have enough money.") # Gets kicked out since you don't have money
                    break
        elif shop_choice == "Wooden Sword":
             if Player.money >= wooden_sword.cost:
                confirmation = input("Are you sure?")
                if confirmation == "Yes":
                    Player.money -= wooden_sword.cost
                    Player.player_weapon = wooden_sword
                    print("You just bought the Wooden Sword (20 damage)")
                    break
                elif confirmation == "No":
                    print("Look around, then! Maybe you'll find something else you like.")
                    continue
                else:
                    print("You don't have enough money.")
        elif shop_choice == "Bow":
             if Player.money >= bow.cost:
                confirmation = input("Are you sure?")
                if confirmation == "Yes":
                    Player.money -= bow.cost
                    Player.player_weapon = bow
                    print("You just bought the Wooden Sword (20 damage)")
                    break
                elif confirmation == "No":
                    print("Look around, then! Maybe you'll find something else you like.")
                    continue
                else:
                    print("You don't have enough money.")

                    
def choose(): # Player chooses what they want to do (4 options)
    option = input("What do you want to do? (1: Scour/ 2: Search for the Lord's Staff in the Maze/3: Go to Shop/4: Check Your Stats/ 5: Check Your Inventory)")
    if option == "1": # "Scouring"
        winnings = random.randrange(1,120)
        print("You got " + str(winnings) + " moneys!")
        Player.money += winnings
        choose()
    elif option == "4": # Shows Player their Stats
        print(f"Your money: {Player.money}")
        print(f"Your health: {Player.health}")
        print(f"Your current damage: {Player.player_weapon.damage}")
        print(f"Your current weapon: {Player.player_weapon.name}")
        print(f"Your inventory: {Player.bag}")
    elif option == "2": # Goes to the "main game"
        maze()
    elif option == "3": # Shop to buy potions and better weapons
        print("You enter a stout shop. Potions fill the shelves on both sides of the cramped shop. A small boy sits at the cashier desk, legs swinging back and forth.")
        print("He seems too young to own a shop like this, so you assume he's the owner's son. The boy is likely not older than 10, but he has a demeanor that makes him look so much older.")
        print(" ")
        if Player.player_weapon.name == "Fists": # Different descriptions based on current weapon
            print("You look around, taking a closer look at the wares. To the left of you, lies a simple Stick.")
            print("It looks like it will add a bit to your damage, having 15 damage instead of 10.")
            print("Behind the boy, lies 3 more weapons, one is slightly stronger weapon: a Wooden Sword.")
            print("This has twice the damage as just your hands (20 damage)")
            print("Next to the Wooden Sword lies a basic Bow, with about 30 damage.")
            print("\nA Metal Sword, gleaming in the afternoon sun, catches your attention. This weapon has 40 damage.")
            print("You notice the boy lifting another large sword from under the desk. Wide-eyed, you look over the weapon.")
            print("\"The Dragonblade,\" the boy said in a wispy voice. \n")
            print("Jewels adorn the sword, shining bright like sunlight on the ocean waves. The tip is sharp, enough to pierce anything it touches. This glorious weapon has 200 damage. ")
            purchasing()
    elif option == "5":
        print("You look inside the bag that you've just noticed was on your back. Take a look inside.")
        print(f"Your weapons: {Player.bag}")
        equip = input("Do you want to equip a certain weapon? (Yes/No): ")
        equip = equip.lower()
        if equip == "yes":
            select = input(f"Select your weapon to equip: {Player.bag}")
            if bag.count(select) == 1 and Player.player_weapon.name != select and select == "Stick":
                Player.player_weapon = stick
        print("That is not a valid option.")
        choose()

# The game begins!!

while 2 + 2 == 4: # Introduction code is in a while loop so that the player doesn't have to reset the program to reenter 1 to start the game
    print("Welcome to The Lord's Staff! Enter 1 to start the game.") # Ready player one reference?????
    enter = input("Enter the Game:")
    if enter == "1":
        print("You spawn in a fantasy city, with witches in crooked hats speeding on their brooms over you, and stone trolls hobbling past you. "
        "You don’t know who you are, where you came from, or what made you come here. " 
        "But you have this overwhelming feeling of heading on a journey to find something. A special something. The Lord’s Staff.")
        break
    else:
        print("Please enter 1 to start the game.")
        continue
choose()



    