import copy, random 
import pokemon, player, challenge 

USER_TEAM_SIZE = 6 
COMPUTER_TEAM_SIZE = 3 
COMPUTER_NAME = "Gary"

def clear_screen(): 
        for i in range(30):
            print("\n")

def init_player(): 
    clear_screen()
    print("Welcome to pokemon battle!")
    global user 
    user = player.Player(input("Please enter your name: ")) 
    clear_screen()
    play_style = input("Would you like to play with random pokemon? y/n: ").lower() 
    clear_screen()
    if play_style == "y": 
        i = 0
        while i < USER_TEAM_SIZE: 
            random_pokemon = random.choice(list(pokemon.pokedex.keys())) 
            user.team.append(copy.deepcopy(pokemon.pokedex[random_pokemon])) 
            i += 1
    else: 
        i = 0
        while i < USER_TEAM_SIZE:
            select_pokemon = input(f"Please enter your pokemon's name {i + 1}/{USER_TEAM_SIZE}: ").lower()
            if select_pokemon in pokemon.pokedex: 
                user.team.append(copy.deepcopy(pokemon.pokedex[select_pokemon])) 
                i += 1 
            else:
                print("Unavailable / Invalid pokemon, try another")
                continue 
    print("Type help for help")

def init_computer(): 
    global computer 
    computer = player.Player(COMPUTER_NAME) 
    i = 0
    while i < COMPUTER_TEAM_SIZE: 
        random_pokemon = random.choice(list(pokemon.pokedex.keys())) 
        if not any(x.name == random_pokemon for x in computer.team): 
            computer.team.append(copy.deepcopy(pokemon.pokedex[random_pokemon])) 
            i += 1 
        else:
             continue 

def view_stats(user_pokemon): 
    clear_screen()
    for x in user.team: 
        if x.name == user_pokemon: 
            print(f"\n{user.name}'s {x.name}:") 
            print(f"    {x.hp}/{x.MAXHP}hp")
            print(f"    Type: {x.types}")
            print(f"    Moves: {[pokemon.movedex[i].name for i in x.moves if i in pokemon.movedex]}")
            return True 
    print("You don't have this pokemon!")

def heal(): 
    clear_screen()
    if user.balance >= 50: 
        user_pokemon = input("(50 Coins) Select your pokemon: ").capitalize() 
        for x in user.team: 
            if x.name == user_pokemon: 
                x.heal(x.MAXHP) 
                user.set_balance(-50) 
                print(f"{x.name} Healed!") 
                return True 
        print("You don't have this pokemon!")
    else: 
        print("You do not have enough coins!")

def commands(command): 
    clear_screen()
    if not (command): 
        return True
    command = command.split() 
    action = command.pop(0) 
    if action == "help":
        help() 
    elif action == "team":
        user.view_team() 
    elif action == "stats":
        user.view_team() 
        view_stats(input("\nSelect your pokemon: ").capitalize()) 
    elif action == "me":
        print(user) 
    elif action == "challenge":
        challenge.Challenge(user,computer) 
        init_computer() 
    elif action == "heal":
        heal()
    elif action == "quit":
        print("Quitting the game...")
        return False 
    else:
        print("Invalid command, please type 'help' for list of commands")
    return True 

init_computer() 
init_player() 

def help(): 
  print("\n")
  print("xxxxxxxxxxxxxxxxxxx Help Menu xxxxxxxxxxxxxxxxxxx")
  print("team - view your team")
  print("stats - view your pokemon's stats")
  print("me - show your stats")
  print("challenge - challenge the computer")
  print("heal - heal your pokemon")
  print("quit - quit the game")
  print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

command_display = "\n\n[Team][Stats][Me][Help]\n[Heal][Challenge][Quit]\n> " 

while commands(input(f"{command_display}").lower()): 
    pass