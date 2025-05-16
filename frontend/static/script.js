// frontend/static/script.js
// ---------------------------------------------------------------
// Dieser Code fängt das Formular ab und sendet es per AJAX.
// ---------------------------------------------------------------

document.getElementById("smartform").addEventListener("submit", async function(e) {
    e.preventDefault(); // Verhindert das Neuladen der Seite

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    const response = await fetch("/validate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email })
    });

    const result = await response.json();

    const ergebnisse = document.getElementById("ergebnisse");
    ergebnisse.innerHTML = "";

    if (result.valid) {
        ergebnisse.innerHTML = "<p style='color: green;'>✔️ Formular ist gültig!</p>";
    } else {
        for (const [feld, fehlermeldung] of Object.entries(result.errors)) {
            const p = document.createElement("p");
            p.textContent = `❌ ${feld}: ${fehlermeldung}`;
            p.style.color = "red";
            ergebnisse.appendChild(p);
        }
    }
});
