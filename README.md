# Grostund

En stund att gro. Stödapp för måltidslogg (självobservation enligt KBT-E), på svenska. Ingen vårdgivare. All data sparas bara i användarens webbläsare (localStorage).

- `src/grostund.html` – källfilen (en fil)
- `tools/build_app.py` – bygger den fristående appen till `site/` (ikoner, manifest, service worker)
- `assets/` – appikon och Grostund-loggan (`assets/logo/grostund/`), växtens stadier (`assets/logo/vaxten/`)
- `site/` – det Netlify publicerar (se `netlify.toml`)

Uppdatera: ändra `src/grostund.html`, kör `python3 tools/build_app.py`, committa och pusha till `main`.
