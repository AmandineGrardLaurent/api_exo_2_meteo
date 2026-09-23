const citySelect = document.getElementById("city");
const meteoContainer = document.querySelector("#weather");
const apiKey = "";
const cityCoordinates = {
    "merignac": { lat: 44.8448769, lon: -0.656358, name: "Mérignac" },
    "st_geours": { lat: 43.6841, lon: -1.2581, name: "Saint-Geours-de-Maremne" },
    "toulouse": { lat: 43.604652, lon: 1.444209, name: "Toulouse" }
};

citySelect.addEventListener("change", function () {
    const selectedCity = citySelect.value;
    const cityData = cityCoordinates[selectedCity];

    if (!cityData) return;

    meteoContainer.innerHTML = `Chargement...`;

    const url = "http://api.openweathermap.org/data/2.5/forecast?lat=" + cityData.lat + "&lon=" + cityData.lon + "&lang=fr&units=metric&appid=" + apiKey;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            meteoContainer.innerHTML = "";

            for (const item of data.list) {
                const div = document.createElement("div");

                // Description
                const description = item.weather[0].description;

               // Température arrondie
                const temp = Math.round(item.main.temp);

                // Modification de la date au format mercredi 23 septembre à 12h
                const date = new Date(item.dt_txt.replace(" ", "T"));
                const dateFormatee = date.toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long' });
                const heure = date.getHours();

                div.className = "p-3 rounded-lg bg-pink-50 border border-pink-100 text-pink-950 text-sm flex justify-between items-center";
                div.innerHTML = `
                    <div>
                        <span class="capitalize font-medium">${dateFormatee}</span>
                        <span class="font-medium"> à ${heure}h</span>
                        <p class="text-xs text-pink-700 capitalize mt-0.5">${description}</p>
                    </div>
                    <span class="font-bold text-base">${temp} °C</span>
                `;

                meteoContainer.appendChild(div);
            }
        })
        .catch(error => {
            meteoContainer.textContent = "Erreur de chargement.";
            console.error(error);
        });
});



