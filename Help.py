###
# Contains the action list names as well as the help menu displays
###

from Util import BOLD_TEXT, NORMAL_TEXT

HELP_ACTION = "~ Help ~"
BACK_ACTION = "Back"
EXIT_ACTION = "Exit"
NEW_SONG_ACTION = "Create a new song (and beatmaps)"
EDIT_SONG_ACTION = "Edit a song"
UPDATE_BEATMAP_ACTION = "Update a beatmap"
EXPORT_SONG_ACTION = "Export a song"

COPY_BEATMAP_ACTION = "Copy beatmap contents"
UPDATE_BEATMAP_DIFFICULTY_ACTION = "Update an existing beatmap's difficulty"
EDIT_SONG_INFO_ACTION = "Edit an existing song's basic information"

SHOW_ALL_LANE_CHANGES_ACTION = "Show all lane changes"
SHIFT_ALL_NOTES_ACTION = "Shift all notes"
SHIFT_SOME_NOTES_ACTION = "Shift some notes"
ADD_NOTE_ACTION = "Add note"
COPY_SOME_NOTES_ACTION = "Copy some notes to another beat"
SET_BEAT_ACTION = "Set beat"
DELETE_NOTE_ACTION = "Delete note"
EDIT_NOTE_ACTION = "Edit note"
SAVE_ACTION = "Save"


# helper method to bold text
def bold_text(text):
    return BOLD_TEXT + text + NORMAL_TEXT


# helper method to print out the bullet point and the name of the help item
def set_help_name(help_menu_name):
    return "  * " + bold_text(help_menu_name) + " - "


# help menu for the User Purpose method in Main
def user_purpose_help():
    print("\n ~~~ HELP ~~~")
    print(set_help_name(EXIT_ACTION) + "Closes the beatmap devtool")
    print(set_help_name(NEW_SONG_ACTION) + "Creates a new song to be stored in the same directory the devtool is run "
                                           "from. Will also create the empty beatmaps for each specified difficulty")
    print(set_help_name(EDIT_SONG_ACTION) + "Change information about the song, such as its name or beats per minute. "
                                            "Also to copy beatmaps from file to file or update a difficulty")
    print(
        set_help_name(UPDATE_BEATMAP_ACTION) + "Add, edit, remove, or copy notes in a given beatmap. This is where the "
                                               "actual development of the beatmap will take place")
    print(
        set_help_name(EXPORT_SONG_ACTION) + "Zip all the files for a given song and will save them wherever you want ("
                                            "via a save menu pop-out)")
    print("")


# help menu for Edit Songs method in Main
def edit_songs_help():
    print("\n ~~~ HELP ~~~")
    print(set_help_name(BACK_ACTION) + "Goes back to the main menu prompts")
    print(set_help_name(COPY_BEATMAP_ACTION) + "Copy an entire beatmap's contents into an already existing beatmap ("
                                               "and will override its content) or into a new beatmap")
    print(set_help_name(UPDATE_BEATMAP_DIFFICULTY_ACTION) + "Update the difficulty rating of an existing beatmap into "
                                                            "one that cannot already exist for that song")
    print(set_help_name(EDIT_SONG_INFO_ACTION) + "Update the basic info for a song that was set when the song was "
                                                 "created")
    print("")


# help menu for Edit Beatmap Input method in BeatmapEdit
def edit_beatmap_input_help():
    print("\n ~~~ HELP ~~~")
    print(set_help_name(BACK_ACTION) + "Goes back to the main menu prompts")
    print(set_help_name(SET_BEAT_ACTION) + "Sets the current beat to the value supplied. All created, edited, "
                                           "and deleted notes will be on this beat")
    print(set_help_name(ADD_NOTE_ACTION) + "Add a note to a lane given the current beat's lane configuration")
    print(set_help_name(EDIT_NOTE_ACTION) + "Edit an existing note on the current beat. Can edit the note type or its "
                                            "lane. Utilize " + bold_text(SHIFT_SOME_NOTES_ACTION) + " to directly move "
                                            "it or " + bold_text(DELETE_NOTE_ACTION) + " and then"
                                            " " + bold_text(ADD_NOTE_ACTION) + " to recreate it on a different beat")
    print(set_help_name(DELETE_NOTE_ACTION) + "Delete an existing note on the current beat")
    print(set_help_name(SHIFT_SOME_NOTES_ACTION) + "Starting at the current beat and ending at the beat specified, "
                                                   "it will then shift all the notes that fall within that range by "
                                                   "the amount of beats specified. The shift amount must begin with "
                                                   "a " + bold_text("+") + " (to shift to higher/later beats) or a"
                                                   " " + bold_text("-") + "(to shift to lower/earlier beats)")
    print(set_help_name(SHIFT_ALL_NOTES_ACTION) + "Shifts all notes in the song by the amount of beats specified. "
                                                  "The shift amount must begin with a " + bold_text("+") + " "
                                                  "(to shift to higher/later beats) or a " + bold_text("-") + " "
                                                  "(to shift to lower/earlier beats)")
    print(set_help_name(SHOW_ALL_LANE_CHANGES_ACTION) + "Displays all the lane changes that exist in the beatmap. "
                                                        "Includes the beat where the swap occurs, the name of the lane "
                                                        "configuration, as well as a visual depiction of what that "
                                                        "looks like")
    print(set_help_name(COPY_SOME_NOTES_ACTION) + "Starting at the current beat and ending at the beat specified, "
                                                  "it will then copy all the notes that fall within that range and "
                                                  "place them starting at another beat that will be specified.")
    print(set_help_name(SAVE_ACTION) + "Saves the current beatmap as-is. Saves are automatically performed when the"
                                       " " + bold_text(BACK_ACTION) + " action is used too")
    print("")
