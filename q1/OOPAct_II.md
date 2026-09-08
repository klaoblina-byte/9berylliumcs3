# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/classObjectUML.md)

## Design Revision

Changes from my previous design:
- Added a method called calculateTotal(minutes: int)
- Added a method called searchSong()
- Removed fastForward() method
- Removed Top Song, Top Artist, and Favorite Genre attributes
- Added the attribute Name of Playlist
- Added the method addSong()
- Removed skip() method

## Visibility Decisions

| Attribute | Data Type | Visibility | Why Public/Private? |
|---|---|---|---|
| Title | string | Public | Every user needs to see the song title to search for, display, or play it. | 
| Duration | int |Public | This is a fixed physical length of the audio file. It is universal track information that does not change regardless of who listens to it. | 
| Song Artist | string | Public | This is public credit/metadata identifying who performed or created the track. It must be accessible globally so users can find music by artist. | 
| Total Amount of Listening Time | int | Private | This measures individual user activity and personal usage habits. Because it tracks private behavior on an account, it is sensitive personal data that shouldn't be publicly exposed. | 
| Name of Playlist | String | Private | Users can create and name playlists with privacy and without the fear of getting judged. |

### Updated UML Class Diagram
[Class Diagram](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/classDiagram.png)

## Python Implementation

[View Python Source](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/classImplementation.py)

## Test Run

[Test Run](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/imagesclassTestRun.png.png)

## Object Diagram


