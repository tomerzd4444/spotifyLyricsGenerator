import spotipy
from Song import Song
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import lyricsgenius
import time

delay = 5  # seconds
load_dotenv(dotenv_path="client.env")
client_id = os.getenv('id')
client_secret = os.getenv('secret')
client_genius_secret = os.getenv('genius_secret')
genius = lyricsgenius.Genius(client_genius_secret)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="https://localhost:8080/callback/",
                                               scope="user-library-read user-read-currently-playing"))


def getSong(spotifyAccount: spotipy.Spotify):
    results = spotifyAccount.current_user_playing_track()
    item = results['item']
    albumData = item['album']
    artist = albumData['artists'][0]['name']
    albumName = albumData['name']
    songName = item['name']
    return Song(artist, albumName, songName, genius, results['progress_ms'], item['duration_ms'])


while True:
    song1 = getSong(sp)
    print(song1.current_ms, song1.total_ms - 10, song1.current_ms >= song1.total_ms - 10)
    if song1.current_ms >= song1.total_ms - 10 or song1.current_ms <= 1000:
        time.sleep(1)
        song1 = getSong(sp)
        print(song1.getLyrics())
