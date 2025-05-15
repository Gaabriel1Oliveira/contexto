
import requests
from datetime import datetime

API_USERNAME = "d710b1de02b44b1"
API_PASSWORD = "xvtx3v01dt72c09"
BASE_URL = "https://api.tradingeconomics.com/calendar"

def fetch_important_events():
    today = datetime.utcnow().strftime("%Y-%m-%d")
    params = {
        'c': f'{API_USERNAME}:{API_PASSWORD}',
        'd1': today,
        'd2': today,
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        events = response.json()

        filtered = [
            e for e in events
            if e.get('country') in ['United States', 'Brazil'] and e.get('importance', 0) >= 2
        ]

        sorted_events = sorted(filtered, key=lambda e: e.get('date', ''))
        return sorted_events

    except Exception as e:
        print(f"Erro ao buscar eventos econômicos: {e}")
        return []
