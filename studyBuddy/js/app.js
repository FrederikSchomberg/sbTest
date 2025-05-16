/*################### Hamburger-Menü ##################*/

const hamMenu = document.querySelector('.ham-menu');

const offscreenMenu = document.querySelector('.offscreen-menu');

hamMenu.addEventListener('click', () => {
    hamMenu.classList.toggle('active');
    offscreenMenu.classList.toggle('active');
})



/*#################### Zeitplan ##########################*/

const addScheduleItemButton = document.getElementById("add-schedule-item");
const scheduleList = document.getElementById("schedule-list");

addScheduleItemButton.addEventListener("click", () => {
    const listeneintrag = prompt("Was möchtest du zum Zeitplan hinzufügen?");
    if (listeneintrag) {
        const sli = document.createElement("li");
        sli.textContent = listeneintrag;
        scheduleList.appendChild(sli);
    }
});



/*#################### Ziele ##########################*/

const addGoalButton = document.getElementById("add-goal-item");
const goalList = document.getElementById("goal-list");

addGoalButton.addEventListener("click", () => {
    const zieleintrag = prompt("Welches Ziel möchtest du hinzufügen?");
    if (zieleintrag) {
        const gli = document.createElement("li");
        gli.textContent = zieleintrag;
        goalList.appendChild(gli);
    }
});



/*#################### Timer ##########################*/

let timer;
let zeit = 25 * 60; // Startzeit (25 Minuten)
let ursprünglicheZeit = zeit; // Speichert die ursprüngliche Zeit

// Timer anzeigen
function updateAnzeige() {
    const minuten = Math.floor(zeit / 60);
    const sekunden = zeit % 60;
    document.getElementById("timer-display").textContent =
        `${minuten.toString().padStart(2, '0')}:${sekunden.toString().padStart(2, '0')}`;
}

// Timer starten
function startTimer() {
    stopTimer(); 
    timer = setInterval(() => {
        if (zeit > 0) {
            zeit--;
            updateAnzeige();
        } else {
            clearInterval(timer);
            alert("Timer fertig!");
            zeit = ursprünglicheZeit; // Zurück zur ursprünglichen Zeit
            updateAnzeige();
        }
    }, 1000);
}

// Timer stoppen
function stopTimer() {
    clearInterval(timer);
}

// Timer zurück auf die ursprüngliche Zeit setzen
function resetTimer() {
    stopTimer(); 
    zeit = ursprünglicheZeit; 
    updateAnzeige(); 
}

// Erlaubt das Setzen der Pomodoro-Zeit
function setTime() {
    const neueZeit = parseInt(document.getElementById("time-input").value);
    if (neueZeit >= 1 && neueZeit <= 60) {
        ursprünglicheZeit = neueZeit * 60; // Zeit anpassen
        zeit = ursprünglicheZeit; // Aktualisierte Zeit setzen
        updateAnzeige(); // Anzeige aktualisieren
    } else {
        alert("Bitte gib eine Zeit zwischen 1 und 60 Minuten ein.");
    }
}

// Anzeige initial setzen
updateAnzeige();

// Logout-Funktion
function logout() {
    alert("Du wurdest ausgeloggt.");
    window.location.href = "index.html"; 
}




