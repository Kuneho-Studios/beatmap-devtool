# Project Radiance Beatmap Devtool

The Project Radiance Beatmap Devtool is a Python tool that significantly aids a user in creating a beatmap for a song in Project Radiance.
<br>
It is a no-code solution where the user will utilize prompts for the various available actions as well as entering numbers for beats and durations when prompted. They do not need to know or memorize the naming conventions or the available note types or lane configurations as they are all available on-demand in this tool.

## Installation
Ensure `Python` is present on the computer
* Recommend version at least 3.9
* Can download from their official website [here](https://www.python.org/downloads/)

Download the `ProjectRadianceBeatmapDevtool.exe`
* Can download from the GitHub page [here](https://github.com/Kuneho-Studios/beatmap-devtool/releases)

## Usage
Once `ProjectRadianceBeatmapDevtool.exe` is downloaded, it can be opened anywhere. 
<br><br>
**Please note that wherever the tool is run from is where the created files will be stored. If the devtool gets moved then it won't be able to find the files**
<br><br>
Upon opening, the user is shown the initial prompts where they can `create a new song` (this includes the necessary beatmap templates), `edit a song`, `update a beatmap` (this is where the majority of the devtool time will be spent), or `export a song`. These prompts branch into other prompts
* `Create a new song`
  *  User supplies the basic information needed for song creation. This includes "song name", "album name", "artist name", "beats per minute" (bpm), "genre", and all the "difficulties" desired
     * The user is initially asked how many "difficulties" they want, then will have to supply the "difficulty" value for each
       * Can read about the "difficulty" values and the guidelines for setting them in the ["Difficulty"]((#difficulty)) glossary section 
* `Edit a song`
  * `Copy beatmaps contents`
    * Takes the contents of the selected beatmap and will copy them over into another existing beatmap, or prompt to create a new one to copy the contents into
      * This could be useful when trying to make beatmaps for multiple difficulties and the user believes it would be easier to start with an existing beatmap for the song opposed to an empty file
  * `Update an existing beatmap's difficulty`
    * Used to change the difficulty level of an existing beatmap if the user decides to change the difficulty from when they first created the beatmap
  * `Edit an existing song's basic information`
    * Change any of the field values that were set when the user initially created the song 
* `Update a beatmap`
  * `Set beat`
    * Sets the current beat to the value supplied. All created, edited, and deleted notes will be on this beat
  * `Add note`
    * Add a note to a lane given the current beat's lane configuration 
  * `Edit note`
    * Edit an existing note on the current beat. Can edit the note type or its lane. Utilize `shift some notes` to directly move it or `delete note` and then `add note` to recreate it on a different beat
  * `Delete note`
    * Delete an existing note on the current beat 
  * `Shift some notes`
    * Starting at the current beat and ending at the beat specified, it will then shift all the notes that fall within that range by the amount of beats specified
    * The shift amount must begin with a `+` (to shift to higher/later beats) or a `-` (to shift to lower/earlier beats)
  * `Shift all notes`
    * Shifts all notes in the song by the amount of beats specified
    * The shift amount must begin with a `+` (to shift to higher/later beats) or a `-` (to shift to lower/earlier beats)
  * `Show all lane changes`
    * Displays all the lane changes that exist in the beatmap
    * Includes the beat where the swap occurs, the name of the lane configuration, as well as a visual depiction of what that looks like
      * Can read about the various lane configurations and depictions in the ["Lane Configurations and Variations"](#lane-configurations-and-variations) glossary section
  * `Copy some notes to another beat`
    * Starting at the current beat and ending at the beat specified, it will then copy all the notes that fall within that range and place them starting at another beat that will be specified
  * `Save`
    * Saves the current beatmap as-is 
    * Saves are automatically performed when the `Back` action is used too
* `Export a song`
  * After selecting the song via the prompts, all the song's files are placed into a zip file and can be downloaded to anywhere on the user's computer via the operating systems save menu that should pop up.

## Glossary
### Difficulty
To Project Radiance, increasing difficulty doesn't just mean that missed notes become more punishing. The game will play slightly differently amongst the difficulties and provide the users with different challenges. Not everyone starts at the same place as some might have a lot of rhythm game experience. No matter what, the goal is that at each difficulty, no matter the song, the player should expect similar conditions and upon "mastering" that difficulty level can move onto the next one and expect to use the skills they were honing in the previous difficulty, plus a little more. Whether that be some more obstacles, or more frequent lane changes, or more variations in notes, that is up to the beatmapper. At Project Radiance, we would like the player to feel the gradual increase in difficulty between the levels and not harsh jumps.

Difficulty is a numerical rating between 1 and 9. The general guidelines for determining what rating your beatmap should be placed under are as follow:

#### Difficulty 1
* Maximum lane count is 3
* Near tutorial-level beatmapping
* Limited obstacles
* Anybody should be able to complete it, or would have great success after little practice

#### Difficulty 2
* Maximum lane count is 3
* Limited lane changes
* Limited obstacles

#### Difficulty 3
* Maximum lane count is 3
* Works towards "mastery" of 3 lane configurations
* Limited lane changes
* Limited obstacles

#### Difficulty 4
* Maximum lane count is 4
* Introduction to the 4th lane and the new configurations that come with it (e.g. four corners)
* Limited lane changes
* Limited obstacles

#### Difficulty 5
* Maximum lane count is 4
* Moderate lane changes
* Moderate obstacles

#### Difficulty 6
* Maximum lane count is 4
* Works towards "mastery" of 4 lane configurations
* Moderate lane changes
* Moderate obstacles

#### Difficulty 7
* Maximum lane count is 5
* Introduction to the 5th lane and the new configurations that come with it (e.g. four corners with a middle, vertical lane)
* Moderate lane changes 
* Moderate obstacles

#### Difficulty 8
* Maximum lane count is 5
* "Maximum" lane changes
* "Maximum" obstacles

#### Difficulty 9
* Maximum lane count is 5
* Works towards "mastery" of the game
  * Highest difficulty and anything goes 
* "Maximum" lane changes
* "Maximum" obstacles


### Lane Configurations and Variations
One of Project Radiance's unique characteristics is for the lane configurations to have the ability to change throughout the song. As a result, there are many different lane configurations on offer in the devtool

For each `Lane Configuration`, there are different `Lane Variations` into how they are displayed. Not all lane sections are necessarily played the same way.

Below, for each lane configuration available, there will be some art depicted an example for each lane configuration. The `x` and a `lane number` can be interchanged to create new variations, but for the essence of not making this document to big, all will not be listed here (but are accessible in the devtool). The notes will move in the direction the arrow is facing and the lane number is placed where the strike zone would be. 

The names "left to right" or "top to bottom" indicate the direction in which the note is moving. Therefore, "left to right" would indicate the note is moving from the left of the screen over to the right, similary "top to bottom" is moving from the top of the screen to the bottom.
#### Two Lanes
* Two lanes left to right
```
╔═══════════════════╗
║           ---→ 1  ║
║           ---→ 2  ║
║           ---- x  ║
║           ---- x  ║
║           ---- x  ║
╚═══════════════════╝
```
* Two lanes right to left
```
╔═══════════════════╗
║  1 ←---           ║
║  2 ←---           ║
║  x ----           ║
║  x ----           ║
║  x ----           ║
╚═══════════════════╝
```

#### Four Lanes
* Four lanes top to bottom
```
╔═══════════════════╗
║                   ║
║   |  |  |  |  |   ║
║   |  |  |  |  |   ║
║   |  ↓  ↓  ↓  ↓   ║
║   x  1  2  3  4   ║
╚═══════════════════╝
```
* Four lanes bottom to top
```
╔═══════════════════╗
║   x  1  2  3  4   ║
║   |  ↑  ↑  ↑  ↑   ║
║   |  |  |  |  |   ║
║   |  |  |  |  |   ║
║                   ║
╚═══════════════════╝
```
* Four lanes left to right
```
╔═══════════════════╗
║           ---- x  ║
║           ---→ 1  ║
║           ---→ 2  ║
║           ---→ 3  ║
║           ---→ 4  ║
╚═══════════════════╝
```
* Four lanes right to left
```
╔═══════════════════╗
║  x ----           ║
║  1 ←---           ║
║  2 ←---           ║
║  3 ←---           ║
║  4 ←---           ║
╚═══════════════════╝
```
* Four corners
```
╔═══════════════════╗
║  1             4  ║
║   ↖           ↗   ║
║     >       <     ║
║   ↙           ↘   ║
║  2             3  ║
╚═══════════════════╝
```

#### Five Lanes
* Five lanes top to bottom
```
╔═══════════════════╗
║                   ║
║   |  |  |  |  |   ║
║   |  |  |  |  |   ║
║   ↓  ↓  ↓  ↓  ↓   ║
║   1  2  3  4  5   ║
╚═══════════════════╝
```
* Five lanes bottom to top
```
╔═══════════════════╗
║   1  2  3  4  x   ║
║   ↑  ↑  ↑  ↑  |   ║
║   |  |  |  |  |   ║
║   |  |  |  |  |   ║
║                   ║
╚═══════════════════╝
```
* Five lanes left to right
```
╔═══════════════════╗
║           ---→ 1  ║
║           ---→ 2  ║
║           ---→ 3  ║
║           ---→ 4  ║
║           ---→ 5  ║
╚═══════════════════╝
```
* Five lanes right to left
```
╔═══════════════════╗
║  1 ←---           ║
║  2 ←---           ║
║  3 ←---           ║
║  4 ←---           ║
║  5 ←---           ║
╚═══════════════════╝
```
* Four corners, middle lane top to bottom
```
╔═══════════════════╗
║  1             4  ║
║   ↖     |     ↗   ║
║     >   |   <     ║
║   ↙     ↓     ↘   ║
║  2      5      3  ║
╚═══════════════════╝
```
* Four corners, middle lane bottom to top
```
╔═══════════════════╗
║  1      5      4  ║
║   ↖     ↑     ↗   ║
║     >   |   <     ║
║   ↙     |     ↘   ║
║  2             3  ║
╚═══════════════════╝
```

### Note Types
There are several different note types that can occur in any given Project Radiance song.The user is given free rein on how many notes different note types they would like to incorporate into their beatmap
#### Tap
A tap note is the primary, classic note. It is a single note that plays on a specific beat

#### Hold
A hold note is a tap note followed by a trail. The player should strike the hold note on the beat (like a tap note), but then continue to hold the key down until the end of the tail

#### Lane Change
This is a single note like the tap note but is visually distinguishable. It changes lane configurations—usually, this involves moving multiple lanes to different positions and/or enabling/disabling lanes.

#### Glitch
This is a single note like the tap note, but is an obstacle and should be intentionally avoided. If the player strikes this note, they will incur some sort of penalty

#### Heal
This is a single note like the tap note, but is visually distinguishable. It will heal the player a small amount.


## Contact
Please report any bugs or address any questions, comments, concerns, or suggestions to `projectradiance@kunehostudios.com` and include `Devtool` in the subject.

## Change Log
### Version 0.1.0 (Latest)

##### [Note Types]
&plus; Tap
<br>
&plus; Hold
<br>
&plus; Lane Change
<br>
&plus; Glitch
<br>
&plus; Heal

##### [Lane Configurations and Variations]
<p>&plus; Two Lanes</p>

* Two lanes left to right
* Two lanes right to left

<p>&plus; Four Lanes</p>

* Four lanes top to bottom
* Four lanes bottom to top
* Four lanes left to right
* Four lanes right to left
* Four corners

<p>&plus; Five Lanes</p>

* Five lanes top to bottom
* Five lanes bottom to top
* Five lanes left to right
* Five lanes right to left
* Four corners, middle lane top to bottom
* Four corners, middle lane bottom to top

##### [Note Functions]
&plus; Set beat
<br>
&plus; Add note
<br>
&plus; Edit note
<br>
&plus; Delete note
<br>
&plus; Shift some notes
<br>
&plus; Shift all notes
<br>
&plus; Copy notes

##### [Other]
&plus; Export song and associated beatmaps
