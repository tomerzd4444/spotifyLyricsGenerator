import spotipy
from Song import Song
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import lyricsgenius
import time
from tkinter import *
import tkinter.font as tkFont
from requests.exceptions import ConnectionError
root = Tk()
var = StringVar()
fontStyle = tkFont.Font(size=10)
label = Label(root, textvariable=var, relief=RAISED, font=fontStyle)
delay = 5  # seconds
load_dotenv(dotenv_path="client.env")
client_id = os.getenv('id')
client_secret = os.getenv('secret')
client_genius_secret = os.getenv('genius_secret')
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="https://localhost:8080/callback/",
                                               scope="user-library-read user-read-currently-playing"))


def changeText(text: str):
    newText = text.split('\n')
    print(newText)
    newText2 = ''
    for count, i in enumerate(newText):
        newText2 += i + ' '
        if count % 2 != 0:
            newText2 += '\n'
        print(count, count % 2)
    return newText2


def getSong(spotifyAccount: spotipy.Spotify):
    results = spotifyAccount.current_user_playing_track()
    item = results['item']
    albumData = item['album']
    artist = albumData['artists'][0]['name']
    albumName = albumData['name']
    songName = item['name']
    genius = lyricsgenius.Genius(client_genius_secret)
    return Song(artist, albumName, songName, genius, results['progress_ms'], item['duration_ms'])


while True:
    song1 = getSong(sp)
    print(song1.current_ms, song1.current_ms <= 2000)
    if song1.current_ms <= 2000:
        song1 = getSong(sp)
        lyrics = ''
        while lyrics == '':
            try:
                lyrics = song1.getLyrics()
            except ConnectionError as e:
                print(e)
                time.sleep(0.5)
        var.set(changeText(lyrics))
        label.pack()
    root.update_idletasks()
    root.update()
