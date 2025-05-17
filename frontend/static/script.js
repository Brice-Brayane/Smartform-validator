// frontend/static/script.js
// ---------------------------------------------------------------
// Dieser Code fängt das Formular ab und sendet es per AJAX.
// ---------------------------------------------------------------

// frontend/static/script.js
// ---------------------------------------------------------------
// AJAX pour valider dynamiquement les champs du formulaire
// ---------------------------------------------------------------

document.getElementById("smartform").addEventListener("submit", async function (e) {
    e.preventDefault(); // Évite le rechargement

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const ergebnisse = document.getElementById("ergebnisse");
    ergebnisse.innerHTML = ""; // Réinitialise l'affichage

    try {
        const response = await fetch("/validate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, email })
        });

        const result = await response.json();
        console.log("✅ Réponse JSON :", result);

        if (result.valid) {
            ergebnisse.innerHTML = "<p style='color: green;'>✔️ Formular ist gültig!</p>";
        } else if (result.errors && Object.keys(result.errors).length > 0) {
            for (const [feld, fehlermeldung] of Object.entries(result.errors)) {
                const p = document.createElement("p");
                p.textContent = `❌ ${feld}: ${fehlermeldung}`;
                p.style.color = "red";
                ergebnisse.appendChild(p);
            }
        } else {
            // Fallback si le backend retourne valid: false sans erreurs spécifiques
            const p = document.createElement("p");
            p.textContent = "❌ Unbekannter Validierungsfehler.";
            p.style.color = "red";
            ergebnisse.appendChild(p);
        }

    } catch (error) {
        console.error("🚨 Erreur réseau :", error);
        ergebnisse.innerHTML = "<p style='color: red;'>❌ Verbindung zum Server fehlgeschlagen.</p>";
    }
});
