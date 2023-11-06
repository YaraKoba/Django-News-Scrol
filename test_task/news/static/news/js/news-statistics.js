import PostService from "./fetchService.js";
import { getDiagramHTML } from "./generateHTML.js";

const diagramContainer = document.getElementById("diagram");
const selectContainer = document.getElementById("select");
const colors = ['#00A1FF', '#0081CC', '#265F7F', '#4CBDFF', '#00517F'];
let currentColorIndex = 0;

const fetchStatistics = async () => {
    const count = selectContainer.value;
    const response = await PostService.getAll(count);
    const rate = 100 / response[0][count];
    diagramContainer.innerHTML = "";
    
    for (const post of response) {
        const color = colors[currentColorIndex];
        diagramContainer.insertAdjacentHTML('beforeend', getDiagramHTML(post, rate, count, color));
        currentColorIndex = (currentColorIndex + 1) % colors.length;
    }
}

window.addEventListener('load', fetchStatistics);
selectContainer.addEventListener('change', fetchStatistics);
