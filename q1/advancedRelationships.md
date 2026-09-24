# Advanced Class Relationships

## Previous Activities

[classAttrib](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/classAttributesMethods.md)

[classRel](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/OOPAct_III.md)

## Existing System Description:

### What classes currently exist in your system?

Class 1: SONGS

Class 2: ALBUM

###  What problem or limitation exists in your current design?

A constraint in my existing design is unclear ownership between the ALBUM and SONGS classes. The ALBUM class contains the song objects, while the SONGS class is unaware of which album it belongs to. This can make it unclear regarding whether a song can be part of multiple albums or just a single album. The ALBUM class currently exclusively manages the relationship through its list of songs.

## Inheritance Relationship

Parent: SONGS

Child: LIVE_TRACK

Explanation: A LIVE_TRACK IS-A SONGS item because it carries a title, duration, artist, and play history. It specializes the parent class by storing concert-specific data like concert  venue, recording date, and crowd noise level.

## Inheritance UML
[Inheritance](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/images/inheritanceDiagram.png)

## Composition/Aggregation
Relationship: Composition

Class containing another object: LIVE_TRACK

Contained object: VENUE_LOG

Explanation: A Composition relationship exists because a LIVE_TRACK creates a VENUE_LOG object to store specific details about the recording of the concert, such as stage location, stage type, recording date, and capacity. This venue log is bound strictly to that specific live performance instance; if the LIVE_TRACK object is deleted, its corresponding VENUE_LOG object is immediately removed.

## Advanced UML Diagram
[Advanced UML](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/images/advancedClassDiagram.png)

## Python Implementation
[Source Code](advancedRelationships.py)

## Test Run
[Test](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/images/advancedTestRun.png)

## Object Diagram
![Objects](https://github.com/klaoblina-byte/9berylliumcs3/blob/main/q1/images/advancedObjectDiagram.png)

## Reflection

### Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.

I chose inheritance because a LIVE_TRACK is a specialized type of SONG. It satisfies the strict "IS-A" relationship by possessing every standard song characteristic, such as a title, artist, duration, and basic playback operations, while simply adding data related to concerts. This ensures a live track can seamlessly function anywhere a standard song is expected in the system.

### How did inheritance reduce duplicate code? Identify attributes or methods that were reused.

Inheritance eliminated the need to rewrite standard media attributes and methods inside LIVE_TRACK. Core attributes like title, song_artist, duration, playlistName, and __total_Listening_time are reused directly from the SONGS constructor using super().__init__(). Standard operational methods like pause(), searchSong(), and calculateTotalListeningTime() were also inherited without writing redundant code.

### Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.

The relationship is Composition because LIVE_TRACK directly embodies its VENUE_LOG inside its __init__ method. The VENUE_LOG cannot exist independently because its data only exists to describe that specific performance. If the LIVE_TRACK instance is deleted, its internal VENUE_LOG object is destroyed along with it.

### What is the difference between Association from Part III and the advanced relationship you implemented?

In Part III, the association between ALBUM and SONGS was a loose containment (aggregation) where song objects existed independently and were simply referenced in a list managed by the album. In contrast, the advanced Composition relationship strictly binds the VENUE_LOG instance to its parent LIVE_TRACK, meaning the venue log is created internally and cannot exist independently if the track is deleted. Additionally, the new Dependency relationship allows LIVE_TRACK to temporarily interact with an external AUDIO_PLAYER hardware object during method execution without storing or owning it long-term.

### How does your design follow the DRY principle?

The design avoids code duplication by centralizing shared media properties and methods within the parent SONGS class. It isolates venue metadata into a single dedicated VENUE_LOG class rather than scattering venue attributes across multiple song definitions. Finally, using Dependency allows all track types to route audio through a single, shared AUDIO_PLAYER class without duplicating playback code.
