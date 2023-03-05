#created by Ben Keil

#credit to https://github.com/fanzeyi/pokemon.json for pokemon information!
# go to https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json and copy everything, put in a file in the same directory as this one, and name that new file pokedex.json
# go to https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/moves.json and copy everything, put in a file in the same directory as this one, and name that new file movedex.json
#Only run this ONCE!

import json
import random

#creates a file named pokedex.py with AMOUNT different pokemon and moves, use to rapidly add pokemon and move objects
AMOUNT = 30

#opening files
newfile = open("pokedex.py", "w")
p = open("pokedex.json")
pfile = json.load(p)
m = open("movedex.json")
mfile = json.load(m)


#adds random moves to the new pokemon
def randomMoves():
  moves = []
  for i in range(random.randint(1, 4)):
    new_move = mfile[random.randrange(1, AMOUNT)]
    if new_move["power"] != None:
      move_name = new_move['ename'].lower().replace(' ', '_')
      if move_name not in moves:
        moves.append(move_name)
  return moves


#writing files
newfile.write("pokedex = {\n")
for i in pfile[:AMOUNT]:
  line = f"    \"{i['name']['english'].lower()}\":Pokemon(\"{i['name']['english']}\",{i['base']['HP']},{randomMoves()},{i['type']},{i['base']['Attack']},{i['base']['Defense']}),\n"
  newfile.write(line)
newfile.write("}\n\n")

newfile.write("movedex = {\n")
for i in mfile[:AMOUNT]:
  if (i['power'] == None):
    continue
  else:
    line = f"    \"{i['ename'].lower().replace(' ', '_')}\":PokeMoves(\"{i['ename']}\",{i['power']},\"{i['type']}\"),\n"
    newfile.write(line)
newfile.write("}")

#typedex // Copy this in!
typedex = {  #key: strength
  "Normal": ("None"),
  "Grass": ("Water", "Ground"),
  "Poison": ("Grass"),
  "Fire": ("Grass", "Ice", "Bug"),
  "Flying": ("Grass", "Fighting"),
  "Water": ("Fire", "Ground"),
  "Bug": ("Grass"),
  "Electric": ("Water", "Flying"),
  "Ground": ("Fire", "Electric", "Poison"),
  "Fighting": ("Normal", "Ice"),
  "Ice": ("Grass", "Ground", "Flying")
}

#closing files
m.close()
p.close()
newfile.close()