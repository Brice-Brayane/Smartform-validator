// frontend/static/script.js
// --------------------------------------------------------------------
// Frontend-Logik für das SmartForm-Projekt.
// Zweck:
//  - Fängt das Formular ab, bevor es klassisch abgeschickt wird
//  - Sendet die Eingaben per AJAX (Fetch) an das Backend (/validate)
//  - Zeigt die Validierungsergebnisse im Frontend an
// --------------------------------------------------------------------

document.getElementById("smartform").addEventListener("submit", async function(e) {
    e.preventDefault(); // Standard-Submit (Seitenreload) unterbinden

    // Formulardaten aus den Eingabefeldern lesen
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    // Asynchronen POST-Request an das Backend senden
    const response = await fetch("/validate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email })
    });

    // Antwort vom Backend parsen (JSON)
    const result = await response.json();

    // Ergebnisbereich zurücksetzen
    const ergebnisse = document.getElementById("ergebnisse");
    ergebnisse.innerHTML = "";

    if (result.valid) {
        // Erfolgsfall: Formular ist gültig
        const p = document.createElement("p");
        p.textContent = "Formular ist gültig.";
        p.style.color = "green";
        ergebnisse.appendChild(p);
    } else {
        // Fehlerfall: alle Validierungsfehler einzeln anzeigen
        for (const [feld, fehlermeldung] of Object.entries(result.errors)) {
            const p = document.createElement("p");
            p.textContent = feld + ": " + fehlermeldung;
            p.style.color = "red";
            ergebnisse.appendChild(p);
        }
    }
});
