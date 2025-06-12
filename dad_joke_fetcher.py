import waveassist
import requests

waveassist.init()

response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'text/plain'})
response.raise_for_status()

joke = response.text.strip()
waveassist.store_data('joke', joke)