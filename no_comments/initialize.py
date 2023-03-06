import json
import random

AMOUNT = 30

newfile = open("pokedex.py", "w")
p = open("pokedex.json")
pfile = json.load(p)
m = open("movedex.json")
mfile = json.load(m)

def randomMoves():
  moves = []
  for i in range(random.randint(1, 4)):
    new_move = mfile[random.randrange(1, AMOUNT)]
    if new_move["power"] != None:
      move_name = new_move['ename'].lower().replace(' ', '_')
      if move_name not in moves:
        moves.append(move_name)
  return moves

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

typedex = {  
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

m.close()
p.close()
newfile.close()