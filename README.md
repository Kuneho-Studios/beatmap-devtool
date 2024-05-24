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
  * `Show all lane swaps`
    * Displays all the lane swaps that exist in the beatmap
    * Includes the beat where the swap occurs, the name of the lane configuration, as well as a visual depiction of what that looks like
      * Can read about the various lane configurations and depictions in the ["Lane Configurations"](#lane-configurations) and ["Lane Variations"](#lane-variations) glossary sections
  * `Copy some notes to another beat`
    * Starting at the current beat and ending at the beat specified, it will then copy all the notes that fall within that range and place them starting at another beat that will be specified
  * `Save`
    * Saves the current beatmap as-is 
    * Saves are automatically performed when the `Back` action is used too
* `Export a song`
  * After selecting the song via the prompts, all the song's files are placed into a zip file and can be downloaded to anywhere on the user's computer via the operating systems save menu that should pop up.

## Glossary
### Note Types
* 

### Lane Configurations
* 

### Lane Variations
* asd

### Difficulty
* 

## Contact
Please report any bugs or address any questions, comments, concerns, or suggestions to `projectradiance@kunehostudios.com` and include `Devtool` in the subject.

## Release Notes
### Version 1.0.0 (Latest)
[Note Types]
* Tap
* Hold
* Lane Change
* Glitch
* Heal

[Lane Configurations and Variations]
* asd

