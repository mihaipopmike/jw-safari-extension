# Verificarea și testele extensiei JW Safari

Aceste fișiere se pun în proiectul de pe GitHub, lângă `JW_Safari_Extension.user.js`. Nu schimbă extensia; o verifică.

- `eslint.config.js` și `package.json` – verificarea automată a codului (variabile nedefinite, globale folosite din greșeală, chei duplicate, cod de neatins).
- `tests/` – testele care deschid extensia într-un Safari simulat (iPhone și iPad): fereastra principală, ținte de 44 px, ajutorul, Rezumatul cu valul, firul de navigare, Locuri, harta extinsă, Cronologie, erori JavaScript.
- `.github/workflows/verificare.yml` – GitHub rulează singur verificarea și testele la fiecare urcare; rezultatul apare în fila „Actions”, cu bifă verde sau cruce roșie.

Cum le urci: Add file › Upload files, apoi tragi în pagină tot conținutul acestui pachet (cu dosarele `tests` și `.github`).
