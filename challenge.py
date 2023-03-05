import random
from pokemon import movedex

def Challenge(user, computer):
    def clear_screen():
        for i in range(30):
            print("\n")
    clear_screen()
    user.view_team()
    invalid_pokemon = True 
    while invalid_pokemon:
        user_pokemon = input("Choose your first pokemon: ").capitalize()
        for x in user.team:
            if x.name == user_pokemon:
                user_pokemon = x
                invalid_pokemon = False
                break
        if invalid_pokemon: 
            print("Pokemon not on team!")
    computer_pokemon = random.choice(computer.team)
    clear_screen()

    def calculate_attack(challenger, move):
        base_damage = movedex[move].damage
        if challenger == user:
            attack = user_pokemon.attack / 100
            defense = computer_pokemon.defense / 100 + 1
        elif challenger == computer:
            attack = computer_pokemon.attack / 100
            defense = user_pokemon.defense / 100 + 1
        damage = base_damage * attack / defense
        return damage
        

    def attack(param_pokemon, challenger):
        if challenger == user:
            attack = input(f"{param_pokemon.challenge_display()}> ")
            clear_screen()
            if attack.lower() == "pass":
                print(f"{challenger.name} passed.")
                return True
            try:
                attack = param_pokemon.moves[int(attack) - 1]
                damage = round(calculate_attack(challenger,attack))
                computer_pokemon.damage(damage)
            except: 
                print("Inalid attack")
                return False
        elif challenger == computer:
            if param_pokemon.moves == []:
                print(f"{challenger.name} passed.")
                return True
            move = random.choice(param_pokemon.moves)
            if move in movedex:
                attack = param_pokemon.moves[param_pokemon.moves.index(move)]
                damage = round(calculate_attack(challenger,attack))
                user_pokemon.damage(damage)
        print(f"{param_pokemon.name} used {movedex[attack].name}!")
        return True

    def swap(challenger):
        try:
            nonlocal user_pokemon, computer_pokemon 
            invalid_pokemon = True
            while invalid_pokemon:
                if challenger == user:
                    swap_pokemon = input("Swap out: ").capitalize()
                    clear_screen()
                    if swap_pokemon == "Back":
                        return False
                elif challenger == computer:
                    swap_pokemon = random.choice(computer.team)
                    swap_pokemon = swap_pokemon.name
                for x in challenger.team:
                    if x.name == swap_pokemon and x.hp > 0:
                        swap_pokemon = x
                        invalid_pokemon = False
                        break
                if invalid_pokemon: 
                    raise Exception("invalid")
            if challenger == user:
                user_pokemon = swap_pokemon
            elif challenger == computer:
                computer_pokemon = swap_pokemon
            print(f"{challenger.name} swapped in {swap_pokemon.name}!")
            return True
        except: 
            print(f"{challenger.name} passed.")
            return True 
            
    def computer_move(computer_pokemon):
        random_move = random.randrange(0,10)
        if random_move == 5 or computer_pokemon.hp < 1:
            swap(computer)
        else:
            if computer_pokemon.hp > 1:
                attack(computer_pokemon, computer)

    def turn(move, param_pokemon):
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
                return False
            else:
                print("Unavailable move")
                return True
        if computer_pokemon.hp < 1:
            print(f"{computer_pokemon.name} feinted!")
        computer_move(computer_pokemon)
        if user_pokemon.hp < 1:
            print(f"{user_pokemon.name} feinted!")
        if all(x.hp == 0 for x in user.team):
            print("You have lost the battle!")
            user.losses += 1
            computer.wins += 1
            return False
        elif all(x.hp == 0 for x in computer.team):
            print("You have won the battle!")
            print("You have earned 300 coins!")
            user.set_balance(300)
            user.wins += 1
            computer.losses += 1
            return False
        else:
            return True

    while turn(input(f"\n{user_pokemon}\t\tvs\t\t{computer_pokemon}\n{'[Attack]' if user_pokemon.hp > 0 else ''}[Pokemon][Run] \n> "), user_pokemon):
        pass
        
    for one_pokemon in computer.team:
        if one_pokemon.hp < 0:
            one_pokemon.heal(one_pokemon.MAXHP)