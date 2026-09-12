class SONGS:
    def __init__(self, title, song_artist, duration, playlistName, total_Listening_time):
        self.title = title
        self.song_artist = song_artist
        self.duration = duration
        self.__total_Listening_time = total_Listening_time
        self.__playlistName = playlistName

    def calculate_total_listening_time(self):
        self.__total_Listening_time += self.duration * 60
        return self.__total_Listening_time

    def calculateTotalListeningTime(self):
        return self.calculate_total_listening_time()

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Artist: {self.song_artist}")
        print(f"Duration: {self.duration} minutes")
        print(f"Total Listening Time: {self.__total_Listening_time} seconds")
        print(f"Playlist: {self.__playlistName}")

    def displaySongDetails(self):
        self.display_details()

    def change_playlist_name(self, new_playlist_name: str):
        self.__playlistName = new_playlist_name
        print(f"Playlist name changed to: {self.__playlistName}")

    def changePlaylistName(self, new_playlist_name: str):
        self.change_playlist_name(new_playlist_name)

    def playSong(self):
        playsong(self)

    def pauseSong(self):
        pauseSong(self)


songs = SONGS

def calculateTotalListeningTime(song: SONGS):
    return song.calculate_total_listening_time()

def displaySongDetails(song: SONGS):
    song.display_details()

def changePlaylistName(song: SONGS, new_playlist_name: str):
    song.change_playlist_name(new_playlist_name)

def playsong(song: SONGS):
    print(f"Now playing: {song.title} by {song.song_artist}")

def pauseSong(song: SONGS):
    print(f"Paused: {song.title} by {song.song_artist}")

#Objects
object1 = SONGS("Merry Christmas, Please Don't Call", "Bleachers", 3.21, "Christmas", 192.6)
object2 = SONGS("Merry Christmas, i miss you", "Alex Crichton", 4.06, "Christmas", 243.6)
object3 = SONGS("Thinking of You", "Katy Perry", 4.06, "Pop", 243.6)
object4 = SONGS("La La Lost You", "NIKI", 3.20, "Indie", 192.0)
object5 = SONGS("All I Need To Hear", "The 1975", 3.30, "Alternative", 198.0)

#Implementing Methods
print("SONGS")

calculateTotalListeningTime(object1)
print("--BEFORE--")
displaySongDetails(object1)
print()
displaySongDetails(object2)
print()

changePlaylistName(object1, "Holiday Hits")

print("--AFTER--")
displaySongDetails(object1)
print()
displaySongDetails(object2)
print()

playsong(object3)
print()
pauseSong(object3)

class ALBUM:
    def __init__(self, album_title: str, album_artist: str, release_year: int):
        self.ALBUM_TITLE = album_title
        self.ALBUM_ARTIST = album_artist
        self.RELEASE_YEAR = release_year
        self.__SONGS_LIST = []

    def ADD_SONG(self, song: SONGS):
        """Adds a song to the album list."""
        self.__SONGS_LIST.append(song)

    def REMOVE_SONG(self, title: str):
        """Removes a song from the album list by title."""
        self.__SONGS_LIST = [song for song in self.__SONGS_LIST if song.title != title]

    def DISPLAY_ALBUM_DETAILS(self):
        """Displays the details of the album and its songs."""
        print(f"Album Title: {self.ALBUM_TITLE}")
        print(f"Artist: {self.ALBUM_ARTIST}")
        print(f"Release Year: {self.RELEASE_YEAR}")
        print(f"Total Tracks: {len(self.__SONGS_LIST)}")
        print()
        print("TRACKLIST:")
        for idx, song in enumerate(self.__SONGS_LIST, 1):
            print(f"{idx}. {song.title} by {song.song_artist} - {song.duration} minutes")

    def CALCULATE_TOTAL_DURATION(self) -> float:
        print()
        """Calculates the total duration of all songs in the album."""
        total_duration = sum(song.duration for song in self.__SONGS_LIST)
        return total_duration

def playsong(song: SONGS):
    print(f"Now playing: {song.title} by {song.song_artist}")

def pauseSong(song: SONGS):
    print(f"Paused: {song.title} by {song.song_artist}")

#OBJECTS

album1 = ALBUM("Nicole", "NIKI", 2022)

song1 = SONGS("La La Lost You", "NIKI", 3.20, "Indie", 192.0)
song2 = SONGS("I Like U", "NIKI", 4.23, "Pop", 263.0)
song3 = SONGS("Take A Chance With Me", "NIKI", 5.03, "Indie", 303.0)
song4 = SONGS("Newsflash", "NIKI", 3.34, "R&B", 214.0)
song5 = SONGS("Paths", "NIKI", 3.45, "Acoustic", 225.0)
song6 = SONGS("The Apartment We Won't Share", "NIKI", 2.29, "Indie", 149.0)

#TEST RUN

print("---BEFORE RELATIONSHIP---")
print(f"Album created: {album1.ALBUM_TITLE} by {album1.ALBUM_ARTIST}")
print("Songs created independently:")
print(f"  - {song1.title}")
print(f"  - {song2.title}")
print(f"  - {song3.title}")
print(f"  - {song4.title}")
print(f"  - {song5.title}")
print(f"  - {song6.title}")

print()

print("---BUILDING RELATIONSHIP---")
print(f"Adding songs to album: {album1.ALBUM_TITLE}")
album1.ADD_SONG(song1)
album1.ADD_SONG(song2)
album1.ADD_SONG(song3)
album1.ADD_SONG(song4)
album1.ADD_SONG(song5)
album1.ADD_SONG(song6)
print("Relationship established. Songs are now part of the album.")

print()

print("---AFTER RELATIONSHIP---")
print(f"Accessing song details through album: {album1.ALBUM_TITLE}")

album1.DISPLAY_ALBUM_DETAILS()
print()

print(f"Total Duration of Album: {album1.CALCULATE_TOTAL_DURATION():.2f} minutes")

print()