import lyricsgenius


class Song:
    def __init__(self, band: str, album: str, song: str, genius: lyricsgenius.Genius, current_ms: int, total_ms: int):
        self.band = band
        self.album = album
        self.song = song
        self.genius = genius
        self.current_ms = current_ms
        self.total_ms = total_ms

    def __eq__(self, other):
        if self.band == other.band and self.album == other.album and self.song == other.song:
            return True
        return False

    def getLyrics(self):
        return self.genius.search_song(self.song, self.band).lyrics

    def __repr__(self):
        return f'band: {self.band}, album: {self.album}, song name: {self.song}'

    def getPercent(self):
        return self.total_ms / self.current_ms
