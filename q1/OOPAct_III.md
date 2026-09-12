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

The association between the ALBUM and SONGS classes is a structural containment relationship where an album acts as a collection container for individual track objects. Rather than operating in isolation, the two classes collaborate to model a real-world music catalog where the ALBUM class manages track listings, displays combined details, and computes aggregate metrics like overall runtime.

### What multiplicity did you choose and why?

The multiplicity chosen for this relationship is 1 (ALBUM) to 0..* (SONGS) because a single album instance can hold zero or multiple song objects. This reflects practical logic: an album can exist as an empty container upon initialization before any tracks are assigned, or it can hold an arbitrary number of tracks as song instances are appended over time.

### How did you implement the relationship in Python?

In Python, this relationship was implemented by initializing a private list attribute, self.__SONGS_LIST, inside the ALBUM class constructor and defining an ADD_SONG(self, song: SONGS) method. Instead of passing plain string or integer data, the ADD_SONG method accepts an actual SONGS instance as an argument and appends its object reference directly into the list.

### Why did you store an object reference instead of copying its data?

Storing actual object references instead of copying data fields ensures a single source of truth and preserves object behavior across the system. Any update to a SONGS object is immediately reflected when accessed through the ALBUM instance, and storing references allows the album to call methods directly on individual song objects while avoiding memory duplication.

### If your relationship uses many, why is a list appropriate?

A Python list is the most appropriate structure for the "many" side because it inherently maintains insertion order, which is essential for preserving an album's sequential tracklist. Furthermore, lists scale dynamically as songs are added or removed, and they allow simple iteration using loops to execute operations across all tracks, such as summing total durations or printing track details.
