import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests

client_id = 'b19960c****2437b9fb2e6dbb1d5***'
client_secret = '3819c***b6c9d46e689b72b36****'

token_url = 'https://accounts.spotify.com/api/token'
payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.post(token_url, data=payload, headers=headers)
if response.status_code == 200:
    token_info = response.json()
    access_token = token_info['access_token']
    print('Access Token:', access_token)
else:
    print('Failed to get access token:', response.status_code)
    print(response.json())
