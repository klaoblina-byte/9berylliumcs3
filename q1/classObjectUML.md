# SG4 - Understanding Classes and Objects
## SONGS
## My class represents the songs that the user is currently playing and represents its details: title of the song, duration of the song, and song artist. It also gets the user's total amount of listening time, their top songs and artist, and favorite genre every month.

## Properties
| Property | Data Type | Description |
|---|---|---| 
| Title | string | Title of the Song |
| Duration | int | How long is the duration of the song |
| Song Artist | string | The one who performs and the person who created/composed the song |
| Total Amount of Listening Time  | int | The total amount of minutes the user spent listening to music |
| Top Song | string | The song that was listened/repeated the most amount of times |
| Top Artist | string | The artist the user listened to the most |
| Favorite Genre | string | The genre that the user favors (ex. Rock, Classical, OPM, HipHop, etc.) |

## Methods
| Method | Description |
|---|---|
| skip() | Skips the song that is playing |
| fastForward() | Changes the speed of the song or the specific part that is playing |
| pause() | Pauses or stops the current song |
| start() | Starts the song |

## Class Diagram
![Class Diagram](q1/classDiagram.png)

## Design Explanation

### Why did you choose this class?

Before choosing the class, I first thought of a context I'm interested in. With that, I chose music. I often listen to music before going to sleep, while preparing, during study period, and whenever I need to write something, it helps me make my thoughts and ideas organized. In short, it has become a part of my life and I simply do not imagine a world where my soul is not deeply rooted to music. To answer your question, choosing "Songs" as my class allows me to connect academics to something that gives my life harmony. 

### Which property is the most important? Why?

The most important property among the given properties is the title. A song simply cannot exist without a title. It defines the fundamental identity of the object. Additionally, it is the primary way that users and systems can identify and distinguish one song from another. 

### Which method is the most useful? Why?

In this case, the most useful and critical method is start(). It serves as the entry point which triggers the initial state change of the audio stream. Without it, the three other methods become useless. The user cannot skip, fast forward, and pause a song that has not yet begun playing.
