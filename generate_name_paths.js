const TextToSVG = require('text-to-svg');
const fs = require('fs');

const textToSVG = TextToSVG.loadSync('./Pacifico.ttf');
const text = "Pranav Navghare";
const fontSize = 72;
let currentX = 0;
let svgPaths = "";

for (let i = 0; i < text.length; i++) {
    const char = text[i];
    if (char === ' ') {
        currentX += 20; // approximate space width
        continue;
    }
    const options = { x: 0, y: 0, fontSize: fontSize, anchor: 'top' };
    const pathD = textToSVG.getD(char, options);
    
    // Animate pop in using CSS classes. Use translation group for position!
    svgPaths += `<g transform="translate(${currentX}, 0)"><path class="name-char char-${i}" fill="url(#nameGrad)" d="${pathD}" style="animation-delay: ${i * 0.1}s; opacity: 0;" /></g>\n`;
    
    // advance X
    const metrics = textToSVG.getMetrics(char, options);
    currentX += metrics.width;
}

fs.writeFileSync('name_paths_individual.svg', svgPaths);
console.log("Written individual paths");
