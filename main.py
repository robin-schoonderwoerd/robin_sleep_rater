import math
from pyscript import Element


class pokemonRater():
    SPECIES_TO_SPECIALTY = {
        'Bulbasaur':'Ingredient', 'Ivysaur':'Ingredient', 'Venusaur':'Ingredient',
        'Charmander':'Ingredient', 'Charmeleon':'Ingredient', 'Charizard':'Ingredient',
        'Squirtle':'Ingredient', 'Wartortle':'Ingredient', 'Blastoise':'Ingredient',
        'Caterpie':'Berry', 'Metapod':'Berry', 'Butterfree':'Berry',
        'Rattata':'Berry', 'Raticate':'Berry','Ekans':'Berry', 
        'Arbok':'Berry','Pikachu':'Berry', 'Raichu':'Berry',
        'Pikachu - Halloween':'Berry','Pikachu - Holiday':'Skill','Clefairy':'Berry', 
        'Clefable':'Berry', 'Vulpix':'Berry', 'Ninetales':'Berry',
        'Jigglypuff':'Skill', 'Wigglytuff':'Skill',
        'Diglett':'Ingredient', 'Dugtrio':'Ingredient','Meowth':'Skill', 
        'Persian':'Skill', 'Psyduck':'Skill', 'Golduck':'Skill',
        'Mankey':'Berry', 'Primeape':'Berry','Growlithe':'Skill', 
        'Arcanine':'Skill','Bellsprout':'Ingredient', 'Weepinbell':'Ingredient', 
        'Victreebel':'Ingredient','Geodude':'Ingredient', 'Graveler':'Ingredient', 
        'Golem':'Ingredient', 'Slowpoke':'Ingredient', 'Slowbro':'Ingredient',
        'Magnemite':'Skill', 'Magneton':'Skill','Doduo':'Berry', 
        'Dodrio':'Berry','Gastly':'Ingredient', 'Haunter':'Ingredient', 
        'Gengar':'Ingredient','Onix':'Berry','Cubone':'Berry', 
        'Marowak':'Berry','Kangaskhan':'Ingredient','Mr. Mime':'Ingredient',
        'Pinsir':'Ingredient','Ditto':'Ingredient','Eevee':'Skill', 
        'Vaporeon':'Skill', 'Jolteon':'Skill', 'Flareon':'Skill',
        'Dratini':'Ingredient', 'Dragonair':'Ingredient','Dragonite':'Ingredient',
        'Chikorita':'Berry', 'Bayleef':'Berry', 'Meganium':'Berry',
        'Cyndaquil':'Berry', 'Quilava':'Berry', 'Typhlosion':'Berry',
        'Totodile':'Berry', 'Croconaw':'Berry', 'Feraligatr':'Berry',
        'Pichu':'Berry','Cleffa':'Berry','Igglybuff':'Skill',
        'Togepi':'Skill', 'Togetic':'Skill','Mareep':'Skill', 
        'Flaaffy':'Skill', 'Ampharos':'Skill','Sudowoodo':'Skill',
        'Wooper':'Ingredient', 'Quagsire':'Ingredient',
        'Espeon':'Skill', 'Umbreon':'Skill','Slowking':'Ingredient',
        'Wobbuffet':'Skill','Steelix':'Berry','Heracross':'Skill',
        'Sneasel':'Berry',
        'Delibird':'Ingredient','Houndour':'Berry', 'Houndoom':'Berry',
        'Raikou':'Skill', 'Entei':'Skill', 'Suicune': 'Skill',
        'Larvitar':'Ingredient', 'Pupitar':'Ingredient', 'Tyranitar':'Ingredient',
        'Ralts':'Skill', 'Kirlia':'Skill','Gardevoir':'Skill',
        'Aron':'Ingredient', 'Lairon':'Ingredient', 'Aggron':'Ingredient',
        'Slakoth':'Skill', 'Vigoroth':'Skill', 'Slaking':'Skill',
        'Sableye':'Skill','Gulpin':'Skill', 'Swalot':'Skill',
        'Swablu':'Berry', 'Altaria':'Berry','Shuppet':'Berry', 
        'Banette':'Berry', 'Absol':'Ingredient','Wynaut':'Skill',
        'Spheal':'Berry', 'Sealeo':'Berry', 'Walrein':'Berry',
        'Shinx':'Ingredient', 'Luxio':'Ingredient', 'Luxray':'Ingredient',
        'Drifloon':'Skill', 'Drifblim':'Skill',
        'Bonsly':'Skill','Mime Jr.':'Ingredient','Riolu':'Skill', 
        'Lucario':'Skill','Croagunk':'Ingredient', 'Toxicroak':'Ingredient',
        'Snover':'Ingredient', 'Abomasnow':'Ingredient', 'Weavile':'Berry',
        'Magnezone':'Skill',
        'Togekiss':'Skill','Leafeon':'Skill', 'Glaceon':'Skill',
        'Gallade':'Skill', 'Sylveon':'Skill', 'Dedenne':'Skill',
        'Grubbin':'Ingredient', 'Charjabug':'Ingredient', 'Vikavolt':'Ingredient',
        'Stufful':'Ingredient','Bewear':'Ingredient', 'Comfey':'Ingredient',
        'Mimikyu':'Skill', 'Cramorant':'Ingredient',
        'Sprigatito':'Ingredient','Floragato':'Ingredient', 'Meowscarada':'Ingredient',
        'Fuecoco':'Ingredient','Crocalor':'Ingredient', 'Skeledirge':'Ingredient',
        'Quaxly':'Ingredient','Quaxwell':'Ingredient', 'Quaquaval':'Ingredient'
    }

    SPECIALTY_CODES = {
        'Berry': 0,
        'Ingredient': 1,
        'Skill': 2,
        'Allrounder': 3
    }

    NATURE_PER_SPECIALTY = {
        'Adamant': [1.0, 0.1, 0.7, 0.4],
        'Bashful': [0.5, 0.5, 0.5, 0.5],
        'Bold': [0.0, 0.1, 0.1, 0.1],
        'Brave': [0.9, 0.5, 0.5, 0.5],
        'Calm': [0.0, 0.1, 0.6, 0.3],
        'Careful': [0.6, 0.1, 1.0, 0.4],
        'Docile': [0.5, 0.5, 0.5, 0.5],
        'Gentle': [0.5, 0.5, 0.9, 0.6],
        'Hardy': [0.5, 0.5, 0.5, 0.5],
        'Hasty': [0.5, 0.5, 0.5, 0.5],
        'Impish': [0.5, 0.0, 0.5, 0.5],
        'Jolly': [0.7, 0.1, 0.5, 0.2],
        'Lax': [0.5, 0.5, 0.0, 0.2],
        'Lonely': [0.9, 0.5, 0.5, 0.5],
        'Mild': [0.1, 0.9, 0.2, 1.0],
        'Modest': [0.0, 0.7, 0.1, 0.3],
        'Naive': [0.5, 0.5, 0.1, 0.2],
        'Naughty': [0.9, 0.7, 0.2, 0.5],
        'Quiet': [0.1, 1.0, 0.2, 0.9],
        'Quirky': [0.5, 0.5, 0.5, 0.5],
        'Rash': [0.1, 1.0, 0.0, 0.5],
        'Relaxed': [0.4, 0.4, 0.4, 0.4],
        'Sassy': [0.2, 0.2, 1.0, 0.6],
        'Serious': [0.5, 0.5, 0.5, 0.5],
        'Timid': [0.0, 0.1, 0.1, 0.1]
    }

    SUBSKILL_PER_SPECIALTY = {
        'Berry Finding S': [1.0, 0.6, 0.8, 0.8],
        'Dream Shard Bonus': [0.3, 0.6, 0.6, 0.6],
        'Energy Recovery Bonus': [0.2, 0.4, 0.4, 0.4],
        'Helping Bonus': [0.5, 1.0, 1.0, 1.0],
        'Helping Speed S': [0.4, 0.5, 0.6, 0.6],
        'Helping Speed M': [0.5, 0.7, 0.8, 0.8],
        'Ingredient Finder S': [0.0, 0.8, 0.0, 0.6],
        'Ingredient Finder M': [0.0, 1.0, 0.1, 0.7],
        'Inventory Up S': [0.1, 0.5, 0.3, 0.6],
        'Inventory Up M': [0.1, 0.6, 0.4, 0.7],
        'Inventory Up L': [0.1, 0.7, 0.5, 0.8],
        'Research EXP Bonus': [0.2, 0.4, 0.4, 0.4],
        'Skill Level Up S': [0.3, 0.5, 0.8, 0.7],
        'Skill Level Up M': [0.4, 0.6, 0.9, 0.8],
        'Skill Trigger S': [0.2, 0.4, 0.9, 0.7],
        'Skill Trigger M': [0.3, 0.5, 1, 0.8],
        'Sleep EXP Bonus': [0.3, 0.6, 0.6, 0.6]
    }

    SPECIES_TO_TIERLIST = {
        'Bulbasaur':0.8, 'Ivysaur':0.8, 'Venusaur':0.8,
        'Charmander':1.0, 'Charmeleon':1.0, 'Charizard':1.0,
        'Squirtle':1.0, 'Wartortle':1.0, 'Blastoise':1.0,
        'Caterpie':0.2, 'Metapod':0.2, 'Butterfree':0.2,
        'Rattata':0.2, 'Raticate':0.2,'Ekans':0.0, 
        'Arbok':0.0,'Pikachu':1.0, 'Raichu':1.0,
        'Pikachu - Halloween':0.4,'Pikachu - Holiday':0.0,
        'Clefairy':0.6, 'Clefable':0.6, 'Vulpix':0.8, 
        'Ninetales':0.8, 'Jigglypuff':0.4, 'Wigglytuff':0.4,
        'Diglett':0.2, 'Dugtrio':0.2,'Meowth':0.0, 
        'Persian':0.0, 'Psyduck':0.6, 'Golduck':0.6,
        'Mankey':0.6, 'Primeape':0.6,'Growlithe':0.4, 
        'Arcanine':0.4,'Bellsprout':0.8, 'Weepinbell':0.8, 
        'Victreebel':0.8,'Geodude':0.6, 'Graveler':0.6, 
        'Golem':0.6, 'Slowpoke':0.2, 'Slowbro':0.2,
        'Magnemite':0.8, 'Magneton':0.8,'Doduo':0.8, 
        'Dodrio':0.8,'Gastly':0.6, 'Haunter':0.6, 
        'Gengar':0.6,'Onix':0.8,'Cubone':0.2, 
        'Marowak':0.2,'Kangaskhan':0.2,'Mr. Mime':0.2,
        'Pinsir':0.8,'Ditto':0.2,'Eevee':0.8, 
        'Vaporeon':0.8, 'Jolteon':0.2, 'Flareon':0.8,
        'Dratini':1.0, 'Dragonair':1.0,'Dragonite':1.0,
        'Chikorita':1.0, 'Bayleef':1.0, 'Meganium':1.0,
        'Cyndaquil':1.0, 'Quilava':1.0, 'Typhlosion':1.0,
        'Totodile':1.0, 'Croconaw':1.0, 'Feraligatr':1.0,
        'Pichu':1.0,'Cleffa':0.6,'Igglybuff':0.4,
        'Togepi':0.2, 'Togetic':0.2,'Mareep':0.4, 
        'Flaaffy':0.4, 'Ampharos':0.4,'Sudowoodo':0.0,
        'Wooper':0.6, 'Quagsire':0.6,
        'Espeon':0.6, 'Umbreon':0.0,'Slowking':0.2,
        'Wobbuffet':0.0,'Steelix':1.0,'Heracross':0.4,
        'Sneasel':1.0,
        'Delibird':0.8,'Houndour':0.6, 'Houndoom':0.6,
        'Raikou':0.6, 'Entei':0.6, 'Suicune': 0.6,
        'Larvitar':1.0, 'Pupitar':1.0, 'Tyranitar':1.0,
        'Ralts':1.0, 'Kirlia':1.0,'Gardevoir':1.0,
        'Aron':0.8, 'Lairon': 0.8, 'Aggron':0.8,
        'Slakoth':0.6, 'Vigoroth':0.6, 'Slaking':0.6,
        'Sableye':0.0,'Gulpin':0.0, 'Swalot':0.0,
        'Swablu':0.2, 'Altaria':0.2,'Shuppet':0.4, 
        'Banette':0.4, 'Absol':0.4,'Wynaut':0.0,
        'Spheal':1.0, 'Sealeo':1.0, 'Walrein':1.0,
        'Shinx':0.6, 'Luxio': 0.6, 'Luxray': 0.6,
        'Drifloon':0.4, 'Drifblim':0.4,
        'Bonsly':0.0,'Mime Jr.':0.2,'Riolu':0.0, 
        'Lucario':0.0,'Croagunk':0.2, 'Toxicroak':0.2,
        'Snover':0.6, 'Abomasnow':0.6, 'Weavile':1.0,
        'Magnezone':0.8,
        'Togekiss':0.2,'Leafeon':0.2, 'Glaceon':0.8,
        'Gallade':0.6, 'Sylveon':0.8, 'Dedenne':0.8,
        'Grubbin':1.0, 'Charjabug':1.0, 'Vikavolt': 1.0,
        'Stufful':1.0,'Bewear':1.0, 'Comfey':0.4,
        'Mimikyu':0.6, 'Cramorant':0.6,
        'Sprigatito':0.8,'Floragato':0.8, 'Meowscarada':0.8,
        'Fuecoco':0.4,'Crocalor':0.4, 'Skeledirge':0.4,
        'Quaxly':0.8,'Quaxwell':0.8, 'Quaquaval':0.8
    }

    ING_COMBI_RATINGS = {
        'Bulbasaur|Honey|Honey': 1.0,
        'Bulbasaur|Honey|Snoozy Tomato': 0.2,
        'Bulbasaur|Honey|Soft Potato': 0.2,
        'Bulbasaur|Snoozy Tomato|Honey': 0.2,
        'Bulbasaur|Snoozy Tomato|Snoozy Tomato': 0.2,
        'Bulbasaur|Snoozy Tomato|Soft Potato': 0.4,
        'Ivysaur|Honey|Honey': 1.0,
        'Ivysaur|Honey|Snoozy Tomato': 0.2,
        'Ivysaur|Honey|Soft Potato': 0.2,
        'Ivysaur|Snoozy Tomato|Honey': 0.2,
        'Ivysaur|Snoozy Tomato|Snoozy Tomato': 0.2,
        'Ivysaur|Snoozy Tomato|Soft Potato': 0.4,
        'Venusaur|Honey|Honey': 1.0,
        'Venusaur|Honey|Snoozy Tomato': 0.2,
        'Venusaur|Honey|Soft Potato': 0.2,
        'Venusaur|Snoozy Tomato|Honey': 0.2,
        'Venusaur|Snoozy Tomato|Snoozy Tomato': 0.2,
        'Venusaur|Snoozy Tomato|Soft Potato': 0.4,
        'Charmander|Bean Sausage|Bean Sausage': 1.0,
        'Charmander|Bean Sausage|Warming Ginger': 0.4,
        'Charmander|Bean Sausage|Fiery Herb': 0.6,
        'Charmander|Warming Ginger|Bean Sausage': 1.0,
        'Charmander|Warming Ginger|Warming Ginger': 0.2,
        'Charmander|Warming Ginger|Fiery Herb': 1.0,
        'Charmeleon|Bean Sausage|Bean Sausage': 1.0,
        'Charmeleon|Bean Sausage|Warming Ginger': 0.4,
        'Charmeleon|Bean Sausage|Fiery Herb': 0.6,
        'Charmeleon|Warming Ginger|Bean Sausage': 1.0,
        'Charmeleon|Warming Ginger|Warming Ginger': 0.2,
        'Charmeleon|Warming Ginger|Fiery Herb': 1.0,
        'Charizard|Bean Sausage|Bean Sausage': 1.0,
        'Charizard|Bean Sausage|Warming Ginger': 0.4,
        'Charizard|Bean Sausage|Fiery Herb': 0.6,
        'Charizard|Warming Ginger|Bean Sausage': 1.0,
        'Charizard|Warming Ginger|Warming Ginger': 0.2,
        'Charizard|Warming Ginger|Fiery Herb': 1.0,
        'Squirtle|Moomoo Milk|Moomoo Milk': 1.0,
        'Squirtle|Moomoo Milk|Soothing Cacao': 1.0,
        'Squirtle|Moomoo Milk|Bean Sausage': 0.2,
        'Squirtle|Soothing Cacao|Moomoo Milk': 0.4,
        'Squirtle|Soothing Cacao|Soothing Cacao': 0.8,
        'Squirtle|Soothing Cacao|Bean Sausage': 0.0,
        'Wartortle|Moomoo Milk|Moomoo Milk': 1.0,
        'Wartortle|Moomoo Milk|Soothing Cacao': 1.0,
        'Wartortle|Moomoo Milk|Bean Sausage': 0.2,
        'Wartortle|Soothing Cacao|Moomoo Milk': 0.4,
        'Wartortle|Soothing Cacao|Soothing Cacao': 0.8,
        'Wartortle|Soothing Cacao|Bean Sausage': 0.0,
        'Blastoise|Moomoo Milk|Moomoo Milk': 1.0,
        'Blastoise|Moomoo Milk|Soothing Cacao': 1.0,
        'Blastoise|Moomoo Milk|Bean Sausage': 0.2,
        'Blastoise|Soothing Cacao|Moomoo Milk': 0.4,
        'Blastoise|Soothing Cacao|Soothing Cacao': 0.8,
        'Blastoise|Soothing Cacao|Bean Sausage': 0.0,
        'Diglett|Snoozy Tomato|Snoozy Tomato': 0.4,
        'Diglett|Snoozy Tomato|Large Leek': 0.6,
        'Diglett|Snoozy Tomato|Greengrass Soybeans': 0.8,
        'Diglett|Large Leek|Snoozy Tomato': 0.4,
        'Diglett|Large Leek|Large Leek': 1.0,
        'Diglett|Large Leek|Greengrass Soybeans': 0.2,
        'Dugtrio|Snoozy Tomato|Snoozy Tomato': 0.4,
        'Dugtrio|Snoozy Tomato|Large Leek': 0.6,
        'Dugtrio|Snoozy Tomato|Greengrass Soybeans': 0.8,
        'Dugtrio|Large Leek|Snoozy Tomato': 0.4,
        'Dugtrio|Large Leek|Large Leek': 1.0,
        'Dugtrio|Large Leek|Greengrass Soybeans': 0.2,
        'Bellsprout|Snoozy Tomato|Snoozy Tomato': 0.8,
        'Bellsprout|Snoozy Tomato|Soft Potato': 1.0,
        'Bellsprout|Snoozy Tomato|Large Leek': 0.4,
        'Bellsprout|Soft Potato|Snoozy Tomato': 0.4,
        'Bellsprout|Soft Potato|Soft Potato': 0.8,
        'Bellsprout|Soft Potato|Large Leek': 0.4,
        'Weepinbell|Snoozy Tomato|Snoozy Tomato': 0.8,
        'Weepinbell|Snoozy Tomato|Soft Potato': 1.0,
        'Weepinbell|Snoozy Tomato|Large Leek': 0.4,
        'Weepinbell|Soft Potato|Snoozy Tomato': 0.4,
        'Weepinbell|Soft Potato|Soft Potato': 0.8,
        'Weepinbell|Soft Potato|Large Leek': 0.4,
        'Victreebel|Snoozy Tomato|Snoozy Tomato': 0.8,
        'Victreebel|Snoozy Tomato|Soft Potato': 1.0,
        'Victreebel|Snoozy Tomato|Large Leek': 0.4,
        'Victreebel|Soft Potato|Snoozy Tomato': 0.4,
        'Victreebel|Soft Potato|Soft Potato': 0.8,
        'Victreebel|Soft Potato|Large Leek': 0.4,
        'Geodude|Greengrass Soybeans|Greengrass Soybeans': 1.0,
        'Geodude|Greengrass Soybeans|Soft Potato': 0.2,
        'Geodude|Greengrass Soybeans|Tasty Mushroom': 1.0,
        'Geodude|Soft Potato|Greengrass Soybeans': 0.2,
        'Geodude|Soft Potato|Soft Potato': 0.6,
        'Geodude|Soft Potato|Tasty Mushroom': 0.8,
        'Graveler|Greengrass Soybeans|Greengrass Soybeans': 1.0,
        'Graveler|Greengrass Soybeans|Soft Potato': 0.2,
        'Graveler|Greengrass Soybeans|Tasty Mushroom': 1.0,
        'Graveler|Soft Potato|Greengrass Soybeans': 0.2,
        'Graveler|Soft Potato|Soft Potato': 0.6,
        'Graveler|Soft Potato|Tasty Mushroom': 0.8,
        'Golem|Greengrass Soybeans|Greengrass Soybeans': 1.0,
        'Golem|Greengrass Soybeans|Soft Potato': 0.2,
        'Golem|Greengrass Soybeans|Tasty Mushroom': 1.0,
        'Golem|Soft Potato|Greengrass Soybeans': 0.2,
        'Golem|Soft Potato|Soft Potato': 0.6,
        'Golem|Soft Potato|Tasty Mushroom': 0.8,
        'Slowpoke|Soothing Cacao|Soothing Cacao': 0.0,
        'Slowpoke|Soothing Cacao|Slowpoke Tail': 0.4,
        'Slowpoke|Soothing Cacao|Snoozy Tomato': 0.0,
        'Slowpoke|Slowpoke Tail|Soothing Cacao': 0.4,
        'Slowpoke|Slowpoke Tail|Slowpoke Tail': 1.0,
        'Slowpoke|Slowpoke Tail|Snoozy Tomato': 0.4,
        'Slowbro|Soothing Cacao|Soothing Cacao': 0.0,
        'Slowbro|Soothing Cacao|Slowpoke Tail': 0.4,
        'Slowbro|Soothing Cacao|Snoozy Tomato': 0.0,
        'Slowbro|Slowpoke Tail|Soothing Cacao': 0.4,
        'Slowbro|Slowpoke Tail|Slowpoke Tail': 1.0,
        'Slowbro|Slowpoke Tail|Snoozy Tomato': 0.4,
        'Gastly|Fiery Herb|Fiery Herb': 0.8,
        'Gastly|Fiery Herb|Tasty Mushroom': 0.2,
        'Gastly|Fiery Herb|Pure Oil': 0.6,
        'Gastly|Tasty Mushroom|Fiery Herb': 0.2,
        'Gastly|Tasty Mushroom|Tasty Mushroom': 1.0,
        'Gastly|Tasty Mushroom|Pure Oil': 0.2,
        'Haunter|Fiery Herb|Fiery Herb': 0.8,
        'Haunter|Fiery Herb|Tasty Mushroom': 0.2,
        'Haunter|Fiery Herb|Pure Oil': 0.6,
        'Haunter|Tasty Mushroom|Fiery Herb': 0.2,
        'Haunter|Tasty Mushroom|Tasty Mushroom': 1.0,
        'Haunter|Tasty Mushroom|Pure Oil': 0.2,
        'Gengar|Fiery Herb|Fiery Herb': 0.8,
        'Gengar|Fiery Herb|Tasty Mushroom': 0.2,
        'Gengar|Fiery Herb|Pure Oil': 0.6,
        'Gengar|Tasty Mushroom|Fiery Herb': 0.2,
        'Gengar|Tasty Mushroom|Tasty Mushroom': 1.0,
        'Gengar|Tasty Mushroom|Pure Oil': 0.2,
        'Kangaskhan|Warming Ginger|Warming Ginger': 0.8,
        'Kangaskhan|Warming Ginger|Soft Potato': 0.2,
        'Kangaskhan|Warming Ginger|Greengrass Soybeans': 1.0,
        'Kangaskhan|Soft Potato|Warming Ginger': 0.2,
        'Kangaskhan|Soft Potato|Soft Potato': 0.2,
        'Kangaskhan|Soft Potato|Greengrass Soybeans': 0.2,
        'Mr. Mime|Snoozy Tomato|Snoozy Tomato': 0.8,
        'Mr. Mime|Snoozy Tomato|Soft Potato': 1.0,
        'Mr. Mime|Snoozy Tomato|Large Leek': 0.4,
        'Mr. Mime|Soft Potato|Snoozy Tomato': 0.2,
        'Mr. Mime|Soft Potato|Soft Potato': 0.6,
        'Mr. Mime|Soft Potato|Large Leek': 0.4,
        'Pinsir|Honey|Honey': 0.6,
        'Pinsir|Honey|Fancy Apple': 1.0,
        'Pinsir|Honey|Bean Sausage': 0.0,
        'Pinsir|Fancy Apple|Honey': 0.8,
        'Pinsir|Fancy Apple|Fancy Apple': 0.4,
        'Pinsir|Fancy Apple|Bean Sausage': 0.0,
        'Ditto|Pure Oil|Pure Oil': 0.2,
        'Ditto|Pure Oil|Large Leek': 0.2,
        'Ditto|Pure Oil|Slowpoke Tail': 0.8,
        'Ditto|Large Leek|Pure Oil': 0.2,
        'Ditto|Large Leek|Large Leek': 0.8,
        'Ditto|Large Leek|Slowpoke Tail': 1.0,
        'Dratini|Fiery Herb|Fiery Herb':1.0,
        'Dratini|Fiery Herb|Greengrass Corn':1.0,
        'Dratini|Fiery Herb|Pure Oil':0.6,
        'Dratini|Greengrass Corn|Fiery Herb':1.0,
        'Dratini|Greengrass Corn|Greengrass Corn':0.6,
        'Dratini|Greengrass Corn|Pure Oil':1.0,
        'Dragonair|Fiery Herb|Fiery Herb':1.0,
        'Dragonair|Fiery Herb|Greengrass Corn':1.0,
        'Dragonair|Fiery Herb|Pure Oil':0.6,
        'Dragonair|Greengrass Corn|Fiery Herb':1.0,
        'Dragonair|Greengrass Corn|Greengrass Corn':0.6,
        'Dragonair|Greengrass Corn|Pure Oil':1.0,
        'Dragonite|Fiery Herb|Fiery Herb':1.0,
        'Dragonite|Fiery Herb|Greengrass Corn':1.0,
        'Dragonite|Fiery Herb|Pure Oil':0.6,
        'Dragonite|Greengrass Corn|Fiery Herb':1.0,
        'Dragonite|Greengrass Corn|Greengrass Corn':0.6,
        'Dragonite|Greengrass Corn|Pure Oil':1.0,
        'Wooper|Tasty Mushroom|Tasty Mushroom':1.0,
        'Wooper|Tasty Mushroom|Soft Potato':0.8,
        'Wooper|Tasty Mushroom|Bean Sausage':0.4,
        'Wooper|Soft Potato|Tasty Mushroom':0.8,
        'Wooper|Soft Potato|Soft Potato':0.2,
        'Wooper|Soft Potato|Bean Sausage':0.4,
        'Quagsire|Tasty Mushroom|Tasty Mushroom':1.0,
        'Quagsire|Tasty Mushroom|Soft Potato':0.8,
        'Quagsire|Tasty Mushroom|Bean Sausage':0.4,
        'Quagsire|Soft Potato|Tasty Mushroom':0.8,
        'Quagsire|Soft Potato|Soft Potato':0.2,
        'Quagsire|Soft Potato|Bean Sausage':0.4,
        'Slowking|Soothing Cacao|Soothing Cacao': 0.0,
        'Slowking|Soothing Cacao|Slowpoke Tail': 0.4,
        'Slowking|Soothing Cacao|Snoozy Tomato': 0.0,
        'Slowking|Slowpoke Tail|Soothing Cacao': 0.4,
        'Slowking|Slowpoke Tail|Slowpoke Tail': 1.0,
        'Slowking|Slowpoke Tail|Snoozy Tomato': 0.4,
        'Delibird|Fancy Egg|Fancy Egg': 1.0,
        'Delibird|Fancy Egg|Fancy Apple': 0.8,
        'Delibird|Fancy Egg|Soothing Cacao': 0.6,
        'Delibird|Fancy Apple|Fancy Egg': 0.8,
        'Delibird|Fancy Apple|Fancy Apple': 0.4,
        'Delibird|Fancy Apple|Soothing Cacao': 0.4,
        'Larvitar|Warming Ginger|Warming Ginger': 1.0,
        'Larvitar|Warming Ginger|Greengrass Soybeans': 0.8,
        'Larvitar|Warming Ginger|Bean Sausage': 1.0,
        'Larvitar|Greengrass Soybeans|Warming Ginger': 0.4,
        'Larvitar|Greengrass Soybeans|Greengrass Soybeans': 0.6,
        'Larvitar|Greengrass Soybeans|Bean Sausage': 0.6,
        'Pupitar|Warming Ginger|Warming Ginger': 1.0,
        'Pupitar|Warming Ginger|Greengrass Soybeans': 0.8,
        'Pupitar|Warming Ginger|Bean Sausage': 1.0,
        'Pupitar|Greengrass Soybeans|Warming Ginger': 0.4,
        'Pupitar|Greengrass Soybeans|Greengrass Soybeans': 0.6,
        'Pupitar|Greengrass Soybeans|Bean Sausage': 0.6,
        'Tyranitar|Warming Ginger|Warming Ginger': 1.0,
        'Tyranitar|Warming Ginger|Greengrass Soybeans': 0.8,
        'Tyranitar|Warming Ginger|Bean Sausage': 1.0,
        'Tyranitar|Greengrass Soybeans|Warming Ginger': 0.4,
        'Tyranitar|Greengrass Soybeans|Greengrass Soybeans': 0.6,
        'Tyranitar|Greengrass Soybeans|Bean Sausage': 0.6,
        'Aron|Bean Sausage|Bean Sausage': 0.6,
        'Aron|Bean Sausage|Rousing Coffee': 1.0,
        'Aron|Bean Sausage|Greengrass Soybeans': 0.4,
        'Aron|Rousing Coffee|Bean Sausage': 0.4,
        'Aron|Rousing Coffee|Rousing Coffee': 0.8,
        'Aron|Rousing Coffee|Greengrass Soybeans': 1.0,
        'Lairon|Bean Sausage|Bean Sausage': 0.6,
        'Lairon|Bean Sausage|Rousing Coffee': 1.0,
        'Lairon|Bean Sausage|Greengrass Soybeans': 0.4,
        'Lairon|Rousing Coffee|Bean Sausage': 0.4,
        'Lairon|Rousing Coffee|Rousing Coffee': 0.8,
        'Lairon|Rousing Coffee|Greengrass Soybeans': 1.0,
        'Aggron|Bean Sausage|Bean Sausage': 0.6,
        'Aggron|Bean Sausage|Rousing Coffee': 1.0,
        'Aggron|Bean Sausage|Greengrass Soybeans': 0.4,
        'Aggron|Rousing Coffee|Bean Sausage': 0.4,
        'Aggron|Rousing Coffee|Rousing Coffee': 0.8,
        'Aggron|Rousing Coffee|Greengrass Soybeans': 1.0,
        'Absol|Soothing Cacao|Soothing Cacao': 1.0,
        'Absol|Soothing Cacao|Fancy Apple': 0.6,
        'Absol|Soothing Cacao|Tasty Mushroom': 0.2,
        'Absol|Fancy Apple|Soothing Cacao': 0.8,
        'Absol|Fancy Apple|Fancy Apple': 0.4,
        'Absol|Fancy Apple|Tasty Mushroom': 0.8,
        'Shinx|Snoozy Tomato|Snoozy Tomato': 0.4, 
        'Shinx|Snoozy Tomato|Pure Oil': 1.0,
        'Shinx|Snoozy Tomato|Rousing Coffee': 0.8,
        'Shinx|Pure Oil|Snoozy Tomato': 0.6,
        'Shinx|Pure Oil|Pure Oil': 0.4,
        'Shinx|Pure Oil|Rousing Coffee': 0.4,
        'Luxio|Snoozy Tomato|Snoozy Tomato': 0.4,
        'Luxio|Snoozy Tomato|Pure Oil': 1.0,
        'Luxio|Snoozy Tomato|Rousing Coffee': 0.8,
        'Luxio|Pure Oil|Snoozy Tomato': 0.6,
        'Luxio|Pure Oil|Pure Oil': 0.4,
        'Luxio|Pure Oil|Rousing Coffee': 0.4,
        'Luxray|Snoozy Tomato|Snoozy Tomato': 0.4,
        'Luxray|Snoozy Tomato|Pure Oil': 1.0,
        'Luxray|Snoozy Tomato|Rousing Coffee': 0.8,
        'Luxray|Pure Oil|Snoozy Tomato': 0.6,
        'Luxray|Pure Oil|Pure Oil': 0.4,
        'Luxray|Pure Oil|Rousing Coffee': 0.4,
        'Mime Jr.|Snoozy Tomato|Snoozy Tomato': 0.8,
        'Mime Jr.|Snoozy Tomato|Soft Potato': 1.0,
        'Mime Jr.|Snoozy Tomato|Large Leek': 0.4,
        'Mime Jr.|Soft Potato|Snoozy Tomato': 0.2,
        'Mime Jr.|Soft Potato|Soft Potato': 0.6,
        'Mime Jr.|Soft Potato|Large Leek': 0.4,
        'Croagunk|Pure Oil|Pure Oil': 1.0,
        'Croagunk|Pure Oil|Bean Sausage': 0.6,
        'Croagunk|Bean Sausage|Pure Oil': 0.2,
        'Croagunk|Bean Sausage|Bean Sausage': 0.2,
        'Toxicroak|Pure Oil|Pure Oil': 1.0,
        'Toxicroak|Pure Oil|Bean Sausage': 0.6,
        'Toxicroak|Bean Sausage|Pure Oil': 0.2,
        'Toxicroak|Bean Sausage|Bean Sausage': 0.2,
        'Snover|Snoozy Tomato|Snoozy Tomato': 0.8,
        'Snover|Snoozy Tomato|Fancy Egg': 0.8,
        'Snover|Snoozy Tomato|Tasty Mushroom': 1.0,
        'Snover|Fancy Egg|Snoozy Tomato': 0.2,
        'Snover|Fancy Egg|Fancy Egg': 0.6,
        'Snover|Fancy Egg|Tasty Mushroom': 0.2,
        'Abomasnow|Snoozy Tomato|Snoozy Tomato': 0.8,
        'Abomasnow|Snoozy Tomato|Fancy Egg': 0.8,
        'Abomasnow|Snoozy Tomato|Tasty Mushroom': 1.0,
        'Abomasnow|Fancy Egg|Snoozy Tomato': 0.2,
        'Abomasnow|Fancy Egg|Fancy Egg': 0.6,
        'Abomasnow|Fancy Egg|Tasty Mushroom': 0.2,
        'Grubbin|Rousing Coffee|Rousing Coffee': 1.0,
        'Grubbin|Rousing Coffee|Tasty Mushroom': 1.0,
        'Grubbin|Rousing Coffee|Honey': 1.0,
        'Grubbin|Tasty Mushroom|Rousing Coffee': 0.6,
        'Grubbin|Tasty Mushroom|Tasty Mushroom': 0.6,
        'Grubbin|Tasty Mushroom|Honey': 0.2,
        'Charjabug|Rousing Coffee|Rousing Coffee': 1.0,
        'Charjabug|Rousing Coffee|Tasty Mushroom': 1.0,
        'Charjabug|Rousing Coffee|Honey': 1.0,
        'Charjabug|Tasty Mushroom|Rousing Coffee': 0.6,
        'Charjabug|Tasty Mushroom|Tasty Mushroom': 0.6,
        'Charjabug|Tasty Mushroom|Honey': 0.2,
        'Vikavolt|Rousing Coffee|Rousing Coffee': 1.0,
        'Vikavolt|Rousing Coffee|Tasty Mushroom': 1.0,
        'Vikavolt|Rousing Coffee|Honey': 1.0,
        'Vikavolt|Tasty Mushroom|Rousing Coffee': 0.6,
        'Vikavolt|Tasty Mushroom|Tasty Mushroom': 0.6,
        'Vikavolt|Tasty Mushroom|Honey': 0.2,
        'Stufful|Greengrass Corn|Greengrass Corn':1.0,
        'Stufful|Greengrass Corn|Bean Sausage':0.8,
        'Stufful|Greengrass Corn|Fancy Egg':0.2,
        'Stufful|Bean Sausage|Greengrass Corn':0.4,
        'Stufful|Bean Sausage|Bean Sausage':0.2,
        'Stufful|Bean Sausage|Fancy Egg':0.6,
        'Bewear|Greengrass Corn|Greengrass Corn':1.0,
        'Bewear|Greengrass Corn|Bean Sausage':0.8,
        'Bewear|Greengrass Corn|Fancy Egg':0.2,
        'Bewear|Bean Sausage|Greengrass Corn':0.4,
        'Bewear|Bean Sausage|Bean Sausage':0.2,
        'Bewear|Bean Sausage|Fancy Egg':0.6,
        'Comfey|Greengrass Corn|Greengrass Corn':0.8,
        'Comfey|Greengrass Corn|Warming Ginger':1.0,
        'Comfey|Greengrass Corn|Soothing Cacao':0.4,
        'Comfey|Warming Ginger|Greengrass Corn':0.8,
        'Comfey|Warming Ginger|Warming Ginger':0.2,
        'Comfey|Warming Ginger|Soothing Cacao':0.4,
        'Cramorant|Pure Oil|Pure Oil':1.0,
        'Cramorant|Pure Oil|Soft Potato':1.0,
        'Cramorant|Pure Oil|Fancy Egg':0.4,
        'Cramorant|Soft Potato|Pure Oil':0.8,
        'Cramorant|Soft Potato|Soft Potato':0.2,
        'Cramorant|Soft Potato|Fancy Egg':0.4,
        'Sprigatito|Soft Potato|Soft Potato':1.0,
        'Sprigatito|Soft Potato|Moomoo Milk':0.8,
        'Sprigatito|Soft Potato|Warming Ginger':0.2,
        'Sprigatito|Moomoo Milk|Soft Potato':0.8,
        'Sprigatito|Moomoo Milk|Moomoo Milk':0.0,
        'Sprigatito|Moomoo Milk|Warming Ginger':0.4,
        'Floragato|Soft Potato|Soft Potato':1.0,
        'Floragato|Soft Potato|Moomoo Milk':0.8,
        'Floragato|Soft Potato|Warming Ginger':0.2,
        'Floragato|Moomoo Milk|Soft Potato':0.8,
        'Floragato|Moomoo Milk|Moomoo Milk':0.0,
        'Floragato|Moomoo Milk|Warming Ginger':0.4,
        'Meowscarada|Soft Potato|Soft Potato':1.0,
        'Meowscarada|Soft Potato|Moomoo Milk':0.8,
        'Meowscarada|Soft Potato|Warming Ginger':0.2,
        'Meowscarada|Moomoo Milk|Soft Potato':0.8,
        'Meowscarada|Moomoo Milk|Moomoo Milk':0.0,
        'Meowscarada|Moomoo Milk|Warming Ginger':0.4,
        'Fuecoco|Fancy Apple|Fancy Apple':1.0,
        'Fuecoco|Fancy Apple|Bean Sausage':0.2,
        'Fuecoco|Fancy Apple|Fiery Herb':0.6,
        'Fuecoco|Bean Sausage|Fancy Apple':0.2,
        'Fuecoco|Bean Sausage|Bean Sausage':0.0,
        'Fuecoco|Bean Sausage|Fiery Herb':0.4,
        'Crocalor|Fancy Apple|Fancy Apple':1.0,
        'Crocalor|Fancy Apple|Bean Sausage':0.2,
        'Crocalor|Fancy Apple|Fiery Herb':0.6,
        'Crocalor|Bean Sausage|Fancy Apple':0.2,
        'Crocalor|Bean Sausage|Bean Sausage':0.0,
        'Crocalor|Bean Sausage|Fiery Herb':0.4,
        'Skeledirge|Fancy Apple|Fancy Apple':1.0,
        'Skeledirge|Fancy Apple|Bean Sausage':0.2,
        'Skeledirge|Fancy Apple|Fiery Herb':0.6,
        'Skeledirge|Bean Sausage|Fancy Apple':0.2,
        'Skeledirge|Bean Sausage|Bean Sausage':0.0,
        'Skeledirge|Bean Sausage|Fiery Herb':0.4,
        'Quaxly|Greengrass Soybeans|Greengrass Soybeans':0.0,
        'Quaxly|Greengrass Soybeans|Large Leek':1.0,
        'Quaxly|Greengrass Soybeans|Pure Oil':0.8,
        'Quaxly|Large Leek|Greengrass Soybeans':0.2,
        'Quaxly|Large Leek|Large Leek':1.0,
        'Quaxly|Large Leek|Pure Oil':0.2,
        'Quaxwell|Greengrass Soybeans|Greengrass Soybeans':0.0,
        'Quaxwell|Greengrass Soybeans|Large Leek':1.0,
        'Quaxwell|Greengrass Soybeans|Pure Oil':0.8,
        'Quaxwell|Large Leek|Greengrass Soybeans':0.2,
        'Quaxwell|Large Leek|Large Leek':1.0,
        'Quaxwell|Large Leek|Pure Oil':0.2,
        'Quaquaval|Greengrass Soybeans|Greengrass Soybeans':0.0,
        'Quaquaval|Greengrass Soybeans|Large Leek':1.0,
        'Quaquaval|Greengrass Soybeans|Pure Oil':0.8,
        'Quaquaval|Large Leek|Greengrass Soybeans':0.2,
        'Quaquaval|Large Leek|Large Leek':1.0,
        'Quaquaval|Large Leek|Pure Oil':0.2
    }

    SUBSKILL_UNLOCK_WEIGHTS = [1, 0.95, 0.85, 0.4, 0.2]

    RATING_WEIGHTS = [
        [0.2, 0.6, 0, 0.2],  # berry
        [0.2, 0.45, 0.2, 0.15],  # ingredient
        [0.2, 0.6, 0, 0.2],  # skill
        [0.1, 0.5, 0.2, 0.2]  # allrounder
    ]

    NATURE_XP_FACTOR = 0.3

    ING_SPECIES = [species for species, specialty in SPECIES_TO_SPECIALTY.items() if specialty == 'Ingredient']

    XP_HARD_SPECIES = [
        'Onix', 'Kangaskhan', 'Pinsir','Ditto', 'Dratini',
        'Dragonair', 'Dragonite','Steelix','Heracross', 'Sneasel',
        'Delibird', 'Raikou', 'Entei', 'Suicune',
        'Larvitar', 'Pupitar', 'Tyranitar', 
        'Absol', 'Weavile', 'Dedenne', 'Comfey', 'Mimikyu', 'Cramorant'
    ]

    XP_NATURE_UP = ['Timid', 'Hasty', 'Jolly', 'Naive']
    XP_NATURE_DOWN = ['Brave', 'Relaxed', 'Quiet', 'Sassy']

    def __init__(self, species, nature, ss10, ss25, ss50, ss75, ss100, ing30, ing60):
        self.species = species
        self.nature = nature 
        self.ss10 = ss10 
        self.ss25 = ss25 
        self.ss50 = ss50 
        self.ss75 = ss75 
        self.ss100 = ss100 
        self.ing30 = ing30 
        self.ing60 = ing60 
        self.match_specialty()

    def match_specialty(self):
        try:
            self.specialty = pokemonRater.SPECIES_TO_SPECIALTY[self.species]
            self.specialty_code = pokemonRater.SPECIALTY_CODES[self.specialty]
        except KeyError:
            Element('warning').write(f"No Pokemon selected")

    def rate_nature(self):
        try:
            self.nature_rating = pokemonRater.NATURE_PER_SPECIALTY[self.nature][self.specialty_code]
            if self.species in pokemonRater.XP_HARD_SPECIES:
                if self.nature in pokemonRater.XP_NATURE_UP:
                    nature_rating_corrected = self.nature_rating + pokemonRater.NATURE_XP_FACTOR
                    self.nature_rating = 1.0 if nature_rating_corrected > 1.0 else nature_rating_corrected
                if self.nature in pokemonRater.XP_NATURE_DOWN:
                    nature_rating_corrected = self.nature_rating - pokemonRater.NATURE_XP_FACTOR
                    self.nature_rating = 0.0 if nature_rating_corrected < 0.0 else nature_rating_corrected
        except KeyError:
            Element('warning').write(f"No nature selected")

    def _get_subskill_score_bounds(self):
        all_scores_per_speciality = [subskill_ratings[self.specialty_code] for subskill_ratings in pokemonRater.SUBSKILL_PER_SPECIALTY.values()]
        subskill_scores_sorted = sorted(all_scores_per_speciality, reverse=True)
        largest_5_scores = subskill_scores_sorted[:5]
        smallest_5_scores = subskill_scores_sorted[-5:]
        self.max_subskill_score = sum([score*weight for score, weight in zip(largest_5_scores, pokemonRater.SUBSKILL_UNLOCK_WEIGHTS)])
        self.min_subskill_score = sum([score*weight for score, weight in zip(sorted(smallest_5_scores), pokemonRater.SUBSKILL_UNLOCK_WEIGHTS)]) 

    def rate_subskills(self):
        subskills = [self.ss10, self.ss25, self.ss50, self.ss75, self.ss100]
        try:
            subskills_unweighted = [pokemonRater.SUBSKILL_PER_SPECIALTY[subskill][self.specialty_code] for subskill in subskills]
            subskills_weighted = [score*weight for score, weight in zip(subskills_unweighted, pokemonRater.SUBSKILL_UNLOCK_WEIGHTS)]
            self._get_subskill_score_bounds()
            self.subskill_rating = (sum(subskills_weighted) - self.min_subskill_score) / (self.max_subskill_score - self.min_subskill_score)
        except KeyError:
            Element('warning').write(f"Not all subskills selected")

    def rate_ingredients(self):
        if self.species in pokemonRater.ING_SPECIES:
            ingredient_key = '|'.join([self.species, self.ing30, self.ing60])
            try:
                self.ingredient_rating = pokemonRater.ING_COMBI_RATINGS[ingredient_key]
            except KeyError:
                Element('warning').write(f"Ingredient combination not found for {self.species}")
        else:
            self.ingredient_rating = 0.5

    def rate_tierlist(self):
        try:
            self.tierlist_rating = pokemonRater.SPECIES_TO_TIERLIST[self.species]
        except KeyError:
            Element('warning').write(f"No Pokemon selected")

    def combine_scores(self):
        rating_weights = pokemonRater.RATING_WEIGHTS[self.specialty_code]
        subscores = [self.nature_rating, self.subskill_rating, self.ingredient_rating, self.tierlist_rating]
        self.score = sum([weight * subscore for weight, subscore in zip(rating_weights, subscores)])
    
    @staticmethod
    def apply_feelgoodfactor(score):
        k = 8
        return 1.04 / (1 + math.exp(-k * (score - 0.5))) - 0.02

    @staticmethod
    def score_to_rating(score):
        return f'{round(score*100)}%'

    def rate_pokemon(self):
        try:
            self.rate_nature()
            self.rate_subskills()
            self.rate_ingredients()
            self.rate_tierlist()
            self.combine_scores()
            self.score = self.apply_feelgoodfactor(self.score)
            Element('warning').write(f"")
            Element('percentage').write(f"{self.score_to_rating(self.score)}")
            Element('score').write(f"""Nature: {self.score_to_rating(self.apply_feelgoodfactor(self.nature_rating))}
Subskills: {self.score_to_rating(self.apply_feelgoodfactor(self.subskill_rating))}{'' if not self.species in pokemonRater.ING_SPECIES else
            '''
Ingredients: ''' + self.score_to_rating(self.apply_feelgoodfactor(self.ingredient_rating))}
Species: {self.score_to_rating(self.apply_feelgoodfactor(self.tierlist_rating))}""")
        except AttributeError:
            Element('score').write(f"Please fill required fields")

def _extract_stats():
    return {
        'species':Element('species').value,
        'nature':Element('nature').value,
        'ss10':Element('ss10').value,
        'ss25':Element('ss25').value,
        'ss50':Element('ss50').value,
        'ss75':Element('ss75').value,
        'ss100':Element('ss100').value,
        'ing30':Element('ing30').value,
        'ing60':Element('ing60').value
    }

def evaluate():
    stats = _extract_stats()
    pokemonRater(**stats).rate_pokemon()
