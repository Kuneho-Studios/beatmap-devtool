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

    with open(
            Util.BEATMAPS_DIRECTORY + song_name_pascal + "/" + song_name_pascal
            + "Data.json", "r") as root_data_file:
        json_data = json.loads(root_data_file.read())
        song_difficulty_list = json_data["difficulty"]
    root_data_file.close()

    already_exists = False
    for song_difficulty in song_difficulty_list:

        # if desired difficulty already exists, prevent it from being updated to it
        if song_difficulty["tier"] == updated_difficulty:
            already_exists = True
            break

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

                json_data["difficulty"] = song_difficulty_list

                with open(
                        Util.BEATMAPS_DIRECTORY + song_name_pascal + "/" + song_name_pascal
                        + "Data.json", "w") as updated_root_data_file:
                    json.dump(json_data,
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


# copy the contents of one beatmap into another, overwritting the destination
def copy_entire_beatmap():
    print("\nSelect the song for the source of the copy")
    source_beatmap = Util.get_user_beatmap()
    if source_beatmap is None:
        update_beatmap_difficulty()
    else:
        source_song = source_beatmap[0]
        source_difficulty = source_beatmap[1]
    source_song_pascal = Util.string_to_pascal_case(source_song)

    print("\nSelect the song for the destination of the copy")
    destination_beatmap = Util.get_user_beatmap()
    if destination_beatmap is None:
        update_beatmap_difficulty()
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
