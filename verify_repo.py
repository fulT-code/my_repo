#!/usr/bin/env python3
"""
Script per verificare l'integrità del repository Tachiyomi Extensions Fork
"""

import os
import json
from pathlib import Path

def check_file_exists(filepath, description):
    """Verifica se un file esiste"""
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        print(f"   ✅ {description}: {filepath} ({size:,} bytes)")
        return True
    else:
        print(f"   ❌ {description}: {filepath} - FILE MANCANTE")
        return False

def verify_repository():
    """Verifica l'integrità del repository"""
    print("🔍 Verifica integrità repository Tachiyomi Extensions Fork")
    print("=" * 70)
    
    errors = 0
    
    # Verifica file principali
    print("\n📄 File di documentazione:")
    files_to_check = [
        ("README.md", "Documentazione principale"),
        ("CHANGELOG.md", "Registro modifiche"),
        ("INSTALLAZIONE.md", "Guida installazione"),
        (".gitignore", "File gitignore"),
    ]
    
    for filepath, description in files_to_check:
        if not check_file_exists(filepath, description):
            errors += 1
    
    # Verifica file di configurazione
    print("\n⚙️ File di configurazione:")
    config_files = [
        ("build.gradle.kts", "Build script principale"),
        ("settings.gradle.kts", "Configurazione Gradle"),
        ("repo.json", "Metadata repository"),
        ("index.json", "Indice estensioni"),
    ]
    
    for filepath, description in config_files:
        if not check_file_exists(filepath, description):
            errors += 1
    
    # Verifica APK
    print("\n📦 File APK:")
    apk_files = [
        ("extensions/apk/tachiyomi-en.asurascans-v1.4.47.apk", "AsuraScans APK"),
        ("extensions/apk/tachiyomi-fr.reaperscans-v1.4.21.apk", "ReaperScans APK"),
        ("extensions/apk/tachiyomi-it.lupiteam-v1.4.6.apk", "LupiTeam APK"),
    ]
    
    for filepath, description in apk_files:
        if not check_file_exists(filepath, description):
            errors += 1
    
    # Verifica icone
    print("\n🎨 Icone estensioni:")
    icon_files = [
        ("extensions/icon/eu.kanade.tachiyomi.extension.en.asurascans.png", "AsuraScans Icon"),
        ("extensions/icon/eu.kanade.tachiyomi.extension.fr.reaperscans.png", "ReaperScans Icon"),
        ("extensions/icon/eu.kanade.tachiyomi.extension.it.lupiteam.png", "LupiTeam Icon"),
    ]
    
    for filepath, description in icon_files:
        if not check_file_exists(filepath, description):
            errors += 1
    
    # Verifica codice sorgente
    print("\n💻 Codice sorgente:")
    source_files = [
        ("extensions/asurascans/src/eu/kanade/tachiyomi/extension/en/asurascans/AsuraScans.kt", "AsuraScans Source"),
        ("extensions/reaperscans/src/eu/kanade/tachiyomi/extension/fr/reaperscans/ReaperScans.kt", "ReaperScans Source"),
        ("extensions/lupiteam/src/eu/kanade/tachiyomi/extension/it/lupiteam/LupiTeam.kt", "LupiTeam Source"),
    ]
    
    for filepath, description in source_files:
        if not check_file_exists(filepath, description):
            errors += 1
    
    # Verifica JSON
    print("\n🔧 Validazione JSON:")
    json_files = ["repo.json", "index.json"]
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                json.load(f)
            print(f"   ✅ {json_file}: JSON valido")
        except json.JSONDecodeError as e:
            print(f"   ❌ {json_file}: JSON non valido - {e}")
            errors += 1
        except FileNotFoundError:
            print(f"   ❌ {json_file}: File non trovato")
            errors += 1
    
    # Statistiche finali
    print("\n" + "=" * 70)
    if errors == 0:
        print("🎉 Repository verificato con successo! Tutto è in ordine.")
        print("\n📊 Statistiche:")
        print(f"   • 3 estensioni pronte")
        print(f"   • 3 file APK disponibili")
        print(f"   • 3 icone incluse")
        print(f"   • Codice sorgente completo")
        print(f"   • Documentazione completa")
        
        print("\n🚀 Prossimi passi:")
        print("   1. Trasferisci i file APK sul tuo dispositivo Android")
        print("   2. Installa le estensioni seguendo INSTALLAZIONE.md")
        print("   3. Testa le estensioni in Tachiyomi/Mihon")
        print("   4. Aggiorna il codice se necessario")
        
    else:
        print(f"⚠️  Trovati {errors} errori nel repository!")
        print("   Controlla i file mancanti e risolvi i problemi.")
    
    return errors == 0

if __name__ == "__main__":
    verify_repository()