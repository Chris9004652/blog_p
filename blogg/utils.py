# blogg/utils.py

import requests
from django.conf import settings

def fetch_nyt_news():
    api_key = settings.NYT_API_KEY  # Make sure to set this in your settings.py
    url = f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data.get('results', [])
    except requests.RequestException as e:
        print(f"Error fetching NYT news: {e}")
        return []
