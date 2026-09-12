# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/classObjectUML.md)

## Design Revision

Changes from my previous design:
- Added a method called calculateTotal(minutes: int)
- Added a method called searchSong()
- Added the attribute Name of Playlist
- Added the method changePlaylistName()
- Removed skip() method
- Removed fastForward() method
- Removed Top Song, Top Artist, and Favorite Genre attributes

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

[Test Run](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/images/imagesclassTestRun.png.png)

## Object Diagram
[Object Diagram](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/images/MODIFIED%20DIAGRAM_Oblina%20(3).png)

## Analysis

### Why did you make your chosen attribute private?

Out of 5 attributes I chose 2 of them to be private. Specifically, the ones I chose are the name of the playlist and the total amount of listening time. I made the total amount of listening time private because it are part of individual user activity and personal usage habits. Moreover, I made the name of the playlist private so that users can freely make playlist and name them, without the fear of getting judged.

### Which method changes the state of your object?

The method that changes the state of my object is the changePlaylistName(). It changes the name of the playlist wherein a specific song is part of.

### How did your two objects demonstrate that instances are independent?

The outputs or the state of each object demonstrated that instances are independent by showing that when the playlist name of object1 was changed, it did not change the playlist name where object 2 is a part of.

### What is the difference between your class diagram and your object diagram?

The main difference of my class diagram between my object diagram is it's components. My class diagram is composed of the blueprint, while my object diagram is composed of the outputs of each diagram when the blueprint is applied. The connections in a class diagram define structural relationships like inheritance or association between classes. In an object diagram, these relationships are realized as "links," which show how actual pieces of data are connected in memory.
