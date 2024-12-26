
class PokemonRater {
    static SPECIALTY_CODES = {
        'Berry': 0,
        'Ingredient': 1,
        'Skill': 2,
        'Allrounder': 3
    };

    static NATURE_PER_SPECIALTY = {
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
    };

    static SUBSKILL_PER_SPECIALTY = {
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
    };

    static SUBSKILL_UNLOCK_WEIGHTS = [1, 0.95, 0.85, 0.4, 0.2];

    static RATING_WEIGHTS = [
        [0.2, 0.6, 0, 0.2],  // Berry
        [0.2, 0.45, 0.2, 0.15],  // Ingredient
        [0.2, 0.6, 0, 0.2],  // Skill
        [0.1, 0.5, 0.2, 0.2]  // Allrounder
    ];

    static NATURE_XP_FACTOR = 0.3;

    // Ingredient species
    // ex. ["Bulbasaur", "Ivysaur"]
    static ing_species = Object.keys(pokemonData)
    .filter(species => pokemonData[species].specialty === 'Ingredient');

    static XP_NATURE_UP = ['Timid', 'Hasty', 'Jolly', 'Naive'];
    static XP_NATURE_DOWN = ['Brave', 'Relaxed', 'Quiet', 'Sassy'];

    constructor(species, nature, ss10, ss25, ss50, ss75, ss100, ing30, ing60) {
        this.species = species;
        this.nature = nature;
        this.ss10 = ss10;
        this.ss25 = ss25;
        this.ss50 = ss50;
        this.ss75 = ss75;
        this.ss100 = ss100;
        this.ing30 = ing30;
        this.ing60 = ing60;
    }

    showWarning(warning) {
        document.getElementById('warning').innerText = warning;
        document.getElementById("percentage").innerText = '';
        document.getElementById("score").innerText = '';
        console.log(warning)
        throw new Error(warning);
    }

    checkInputs() {
        if (this.species === undefined || this.species === '') {
            this.showWarning("No Pokemon selected")
        };
        if (this.nature === undefined || this.nature === '') {
            this.showWarning("No nature selected")
        };
        let subskills = [this.ss10, this.ss25, this.ss50, this.ss75, this.ss100]
        for (let i = 0; i < subskills.length; i++) {
            if (subskills[i] === undefined || subskills[i] === '') {
                this.showWarning("Not all subskills selected")
            }
        }
    }

    matchSpecialty() {
        this.specialty = pokemonData[this.species].specialty;
        this.specialtyCode = PokemonRater.SPECIALTY_CODES[this.specialty];        
    }

    rateNature() {
        this.natureRating = PokemonRater.NATURE_PER_SPECIALTY[this.nature][this.specialtyCode];
        if (pokemonData[this.species].XPHard) {
            if (PokemonRater.XP_NATURE_UP.includes(this.nature)) {
                const corrected = this.natureRating + PokemonRater.NATURE_XP_FACTOR;
                this.natureRating = Math.min(corrected, 1.0);
            } else if (PokemonRater.XP_NATURE_DOWN.includes(this.nature)) {
                const corrected = this.natureRating - PokemonRater.NATURE_XP_FACTOR;
                this.natureRating = Math.max(corrected, 0.0);
            }
        }
    }

    _getSubskillScoreBounds() {
        const allScoresPerSpecialty = Object.values(PokemonRater.SUBSKILL_PER_SPECIALTY)
            .map(subskillRatings => subskillRatings[this.specialtyCode]);

        const subskillScoresSorted = allScoresPerSpecialty.slice().sort((a, b) => b - a); // Sort in descending order
        const largest5Scores = subskillScoresSorted.slice(0, 5); // Take the top 5 scores
        const smallest5Scores = subskillScoresSorted.slice(-5); // Take the bottom 5 scores
    
        this.maxSubskillScore = largest5Scores.reduce((sum, score, index) => 
            sum + score * PokemonRater.SUBSKILL_UNLOCK_WEIGHTS[index], 0);
    
        this.minSubskillScore = [...smallest5Scores].sort((a, b) => a - b) // Sort smallest 5 in ascending order
            .reduce((sum, score, index) => 
                sum + score * PokemonRater.SUBSKILL_UNLOCK_WEIGHTS[index], 0);
    }

    rateSubskills() {
        const subskills = [this.ss10, this.ss25, this.ss50, this.ss75, this.ss100];
        // Retrieve unweighted subskill scores
        const subskillsUnweighted = subskills.map(subskill => {
            return PokemonRater.SUBSKILL_PER_SPECIALTY[subskill][this.specialtyCode];
        });

        // Calculate weighted subskill scores
        const subskillsWeighted = subskillsUnweighted.map((score, index) => 
            score * PokemonRater.SUBSKILL_UNLOCK_WEIGHTS[index]
        );

        // Calculate subskill bounds and rating
        this._getSubskillScoreBounds();
        const subskillScoreRange = this.maxSubskillScore - this.minSubskillScore;
        this.subskillRating = (subskillsWeighted.reduce((a, b) => a + b, 0) - this.minSubskillScore) / subskillScoreRange;

    }

    _mapIngredient() {
        let ing30Letter, ing60Letter;
        switch (this.ing30) {
            case pokemonData[this.species].ingA:
                ing30Letter = "A";
                break;
            case pokemonData[this.species].ingB:
                ing30Letter = "B";
                break;
            }
        switch (this.ing60) {
            case pokemonData[this.species].ingA:
                ing60Letter = "A";
                break;
            case pokemonData[this.species].ingB:
                ing60Letter = "B";
                break;
            case pokemonData[this.species].ingC:
                ing60Letter = "C";
                break;
            }
        return ["A", ing30Letter, ing60Letter].join('');
      }

    rateIngredients() {
        if (PokemonRater.ing_species.includes(this.species)) {
            let ingSpread = this._mapIngredient();
            this.ingredientRating = pokemonData[this.species][ingSpread];
        } else {
            this.ingredientRating = 0.5;
        }
    }    
    
    rateTierlist() {
        this.tierlistRating = pokemonData[this.species].tierlist;
    }

    combineScores() {
        const ratingWeights = PokemonRater.RATING_WEIGHTS[this.specialtyCode];
        const subscores = [this.natureRating, this.subskillRating, this.ingredientRating, this.tierlistRating];
        this.score = ratingWeights.reduce((total, weight, index) => total + weight * subscores[index], 0);
    }

    applyFeelGoodFactor(score) {
        const k = 8;
        return 1.04 / (1 + Math.exp(-k * (score - 0.5))) - 0.02;
    }

    scoreToRating(score) {
        return `${Math.round(score * 100)}%`;
    }

    perform() {
        this.matchSpecialty();
        this.rateNature();
        this.rateSubskills();
        this.rateIngredients();
        this.rateTierlist();
        this.combineScores();
        this.score = this.applyFeelGoodFactor(this.score)
    }

    generateOutput() {
        const rating = this.scoreToRating(this.score)
        document.getElementById("percentage").innerText = rating;

        const subscores = `
Nature: ${this.scoreToRating(this.applyFeelGoodFactor(this.natureRating))}
Subskills: ${this.scoreToRating(this.applyFeelGoodFactor(this.subskillRating))}${
        PokemonRater.ing_species.includes(this.species)
            ? `\nIngredients: ${this.scoreToRating(this.applyFeelGoodFactor(this.ingredientRating))}`
            : ''
        }
Species: ${this.scoreToRating(this.applyFeelGoodFactor(this.tierlistRating))}`;
        document.getElementById("score").innerText = subscores;
        document.getElementById("warning").innerText = '';
    }
    
}

function extract_stats() {
    return [
        document.getElementById('species').value,
        document.getElementById('nature').value,
        document.getElementById('ss10').value,
        document.getElementById('ss25').value,
        document.getElementById('ss50').value,
        document.getElementById('ss75').value,
        document.getElementById('ss100').value,
        document.getElementById('ing30').value,
        document.getElementById('ing60').value
    ]
}

function evaluate_pokkie() {
    try {
        const rater = new PokemonRater(...extract_stats());
        rater.checkInputs();
        rater.perform();
        rater.generateOutput();
    } catch {
        console.log('Please fix your inputs')
    }
}
