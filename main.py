#credit to https://github.com/fanzeyi/pokemon.json for pokemon information! 


import copy, random #import copy and random libraries
import pokemon, player, challenge #import pokemon.py, player.py, and challenge.py python files

USER_TEAM_SIZE = 6 # declare constant size for the user's team
COMPUTER_TEAM_SIZE = 3 # declare constant size for the computer's team
COMPUTER_NAME = "Gary"

def clear_screen(): #clear the screen for a clean user interface 
        for i in range(30):
            print("\n")

def init_player(): #initialize the player
    clear_screen()
    print("Welcome to pokemon battle!")
    global user #declare user variable global to use in other functions 
    user = player.Player(input("Please enter your name: ")) #make a new player object using the user's input as the new object's name
    clear_screen()
    play_style = input("Would you like to play with random pokemon? y/n: ").lower() #Ask the user to choose their team or have the computer pick theirs. set string to all lowercase 
    clear_screen()
    if play_style == "y": #if the user wants a random team
        i = 0
        while i < USER_TEAM_SIZE: #call the loop n times
            random_pokemon = random.choice(list(pokemon.pokedex.keys())) #find a random pokemon in your generated pokemon list
            user.team.append(copy.deepcopy(pokemon.pokedex[random_pokemon])) # create a deep copy of the pokemon and add to your team
            i += 1
    else: # if the user doesnt want a random team
        i = 0
        while i < USER_TEAM_SIZE:#call the loop n times 
            select_pokemon = input(f"Please enter your pokemon's name {i + 1}/{USER_TEAM_SIZE}: ").lower() #ask the user for a pokemon to add to team, using print f 
            if select_pokemon in pokemon.pokedex: # if the pokemon is valid a.k.a in the generated pokemon list
                user.team.append(copy.deepcopy(pokemon.pokedex[select_pokemon])) # create a deep copy of the pokemon and add to your team
                i += 1 #decrease the loop by 1 if pokemon add is successful 
            else:
                print("Unavailable / Invalid pokemon, try another")
                continue # run the loop again, but dont decrease the loop
    print("Type help for help")

def init_computer(): #initialize the computer, set their name and a random team. No output
    global computer #declare variable computer to be global, to use in other functions 
    computer = player.Player(COMPUTER_NAME) # makes a new player object using the constant COMPUTER_NAME as the name 
    i = 0
    while i < COMPUTER_TEAM_SIZE: #call the loop n times
        random_pokemon = random.choice(list(pokemon.pokedex.keys())) #random select a pokemon in the generated pokemon list
        if not any(x.name == random_pokemon for x in computer.team): # if the pokemon is not already in the computer's team
            computer.team.append(copy.deepcopy(pokemon.pokedex[random_pokemon])) # create a deep copy of the pokemon and add to the computer's team
            i += 1 # decrease the loop by 1 if pokemon add is successful
        else:
             continue # run the loop again, but dont decrease loop 

def view_stats(user_pokemon): #called from the commands() function, requires 1 paramater of the user's pokemon's name
    clear_screen()
    for x in user.team: #loop through your team
        if x.name == user_pokemon: #checks that the name you passed as a paramater is in your team, sets x to the pokemon OBJECT
            print(f"\n{user.name}'s {x.name}:") # print stats using print f 
            print(f"    {x.hp}/{x.MAXHP}hp")
            print(f"    Type: {x.types}")
            print(f"    Moves: {[pokemon.movedex[i].name for i in x.moves if i in pokemon.movedex]}")
            return True # return any value to break the foor loop and not display the print statement below 
    print("You don't have this pokemon!")

def heal(): #called from the commands() function, no paramaters required
    clear_screen()
    if user.balance >= 50: #costs 50 coins to heal a pokemon
        user.view_team()
        user_pokemon = input("(50 Coins) Select your pokemon: ").capitalize() #select your pokemon, capitalize input to match pokemon name
        for x in user.team: #loop through your team
            if x.name == user_pokemon and x.hp != x.MAXHP: #if you have a pokemon with the same name as you inputed:
                x.heal(x.MAXHP) #full heal the pokemon using a pokemon object method 
                user.set_balance(-50) #subtract 50 coins per pokemon // Player method 
                user.view_team()
                print(f"{x.name} Healed!") #print f the pokemon was healed 
                return True # return any value to break the foor loop and not display the print statement below 
        print("You don't have this pokemon!")
    else: #prints if you have less than 50 coins
        print("You do not have enough coins!")

def commands(command): #called from a infinite while loop, requires 1 paramater of the user's command
    clear_screen()
    if not (command): # if no command is given, skip 
        return True
    command = command.split() #separates individual words into a list
    action = command.pop(0) #takes the first item in the list, aka the command
    if action == "help":
        help() 
    elif action == "team":
        user.view_team() #player method 
    elif action == "stats":
        user.view_team() #player method 
        view_stats(input("\nSelect your pokemon: ").capitalize()) 
    elif action == "me":
        print(user) #prints Player object __str__() function
    elif action == "challenge":
        challenge.Challenge(user,computer) #begin the challenge sequence on challenge.py
        init_computer() # reset the computer's team 
    elif action == "heal":
        heal()
    elif action == "quit":
        print("Quitting the game...")
        return False #returns to the while loop false to break the while loop, breaks the function and skips over the code below
    else:
        print("Invalid command, please type 'help' for list of commands")
    return True # returns to the while loop true to continue the while loop

init_computer() #initialize the computer
init_player() #initialize the user 

def help(): # expansive help statement
  print("\n")
  print("xxxxxxxxxxxxxxxxxxx Help Menu xxxxxxxxxxxxxxxxxxx")
  print("team - view your team")
  print("stats - view your pokemon's stats")
  print("me - show your stats")
  print("challenge - challenge the computer")
  print("heal - heal your pokemon")
  print("quit - quit the game")
  print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

command_display = "\n\n[Team][Stats][Me][Help]\n[Heal][Challenge][Quit]\n> " # string variable with multiple line breaks 

while commands(input(f"{command_display}").lower()): #main while loop, passes user input to commands() function, which returns true or false to continue or break loop
    pass