from app import app
from app.spotify.spotifyHelper import auth_token, search_artist, search_track


@app.route('/spotify')
def spotify():
    auth_token()
    return {}

@app.route('/spotify/search_track')
def searchTrack():
    return search_track('young wild and free')

@app.route('/spotify/search_artist')
def searchArtist():
    return search_artist('jarabe de palo')