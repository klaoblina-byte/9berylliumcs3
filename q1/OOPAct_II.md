# OOPAct Part II

## Step 1
## Design Revision

Changes from my previous design:
- Added a method called calculateTotal(minutes: int)
- Added a method called searchSong()
- Removed fastForward() method
- Removed Top Song, Top Artist, and Favorite Genre attributes
- Added the attribute Name of Playlist
- Added the method addSong()

## Step 2

| Attribute | Data Type | Visibility | Why Public/Private? |
|---|---|---|---|
| Title | string | Public | Every user needs to see the song title to search for, display, or play it. | 
| Duration | int |Public | This is a fixed physical length of the audio file. It is universal track information that does not change regardless of who listens to it. | 
| Song Artist | string | Public | This is public credit/metadata identifying who performed or created the track. It must be accessible globally so users can find music by artist. | 
| Total Amount of Listening Time | int | Private | This measures individual user activity and personal usage habits. Because it tracks private behavior on an account, it is sensitive personal data that shouldn't be publicly exposed. | 
| Name of Playlist | String | Private | Users can create and name playlists with privacy and without the fear of getting judged. |

## Step 3

### MODIFIED UML DIAGRAM
[Modified UML Diagram]{https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/classDiagram.png}

## Step 4 - Step 6

