###
# Contains the flow for updating a song's metadata and copying files
###

import json
import os
import shutil

import Util


# update the difficulty of an existing beatmap in the root Data.json file
def update_beatmap_difficulty():
    beatmap = Util.get_user_beatmap()
    if beatmap is None:
        update_beatmap_difficulty()
    else:
        current_song = beatmap[0]
        current_difficulty = beatmap[1]

    song_name_pascal = Util.string_to_pascal_case(current_song)

    updated_difficulty = input(
        "Enter the desired updated difficulty: ")

    while isinstance(updated_difficulty, str) or int(updated_difficulty) < 1:
        try:
            updated_difficulty = int(updated_difficulty)
            if updated_difficulty < 1:
                print("\nPlease enter a difficulty greater than 0\n")
                updated_difficulty = input(
                    "Enter the desired updated difficulty: ")
            elif updated_difficulty > 10:
                print("\nPlease enter a difficulty less than 11\n")
                updated_difficulty = input(
                    "Enter the desired updated difficulty: ")
        except ValueError:
            print("\nPlease enter a number.\n")
            updated_difficulty = input(
                "Enter the desired updated difficulty: ")

    already_exists, song_data = does_difficulty_exist(song_name_pascal, updated_difficulty)
    song_difficulty_list = song_data["difficulty"]

    if already_exists:
        print("\nDifficulty", updated_difficulty, "already exists for "
              + current_song + ". Please choose a different difficulty")
    else:
        for song_difficulty in song_difficulty_list:

            # if current difficulty matches, then this is the reference need to update
            if song_difficulty["tier"] == int(current_difficulty):
                song_difficulty["tier"] = updated_difficulty
                song_difficulty["filePath"] = Util.FILE_PATH_ROOT + song_name_pascal + "_" + str(
                    updated_difficulty) + ".json"

                song_difficulty_list = sorted(song_difficulty_list,
                                              key=lambda difficulty: (difficulty['tier']))

                song_data["difficulty"] = song_difficulty_list

                with open(
                        Util.BEATMAPS_DIRECTORY + song_name_pascal + "/" + song_name_pascal
                        + "Data.json", "w") as updated_root_data_file:
                    json.dump(song_data,
                              updated_root_data_file, indent=4)
                updated_root_data_file.close()

                beatmap_directory = "beatmaps/" + song_name_pascal + "/"
                # os.rename(
                #     beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json"),
                #     beatmap_directory + (song_name_pascal + "_" + str(updated_difficulty) + ".json"))
                shutil.copy2(beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json"),
                             beatmap_directory + (song_name_pascal + "_" + str(updated_difficulty) + ".json"))

                if os.path.exists(beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json")):
                    os.remove(beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json"))
                    if os.path.exists(beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json")):
                        print("STILL EXISTS")
                else:
                    try:
                        os.remove(beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json"))
                    except FileNotFoundError:
                        print("FileNotFound - " + (
                                beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json")))
                print("\nDifficulty updated to be", updated_difficulty)
                break


# copy the contents of one beatmap into another, overwriting the destination
def copy_entire_beatmap():
    print("\nSelect the song for the source of the copy")
    source_beatmap = Util.get_user_beatmap()
    if source_beatmap is None:
        print("There are no songs saved, please create one before copying")
        return None
    else:
        source_song = source_beatmap[0]
        source_difficulty = source_beatmap[1]

    print("\nCopy into an existing beatmap or create a new one?")
    Util.dropdown_for_user_input(["Use existing beatmap", "Create new beatmap"])

    destination_input = (
        input("Enter the number of the action you'd like to perform: "))

    destination_input = (Util.validate_dropdown_input(destination_input, 2))

    if destination_input == 1:
        copy_into_existing_beatmap(source_song, source_difficulty)
    elif destination_input == 2:
        copy_into_new_beatmap(source_song, source_difficulty)


# find the desired beatmap to copy into, and perform the copy
def copy_into_existing_beatmap(source_song, source_difficulty):
    print("\nSelect the song for the destination of the copy")
    destination_beatmap = Util.get_user_beatmap()
    if destination_beatmap is None:
        print("There are no songs saved, please create one before copying")
        return None
    else:
        destination_song = destination_beatmap[0]
        destination_difficulty = destination_beatmap[1]
    destination_song_pascal = Util.string_to_pascal_case(destination_song)

    print("\nYou are about to copy " + source_song
          + " (difficulty " + source_difficulty + ") into " + destination_song
          + " (difficulty " + destination_difficulty + ") "
          + "\n⚠ THIS WILL OVERRIDE ALL CONTENTS OF " + destination_song
          + " (difficulty " + destination_difficulty + ")⚠"
          + "\nAre you sure you want to proceed?")

    Util.dropdown_for_user_input(["Yes - perform the copy", "No - I changed my mind"])

    confirmation_input = (
        input("Enter the number of the action you'd like to perform: "))

    confirmation_input = (Util.validate_dropdown_input(confirmation_input, 2))

    if confirmation_input == 1:
        source_song_pascal = Util.string_to_pascal_case(source_song)

        source_notes, source_lane_events = \
            Util.read_beatmap(source_song_pascal, source_difficulty)

        with open(Util.BEATMAPS_DIRECTORY + destination_song_pascal + "/"
                  + destination_song_pascal + "_" + str(destination_difficulty) + ".json",
                  "w") as file_to_copy_into:
            json.dump(
                {"notes": source_notes, "laneEvents": source_lane_events},
                file_to_copy_into, indent=4)
        file_to_copy_into.close()
        print("Copied " + source_song + " (difficulty " + source_difficulty + ") into "
              + destination_song + " (difficulty " + destination_difficulty + ")")
    else:
        print("Copy cancelled")


# create the beatmap to copy into, and perform the copy
def copy_into_new_beatmap(source_song, source_difficulty):
    # create new file
    print("\nSelect the song to add the new difficulty to")
    song_list = Util.get_stored_songs()

    if len(song_list) == 0:
        Util.fancy_print_box(
            "⚠ There are no songs present to copy add a new difficulty to ⚠")
        return None
    else:
        selected_song = Util.input_stored_songs(song_list)
        print("selected song", selected_song)

        difficulty = input("Enter the new difficulty: ")
        while isinstance(difficulty, str) or int(difficulty) < 1:
            try:
                difficulty = int(difficulty)

                if difficulty < 1 or difficulty > 10:
                    print("\nDifficulty must be a whole number between 1 and 10 "
                          "(inclusive). Please enter again.\n")
                    difficulty = input("Enter the new difficulty: ")
            except ValueError:
                print("\nDifficulty must be a whole number. "
                      "Please enter a number.\n")
                difficulty = input("Enter the new difficulty: ")

            selected_song_data = does_difficulty_exist(Util.string_to_pascal_case(selected_song), difficulty)
            already_exists = selected_song_data[0]
            if already_exists:
                print("\nDifficulty", difficulty, "already exists for "
                      + selected_song + ". Please choose a different difficulty\n")
                difficulty = input("Enter the new difficulty: ")

        print("COPY CONTENTS FOR", difficulty, " ", selected_song)

    # copy contents
    source_song_pascal = Util.string_to_pascal_case(source_song)
    destination_song_pascal = Util.string_to_pascal_case(selected_song)
    try:
        with open(Util.BEATMAPS_DIRECTORY + source_song_pascal + "/"
                  + source_song_pascal + "_" + str(source_difficulty) + ".json", 'r') as source:
            with open(Util.BEATMAPS_DIRECTORY + destination_song_pascal + "/"
                      + destination_song_pascal + "_" + str(difficulty) + ".json",
                      'w') as destination:
                destination.write(source.read())
        print("Copied " + source_song + " (difficulty " + source_difficulty + ") into "
              + selected_song + " (difficulty " + str(difficulty) + ")")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

    # add difficulty to that song's directory
    song_data = selected_song_data[1]
    song_difficulty_list = song_data["difficulty"]
    song_difficulty_list.append({
        "tier": difficulty,
        "filePath": Util.FILE_PATH_ROOT + destination_song_pascal + "_" + str(difficulty) + ".json"
    })

    song_difficulty_list = sorted(song_difficulty_list,
                                  key=lambda difficulty: (difficulty['tier']))
    song_data["difficulty"] = song_difficulty_list
    with (open(Util.BEATMAPS_DIRECTORY + selected_song + "/" + selected_song + "Data.json", "w")
          as updated_root_data_file):
        json.dump(song_data, updated_root_data_file, indent=4)
    updated_root_data_file.close()

def does_difficulty_exist(song_name_pascal, updated_difficulty):
    with open(
            Util.BEATMAPS_DIRECTORY + song_name_pascal + "/" + song_name_pascal
            + "Data.json", "r") as root_data_file:
        json_data = json.loads(root_data_file.read())
        song_difficulty_list = json_data["difficulty"]
    root_data_file.close()

    for song_difficulty in song_difficulty_list:

        # if desired difficulty already exists, prevent it from being updated to it
        if song_difficulty["tier"] == updated_difficulty:
            return True, json_data

    return False, json_data
