import requests
import time

# --- CONFIGURAZIONE ---
TOKEN_TELEGRAM = "8627721392:AAGgEc5BoH3ctVKRSMPXcLLSjOo9UJYCUU0"
ID_CHATTATELEGRAM = "81176546"
API_KEY_FOOTBALL = "75ad622ad3094500be996ee5addfa018"

def analizza():
    # Usiamo l'endpoint standard che di solito non viene bloccato
    url = "https://v3.football.api-sports.io/fixtures"
    params = {"live": "all"}
    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': API_KEY_FOOTBALL
    }
    
    try:
        print("Tentativo di connessione...")
        r = requests.get(url, headers=headers, params=params, timeout=10)
        data = r.json()
        partite = data.get('response', [])
        
        print(f"Risposta ricevuta! Partite trovate: {len(partite)}")
        
        for m in partite:
            casa = m['teams']['home']['name']
            minuto = m['fixture']['status']['elapsed']
            # Se trova almeno una partita, mandiamo un test su Telegram
            if minuto > 1:
                print(f"Match trovato: {casa} al minuto {minuto}")
                # Qui poi il bot farà i suoi calcoli...
                
    except Exception as e:
        print(f"Errore di connessione: {e}")

# Test immediato
analizza()
