from os import getenv
from typing import Set
from requests import get, post
from base64 import b64encode

AUTH_ENDPOINT = 'https://accounts.spotify.com/api/token'
SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'



def auth_token():
    client_id = getenv('SPOTIFY_CLIENT_ID')    
    secret_id = getenv('SPOTIFY_CLIENT_SECRET')

    auth_client = f'{client_id}:{secret_id}'
    message = auth_client.encode('ascii')
    b64_token = b64encode(message)
    token = b64_token.decode('ascii')

    headers = {
        'Authorization' : f'Basic {token}'
    }

    data = {
        'grant_type' : 'client_credentials'
    }

    response = post(AUTH_ENDPOINT, headers=headers, data=data)
    print(response.json())
    return response.json()['access_token']


def search_track(track):
    headers = {
        'Authorization' : f'Bearer {auth_token()}'
    }

    params = {
        'q' : track,
        'type' : 'track'
    }

    response = get(SEARCH_ENDPOINT, headers=headers, params=params)
    return response.json()

def search_artist(artist):
    headers = {
        'Authorization' : f'Bearer {auth_token()}'
    }

    params = {
        'q' : artist,
        'type' : 'artist'
    }

    response = get(SEARCH_ENDPOINT, headers=headers, params=params)
    return response.json()