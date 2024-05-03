# update the difficulty of an existing beatmap in the root Data.json file
import json
import os
import shutil

import Util


def update_beatmap_difficulty():
    global current_song, current_difficulty
    song_name_pascal = Util.string_to_pascal_case(current_song)

    updated_difficulty = input(
        "Enter the desired updated difficulty: ")
    try:
        updated_difficulty = int(updated_difficulty)
    except ValueError:
        print("\n Please enter a number.")
        update_beatmap_difficulty()

    if updated_difficulty < 1:
        print("\n Please enter a difficulty greater than 1")

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
                print("IF REMOVE")
                os.remove(beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json"))
                if os.path.exists(beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json")):
                    print("STILL EXISTS")
            else:
                print("ELSE REMOVE")
                try:
                    os.remove(beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json"))
                except FileNotFoundError:
                    print("FileNotFound - " + (
                                beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json")))
            break

    if already_exists:
        print("\n Difficulty", updated_difficulty, "already exists for "
              + current_song + ". Please choose a different difficulty")
    else:
        print("\n Difficulty updated to be", updated_difficulty)


# copy this beatmap into another difficulty
def copy_beatmap_into():
    song_name, song_difficulty = Util.get_beatmap(Util.get_stored_songs())
    song_name = Util.string_to_pascal_case(song_name)
    current_notes, current_lane_events = \
        Util.read_beatmap(current_song, current_difficulty)

    print("\nYou are about to copy " + current_song
          + " (difficulty " + current_difficulty + ") into " + song_name
          + " (difficulty " + song_difficulty + ") "
          + "\n⚠ THIS WILL OVERRIDE ALL CONTENTS OF " + song_name
          + " (difficulty " + song_difficulty + ")⚠"
          + "\nAre you sure you want to proceed?")

    Util.dropdown_for_user_input(["Yes - perform the copy", "No - I changed my mind"])

    confirmation_input = (
        input("Enter the number of the action you'd like to perform: "))

    confirmation_input = (Util.validate_dropdown_input(confirmation_input, 2))

    if confirmation_input == 1:
        with open(Util.BEATMAPS_DIRECTORY + song_name + "/"
                  + song_name + "_" + str(song_difficulty) + ".json",
                  "w") as file_to_copy_into:
            json.dump(
                {"notes": current_notes, "laneEvents": current_lane_events},
                file_to_copy_into, indent=4)
        file_to_copy_into.close()
        print("Copied " + current_song + " (difficulty " + current_difficulty + ") into "
              + song_name + " (difficulty " + song_difficulty + ")")
    else:
        print("Copy cancelled")


# copy a beatmap from another difficulty into this one
def copy_beatmap_from():
    song_name, song_difficulty = Util.get_beatmap(Util.get_stored_songs())
    new_notes, new_lane_events = \
        Util.read_beatmap(song_name, song_difficulty)

    print("\nYou are about to copy " + song_name
          + " (difficulty " + song_difficulty + ") into " + current_song
          + " (difficulty " + current_difficulty + ") "
          + "\n⚠ THIS WILL OVERRIDE ALL CONTENTS OF " + current_song
          + " (difficulty " + current_difficulty + ")⚠"
          + "\nAre you sure you want to proceed?")

    Util.dropdown_for_user_input(["Yes - perform the copy", "No - I changed my mind"])

    confirmation_input = (
        input("Enter the number of the action you'd like to perform: "))

    confirmation_input = (Util.validate_dropdown_input(confirmation_input, 2))

    if confirmation_input == 1:
        with open(Util.BEATMAPS_DIRECTORY + Util.string_to_pascal_case(current_song) + "/"
                  + Util.string_to_pascal_case(current_song) + "_" + str(current_difficulty) + ".json",
                  "w") as file_to_copy_from:
            json.dump(
                {"notes": new_notes, "laneEvents": new_lane_events},
                file_to_copy_from, indent=4)
        file_to_copy_from.close()
        print("Copied " + song_name + " (difficulty " + song_difficulty + ") into "
              + current_song + " (difficulty " + current_difficulty + ")")

    else:
        print("Copy cancelled")
