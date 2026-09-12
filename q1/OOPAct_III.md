# Class Relationships: Association and Multiplicity
## Previous Work

[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
Class: SONGS
Description: The SONGS class represents an individual song in a music application. It stores important information about the song, such as its title, duration, artist, total listening time, and playlist. It also allows the user to perform actions such as playing, pausing, displaying song details, changing the playlist, and calculating listening time. 

### Which existing attributes and methods will still be useful when it interacts with another class?
The title, song_artist, duration, total_Listening_time, and playlistName attributes will remain useful. The display_details(), calculate_total_listening_time(), playSong(), pauseSong(), and change_playlist_name() methods can also be used when the SONGS class interacts with the ALBUM class.

## New Related Class
Class: ALBUM
Description: The ALBUM class represents a collection of songs released together by an artist. It can store information about the album and manage the songs included in it. The class can also perform actions such as adding or removing songs, displaying the songs in the album, and calculating the album's total duration.


### Why should these two classes be connected?

The SONGS and ALBUM classes should be connected because an album is made up of multiple songs. The SONGS class stores information about each individual song, such as its title, artist, and duration, while the ALBUM class organizes and manages those songs as a collection. This connection allows the ALBUM class to add, remove, display, and manage the songs belonging to it. It also allows the album to use the song information, such as calculating the total duration of all songs in the album.

## Association
Relationship: ALBUM contains SONGS
Explanation: The ALBUM and SONGS classes are connected because an album contains multiple songs. The SONGS class represents individual songs, while the ALBUM class organizes those songs as a collection. This relationship allows the album to manage its songs, such as adding, removing, and displaying them.

## Multiplicity
Multiplicity: One-to-Many ALBUM 1───────── 0..* SONGS
Explanation: This multiplicity fits because one album can contain zero or more songs, depending on the songs added to it. The ALBUM class can store multiple SONGS objects in a Python list, allowing it to organize and manage the songs in the album.

## UML Class Relationship Diagram
[Class Relationship Diagram](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source]([classRelationships.py](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/classRelationships.py))

## Test Run
[Relationship Test Run](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/images/relationshipTestRun.png)

## Object Relationship Diagram
[Object Relationship Diagram](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/images/objectRelationshipDiagram.png)

## Analysis

### What is the association between your two classes?

The association between the ALBUM and SONGS classes is a containment relationship where an album acts as a container for track objects. Rather than operating in isolation, the two classes collaborate to model a real-world music catalog. The ALBUM class manages track listings, displays combined details, and computes the overall amount of minutes in a playlist, while the SONGS class manages the details of individual songs, such as title, artist, duration.

### What multiplicity did you choose and why?

The multiplicity chosen for this relationship is 1 (ALBUM) to 0..* (SONGS) because a single album can hold zero or multiple song objects. This relationship accurately mirrors how music is produced and organized in the real world. By defining the connection this way, it ensures structural integrity which allows the system to easily query all songs associated with a unique album and can easily simplify data.

### How did you implement the relationship in Python?

In Python, this relationship was implemented by initializing a private list attribute, self.__SONGS_LIST, inside the ALBUM constructor. An ADD_SONG(self, song: SONGS) method was then created to establish the direct connection between objects. Instead of passing plain string or integer data, this method accepts an actual SONGS instance and appends its object reference into the list.

### Why did you store an object reference instead of copying its data?

Storing actual object references instead of copying data fields maintains a single source of truth across the system. Any update to a SONGS object is immediately reflected when accessed through the ALBUM instance. Furthermore, referencing the full object preserves behavioral functionality, allowing the album to call methods directly on individual song objects while avoiding memory duplication.

### If your relationship uses many, why is a list appropriate?

A Python list is the most appropriate structure for the "many" side because it inherently maintains insertion order, which is essential for preserving an album's sequential tracklist. Additionally, lists scale dynamically as songs are added or removed from the collection. They also enable simple iteration using loops to execute operations across all tracks, such as summing total durations or printing song details.
