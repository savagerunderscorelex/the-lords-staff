import random
"""
TODO: 
Add function to select name
Finish inventory select function
begin on maze code, figure out monsters, directions, etc. 
Finish adding comments as well

CURRENT PROBLEMS: 
- 

"""

"""
UPDATES (For Devlogs and Commit messages because I keep forgetting to write them):
6/21 - More comments, made certain inputs output as lowercase so that users can enter inputs whether they are capitalized or not
started on equipping weapons selection "screen," fixed bugs in the purchasing function

6/22 (Nigeria Time) - Made print statements more "story-like", including making the no-money statement, confirmation statement (the question), and confirmation statement (the answer) more detailed :P,
made the print weapons statement a for loop instead, I also decided to separate some of the choose() function options into their own separate functions so that the code looks kinda better

6/25 (Nigeria Time) - Made a specific fists instance in case players want to equip the fists weapon, also coded lowercase and capital case options into the code for 
equipping a weapon by making the condition an or comparison instead of whatever I was trying to do before. Basic solution but whatever
also just realized I kinda wasted my time trying to format the player's answer, when I could've done 1 for Stick, 2 for Metal Sword, etc. (LIKE
I DID FOR THE CHOOSE() FUNCTION WHAT THE HELLLLLLLLLLLLLLLLLLLLLLLLL)

6/25 (late at night) / 6/26 (Nigeria time, it's like 6pm Eastern) finally changed the inputs to be based on numbers, updated costs for weapons
to make them harder to obtain, updated add_weapon() function based on the number inputs

"""

# Initializing variables, Player class, Weapon Class + instances, and functions for gameplay

#Classes
class Weapon():
    def __init__(self, damage, name, cost):
        self.damage = damage
        self.name = name
        self.cost = cost
    def __str__(self):
        return f"{self.damage}, {self.name}, {self.cost}"

# Fists
fists = Weapon(10, "Fists", 0) # decided to create an instance of the default weapon in case players would want to equip fists for whatever reason


class Player():
    health = 100 # Player's HP, doesn't increase, but can be healed by buying potions
    money = 0 # Base money, can be increased through "Scouring"
    health_potions = 0 # Health Potions that can be used to recover a player's health
    player_weapon = fists # Starter weapon + base damage, decided to have both in one variable
    bag = [] # Initializing bag, so that players can purchase multiple weapons

# Standalone variables
shop_choice = 0
bag = Player.bag

# Tests
bag.append("Fists")
print(*bag)
print(Player.player_weapon)
#------------------------------------ 

# Weapons and their stats: Damage, Name, and shop Cost
stick = Weapon(15, "Stick", 500)
wooden_sword = Weapon(20, "Wooden Sword", 1000)
bow = Weapon(30, "Bow", 3000)
metal_sword = Weapon(40, "Metal Sword", 7000)
dragonblade = Weapon(200, "Dragonblade", 20000)
# ------------------------------------------------

# Small Functions: Short message statements or code that does like one thing
def equip_message():
    print(f"You've equipped the {Player.player_weapon.name}!")
def add_weapon(bag, shop_choice):
    if shop_choice == "1":
        bag.append("Stick")
    elif shop_choice == "2":
        bag.append("Wooden Sword")
    elif shop_choice == "3":
        bag.append("Bow")
    elif shop_choice == "4":
        bag.append("Metal Sword")
    elif shop_choice == "5":
        bag.append("Dragonsblade")
    else:
        pass
def purchase_message():
    print(f"You just bought the {Player.player_weapon.name}! ({Player.player_weapon.damage} damage)")
    print(f"You've equipped the {Player.player_weapon.name}.")
    print("You leave the shop, a new weapon in hand. ")
def print_weapons():
    for i in bag:
        print(i, end=", ")

# Medium Sized Functions: Functions in choose() function, since I decided to compact the choose() function a bit by turning the print statements/minor pieces of code into their own functions
def print_player_stats():
    print(f"Your money: {Player.money}")
    print(f"Your health: {Player.health}")
    print(f"Your current damage: {Player.player_weapon.damage}")
    print(f"Your current weapon: {Player.player_weapon.name}")
def shop_desc_fists():
    print("You look around, taking a closer look at the wares. To the left of you, lies a simple Stick.")
    print("It looks like it will add a bit to your damage, having 15 damage instead of 10.")
    print("Behind the boy, lies 3 more weapons, one is slightly stronger weapon: a Wooden Sword.")
    print("This has twice the damage as just your hands (20 damage)")
    print("Next to the Wooden Sword lies a basic Bow, with about 30 damage.")
    print("\nA Metal Sword, gleaming in the afternoon sun, catches your attention. This weapon has 40 damage.")
    print("You notice the boy lifting another large sword from under the desk. Wide-eyed, you look over the weapon.")
    print("\"The Dragonblade,\" the boy said in a wispy voice. \n")
    print("Jewels adorn the sword, shining bright like sunlight on the ocean waves. The tip is sharp, enough to pierce anything it touches. This glorious weapon has 200 damage. ")

# HUMONGOUS Functions: The main 3 functions that are part of the game, some made out of mid-sized and/or small functions
def maze():
    print("You walk along the path set before you. In a few minutes, you're in front of a castle. Its stone walls are cracked, evidence of its old age."
          "Moss, vines, and other vegetation have conquered the castle's high towers and grasp the building like a "
    "You don't know why it's here or why you even"
    "felt called to it. But deep inside your heart, you knew that this is where the Lord's Staff is hidden, deep within the labryinth"
    "filled with monsters and other entities wishing to find it.")
    """
    This might not stay a function, it's just a placeholder for the options. Still planning out how the maze will work.
    Or not really how the maze "works" but the paths the maze has. The players can choose between certain directions when approaching a point in the
    maze with multiple directions (Left, Right, etc). I'm still figuring out how extensive this maze will b e. 
    """
def purchasing(): # Function for buying things at the shop
    print(" ") # Whitespace for easier reading
    print(f"Wares: \n1.Stick ({stick.cost} coins)\n2. Wooden Sword ({wooden_sword.cost} coins)\n3. Bow {bow.cost})\n4. Metal Sword ({metal_sword.cost} coins)\n5. Dragonblade ({dragonblade.cost} coins), ")
    while 1 == 1: # Loop of buying things in shop
        shop_choice = input("What would you like to buy? (1: Stick, 2: Wooden Sword, 3: Bow, 4: Metal Sword, 5: Dragonblade (or 6: Nothing?)): ")
        shop_choice = shop_choice
        if shop_choice == "6":
            print("\"Have a nice day!\" the boy says, waving his hand goodbye.")
            print(" ")
            print("You have left the shop.")
            break # Leaves the shop
        elif shop_choice == "1":
            if bag.count("Stick") > 0: # If the player already has this item in their bag, they're kicked out of the shop teehee
                print("You already have this item.")
                break
            else: 
                if Player.money >= stick.cost: 
                    confirmation = input("\"Are you sure?\" the boy asks. (Yes/No): ") # Making sure the player actually wants the item
                    confirmation = confirmation.lower()
                    if confirmation == "yes": 
                        print(f"\"Yes,\" you reply, handing over {stick.cost} coins to the boy. The boy collects the coins with both of his hands, and counts them slowly. He then gives you the {stick.name}.")
                        print(" ")
                        add_weapon(bag, shop_choice)
                        Player.money -= stick.cost
                        Player.player_weapon = stick
                        purchase_message()
                    elif confirmation == "no":
                        print("\"Look around, then! Maybe you'll find something else you like,\" the boy says.")
                        continue
                else:
                    print("The boy counts the gold coins you've given him, a frown appearing on his face when he was finished. \"You don't have enough money.\"") 
                    break # You get kicked out since you don't have money
        elif shop_choice == "2":
                if bag.count("Wooden Sword") > 0: # If the player already has this item in their bag, they're kicked out of the shop teehee
                    print("You already have this item.")
                    break
                else: 
                    if Player.money >= wooden_sword.cost: 
                        confirmation = input("\"Are you sure?\" the boy asks. (Yes/No): ") # Making sure the player actually wants the item
                        confirmation = confirmation.lower()
                        if confirmation == "yes": 
                            print(f"\"Yes,\" you reply, handing over {wooden_sword.cost} coins to the boy. The boy collects the coins with both of his hands, and counts them slowly. He then gives you the {wooden_sword.name}.")
                            print(" ")
                            add_weapon(bag, shop_choice)
                            Player.money -= wooden_sword.cost
                            Player.player_weapon = wooden_sword
                            purchase_message()
                        elif confirmation == "no":
                            print("\"Look around, then! Maybe you'll find something else you like,\" the boy says.")
                            continue
                    else:
                        print("The boy counts the gold coins you've given him, a frown appearing on his face when he was finished. \"You don't have enough money.\"") 
                        break # You get kicked out since you don't have money
        elif shop_choice == "4":
            if bag.count("Metal Sword") > 0: # If the player already has this item in their bag, they're kicked out of the shop teehee
                print("You already have this item.")
                break
            else: 
                if Player.money >= metal_sword.cost: 
                    confirmation = input("\"Are you sure?\" the boy asks. (Yes/No): ") # Making sure the player actually wants the item
                    confirmation = confirmation.lower()
                    if confirmation == "yes": 
                        print(f"\"Yes,\" you reply, handing over {metal_sword.cost} coins to the boy. The boy collects the coins with both of his hands, and counts them slowly. He then gives you the {metal_sword.name}.")
                        print(" ")
                        add_weapon(bag, shop_choice)
                        Player.money -= metal_sword.cost
                        Player.player_weapon = metal_sword
                        purchase_message()
                    elif confirmation == "no":
                        print("\"Look around, then! Maybe you'll find something else you like,\" the boy says.")
                        continue
                else:
                    print("The boy counts the gold coins you've given him, a frown appearing on his face when he was finished. \"You don't have enough money.\"") 
                    break # You get kicked out since you don't have money
        elif shop_choice == "3":
            if bag.count("Bow") > 0: # If the player already has this item in their bag, they're kicked out of the shop teehee
                print("You already have this item.")
                break
            else: 
                if Player.money >= bow.cost: 
                    confirmation = input("\"Are you sure?\" the boy asks. (Yes/No): ") # Making sure the player actually wants the item
                    confirmation = confirmation.lower()
                    if confirmation == "yes": 
                        print(f"\"Yes,\" you reply, handing over {bow.cost} coins to the boy. The boy collects the coins with both of his hands, and counts them slowly. He then gives you the {bow.name}.")
                        print(" ")
                        add_weapon(bag, shop_choice)
                        Player.money -= bow.cost
                        Player.player_weapon = bow
                        purchase_message()
                    elif confirmation == "no":
                        print("\"Look around, then! Maybe you'll find something else you like,\" the boy says.")
                        continue
                else:
                    print("The boy counts the gold coins you've given him, a frown appearing on his face when he was finished. \"You don't have enough money.\"")  
                    break # You get kicked out since you don't have money
        elif shop_choice == "5":
            if bag.count("Dragonsblade") > 0: # If the player already has this item in their bag, they're kicked out of the shop teehee
                print("You already have this item.")
                break
            else: 
                if Player.money >= dragonblade.cost: 
                    confirmation = input("\"Are you sure?\" the boy asks. (Yes/No): ") # Making sure the player actually wants the item
                    confirmation = confirmation.lower()
                    if confirmation == "yes": 
                        print(f"\"Yes,\" you reply, handing over {dragonblade.cost} coins to the boy. The boy collects the coins with both of his hands, and counts them slowly. He then gives you the {dragonblade.name}.")
                        print(" ")    
                        add_weapon(bag, shop_choice)
                        Player.money -= dragonblade.cost
                        Player.player_weapon = dragonblade
                        purchase_message()
                    elif confirmation == "no":
                        print("\"Look around, then! Maybe you'll find something else you like,\" the boy says.")
                        continue
                else:
                    print("The boy counts the gold coins you've given him, a frown appearing on his face when he was finished. \"You don't have enough money.\"") 
                    break # You get kicked out since you don't enough money, brokie
        else:
            print("\"Uhm, I don't have that in the store right now,\" the boy says. \"Maybe you should choose something else.\"")
            print("\"Oh! Okay!\" you say in embarassment.")
            continue # Player gets to rechoose their options if they mistype something (or something...)
    choose()
                    
def choose(): # Player chooses what they want to do (5 options)
    option = input("What do you want to do? (1: Scour/ 2: Search for the Lord's Staff in the Maze/3: Go to Shop/4: Check Your Stats/ 5: Check Your Inventory)")
    if option == "1": # "Scouring"
        winnings = random.randrange(1,120)
        print("You got " + str(winnings) + " moneys!")
        Player.money += winnings
        choose()
    elif option == "4": # Shows Player their Stats
        print_player_stats()
        choose()
    elif option == "2": # Goes to the "main game"
        maze()
    elif option == "3": # Shop to buy potions and better weapons
        print(" ")
        print("You enter a stout shop. Potions fill the shelves on both sides of the cramped shop. A small boy sits at the cashier desk, legs swinging back and forth.")
        print("He seems too young to own a shop like this, so you assume he's the owner's son. The boy is likely not older than 10, but he has a demeanor that makes him look so much older.")
        print(" ")
        if Player.player_weapon.name == "Fists": # Different descriptions based on current weapon
            shop_desc_fists()
            purchasing()
    elif option == "5":
        print("You notice the bag that was hanging on your back. Take a look inside.")
        print(f"Your weapons: ")
        print_weapons()
        print(" ")
        equip = input("Do you want to equip a certain weapon? (Yes/No): ")
        equip = equip.lower()
        if equip == "yes":
            print("Your weapons: ")
            print_weapons()
            print(" ")
            select = input(f"Select your weapon to equip: ") # not case sensitive
            if bag.count(select) > 0 or bag.count(select.capitalize()) > 0:
                if Player.player_weapon.name != select or Player.player_weapon.name.lower() != select: 
                    if select == "Stick" or select.lower() == "stick":
                        Player.player_weapon = stick
                        equip_message()
                    elif select == "Metal Sword" or select.lower() == "metal sword":
                        Player.player_weapon = metal_sword
                        equip_message()
                    elif select == "Bow" or select.lower() == "bow":
                        Player.player_weapon = bow
                        equip_message()
                    elif select == "Wooden Sword" or select.lower() == "wooden sword":
                        Player.player_weapon = wooden_sword
                        equip_message()
                    elif select == "Dragonblade" or select.lower() == "dragonblade":
                        Player.player_weapon = dragonblade
                        equip_message()
                    elif select == "Fists" or select.lower() == "fists":
                        Player.player_weapon = fists
                else:
                    print("You already have this item equipped.")
            else:
                print("You don't have this item.")

        choose()
    else:
        print("That is not a valid option.")
        choose()

# The game begins!!
# Waow i can't believe this little code (not defining functions, not defining classes) is what it takes to run the program. 
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



    