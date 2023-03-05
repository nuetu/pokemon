#credit to https://github.com/fanzeyi/pokemon.json for pokemon information! 
import copy
import random
import pokemon
import player
import challenge

def start():
    print("Welcome to pokemon battle!")
    global user
    user = player.Player(input("Please enter your name: "))
    play_style = input("Would you like to play with random pokemon? y/n: ").lower()
    if play_style == "y": 
        i = 0
        while i < 6:
            random_pokemon = random.choice(list(pokemon.pokedex.keys()))
            user.team.append(copy.deepcopy(pokemon.pokedex[random_pokemon]))
            i += 1
    else:
        i = 0
        while i < 6:
            select_pokemon = input(f"Please enter your pokemon's name {i + 1}/6: ")
            if select_pokemon in pokemon.pokedex and not any(x.name == random_pokemon for x in user.team):
                user.team.append(copy.deepcopy(pokemon.pokedex[select_pokemon]))
                i += 1
            else:
                print("Unavailable / Invalid pokemon, try another")
                continue
    global computer
    computer = player.Player("Gary")
    i = 0
    while i < 3:
        random_pokemon = random.choice(list(pokemon.pokedex.keys()))
        if not any(x.name == random_pokemon for x in computer.team):
            computer.team.append(copy.deepcopy(pokemon.pokedex[random_pokemon]))
            i += 1
        else:
             continue
    print("Type /help for help")

def view_stats(user_pokemon):
    for x in user.team:
        if x.name == user_pokemon:
            print(f"\n{user.name}'s {x.name}:")
            print(f"    {x.hp}/{x.MAXHP}hp")
            print(f"    Type: {x.types}")
            print(f"    Moves: {x.moves}")

def heal():
    if user.balance >= 50:
        user_pokemon = input("Select your pokemon: ")
        for x in user.team:
            if x.name == user_pokemon:
                x.hp = x.MAXHP
                user.set_balance(-50)
                print(f"{x.name} Healed!")
    else: 
        print("You do not have enough coins!")

def commands(command):
    if not (command):
        return True
    if command[0] != "/":
        print(f"{user.name}: {command}")
        return True
    command = command.split()
    action = command.pop(0)
    if action == "/help":
        help()
    elif action == "/team":
        user.view_team()
    elif action == "/stats":
        view_stats(input("Select your pokemon: "))
    elif action == "/me":
        print(user)
    elif action == "/challenge":
        challenge.Challenge(user,computer)
    elif action == "/heal":
        heal()
    elif action == "/quit":
        print("Quitting the game...")
        return False
    else:
        print("Invalid command, please type '/help' for list of commands")
    return True

start()

def help():
  print("\n")
  print("xxxxxxxxxxxxxxxxxxx Help Menu xxxxxxxxxxxxxxxxxxx")
  print("/team - view your team")
  print("/stats - view your pokemon's stats")
  print("/me - show your stats")
  print("/challenge - challenge the computer")
  print("/heal - heal your pokemon")
  print("/quit - quit the game")
  print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

while commands(input("> ")):
    pass