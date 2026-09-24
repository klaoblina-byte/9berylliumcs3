class SONGS:
    def __init__(self, title, song_artist, duration, playlistName, total_Listening_time):
        self.title = title
        self.song_artist = song_artist
        self.duration = duration
        self.__total_Listening_time = total_Listening_time
        self.__playlistName = playlistName

def pause(self):
        print(f"Paused: {self.title} by {self.song_artist}")

def start(self):
        print(f"Now playing: {self.title} by {self.song_artist}")

def searchSong(self):
        print(f"Searching for: {self.title} by {self.song_artist}")

def calculateTotalListeningTime(self):
        self.__total_Listening_time += self.duration * 60
        return self.__total_Listening_time


class LIVE_TRACK(SONGS):
    def __init__(self, title: str, song_artist: str, duration: int, total_Listening_time: int, playlistName: str, venue_name: str, recording_date: str, has_crowd_noise: bool):
            super().__init__(title, song_artist, duration, playlistName, total_Listening_time)
            self.venue_name = venue_name
            self.recording_date = recording_date
            self.has_crowd_noise = has_crowd_noise

def playLiveApplause (self):
    print(f"Playing live applause for: {self.title} by {self.song_artist} at {self.venue_name} recorded on {self.recording_date}")

def displayLiveDetails(self):
    print("--- LIVE TRACK DETAILS ---")
    print(f"Title: {self.title}")
    print(f"Artist: {self.song_artist}")
    print(f"Duration: {self.duration} seconds")
    print(f"Venue: {self.venue_name}")
    print(f"Recording Date: {self.recording_date}")
    print(f"Has Crowd Noise: {self.has_crowd_noise}")