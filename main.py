import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import lyricsgenius
genius = lyricsgenius.Genius("my_client_access_token_here")
load_dotenv(dotenv_path="client.env")
client_id = os.getenv('id')
client_secret = os.getenv('secret')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="https://localhost:8080/callback/",
                                               scope="user-library-read user-read-currently-playing"))

results = sp.current_user_playing_track()
item = results['item']
albumData = item['album']
artist = albumData['artists'][0]['name']
albumName = albumData['name']
songName = item['name']
print(f'band name: {artist}\nalbum name: {albumName}\nsong name: {songName}')
song = genius.search_song(songName, artist)
print(song.lyrics)
