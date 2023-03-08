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
    print(f"{self.name} [{self.hp}/{self.MAXHP}hp]")
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
    "bulbasaur":Pokemon("Bulbasaur",45,['acid', 'double_slap'],['Grass', 'Poison'],49,49),
    "ivysaur":Pokemon("Ivysaur",60,['poison_sting', 'stomp'],['Grass', 'Poison'],62,63),
    "venusaur":Pokemon("Venusaur",80,['poison_sting', 'acid'],['Grass', 'Poison'],82,83),
    "charmander":Pokemon("Charmander",39,['fire_punch', 'flamethrower'],['Fire'],52,43),
    "charmeleon":Pokemon("Charmeleon",58,['ember', 'thrash', 'headbutt'],['Fire'],64,58),
    "charizard":Pokemon("Charizard",78,['fire_punch', 'flamethrower', 'take_down', 'mega_punch'],['Fire', 'Flying'],84,78),
    "squirtle":Pokemon("Squirtle",44,['hydro_pump', 'water_gun', 'tackle', 'slam'],['Water'],48,65),
    "wartortle":Pokemon("Wartortle",59,['surf'],['Water'],63,80),
    "blastoise":Pokemon("Blastoise",79,['hydro_pump', 'slam'],['Water'],83,100),
    "caterpie":Pokemon("Caterpie",45,['pin_missile', 'twineedle'],['Bug'],30,35),
    "metapod":Pokemon("Metapod",50,['pin_missile', 'twineedle', 'comet_punch', 'take_down'],['Bug'],20,55),
    "butterfree":Pokemon("Butterfree",60,['pin_missile'],['Bug', 'Flying'],45,50),
    "weedle":Pokemon("Weedle",40,['acid'],['Bug', 'Poison'],35,30),
    "kakuna":Pokemon("Kakuna",45,['acid', 'pin_missile'],['Bug', 'Poison'],25,50),
    "beedrill":Pokemon("Beedrill",65,['twineedle', 'pin_missile'],['Bug', 'Poison'],90,40),
    "pidgey":Pokemon("Pidgey",40,['pound', 'pay_day', 'double_slap', 'cut'],['Normal', 'Flying'],45,40),
    "pidgeotto":Pokemon("Pidgeotto",63,['pound', 'razor_wind', 'scratch', 'comet_punch'],['Normal', 'Flying'],60,55),
    "pidgeot":Pokemon("Pidgeot",83,['bind', 'slam'],['Normal', 'Flying'],80,75),
    "rattata":Pokemon("Rattata",30,['bind', 'comet_punch', 'double_slap'],['Normal'],56,35),
    "raticate":Pokemon("Raticate",55,['cut', 'mega_punch', 'tackle'],['Normal'],81,60),
    "spearow":Pokemon("Spearow",40,['mega_kick', 'mega_punch'],['Normal', 'Flying'],60,30),
    "fearow":Pokemon("Fearow",65,['stomp', 'cut', 'vice_grip', 'comet_punch'],['Normal', 'Flying'],90,65),
    "ekans":Pokemon("Ekans",35,['acid'],['Poison'],60,44),
    "arbok":Pokemon("Arbok",60,['poison_sting', 'acid', 'take_down', 'stomp'],['Poison'],95,69),
    "pikachu":Pokemon("Pikachu",35,['thunder_punch'],['Electric'],55,40),
    "raichu":Pokemon("Raichu",60,['thunder_punch', 'headbutt'],['Electric'],90,55),
    "sandshrew":Pokemon("Sandshrew",50,['pay_day', 'mega_punch'],['Ground'],75,85),
    "sandslash":Pokemon("Sandslash",75,['tackle', 'comet_punch'],['Ground'],100,110),
    "nidoran♀":Pokemon("Nidoran♀",55,['acid', 'poison_sting', 'take_down', 'pay_day'],['Poison'],47,52),
    "nidorina":Pokemon("Nidorina",70,['poison_sting', 'vice_grip', 'headbutt'],['Poison'],62,67),
    "nidoqueen":Pokemon("Nidoqueen",90,['poison_sting', 'acid', 'stomp'],['Poison', 'Ground'],92,87),
    "nidoran♂":Pokemon("Nidoran♂",46,['poison_sting', 'take_down'],['Poison'],57,40),
    "nidorino":Pokemon("Nidorino",61,['poison_sting', 'fury_attack'],['Poison'],72,57),
    "nidoking":Pokemon("Nidoking",81,['acid', 'poison_sting', 'take_down', 'double-edge'],['Poison', 'Ground'],102,77),
    "clefairy":Pokemon("Clefairy",70,['wrap', 'thrash', 'tackle', 'vice_grip'],['Fairy'],45,48),
    "clefable":Pokemon("Clefable",95,['stomp', 'razor_wind', 'vice_grip'],['Fairy'],70,73),
    "vulpix":Pokemon("Vulpix",38,['flamethrower', 'pound'],['Fire'],41,40),
    "ninetales":Pokemon("Ninetales",73,['ember', 'fire_punch', 'wrap', 'pay_day'],['Fire'],76,75),
    "jigglypuff":Pokemon("Jigglypuff",115,['double_slap', 'comet_punch'],['Normal', 'Fairy'],45,20),
    "wigglytuff":Pokemon("Wigglytuff",140,['take_down', 'vice_grip'],['Normal', 'Fairy'],70,45),
    "zubat":Pokemon("Zubat",40,['acid', 'cut', 'body_slam'],['Poison', 'Flying'],45,35),
    "golbat":Pokemon("Golbat",75,['acid', 'poison_sting'],['Poison', 'Flying'],80,70),
    "oddish":Pokemon("Oddish",45,['vine_whip', 'acid', 'mega_kick', 'comet_punch'],['Grass', 'Poison'],50,55),
    "gloom":Pokemon("Gloom",60,['poison_sting', 'acid', 'comet_punch'],['Grass', 'Poison'],65,70),
    "vileplume":Pokemon("Vileplume",75,['poison_sting', 'acid', 'slam'],['Grass', 'Poison'],80,85),
    "paras":Pokemon("Paras",35,['twineedle', 'pin_missile', 'bind'],['Bug', 'Grass'],70,55),
    "parasect":Pokemon("Parasect",60,['pin_missile', 'twineedle', 'slam'],['Bug', 'Grass'],95,80),
    "venonat":Pokemon("Venonat",60,['twineedle', 'pin_missile', 'take_down', 'slam'],['Bug', 'Poison'],55,50),
    "venomoth":Pokemon("Venomoth",70,['poison_sting', 'twineedle', 'tackle'],['Bug', 'Poison'],65,60),
    "diglett":Pokemon("Diglett",10,['tackle', 'comet_punch', 'mega_punch'],['Ground'],55,25),
    "dugtrio":Pokemon("Dugtrio",35,['double_slap', 'take_down', 'scratch'],['Ground'],100,50),
    "meowth":Pokemon("Meowth",40,['double-edge', 'mega_kick', 'bind', 'razor_wind'],['Normal'],45,35),
    "persian":Pokemon("Persian",65,['take_down', 'mega_kick', 'cut'],['Normal'],70,60),
    "psyduck":Pokemon("Psyduck",50,['surf', 'water_gun', 'pound'],['Water'],52,48),
    "golduck":Pokemon("Golduck",80,['surf'],['Water'],82,78),
    "mankey":Pokemon("Mankey",40,['wing_attack', 'double_kick'],['Fighting'],80,35),
    "primeape":Pokemon("Primeape",65,['wing_attack', 'double_kick', 'body_slam', 'horn_attack'],['Fighting'],105,60),
    "growlithe":Pokemon("Growlithe",55,['flamethrower', 'ember'],['Fire'],70,45),
    "arcanine":Pokemon("Arcanine",90,['ember', 'comet_punch', 'vice_grip'],['Fire'],110,80),
    "poliwag":Pokemon("Poliwag",40,['surf', 'water_gun'],['Water'],50,40),
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
    "fury_attack":PokeMoves("Fury Attack",15,"Normal"),
    "tackle":PokeMoves("Tackle",50,"Normal"),
    "body_slam":PokeMoves("Body Slam",85,"Normal"),
    "wrap":PokeMoves("Wrap",15,"Normal"),
    "take_down":PokeMoves("Take Down",90,"Normal"),
    "thrash":PokeMoves("Thrash",120,"Normal"),
    "double-edge":PokeMoves("Double-Edge",120,"Normal"),
    "poison_sting":PokeMoves("Poison Sting",15,"Poison"),
    "twineedle":PokeMoves("Twineedle",25,"Bug"),
    "pin_missile":PokeMoves("Pin Missile",25,"Bug"),
    "bite":PokeMoves("Bite",60,"Dark"),
    "acid":PokeMoves("Acid",40,"Poison"),
    "ember":PokeMoves("Ember",40,"Fire"),
    "flamethrower":PokeMoves("Flamethrower",90,"Fire"),
    "water_gun":PokeMoves("Water Gun",40,"Water"),
    "hydro_pump":PokeMoves("Hydro Pump",110,"Water"),
    "surf":PokeMoves("Surf",90,"Water"),
    "ice_beam":PokeMoves("Ice Beam",90,"Ice"),
    "blizzard":PokeMoves("Blizzard",110,"Ice"),
    "psybeam":PokeMoves("Psybeam",65,"Psychic"),
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