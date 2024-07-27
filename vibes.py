import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials


class Vibes:
    def __init__(self, ID, SECRET):
        self.spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=ID, client_secret=SECRET))

    def artistStats(self, artist: str):
        artist = self.spotify.search(q=artist, type="artist", limit=1)["artists"]["items"][0]
        followers = artist["followers"]["total"]
        genres = artist["genres"]
        popularity = artist["popularity"]
        ID = artist["id"]
        return (followers, genres, popularity, artist['images'][0]['url'], ID)
    
    def artistTopTracks(self, ID: str, country: str = "US"):
        tracks = self.spotify.artist_top_tracks(ID, country)['tracks']
        songs, popularity, album, duration, explicit = [], [], [], [], []
        for t in range(len(tracks)):
            songs.append(tracks[t]["name"])
            popularity.append(tracks[t]["popularity"])
            duration.append(self.__convert__(tracks[t]["duration_ms"]))
            
            if tracks[t]["explicit"] == True:
                explicit.append("Explicit")
            else:
                explicit.append("Not Explicit")
            
            if tracks[t]['album']['album_type'] != "single":
                album.append(tracks[t]["album"]["name"])
            else:
                album.append("Single")
            
        return songs, popularity, album, duration, explicit
    
    def artistAlbums(self, ID: str):
        albums = self.spotify.artist_albums(ID)['items']
        names, release, tracks = [], [], []
        for a in range(len(albums)):
            if albums[a]['album_type'] == "single":
                continue
            else:
                names.append(albums[a]['name'])
                release.append(albums[a]['release_date'])
                tracks.append(albums[a]['total_tracks'])
            
        return names, release, tracks
    
    def __convert__(self, ms: int):
        sec = ms // 1000
        min = sec // 60
        return f"{min}:{sec % 60}"

load_dotenv()
ID, SECRET = os.getenv("ID"), os.getenv("SECRET")
