###
# Contains the main method. This is the file that is run to initiate the script
# and get the initial user input to determine which flow to take.
###

import BeatmapCreation
import BeatmapEdit
import SongEdit
import SongExport
import Util

start_actions_list = [
    "Exit",
    "Create A New Song (And Beatmaps)",
    "Edit A Song's Metadata",
    "Update A Beatmap",
    "Export A Song"
]

available_song_edit_actions = [
    "Back",
    "Copy Beatmap Contents",
    "Update Existing Beatmap Difficulty",
    "Edit Song Basic Info"
]


# display the starting message and call the entry method
# determine if editing or creating a beatmap
def main():
    Util.fancy_print_box("✨ Welcome To Project Radiance's Beatmap Dev Tool ✨")
    get_user_purpose()


# gets initial user input. if 'create', then create a new beatmap.
# if 'edit', then identify what to edit.
def get_user_purpose():
    print("What would you like to do?")
    Util.dropdown_for_user_input(start_actions_list)

    starter_input = (
        input("Enter the number of the action you'd like to perform: "))

    starter_input = (
        Util.validate_dropdown_input(starter_input, len(start_actions_list)))

    if starter_input is None:
        print("")
        get_user_purpose()
    elif start_actions_list[starter_input - 1] == "Exit":
        Util.fancy_print_box(
            "💛 Thanks for using Project Radiance's Beatmap Dev Tool 💛")
        return ""
    elif start_actions_list[starter_input - 1] == "Create A New Song (And Beatmaps)":
        BeatmapCreation.get_user_input()
    elif start_actions_list[starter_input - 1] == "Edit A Song's Metadata":
        edit_songs()
    elif start_actions_list[starter_input - 1] == "Update A Beatmap":
        beatmap = Util.get_user_beatmap()

        if beatmap is None:
            get_user_purpose()
        else:
            name = beatmap[0]
            difficulty = beatmap[1]

        Util.fancy_print_box("✨ Editing \"" + Util.get_song_name(str(name))
                             + "\" on difficulty " + difficulty + " ✨")
        BeatmapEdit.edit_beatmap(name, difficulty)
    elif start_actions_list[starter_input - 1] == "Export A Song":
        SongExport.export_song()


def edit_songs():
    print("\nAvailable Song Metadata Editing Options")

    Util.dropdown_for_user_input(available_song_edit_actions)

    action_input = (
        input("Enter the number of the action you'd like to perform: "))

    action_input = (
        Util.validate_dropdown_input(action_input, len(available_song_edit_actions)))

    if action_input is None:
        edit_songs()
    elif available_song_edit_actions[action_input - 1] == "Back":
        print("")
        get_user_purpose()
    elif available_song_edit_actions[action_input - 1] == "Copy Beatmap Contents":
        SongEdit.copy_entire_beatmap()
        edit_songs()
    elif available_song_edit_actions[action_input - 1] == "Update Existing Beatmap Difficulty":
        SongEdit.update_beatmap_difficulty()
        edit_songs()
    elif available_song_edit_actions[action_input - 1] == "Edit Song Basic Info":
        SongEdit.update_basic_info()
        edit_songs()


main()
