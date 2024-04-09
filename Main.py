###
# Contains the main method. This is the file that is ran to initiate the script and get the initial user input to
# determine which flow to take.
###


import BeatmapCreation
import BeatmapEdit
import Util


# display the starting message and call the entry method to determine if editing or creating a beatmap
def main():
    print(
        Util.border + "   ✨ Welcome To Project Radiance's Beatmap Dev Tool ✨" + Util.border)
    get_user_purpose()


# gets initial user input. if create, then create a new beatmap. if edit, then identify what to edit.
def get_user_purpose():
    create_or_edit = input(
        "Would you like to create a new beatmap or edit an existing one? (create/edit) ")
    if create_or_edit.lower() == "create" or create_or_edit.lower() == "c":
        BeatmapCreation.get_user_input()
    elif create_or_edit.lower() == "edit" or create_or_edit.lower() == "e":
        name, difficulty = get_beatmap()
        BeatmapEdit.edit_beatmap(name, difficulty)
    elif create_or_edit.lower() == "exit":
        print(Util.border + "❤ Thanks for using Project Radiance's Beatmap Dev Tool ❤" + Util.border)
    else:
        print("Please only enter 'create' or 'edit'")
        get_user_purpose()
    # get_user_purpose()


# gets the specified beatmap that the user would like to edit
def get_beatmap():
    song_list = Util.get_stored_songs()

    if len(song_list) == 0:
        print("⚠ There are no beatmaps present. Please create one first ⚠")
        get_user_purpose()
    else:
        song = Util.input_stored_songs(song_list)
        difficulty_list = Util.extract_and_sort_difficulties(Util.get_stored_difficulties(song))
        difficulty = str(Util.input_stored_difficulties(difficulty_list))
        print(
            Util.border + "\t\t✨ Editing " + str(song) + " on difficulty " + difficulty + " updated ✨" + Util.border)
        return song, difficulty


main()
