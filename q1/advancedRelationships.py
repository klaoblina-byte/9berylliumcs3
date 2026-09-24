class VENUE_LOG:
    def __init__(self, stage_location: str, stage_type: str, recording_date: str, capacity: int):
        self.stage_location = stage_location
        self.stage_type = stage_type
        self.recording_date = recording_date
        self.capacity = capacity

    def get_log_details(self) -> str:
        return f"Location: {self.stage_location} | Type: {self.stage_type} | Date: {self.recording_date} | Capacity: {self.capacity:,}"


# Class for Dependency
class AUDIO_PLAYER:
    def output_audio(self, track_title: str):
        print(f"[AUDIO HARDWARE] Outputting audio signal for: '{track_title}'")


class SONGS:
    def __init__(self, title: str, song_artist: str, duration: int, playlistName: str, total_Listening_time: int):
        self.title = title
        self.song_artist = song_artist
        self.duration = duration
        self.__total_Listening_time = total_Listening_time
        self.__playlistName = playlistName

    def pause(self):
        print(f"Paused: {self.title} by {self.song_artist}")

    # STEP 8 DEPENDENCY: Accepts AUDIO_PLAYER object temporarily
    def start(self, player: AUDIO_PLAYER):
        print(f"Now playing: {self.title} by {self.song_artist}")
        player.output_audio(self.title)

    def searchSong(self):
        print(f"Searching for: {self.title} by {self.song_artist}")

    def calculateTotalListeningTime(self):
        self.__total_Listening_time += self.duration * 60
        return self.__total_Listening_time


class LIVE_TRACK(SONGS):
    def __init__(self, title: str, song_artist: str, duration: int, total_Listening_time: int, 
                 playlistName: str, stage_location: str, stage_type: str, recording_date: str, 
                 capacity: int, has_crowd_noise: bool):
        super().__init__(title, song_artist, duration, playlistName, total_Listening_time)

        self.venue_log = VENUE_LOG(stage_location, stage_type, recording_date, capacity)
        
        self.has_crowd_noise = has_crowd_noise

    def playLiveApplause(self):
        print(f"Playing live applause for: {self.title} by {self.song_artist} at {self.venue_log.stage_location} recorded on {self.venue_log.recording_date}")

    def displayLiveDetails(self):
        print("--- LIVE TRACK DETAILS ---")
        print(f"Title: {self.title}")
        print(f"Artist: {self.song_artist}")
        print(f"Duration: {self.duration} seconds")
        print(f"Log Info: {self.venue_log.get_log_details()}")
        print(f"Has Crowd Noise: {self.has_crowd_noise}")

# TEST RUN

print("=== Test 1 — Inheritance ===")
live_track_case = LIVE_TRACK(
    title="La La Lost You - Live at The Forum",
    song_artist="NIKI",
    duration=240,
    total_Listening_time=1200,
    playlistName="Live Concerts",
    stage_location="The Forum, LA",
    stage_type="Indoor Arena",
    recording_date="2023-10-15",
    capacity=17500,
    has_crowd_noise=True
)

print("Child object (LIVE_TRACK) accessing parent attributes directly:")
print(f"Parent Song Title: {live_track_case.title}")
print(f"Parent Song Artist: {live_track_case.song_artist}")
print(f"Parent Song Duration: {live_track_case.duration}")
print(f"Parent Method Call (pause):")
live_track_case.pause()
print()

print("=== Test 2 — Composition ===")
print("LIVE_TRACK contains VENUE_LOG:")
print(f"Venue Log inside Live Track: {live_track_case.venue_log.get_log_details()}\n")
print()

print("=== Test 3 — Dependency ===")
speaker = AUDIO_PLAYER()
live_track_case.start(speaker)
print()