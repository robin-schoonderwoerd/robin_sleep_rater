
class PokemonRater {
    static SUBSKILL_UNLOCK_WEIGHTS = [1, 1, 0.85, 0.4, 0.1]; // lvl 10, 25, 50, 75, 100

    // Ingredient species
    // ex. ["Bulbasaur", "Ivysaur"]
    static ing_species = Object.keys(pokemonData)
    .filter(species => pokemonData[species].specialty === 'Ingredient');

    static NATURE_XP_FACTOR = 0.3;
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

        setTimeout(() => {
            document.getElementById('ing1').className = '';
            document.getElementById('ing30').className = '';
            document.getElementById('ing60').className = '';
            document.getElementById('nature').className = '';
            document.getElementById('species').className = '';
            document.getElementById('ss10').className = '';
            document.getElementById('ss25').className = '';
            document.getElementById('ss50').className = '';
            document.getElementById('ss75').className = '';
            document.getElementById('ss100').className = '';
        }, 0);
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
            if ((subskills[i] === undefined || subskills[i] === '') && this.species != 'Darkrai') {
                this.showWarning("Not all subskills selected")
            }
        }
    }

    matchSpecialty() {
        this.specialty = pokemonData[this.species].specialty;
    }

    rateNature() {
        this.natureRating = specialtyData[this.specialty]['natures'][this.nature];
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
        const allScoresPerSpecialty = Object.values(specialtyData[this.specialty]['subskills']);

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
        this.subskillsUnweighted = subskills.map(subskill => {
            return specialtyData[this.specialty]['subskills'][subskill] ?? 0;
        });

        // Calculate weighted subskill scores
        const subskillsWeighted = this.subskillsUnweighted.map((score, index) => 
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
        this.score =         
            (this.natureRating * specialtyData[this.specialty].ratingWeights.nature) +
            (this.subskillRating * specialtyData[this.specialty].ratingWeights.subskills) +
            (this.ingredientRating * specialtyData[this.specialty].ratingWeights.ingredients) +
            (this.tierlistRating * specialtyData[this.specialty].ratingWeights.tierlist);
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

    storeSubratingData() {
        const subrating_data_input = document.getElementById("subrating_data");
    
        // Store individual values
        subrating_data_input.dataset.natureRating = this.natureRating;
        subrating_data_input.dataset.ingredientRating = this.ingredientRating;
        subrating_data_input.dataset.tierlistRating = this.tierlistRating;
        subrating_data_input.dataset.ssRating = this.subskillsUnweighted;
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
        rater.storeSubratingData();
    } catch {
        console.log('Please fix your inputs')
    }
}
