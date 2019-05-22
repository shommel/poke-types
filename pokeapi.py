#responsible for retrieving all existing Pokemon and their types

import pokepy
import pickle as pk

client = pokepy.V2Client()

pokedexFull = False

i = 1
dex = {}
poke = client.get_pokemon(i) 

while not pokedexFull:
    
    dex.update({i: []})
    for t in poke.types:
        dex[i].append(t.type.name)
    i+=1
    
    try:
        poke = client.get_pokemon(i) #tries to get next pokemon in pokedex
    except:
        pokedexFull = True

pk.dump(dex, open("dex.p", "wb")) #pickling the completed dex
