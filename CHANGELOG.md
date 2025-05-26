# Changelog

Tutte le modifiche importanti a questo progetto saranno documentate in questo file.

## [1.0.0] - 2025-05-26

### Aggiunto
- Fork iniziale del progetto Tachiyomi
- Estensione AsuraScans v1.4.47 (Inglese)
  - URL base: https://asuracomic.net
  - API: https://gg.asuracomic.net/api
  - Supporto per URL dinamici
  - Filtri avanzati per generi, stato e tipo
  - Opzione per nascondere capitoli premium
  - Supporto immagini ad alta qualità
- Estensione ReaperScans v1.4.21 (Francese)
  - URL base: https://reaper-scans.fr
  - Basato su framework Keyoapp
  - Migrato da Madara (versionId = 4)
- Estensione LupiTeam v1.4.6 (Italiano)
  - URL base: https://lupiteam.net
  - Basato su framework PizzaReader
  - versionId = 2
- Script di test per verificare connettività siti
- Documentazione completa (README.md)
- File di configurazione per build system
- Metadata repository (repo.json, index.json)

### Testato
- ✅ AsuraScans: Sito e API raggiungibili
- ✅ ReaperScans: Sito raggiungibile
- ✅ LupiTeam: Sito raggiungibile

### Note
- Tutte le estensioni sono state verificate come funzionanti alla data di creazione
- I file APK sono pronti per l'installazione diretta
- Il codice sorgente è disponibile per modifiche future