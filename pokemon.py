class Pokemon:
  def __init__(self, name, hp, moves, ptype, attack, defense): #pokemon objects require parameters for name, hp, moves list, pokemon type, attack num, defense num
    self.name = name
    self.MAXHP = hp
    self.hp = hp
    self.moves = moves
    self.types = ptype
    self.attack = attack
    self.defense = defense

  def __str__(self): # returns the current status of the pokemon, called from player.py
    if self.hp < 1:
      return f"{self.name} [Fainted]"
    elif self.hp == self.MAXHP:
      return "[Max Health]"
    else:
      return f"{self.name} [{self.hp}/{self.MAXHP}hp]"

  def damage(self, amount): #pokemon object method to set the hp of the pokemon, called from challenge.py. Requires integer as the paramater
    if ((self.hp - amount) >= 0):
      self.hp -= amount
    else:
      self.hp = 0 

  def heal(self, amount): #called from main.py. Requires integer as the paramater
    if ((self.hp + amount) > self.MAXHP):
      self.hp = self.MAXHP
    else: 
      self.hp += amount

  def moves_display(self): #display moves details, unused. No need to replicate, unless move stats desired.
    print(f"{self.name}'s Moves:")
    for move in self.moves:
      if move in movedex:
        print(movedex[move])

  def challenge_display(self): # returns a list of moves and a command display, used in challenge.py
    print(f"{self.name} {self.hp_display()}hp")
    number = 1
    string = "\n"
    for move in self.moves:
      if move in movedex:
        print(f"{number}. {movedex[move]}")
        string += f"[{str(number)}]"
        number += 1
      elif self.moves.length == 0:
        print(f"{self.name} has no moves!")
        break
    string += "[Pass]\n"
    return string
       

class PokeMoves:  #move object, requires paramaters name, damage, and move type 
  def __init__(self, name, damage, mtype):
    self.name = name
    self.damage = damage
    self.type = mtype

  def __str__(self): #returns move name and type when move object called, used in pokemon.py in the moves_display() method of Pokemon Objext
    return f"{self.name} [Type: {self.type}]"

#replace with initialize.py (typedex) and pokedex.py (pokedex + movedex)
pokedex = { 
    "bulbasaur":Pokemon("Bulbasaur",45,['mega_kick'],['Grass', 'Poison'],49,49),
    "ivysaur":Pokemon("Ivysaur",60,['vice_grip', 'gust'],['Grass', 'Poison'],62,63),
    "venusaur":Pokemon("Venusaur",80,['fly', 'horn_attack', 'fire_punch'],['Grass', 'Poison'],82,83),
    "charmander":Pokemon("Charmander",39,['stomp', 'karate_chop', 'vine_whip', 'gust'],['Fire'],52,43),
    "charmeleon":Pokemon("Charmeleon",58,['headbutt', 'double_slap', 'scratch', 'vice_grip'],['Fire'],64,58),
    "charizard":Pokemon("Charizard",78,['razor_wind', 'thunder_punch'],['Fire', 'Flying'],84,78),
    "squirtle":Pokemon("Squirtle",44,['stomp'],['Water'],48,65),
    "wartortle":Pokemon("Wartortle",59,['fly', 'double_slap', 'headbutt'],['Water'],63,80),
    "blastoise":Pokemon("Blastoise",79,['slam', 'scratch'],['Water'],83,100),
    "caterpie":Pokemon("Caterpie",45,['pay_day', 'rolling_kick', 'comet_punch'],['Bug'],30,35),
    "metapod":Pokemon("Metapod",50,['fly', 'karate_chop'],['Bug'],20,55),
    "butterfree":Pokemon("Butterfree",60,['fly', 'ice_punch', 'vine_whip'],['Bug', 'Flying'],45,50),
    "weedle":Pokemon("Weedle",40,['gust', 'headbutt', 'cut'],['Bug', 'Poison'],35,30),
    "kakuna":Pokemon("Kakuna",45,['mega_punch'],['Bug', 'Poison'],25,50),
    "beedrill":Pokemon("Beedrill",65,['rolling_kick', 'thunder_punch', 'fire_punch', 'vine_whip'],['Bug', 'Poison'],90,40),
    "pidgey":Pokemon("Pidgey",40,['stomp', 'slam'],['Normal', 'Flying'],45,40),
    "pidgeotto":Pokemon("Pidgeotto",63,['slam', 'pay_day'],['Normal', 'Flying'],60,55),
    "pidgeot":Pokemon("Pidgeot",83,['stomp', 'razor_wind'],['Normal', 'Flying'],80,75),
    "rattata":Pokemon("Rattata",30,[],['Normal'],56,35),
    "raticate":Pokemon("Raticate",55,[],['Normal'],81,60),
    "spearow":Pokemon("Spearow",40,['gust', 'headbutt', 'mega_punch'],['Normal', 'Flying'],60,30),
    "fearow":Pokemon("Fearow",65,['headbutt', 'ice_punch'],['Normal', 'Flying'],90,65),
    "ekans":Pokemon("Ekans",35,['slam'],['Poison'],60,44),
    "arbok":Pokemon("Arbok",60,['stomp', 'scratch'],['Poison'],95,69),
    "pikachu":Pokemon("Pikachu",35,['mega_kick'],['Electric'],55,40),
    "raichu":Pokemon("Raichu",60,['stomp', 'fly', 'fire_punch', 'cut'],['Electric'],90,55),
    "sandshrew":Pokemon("Sandshrew",50,['slam'],['Ground'],75,85),
    "sandslash":Pokemon("Sandslash",75,['headbutt'],['Ground'],100,110),
    "nidoran":Pokemon("Nidoran",55,[],['Poison'],47,52),
    "nidorina":Pokemon("Nidorina",70,['mega_punch'],['Poison'],62,67),
}

movedex = {
    "pound":PokeMoves("Pound",40,"Normal"),
    "karate_chop":PokeMoves("Karate Chop",50,"Fighting"),
    "double_slap":PokeMoves("Double Slap",15,"Normal"),
    "comet_punch":PokeMoves("Comet Punch",18,"Normal"),
    "mega_punch":PokeMoves("Mega Punch",80,"Normal"),
    "pay_day":PokeMoves("Pay Day",40,"Normal"),
    "fire_punch":PokeMoves("Fire Punch",75,"Fire"),
    "ice_punch":PokeMoves("Ice Punch",75,"Ice"),
    "thunder_punch":PokeMoves("Thunder Punch",75,"Electric"),
    "scratch":PokeMoves("Scratch",40,"Normal"),
    "vice_grip":PokeMoves("Vice Grip",55,"Normal"),
    "razor_wind":PokeMoves("Razor Wind",80,"Normal"),
    "cut":PokeMoves("Cut",50,"Normal"),
    "gust":PokeMoves("Gust",40,"Fighting"),
    "wing_attack":PokeMoves("Wing Attack",60,"Fighting"),
    "fly":PokeMoves("Fly",90,"Fighting"),
    "bind":PokeMoves("Bind",15,"Normal"),
    "slam":PokeMoves("Slam",80,"Normal"),
    "vine_whip":PokeMoves("Vine Whip",45,"Grass"),
    "stomp":PokeMoves("Stomp",65,"Normal"),
    "double_kick":PokeMoves("Double Kick",30,"Fighting"),
    "mega_kick":PokeMoves("Mega Kick",120,"Normal"),
    "jump_kick":PokeMoves("Jump Kick",130,"Fighting"),
    "rolling_kick":PokeMoves("Rolling Kick",60,"Fighting"),
    "headbutt":PokeMoves("Headbutt",70,"Normal"),
    "horn_attack":PokeMoves("Horn Attack",65,"Normal"),
}

typedex = { #key: strength
  "Normal":("None"),
  "Grass":("Water", "Ground"),
  "Poison":("Grass"),
  "Fire":("Grass","Ice","Bug"),
  "Flying":("Grass","Fighting"),
  "Water":("Fire","Ground"),
  "Bug":("Grass"),
  "Electric":("Water","Flying"),
  "Ground":("Fire","Electric","Poison"),
  "Fighting":("Normal","Ice"),
  "Ice":("Grass","Ground","Flying")
}