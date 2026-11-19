# Grostund

En stund att gro. Stödapp för måltidslogg (självobservation enligt KBT-E), på svenska. Ingen vårdgivare. All data sparas bara i användarens webbläsare (localStorage).

- `src/grostund.html` – källfilen (en fil)
- `tools/build_app.py` – bygger den fristående appen till `site/` (ikoner, manifest, service worker)
- `assets/` – appikon och Grostund-loggan (`assets/logo/grostund/`), växtens stadier (`assets/logo/vaxten/`)
- `site/` – det Netlify publicerar (se `netlify.toml`)

Uppdatera: ändra `src/grostund.html`, kör `python3 tools/build_app.py`, committa och pusha till `main`.

## iPhone-app (Capacitor)

`site/` paketeras som iOS-app med Capacitor (`capacitor.config.json`, mappen `ios/`). Kräver Node och Xcode.

1. `npm install` (första gången)
2. `npx cap sync ios` (kopierar `site/` in i appen, kör efter varje ändring)
3. `npx cap open ios` öppnar Xcode. Välj en iPhone-simulator upptill och tryck på ▶.
