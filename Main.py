###
# Contains the main method. This is the file that is run to initiate the script
# and get the initial user input to determine which flow to take.
###


import BeatmapCreation
import BeatmapEdit
import SongEdit
import Util

start_actions_list = [
    "Exit",
    "Create A New Song (And Beatmaps)",
    "Edit A Song's Metadata",
    "Update A Beatmap"
]

available_song_edit_actions = [
    "Back",
    "Copy This Beatmap Into Another",
    "Copy From Another Beatmap Into This",
    "Update Beatmap Difficulty"
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
        # "METADATA SUCH AS EDITING EXISTING DIFFICULTIES, CREATING, AND REMOVING DIFFICULTIES. UPDATING STARTER FIELDS")
    elif start_actions_list[starter_input - 1] == "Update A Beatmap":
        name, difficulty = get_user_beatmap()
        Util.fancy_print_box("✨ Editing \"" + Util.get_song_name(str(name))
                             + "\" on difficulty " + difficulty + " ✨")
        BeatmapEdit.edit_beatmap(name, difficulty)

    get_user_purpose()


# gets the specified beatmap that the user would like to edit
def get_user_beatmap():
    song_list = Util.get_stored_songs()

    if len(song_list) == 0:
        Util.fancy_print_box(
            "⚠ There are no beatmaps present. Please create one first ⚠")
        get_user_purpose()
    else:
        return Util.get_beatmap(song_list)


def edit_songs():

    print("\nAvailable Song Metadata Editing Options")

    Util.dropdown_for_user_input(available_song_edit_actions)

    action_input = (
        input("Enter the number of the action you'd like to perform: "))

    action_input = (
        Util.validate_dropdown_input(action_input, len(available_song_edit_actions)))

    if available_song_edit_actions[action_input - 1] == "Back":
        get_user_purpose()
    elif available_song_edit_actions[action_input - 1] == "Copy This Beatmap Into Another":
        SongEdit.copy_beatmap_into()
        edit_songs()
    elif available_song_edit_actions[action_input - 1] == "Copy From Another Beatmap Into This":
        SongEdit.copy_beatmap_from()
        edit_songs()
    elif available_song_edit_actions[action_input - 1] == "Update Beatmap Difficulty":
        SongEdit.update_beatmap_difficulty()
        edit_songs()


main()
