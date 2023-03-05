class Player: #player object, requires a name. Defaults balance, team, wins, and losses to nothing on creation
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.team = []
        self.wins = 0
        self.losses = 0
    
    def __str__(self): #returns player stats when object called, used in main.py
        return f"\n{self.name}'s Stats: \n    Balance: {self.view_balance()}\n    Wins: {self.wins}\n    Losses: {self.losses}" #returns print f string

    def view_team(self): #prints the user's team, used in challenge.py and main.py
        print("\n")
        print(f"{self.name}'s team: ")
        for pokemon in self.team:
            print(f"    {pokemon}")
        
    def set_balance(self, amount): #adds or subtracts from the balance, used in challenge.py and main.py. Requires integer as the parameter.
        self.balance += amount

    def view_balance(self): #shows balance, used in player.py 
        if self.balance == 1:
            print(f"{self.balance} coin")
        else: 
            print(f"{self.balance} coins")