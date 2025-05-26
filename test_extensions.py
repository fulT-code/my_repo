#!/usr/bin/env python3
"""
Script per testare la connettività delle estensioni Tachiyomi
"""

import requests
import json
from urllib.parse import urljoin

def test_website_connectivity(name, base_url, api_url=None):
    """Testa la connettività di un sito web"""
    print(f"\n🔍 Testando {name}...")
    print(f"   URL base: {base_url}")
    
    try:
        # Test connessione base
        response = requests.get(base_url, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        if response.status_code == 200:
            print(f"   ✅ Sito principale raggiungibile (Status: {response.status_code})")
        else:
            print(f"   ⚠️  Sito principale risponde con status: {response.status_code}")
            
        # Test API se disponibile
        if api_url:
            print(f"   API URL: {api_url}")
            try:
                api_response = requests.get(f"{api_url}/series/filters", timeout=10, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    'Referer': f"{base_url}/"
                })
                if api_response.status_code == 200:
                    print(f"   ✅ API raggiungibile (Status: {api_response.status_code})")
                else:
                    print(f"   ⚠️  API risponde con status: {api_response.status_code}")
            except Exception as e:
                print(f"   ❌ Errore API: {str(e)}")
                
    except Exception as e:
        print(f"   ❌ Errore connessione: {str(e)}")

def main():
    print("🚀 Test di connettività per le estensioni Tachiyomi")
    print("=" * 60)
    
    # Configurazione estensioni
    extensions = [
        {
            "name": "AsuraScans",
            "base_url": "https://asuracomic.net",
            "api_url": "https://gg.asuracomic.net/api"
        },
        {
            "name": "ReaperScans",
            "base_url": "https://reaper-scans.fr",
            "api_url": None
        },
        {
            "name": "LupiTeam",
            "base_url": "https://lupiteam.net",
            "api_url": None
        }
    ]
    
    # Test ogni estensione
    for ext in extensions:
        test_website_connectivity(ext["name"], ext["base_url"], ext.get("api_url"))
    
    print("\n" + "=" * 60)
    print("✨ Test completato!")

if __name__ == "__main__":
    main()