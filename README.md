# ELIN

Stödapp för måltidslogg (självobservation enligt KBT-E), på svenska. Ingen vårdgivare. All data sparas bara i användarens webbläsare (localStorage).

- `src/elin.html` – källfilen (en fil, samma som Claude-artefakten)
- `tools/build_app.py` – bygger den fristående appen till `site/` (ikoner, manifest, service worker)
- `site/` – det Netlify publicerar (se `netlify.toml`)

Uppdatera: ändra `src/elin.html`, kör `python3 tools/build_app.py`, committa och pusha till `main`.
