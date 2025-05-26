# Tachiyomi Extensions Fork

Questo è un fork personalizzato del progetto Tachiyomi che contiene estensioni aggiornate per alcuni siti di manga specifici.

## Estensioni Incluse

### 1. AsuraScans (Inglese)
- **File APK**: `extensions/apk/tachiyomi-en.asurascans-v1.4.47.apk`
- **Codice sorgente**: `extensions/asurascans/`
- **URL base**: `https://asuracomic.net`
- **API URL**: `https://gg.asuracomic.net/api`
- **Stato**: ✅ Funzionante (versione 1.4.47)

### 2. ReaperScans (Francese)
- **File APK**: `extensions/apk/tachiyomi-fr.reaperscans-v1.4.21.apk`
- **Codice sorgente**: `extensions/reaperscans/`
- **URL base**: `https://reaper-scans.fr`
- **Stato**: ✅ Funzionante (versione 1.4.21)
- **Note**: Utilizza il framework Keyoapp

### 3. LupiTeam (Italiano)
- **File APK**: `extensions/apk/tachiyomi-it.lupiteam-v1.4.6.apk`
- **Codice sorgente**: `extensions/lupiteam/`
- **URL base**: `https://lupiteam.net`
- **Stato**: ✅ Funzionante (versione 1.4.6)
- **Note**: Utilizza il framework PizzaReader

## Installazione

### Metodo 1: Installazione diretta APK
1. Scarica i file APK dalla cartella `extensions/apk/`
2. Installa i file APK sul tuo dispositivo Android
3. Aggiungi le estensioni in Tachiyomi/Mihon

### Metodo 2: Compilazione dal codice sorgente
1. Clona questo repository
2. Apri il progetto in Android Studio
3. Compila le estensioni che ti interessano
4. Installa gli APK generati

## Struttura del Progetto

```
my_repo/
├── extensions/
│   ├── apk/                    # File APK pronti per l'installazione
│   ├── icon/                   # Icone delle estensioni
│   ├── asurascans/            # Codice sorgente AsuraScans
│   ├── reaperscans/           # Codice sorgente ReaperScans
│   └── lupiteam/              # Codice sorgente LupiTeam
└── README.md
```

## Note Tecniche

### AsuraScans
- Utilizza un sistema di URL dinamici per evitare errori 404
- Supporta filtri avanzati (generi, stato, tipo)
- Ha opzioni per nascondere capitoli premium
- Supporta immagini ad alta qualità

### ReaperScans
- Basato sul framework multisrc Keyoapp
- Migrato da Madara a Keyoapp (versionId = 4)
- Supporta parsing personalizzato per descrizioni e generi

### LupiTeam
- Basato sul framework multisrc PizzaReader
- Implementazione semplice e diretta
- versionId = 2

## Aggiornamenti

Per aggiornare le estensioni:

1. Controlla se ci sono nuove versioni nel repository originale
2. Aggiorna il codice sorgente se necessario
3. Testa le modifiche
4. Compila nuovi APK
5. Aggiorna la documentazione

## Compatibilità

Queste estensioni sono compatibili con:
- Tachiyomi (versioni recenti)
- Mihon (fork di Tachiyomi)
- Altri fork compatibili con le estensioni Tachiyomi

## Disclaimer

Questo fork è creato per uso personale e educativo. Rispetta sempre i termini di servizio dei siti web e le leggi sul copyright del tuo paese.

## Crediti

- Progetto Tachiyomi originale
- Community Keiyoushi per le estensioni aggiornate
- Sviluppatori delle estensioni specifiche