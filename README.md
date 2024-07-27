# Vibes
**Musical Artist Information API**

## About
Vibes is an open-source API designed to retrieve information about a musical artist, including their songs and albums, using the `spotipy` library.

# Installation
Clone: `https://github.com/MG-Corp/Vibes.git`

# Documentation
     example = Vibes(ID, SECRET)
     stats = example.artistStats(artist)
     ID = stats[-1]
     print(stats)      -> Returns (followers, genres, popularity, artist picture, ID)
     print(example.artistTopTracks(ID))      -> Returns (songs, popularity, album, duration, explicit)
     print(example.artistAlbums(ID))      -> Returns (names, release, tracks)
