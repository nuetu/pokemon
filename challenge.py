import random #import random library 
from pokemon import movedex #import the movedex from pokemon.py 

def Challenge(user, computer): #called from main.py, requires user and computer player objects as paramaters, runs a while loop until someone loses

    def clear_screen(): #clear the screen for a clean user interface 
        for i in range(30):
            print("\n")

    clear_screen()

    user.view_team() #display the user's team
    invalid_pokemon = True 
    while invalid_pokemon: #run a while loop utill invalid_pokemon is false
        user_pokemon = input("\n\nChoose your first pokemon: ").capitalize() #asks the user to selecty their first pokemon, capitalize to match 
        for x in user.team: 
            if x.name == user_pokemon: #loops through the users team and finds a pokemon that matches the name from the input
                user_pokemon = x #sets user_pokemon to the match
                invalid_pokemon = False #break the while loop 
                break #stops the while loop and doesn't display the code below 
        if invalid_pokemon: 
            print("Pokemon not on team!")

    computer_pokemon = random.choice(computer.team) #computer's first pokemon is a random choice

    clear_screen()

    def calculate_attack(challenger, move): #calculates attack! requires two paramaters, a challenger (Player Object), and a move (Move Object), returns an int damage 
        base_damage = movedex[move].damage #the move's damage stat
        if challenger == user:
            attack = user_pokemon.attack / 100 
            defense = computer_pokemon.defense / 100 + 1
            damage_multiplier = .9
        elif challenger == computer:
            attack = computer_pokemon.attack / 100
            defense = user_pokemon.defense / 100 + 1
            damage_multiplier = 1.1
        damage = base_damage * (attack / defense) * damage_multiplier #damage done is (the move's damage) x (the attack to defense ratio) * (computer boost / user decrease)
        return damage
        

    def attack(param_pokemon, challenger): #performs the attack sequence, requires a pokemon object, and a player object as the paramaters 
        if challenger == user: # if the user attacks
            attack = input(f"{param_pokemon.challenge_display()}> ") #ask the user which attack (string number) to use, or if they want to pass
            clear_screen()
            if attack.lower() == "pass": 
                print(f"{challenger.name} passed.")
                return True #if the user chooses pass, break the function call, no code below will run, and while loop will break
            try: #make sure the user chooses a correct attack 
                attack = param_pokemon.moves[int(attack) - 1] #set the input to an integer, and selects the index of the number from the pokemon's move list to set attack to a move object
                damage = round(calculate_attack(challenger,attack)) #calculate the damage, then round the result to a whole number
                computer_pokemon.damage(damage) # pokemon object method
            except: #if something went wrong, tell the user it was an invalid attack
                print("Inalid attack")
                return False #break the function call, no code below will run, and while loop will break
        elif challenger == computer: #if the computer attacks
            if param_pokemon.moves == []: # if the computer's pokemon has no moves, pass
                print(f"{challenger.name} passed.")
                return True #break the function call, no code below will run, and while loop will break
            move = random.choice(param_pokemon.moves) #a random move from the computer's pokemon will be chosen
            if move in movedex: #validate the move 
                attack = param_pokemon.moves[param_pokemon.moves.index(move)] #select the move object
                damage = round(calculate_attack(challenger,attack)) #calulate the damage
                user_pokemon.damage(damage) # pokemon object method
        print(f"{param_pokemon.name} used {movedex[attack].name}!") #print f display the move used 
        return True #break the while loop

    def swap(challenger): #swaps out current pokemon for another pokemon on your team. Requires player object as paramater
        try: # makes sure the user can swap, will break if invalid pokemon is selected
            nonlocal user_pokemon, computer_pokemon #tells the computer that these variables are not local to this function and instead use the original variables
            invalid_pokemon = True
            while invalid_pokemon: #run a while loop utill invalid_pokemon is false
                if challenger == user: 
                    swap_pokemon = input("Swap out: ").capitalize()
                    clear_screen()
                    if swap_pokemon == "Back": 
                        return False #end the swap function
                elif challenger == computer:
                    swap_pokemon = random.choice([x for x in computer.team if x != computer_pokemon and x.hp > 0]) #select a random pokemon in the computer's team if the pokemon is not the one active and not fainted
                    swap_pokemon = swap_pokemon.name
                for x in challenger.team: #validates the pokemon being swapped
                    if x.name == swap_pokemon and x.hp > 0:
                        swap_pokemon = x
                        invalid_pokemon = False
                        break
                if invalid_pokemon: 
                    raise Exception("invalid")
            if challenger == user: 
                user_pokemon = swap_pokemon #sets the swapped pokemon object to the nonlocal user_pokemon variable
            elif challenger == computer:
                computer_pokemon = swap_pokemon #sets the swapped pokemon object to the nonlocal computer_pokemon variable
            print(f"{challenger.name} swapped in {swap_pokemon.name}!") #print f display the challenger swapping out their pokemon
            return True
        except: #pass if invalid pokemon is selected
            print(f"{challenger.name} passed.")
            return True #breaks the while loop
            
    def computer_move(computer_pokemon): #computer's turn
        random_move = random.randrange(0,10)
        if random_move == 5 or computer_pokemon.hp < 1: #1 in 10 chance of swapping, or swap if pokemon is feinted
            swap(computer) #perform swap
        else:
            if computer_pokemon.hp >= 1: #perform attack if pokemon is not feinted
                attack(computer_pokemon, computer) #perform attack 

    def turn(move, param_pokemon): #user's turn, returns True to while loop until the game is over
        clear_screen()
        back = False 
        while not back:
            if move.lower() == "attack" and user_pokemon.hp >= 1:
                back = attack(param_pokemon, user)
            elif move.lower() == "pokemon":
                user.view_team()
                back = swap(user)
            elif move.lower() == "run":
                print(f"{user.name} fled!")
                user.losses += 1
                computer.wins += 1
                return False
            else:
                print("Unavailable move")
                return True
        if computer_pokemon.hp < 1: #prints when the computer's pokemon faints
            print(f"{computer_pokemon.name} feinted!")
        computer_move(computer_pokemon) #The computer takes it's turn AFTER you make your move, so it can swap if its pokemon faints. 
        if user_pokemon.hp < 1: #prints when the player's pokemon faints
            print(f"{user_pokemon.name} feinted!")
        if all(x.hp == 0 for x in user.team): #if all pokemon in player's team have fainted
            print("You have lost the battle!")
            user.losses += 1 #player value
            computer.wins += 1 #player value
            return False
        elif all(x.hp == 0 for x in computer.team): #if all pokemon in computers's team have fainted
            print("You have won the battle!")
            print("You have earned 300 coins!")
            user.set_balance(300) #player method
            user.wins += 1 #player value
            computer.losses += 1 #player value
            return False
        else:
            return True

    while turn(input(f"\n{user_pokemon}\t\tvs\t\t{computer_pokemon}\n{'[Attack]' if user_pokemon.hp > 0 else ''}[Pokemon][Run] \n> "), user_pokemon):
        pass #while loop calls turn() function with the user input as the paramater, also hides [Attack] in selected pokemon has fainted 
        
    for one_pokemon in computer.team: #heals the computer's team. However, the computer resets after the challenge is over, unless you remove that re-initialization from main.py
        if one_pokemon.hp < 0:
            one_pokemon.heal(one_pokemon.MAXHP)