var all_species = [
    '', 'Bulbasaur', 'Ivysaur', 'Venusaur','Charmander', 'Charmeleon', 
    'Charizard','Squirtle', 'Wartortle', 'Blastoise','Caterpie', 'Metapod', 
    'Butterfree','Rattata', 'Raticate','Ekans', 'Arbok','Pikachu', 'Raichu',
    'Pikachu - Halloween','Pikachu - Holiday','Clefairy', 'Clefable',
    'Jigglypuff', 'Wigglytuff','Diglett', 'Dugtrio','Meowth', 'Persian',
    'Psyduck', 'Golduck','Mankey', 'Primeape','Growlithe', 'Arcanine',
    'Bellsprout', 'Weepinbell', 'Victreebel','Geodude', 'Graveler', 'Golem',
    'Slowpoke', 'Slowbro','Magnemite', 'Magneton','Doduo', 'Dodrio','Gastly', 
    'Haunter', 'Gengar','Onix','Cubone', 'Marowak','Kangaskhan','Mr. Mime',
    'Pinsir','Ditto','Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Dratini', 
    'Dragonair', 'Dragonite', 'Chikorita', 
    'Bayleef', 'Meganium','Cyndaquil', 'Quilava', 'Typhlosion','Totodile', 
    'Croconaw', 'Feraligatr','Pichu','Cleffa','Igglybuff','Togepi', 'Togetic',
    'Mareep', 'Flaaffy', 'Ampharos','Sudowoodo','Espeon', 'Umbreon','Slowking',
    'Wobbuffet','Steelix','Heracross','Delibird','Houndour', 'Houndoom',
    'Larvitar', 'Pupitar', 'Tyranitar','Ralts', 'Kirlia', 'Gardevoir',
    'Slakoth', 'Vigoroth', 'Slaking', 
    'Sableye','Gulpin', 'Swalot','Swablu', 'Altaria','Shuppet', 'Banette',
    'Absol','Wynaut','Spheal', 'Sealeo', 'Walrein','Bonsly','Mime Jr.',
    'Riolu', 'Lucario','Croagunk', 'Toxicroak','Snover', 'Abomasnow',
    'Magnezone', 'Togekiss','Leafeon', 'Glaceon','Gallade', 'Sylveon', 
    'Stufful', 'Bewear'
];

var all_natures = [
    '', 'Adamant','Bashful','Bold','Brave','Calm','Careful','Docile',
    'Gentle','Hardy','Hasty','Impish','Jolly','Lax','Lonely','Mild',
    'Modest','Naive','Naughty','Quiet','Quirky','Rash','Relaxed',
    'Sassy','Serious','Timid'
]

var all_subskills = [
    '','Berry Finding S', 'Dream Shard Bonus','Energy Recovery Bonus',
    'Helping Bonus', 'Helping Speed S', 'Helping Speed M',
    'Ingredient Finder S', 'Ingredient Finder M','Inventory Up S', 
    'Inventory Up M', 'Inventory Up L','Research EXP Bonus',
    'Skill Level Up S', 'Skill Level Up M', 'Skill Trigger S', 
    'Skill Trigger M','Sleep EXP Bonus'
]

var all_ingredients = [
    '', 'Large Leek', 'Tasty Mushroom', 'Fancy Egg', 'Soft Potato', 
    'Fancy Apple','Fiery Herb', 'Bean Sausage', 'Moomoo Milk', 'Honey', 
    'Pure Oil','Warming Ginger', 'Snoozy Tomato', 'Soothing Cacao', 
    'Slowpoke Tail','Greengrass Soybeans', 'Greengrass Corn'
]

var ing_species = [
    'Bulbasaur', 'Ivysaur', 'Venusaur','Charmander', 'Charmeleon', 
    'Charizard','Squirtle', 'Wartortle', 'Blastoise','Diglett', 'Dugtrio',
    'Bellsprout', 'Weepinbell', 'Victreebel','Geodude', 'Graveler', 'Golem',
    'Slowpoke', 'Slowbro','Gastly','Haunter', 'Gengar','Kangaskhan','Mr. Mime',
    'Pinsir','Ditto','Dratini','Dragonair','Dragonite',
    'Slowking','Delibird', 'Larvitar', 'Pupitar', 'Tyranitar',
    'Absol','Mime Jr.','Croagunk', 'Toxicroak','Snover', 'Abomasnow', 'Stufful', 
    'Bewear'
]

var ing_options = {
    'Bulbasaur':['Honey', 'Snoozy Tomato', 'Soft Potato'], 
    'Ivysaur':['Honey', 'Snoozy Tomato', 'Soft Potato'], 
    'Venusaur':['Honey', 'Snoozy Tomato', 'Soft Potato'],
    'Charmander':['Bean Sausage', 'Warming Ginger', 'Fiery Herb'],
    'Charmeleon':['Bean Sausage', 'Warming Ginger', 'Fiery Herb'],
    'Charizard':['Bean Sausage', 'Warming Ginger', 'Fiery Herb'],
    'Squirtle':['Moomoo Milk', 'Soothing Cacao', 'Bean Sausage'],
    'Wartortle':['Moomoo Milk', 'Soothing Cacao', 'Bean Sausage'],
    'Blastoise':['Moomoo Milk', 'Soothing Cacao', 'Bean Sausage'],
    'Diglett':['Snoozy Tomato', 'Large Leek', 'Greengrass Soybeans'],
    'Dugtrio':['Snoozy Tomato', 'Large Leek', 'Greengrass Soybeans'],
    'Bellsprout':['Snoozy Tomato', 'Soft Potato', 'Large Leek'],
    'Weepinbell':['Snoozy Tomato', 'Soft Potato', 'Large Leek'],
    'Victreebel':['Snoozy Tomato', 'Soft Potato', 'Large Leek'],
    'Geodude':['Greengrass Soybeans', 'Soft Potato', 'Tasty Mushroom'],
    'Graveler':['Greengrass Soybeans', 'Soft Potato', 'Tasty Mushroom'],
    'Golem':['Greengrass Soybeans', 'Soft Potato', 'Tasty Mushroom'],
    'Slowpoke':['Soothing Cacao', 'Slowpoke Tail', 'Snoozy Tomato'],
    'Slowbro':['Soothing Cacao', 'Slowpoke Tail', 'Snoozy Tomato'],
    'Gastly':['Fiery Herb', 'Tasty Mushroom', 'Pure Oil'],
    'Haunter':['Fiery Herb', 'Tasty Mushroom', 'Pure Oil'],
    'Gengar':['Fiery Herb', 'Tasty Mushroom', 'Pure Oil'],
    'Kangaskhan':['Warming Ginger', 'Soft Potato', 'Greengrass Soybeans'],
    'Mr. Mime':['Snoozy Tomato', 'Soft Potato', 'Large Leek'],
    'Pinsir':['Honey', 'Fancy Apple', 'Bean Sausage'],
    'Ditto':['Pure Oil', 'Large Leek', 'Slowpoke Tail'],
    'Dratini':['Fiery Herb', 'Greengrass Corn', 'Pure Oil'],
    'Dragonair':['Fiery Herb', 'Greengrass Corn', 'Pure Oil'],
    'Dragonite':['Fiery Herb', 'Greengrass Corn', 'Pure Oil'],
    'Slowking':['Soothing Cacao', 'Slowpoke Tail', 'Snoozy Tomato'],
    'Delibird':['Fancy Egg', 'Fancy Apple', 'Soothing Cacao'],
    'Larvitar':['Warming Ginger', 'Greengrass Soybeans', 'Bean Sausage'],
    'Pupitar':['Warming Ginger', 'Greengrass Soybeans', 'Bean Sausage'],
    'Tyranitar':['Warming Ginger', 'Greengrass Soybeans', 'Bean Sausage'],
    'Absol':['Soothing Cacao', 'Fancy Apple', 'Tasty Mushroom'],
    'Mime Jr.':['Snoozy Tomato', 'Soft Potato', 'Large Leek'],
    'Croagunk':['Pure Oil', 'Bean Sausage'],
    'Toxicroak':['Pure Oil', 'Bean Sausage'],
    'Snover':['Snoozy Tomato', 'Fancy Egg', 'Tasty Mushroom'],
    'Abomasnow':['Snoozy Tomato', 'Fancy Egg', 'Tasty Mushroom'],
    'Stufful':['Greengrass Corn', 'Bean Sausage', 'Fancy Egg'],
    'Bewear':['Greengrass Corn', 'Bean Sausage', 'Fancy Egg']
}

var species_name_to_id = {
    'Bulbasaur': 1, 'Ivysaur': 2, 'Venusaur': 3, 
    'Charmander': 4, 'Charmeleon': 5, 'Charizard': 6, 
    'Squirtle': 7, 'Wartortle': 8, 'Blastoise': 9, 
    'Caterpie': 10, 'Metapod': 11, 'Butterfree': 12, 
    'Rattata': 19, 'Raticate': 20, 
    'Ekans': 23, 'Arbok': 24, 
    'Pikachu': 25, 'Raichu': 26, 
    'Pikachu - Halloween': '25-halloween',
    'Pikachu - Holiday': '25-holiday',
    'Clefairy': 35, 'Clefable': 36, 
    'Jigglypuff': 39, 'Wigglytuff': 40, 
    'Diglett': 50, 'Dugtrio': 51, 
    'Meowth': 52, 'Persian': 53, 
    'Psyduck': 54, 'Golduck': 55, 
    'Mankey': 56, 'Primeape': 57, 
    'Growlithe': 58, 'Arcanine': 59, 
    'Bellsprout': 69, 'Weepinbell': 70, 'Victreebel': 71, 
    'Geodude': 74, 'Graveler': 75, 'Golem': 76, 
    'Slowpoke': 79, 'Slowbro': 80, 
    'Magnemite': 81, 'Magneton': 82, 
    'Doduo': 84, 'Dodrio': 85, 
    'Gastly': 92, 'Haunter': 93, 'Gengar': 94, 
    'Onix': 95, 'Cubone': 104, 'Marowak': 105, 
    'Kangaskhan': 115, 'Mr. Mime': 122, 'Pinsir': 127, 
    'Ditto': 132, 'Eevee': 133, 'Vaporeon': 134, 
    'Jolteon': 135, 'Flareon': 136, 
    'Dratini': 147, 'Dragonair': 148, 'Dragonite': 149, 
    'Chikorita': 152, 'Bayleef': 153, 'Meganium': 154, 
    'Cyndaquil': 155, 'Quilava': 156, 'Typhlosion': 157, 
    'Totodile': 158, 'Croconaw': 159, 'Feraligatr': 160, 
    'Pichu': 172, 'Cleffa': 173, 'Igglybuff': 174, 
    'Togepi': 175, 'Togetic': 176, 
    'Mareep': 179, 'Flaaffy': 180, 'Ampharos': 181, 
    'Sudowoodo': 185, 'Espeon': 196, 'Umbreon': 197, 
    'Slowking': 199, 'Wobbuffet': 202, 'Steelix': 208, 
    'Heracross': 214, 'Delibird': 225, 
    'Houndour': 228, 'Houndoom': 229, 
    'Larvitar': 246, 'Pupitar': 247, 'Tyranitar': 248, 
    'Ralts': 280, 'Kirlia': 281, 'Gardevoir': 282, 
    'Slakoth': 287, 'Vigoroth': 288, 'Slaking': 289, 
    'Sableye': 302, 'Gulpin': 316, 'Swalot': 317, 
    'Swablu': 333, 'Altaria': 334, 
    'Shuppet': 353, 'Banette': 354, 
    'Absol': 359, 'Wynaut': 360, 
    'Spheal': 363, 'Sealeo': 364, 'Walrein': 365, 
    'Bonsly': 438, 'Mime Jr.': 439, 
    'Riolu': 447, 'Lucario': 448, 
    'Croagunk': 453, 'Toxicroak': 454, 
    'Snover': 459, 'Abomasnow': 460, 
    'Magnezone': 462, 'Togekiss': 468, 
    'Leafeon': 470, 'Glaceon': 471, 
    'Gallade': 475, 'Sylveon': 700, 
    'Stufful': 759, 'Bewear': 760
}

// Function to populate select dropdown
function populateSelect(elementId, data) {
    var selectElement = document.getElementById(elementId);

    // Clear existing options
    selectElement.innerHTML = '';

    // Add options from data array
    data.forEach(function(item) {
        var option = document.createElement('option');
        option.value = item;
        option.text = item;
        selectElement.add(option);
    });
}

// Function to update options based on selected species
function updateOptions(species, ing1, ing30, ing60) {
    var selected_species = document.getElementById(species).value;
    var image = document.getElementById('image');
    var ing1 = document.getElementById(ing1);
    var ing30 = document.getElementById(ing30);
    var ing60 = document.getElementById(ing60);
    var ingredient_fields = document.getElementById('ingredient_fields');

    image.src = (selected_species !== '') ? 'https://www.serebii.net/pokemonsleep/pokemon/' + species_name_to_id[selected_species] + '.png' : './empty.png'

    populateSelect('ing1', !ing_options[selected_species] ? [''] : ing_options[selected_species].slice(0,1));
    populateSelect('ing30', !ing_options[selected_species] ? [''] : ing_options[selected_species].slice(0,2));
    populateSelect('ing60', !ing_options[selected_species] ? [''] : ing_options[selected_species]);

    ingredient_fields.hidden = !ing_species.includes(selected_species);

    // Enable/disable ing30 based on the selected species
    ing30.disabled = !ing_species.includes(selected_species);
    ing30.selectedIndex = 0; // Reset selection

    // Enable/disable ing60 based on the selected species
    ing60.disabled = !ing_species.includes(selected_species);
    ing60.selectedIndex = 0; // Reset selection
}

// Initial population of species
populateSelect('species', all_species.sort());
populateSelect('nature', all_natures);
var subskills = ['ss10','ss25','ss50','ss75','ss100']
for (let i = 0; i < subskills.length; i++) {
    populateSelect(subskills[i], all_subskills)
}
