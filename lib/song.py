class Song:
    
    count = 0
    genres = []  
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.append(genre) 
        Song.artists.append(artist)
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1 
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
    
    def get_count(self):
        return Song.count
    
    def add_to_genres(self, genre):
        Song.genres.append(genre) 

    def add_to_artists(self, artist):
        Song.artists.append(artist)

    def add_to_genre_count(self, genre):
        Song.genres.append(genre)

    def add_to_artists_count(self, artist):
        Song.artists.append(artist)