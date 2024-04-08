###
# Contains the main method. This is the file that is ran to initiate the script and get the initial user input to
# determine which flow to take.
###


import beatmapCreation
import beatmapEdit
import util


def main():
    print(
        util.border + "   ✨ Welcome To Project Radiance's Beatmap Dev Tool ✨" + util.border)
    get_user_purpose()


def get_user_purpose():
    create_or_edit = input(
        "Would you like to create a new beatmap or edit an existing one? (create/edit) ")
    if create_or_edit.lower() == "create" or create_or_edit.lower() == "c":
        beatmapCreation.get_user_input()
    elif create_or_edit.lower() == "edit" or create_or_edit.lower() == "e":
        name, difficulty = get_beatmap()
        beatmapEdit.edit_beatmap(name, difficulty)
    else:
        print("Please only enter 'create' or 'edit'")
        get_user_purpose()
    get_user_purpose()


def get_beatmap():
    song_list = util.get_stored_songs()

    if len(song_list) == 0:
        print("⚠ There are no beatmaps present. Please create one first ⚠")
        get_user_purpose()
    else:
        song = util.input_stored_songs(song_list)
        beatmap = util.input_stored_difficulties(util.get_stored_difficulties(song))
        beatmap_file_name = beatmap.split("_")
        beatmap_song_name = beatmap_file_name[0]
        beatmap_song_difficulty = beatmap_file_name[1].split(".json")[0]
        print(
            util.border + "\t\t✨ Editing " + beatmap_song_name + " on " + beatmap_song_difficulty + " difficulty ✨" + util.border)
        return beatmap_song_name, beatmap_song_difficulty


main()
