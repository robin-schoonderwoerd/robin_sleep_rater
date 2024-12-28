// Extract all data
// All Pokemon species
// ex. ["", "Bulbasaur", "Ivysaur"]
var all_species = Object.keys(pokemonData);
all_species.unshift('');

// All natures
// ex. ['', 'Adamant','Bashful']
var all_natures = Object.keys(specialtyData.Berry.natures);
all_natures.unshift('');

// All subskills
// ex. ['','Berry Finding S', 'Dream Shard Bonus']
var all_subskills = Object.keys(specialtyData.Berry.subskills);
all_subskills.unshift('');

// All ingredients
// ex. ["", "Honey", "Snoozy Tomato"]
var all_ingredients = Object.values(pokemonData).reduce((acc, pokemon) => {
    const { ingA, ingB, ingC } = pokemon; // Destructure ingredient properties
    [ingA, ingB, ingC].forEach(ingredient => {
        if (ingredient && !acc.includes(ingredient)) { // Add only if it's not already in the array
            acc.push(ingredient);
        }
    });
    return acc;
}, []);
all_ingredients.unshift('');

// Ingredient species
// ex. ["Bulbasaur", "Ivysaur"]
var ing_species = Object.keys(pokemonData)
.filter(species => pokemonData[species].specialty === 'Ingredient');

// Ingredient options per Pokemon
// ex. {"Bulbasaur":["Honey", "Snoozy Tomato", "Soft Potato"]}
var ing_options = Object.keys(pokemonData).reduce((acc, pokemon) => {
    const { ingA, ingB, ingC } = pokemonData[pokemon]; // Destructure the ingredients
    const ingredients = [ingA, ingB, ingC].filter(Boolean); // Filter out undefined or null values
    if (ingredients.length) { // Only include Pokémon with ingredients
        acc[pokemon] = ingredients;
    }
    return acc;
}, {});

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
    var percentage = document.getElementById('percentage');
    var score = document.getElementById('score');
    var warning = document.getElementById('warning');

    image.src = (selected_species !== '') ? 'https://www.serebii.net/pokemonsleep/pokemon/' + pokemonData[selected_species].id + '.png' : './empty.png'

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

    // Remove percentage
    percentage.innerHTML = ''
    score.innerHTML = ''
    warning.innerHTML = ''
}

// Initial population of species
populateSelect('species', all_species.sort());
populateSelect('nature', all_natures);
var subskills = ['ss10','ss25','ss50','ss75','ss100']
for (let i = 0; i < subskills.length; i++) {
    populateSelect(subskills[i], all_subskills)
}

function toggleVisibility() {
    const div = document.getElementById('debuginfo');
    if (div.style.display === 'none') {
        div.style.display = 'block';
    } else {
        div.style.display = 'none';
    }
}

// Set color of percentage
function updateTextColor(percentage) {
    const percentageText = percentage.innerText;
    const percentageValue = parseFloat(percentageText);
    percentage.className = ''; // Remove existing class
    if (!isNaN(percentageValue)) { // Check if percentageValue is valid
        if (percentageValue < 50) {
            percentage.classList.add('low-percentage');
        } else if (percentageValue >= 50 && percentageValue < 75) {
            percentage.classList.add('medium-percentage');
        } else {
            percentage.classList.add('high-percentage');
        }
    }
}
const percentage = document.getElementById('percentage'); // Initial color setting
updateTextColor(percentage);
const observer = new MutationObserver(() => { // Create a MutationObserver to watch for changes to the div's innerHTML
    updateTextColor(percentage);
});
observer.observe(percentage, { childList: true, subtree: true }); // Start observing the div for changes in its child nodes (e.g., text changes)


// Upload screenshot
document.getElementById('imageUpload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (!file) {
        return;
    }

    const reader = new FileReader();
    reader.onload = function(e) {
        const img = new Image();
        img.src = e.target.result;

        img.onload = function() {
            // Image cropping part
            const canvas = document.getElementById('canvas');
            const ctx = canvas.getContext('2d');
    
            // Define crop areas based on screenshot size
            let img_size_factor = img.height / img.width
            console.log(img_size_factor)
            let crops = []

            let standardWidth = img.width;
            let standardHeight = img.height;

            if (img_size_factor > 2.2) {
                // Eric screenshot size (2.22)
                crops = [
                    {x: 438, y: 324, width: 326, height: 76}, // species
                    {x: 232, y: 2731, width: 326, height: 98}, // nature
                    {x: 168, y: 1793, width: 470, height: 98}, // subskill10
                    {x: 814, y: 1793, width: 470, height: 98}, // subskill25
                    {x: 168, y: 2017, width: 470, height: 98}, // subskill50
                    {x: 814, y: 2017, width: 470, height: 98}, // subskill75
                    {x: 168, y: 2244, width: 470, height: 98}, // subskill100
                ];
                standardWidth = 1440;
                standardHeight = 3200;
        
                // Resize the image to the standard size
                canvas.width = standardWidth;
                canvas.height = standardHeight;
                ctx.drawImage(img, 0, 0, standardWidth, standardHeight);
            }
            else if (img_size_factor > 2) {
                // Maartje screenshot size (2.17)
                crops = [
                    {x: 438, y: 324, width: 326, height: 76}, // species
                    {x: 232, y: 2731, width: 326, height: 98}, // nature
                    {x: 168, y: 1751, width: 480, height: 98}, // subskill10
                    {x: 830, y: 1751, width: 480, height: 98}, // subskill25
                    {x: 168, y: 1989, width: 480, height: 98}, // subskill50
                    {x: 830, y: 1989, width: 480, height: 98}, // subskill75
                    {x: 168, y: 2224, width: 480, height: 98}, // subskill100
                ];
                standardWidth = 1476;
                standardHeight = 3200;
        
                // Resize the image to the standard size
                canvas.width = standardWidth;
                canvas.height = standardHeight;
                ctx.drawImage(img, 0, 0, standardWidth, standardHeight);
            }
            else {
                // Robin screenshot size (1.78)
                crops = [
                    {x: 438, y: 334, width: 326, height: 76}, // species
                    {x: 250, y: 2291, width: 326, height: 98}, // nature
                    {x: 168, y: 1306, width: 500, height: 98}, // subskill10
                    {x: 830, y: 1306, width: 500, height: 98}, // subskill25
                    {x: 168, y: 1545, width: 500, height: 98}, // subskill50
                    {x: 830, y: 1545, width: 500, height: 98}, // subskill75
                    {x: 168, y: 1779, width: 500, height: 98}, // subskill100
                ];
                standardWidth = 1500;
                standardHeight = 2668;
        
                // Resize the image to the standard size
                canvas.width = standardWidth;
                canvas.height = standardHeight;
                ctx.drawImage(img, 0, 0, standardWidth, standardHeight);
            }

            
            // Make black/white
            function makeBlackWhite (image_ctx) {
                const imageData = image_ctx.getImageData(0, 0, canvas.width, canvas.height);
                const data = imageData.data;
                
                for (let i = 0; i < data.length; i += 4) {
                    const red = data[i];
                    const green = data[i + 1];
                    const blue = data[i + 2];
                    
                    const grey = 0.3 * red + 0.59 * green + 0.11 * blue; // Calculate the greyscale value
                    
                    data[i] = grey;
                    data[i + 1] = grey;
                    data[i + 2] = grey; // Set the RGB values to the greyscale value
                }
                image_ctx.putImageData(imageData, 0, 0); // Update the canvas with the new image data
                return image_ctx
            }
    
            const outputCanvasSpecies = document.getElementById('outputCanvasSpecies');
            let outputCtxSpecies = outputCanvasSpecies.getContext('2d');

            const outputCanvasNature = document.getElementById('outputCanvasNature');
            let outputCtxNature = outputCanvasNature.getContext('2d');

            const outputCanvasSS10 = document.getElementById('outputCanvasSS10');
            let outputCtxSS10 = outputCanvasSS10.getContext('2d');

            const outputCanvasSS25 = document.getElementById('outputCanvasSS25');
            let outputCtxSS25 = outputCanvasSS25.getContext('2d');

            const outputCanvasSS50 = document.getElementById('outputCanvasSS50');
            let outputCtxSS50 = outputCanvasSS50.getContext('2d');

            const outputCanvasSS75 = document.getElementById('outputCanvasSS75');
            let outputCtxSS75 = outputCanvasSS75.getContext('2d');

            const outputCanvasSS100 = document.getElementById('outputCanvasSS100');
            let outputCtxSS100 = outputCanvasSS100.getContext('2d');

            const canvas_list = [
                outputCanvasSpecies, 
                outputCanvasNature, 
                outputCanvasSS10,
                outputCanvasSS25,
                outputCanvasSS50,
                outputCanvasSS75,
                outputCanvasSS100
            ]
            const ctx_list = [
                outputCtxSpecies, 
                outputCtxNature, 
                outputCtxSS10,
                outputCtxSS25,
                outputCtxSS50,
                outputCtxSS75,
                outputCtxSS100
            ]
            const element_list = ['species', 'nature', 'ss10', 'ss25', 'ss50', 'ss75', 'ss100']
            const result_list = [
                "resultSpecies",
                "resultNature",
                "resultSS10",
                "resultSS25",
                "resultSS50",
                "resultSS75",
                "resultSS100",
            ]


            function doTesseract (i) {
                // Tesseract part to extract text from image
                document.getElementById('status').innerText = 'Recognizing text...';
                document.getElementById('visible_status').innerText = 'Extracting from screenshot...';
                    Tesseract.recognize(
                        canvas_list[i],
                        'eng',
                        {
                            logger: m => console.log(m),
                            tessedit_pageseg_mode: Tesseract.PSM.SINGLE_LINE,
                        }
                    ).then(({ data: { text } }) => {
                        document.getElementById('status').innerText = 'Text recognized:';
                        document.getElementById('visible_status').innerText = '';
                        document.getElementById(result_list[i]).innerText = text;
                        
                        // Preprocess extracted text
                        let words = text.split('\n');

                        // Prefill selectpickers
                        var fill_element = document.getElementById(element_list[i]);
                        console.log(words[0].replace(/[^a-zA-Z\s]/g, ''))

                        fill_element.value = words[0].replace(/[^a-zA-Z\s]/g, '')
                        if (element_list[i] === 'species') {
                            updateOptions('species', 'ing1', 'ing30', 'ing60')
                        }
                        
                    }).catch(err => {
                        document.getElementById('status').innerText = 'Error recognizing text';
                        console.error(err);
                    });
            }

            // Crop and perform Tesseract
            for (let i = 0; i < crops.length; i++) {
                const sx = crops[i].x, sy = crops[i].y-10, sw = crops[i].width, sh = crops[i].height;
                canvas_list[i].width = crops[2].width;
                ctx_list[i].drawImage(canvas, sx, sy, sw, sh, 0, 0, sw, sh);
                ctx_list[i] = makeBlackWhite(ctx_list[i])
                doTesseract(i)
            };
        };
    };
    reader.readAsDataURL(file);
});
