###
# Contains the main method. This is the file that is run to initiate the script
# and get the initial user input to determine which flow to take.
###

import BeatmapCreation
import BeatmapEdit
import SongEdit
import SongExport
import Util
from Help import *

start_actions_list = [
    HELP_ACTION,
    EXIT_ACTION,
    NEW_SONG_ACTION,
    EDIT_SONG_ACTION,
    UPDATE_BEATMAP_ACTION,
    EXPORT_SONG_ACTION
]

available_song_edit_actions_list = [
    HELP_ACTION,
    BACK_ACTION,
    COPY_BEATMAP_ACTION,
    UPDATE_BEATMAP_DIFFICULTY_ACTION,
    EDIT_SONG_INFO_ACTION
]


# display the starting message and call the entry method
# determine if editing or creating a beatmap
def main():
    Util.fancy_print_box("✨ Welcome To Project Radiance's Beatmap Dev Tool ✨")
    get_user_purpose()
    Util.fancy_print_box(
        "💛 Thanks for using Project Radiance's Beatmap Dev Tool 💛")


# gets initial user input. if 'create', then create a new beatmap.
# if 'edit', then identify what to edit.
def get_user_purpose():
    starter_input = ""
    while starter_input != 1:
        print("What would you like to do?")
        Util.dropdown_for_user_input(start_actions_list, True)

        starter_input = (
            input("Enter the number of the action you'd like to perform: "))

        starter_input = (
            Util.validate_dropdown_input(starter_input, len(start_actions_list), True))

        if starter_input is None:
            print("")
            get_user_purpose()
        elif start_actions_list[starter_input] == HELP_ACTION:
            user_purpose_help()
        elif start_actions_list[starter_input] == NEW_SONG_ACTION:
            BeatmapCreation.get_user_input()
        elif start_actions_list[starter_input] == EDIT_SONG_ACTION:
            edit_songs()
        elif start_actions_list[starter_input] == UPDATE_BEATMAP_ACTION:
            beatmap = Util.get_user_beatmap()

            if beatmap is None:
                get_user_purpose()
            else:
                name = beatmap[0]
                difficulty = beatmap[1]

            Util.fancy_print_box("✨ Editing \"" + Util.get_song_name(str(name))
                                 + "\" on difficulty " + difficulty + " ✨")
            BeatmapEdit.edit_beatmap(name, difficulty)
        elif start_actions_list[starter_input] == EXPORT_SONG_ACTION:
            SongExport.export_song()


# prompt entry for editing a song's metadata
def edit_songs():
    print("\nAvailable Song Metadata Editing Options")

    Util.dropdown_for_user_input(available_song_edit_actions_list, True)

    action_input = (
        input("Enter the number of the action you'd like to perform: "))

    action_input = (
        Util.validate_dropdown_input(action_input, len(available_song_edit_actions_list), True))

    if action_input is None:
        edit_songs()
    elif available_song_edit_actions_list[action_input] == HELP_ACTION:
        edit_songs_help()
    elif available_song_edit_actions_list[action_input] == BACK_ACTION:
        print("")
        get_user_purpose()
    elif available_song_edit_actions_list[action_input] == COPY_BEATMAP_ACTION:
        SongEdit.copy_entire_beatmap()
        edit_songs()
    elif available_song_edit_actions_list[action_input] == UPDATE_BEATMAP_DIFFICULTY_ACTION:
        SongEdit.update_beatmap_difficulty()
        edit_songs()
    elif available_song_edit_actions_list[action_input] == EDIT_SONG_INFO_ACTION:
        SongEdit.update_basic_info()
        edit_songs()


main()
