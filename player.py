class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.team = []
        self.wins = 0
        self.losses = 0
    
    def __str__(self):
        return f"\n{self.name}'s Stats: \n    Coins: {self.balance}\n    Wins: {self.wins}\n    Losses: {self.losses}"

    def view_team(self):
        print("\n")
        print(f"{self.name}'s team: ")
        for pokemon in self.team:
            print(f"    {pokemon}")
        
    def set_balance(self, amount):
        self.balance += amount

    def view_balance(self):
        if self.balance == 1:
            print(f"{self.balance} coin")
        else: 
            print(f"{self.balance} coins")