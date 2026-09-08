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