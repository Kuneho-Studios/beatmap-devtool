###
# Contains the flow for when a user would like to update an existing beatmap.
# This does the bulk of that work. Fetches the desired song and difficulty
# beatmap then provides prompts to the user to aid in editing the beatmap.
###
import json
import copy
import os

import Util

current_lane_count = None
current_lane_configuration = None
current_lane_configuration_art = None

current_song = None
current_difficulty = None
current_beat = None

available_actions_list = [
    "Exit",
    # Enter any new commands after exit
    "Add Notes",
    # "Edit Note",
    # "Delete Note",
    "Shift All Notes",
    "Shift Some Notes",
    "Show All Lane Swaps",
    "Copy This Beatmap Into Another",
    "Copy From Another Beatmap Into This",
    "Copy Some Notes To Another Place",
    "Update Beatmap Difficulty"
]


# open the existing beatmap for editing. then calls method edit_beatmap_input
# to loop through the editing/adding process obtain the laneEvents since it
# will not be changed here. paste it at the end of the editing process to
# ensure it remains.
def edit_beatmap(song_name, song_difficulty):
    global current_song, current_difficulty, current_beat
    current_song = song_name
    current_difficulty = song_difficulty
    current_beat = 0

    notes, lane_events = Util.read_beatmap(song_name, song_difficulty)

    if not lane_events:
        lane_events = set_lane_event()
        Util.fancy_print_box("✨ Initial lane configuration set!"
                             " You can proceed to beatmapping now! ✨")
    else:
        global current_lane_count, current_lane_configuration, \
            current_lane_configuration_art

        last_lane_swap = \
            Util.get_lane_swaps(notes, song_name, song_difficulty)[-1]
        current_lane_count = last_lane_swap[1]
        current_lane_configuration = last_lane_swap[2]
        current_lane_configuration_art = last_lane_swap[3]

        if len(notes) > 0:
            current_beat = notes[-1]["startBeat"]

    sorted_notes = sorted(edit_beatmap_input(notes),
                          key=lambda note: (note['startBeat'], note['lane']))

    with open('beatmaps/' + song_name + "/" + song_name + "_" + song_difficulty
              + ".json", "w") as beatmap_write:
        json.dump({"notes": sorted_notes, "laneEvents": lane_events},
                  beatmap_write, indent=4)
    beatmap_write.close()

    set_song_note_length(song_name, sorted_notes)

    Util.fancy_print_box("✨ " + song_name + " on " + song_difficulty
                         + " difficulty updated! ✨")


# obtain the beat for the current note to be added to the beatmap
def edit_beatmap_input(notes):
    global current_beat

    Util.note_report(current_lane_configuration, current_lane_configuration_art,
                     Util.get_last_beat(current_beat, notes))

    print("\nAvailable Beatmap Actions:")
    Util.dropdown_for_user_input(available_actions_list)

    action_input = (
        input("Enter the number of the action you'd like to perform: "))

    action_input = (
        Util.validate_dropdown_input(action_input, len(available_actions_list)))

    if available_actions_list[action_input - 1] == "Exit":
        return ""
    elif available_actions_list[action_input - 1] == "Show All Lane Swaps":
        Util.show_lane_swaps(notes, current_song, current_difficulty)
        edit_beatmap_input(notes)
    elif available_actions_list[action_input - 1] == "Shift All Notes":
        shift_all_notes(notes)
        edit_beatmap_input(notes)
    elif available_actions_list[action_input - 1] == "Shift Some Notes":
        shift_some_notes(notes)
        edit_beatmap_input(notes)
    elif available_actions_list[action_input - 1] == "Add Notes":
        notes = add_note(notes)
        edit_beatmap_input(notes)
    elif available_actions_list[action_input - 1] == "Copy This Beatmap Into Another":
        copy_beatmap_into()
        edit_beatmap_input(notes)
    elif available_actions_list[action_input - 1] == "Copy From Another Beatmap Into This":
        copy_beatmap_from()
        edit_beatmap_input(notes)
    elif available_actions_list[action_input - 1] == "Copy Some Notes To Another Place":
        copy_note_segment(notes)
        edit_beatmap_input(notes)
    elif available_actions_list[action_input - 1] == "Update Beatmap Difficulty":
        update_beatmap_difficulty()
        edit_beatmap_input(notes)

    print("")
    return notes


# set the lane that the current beat will reside on
def set_lane(beat):
    print("\nAvailable Lanes:")
    for i in range(current_lane_count):
        print(str(i + 1) + ") Lane " + str(i + 1))

    lane_input = input("What lane is beat " + str(beat) + " on? ")

    lane_input = Util.validate_dropdown_input(lane_input, current_lane_count)
    if lane_input is None:
        return set_lane(beat)
    else:
        return lane_input


# set the note type.
# if is a "laneSwap" then call methods to determine what to swap to
def set_note_data(beat, lane):
    print("\nAvailable Note Types:")
    Util.dropdown_for_user_input(Util.note_types_list)

    note_type_input = input("Enter the number of beat " + str(beat) + " lane "
                            + str(lane) + "'s note type: ")

    note_type_input = Util.validate_dropdown_input(
        note_type_input, len(Util.note_types_list))
    if note_type_input is None:
        return set_note_data(beat, lane)
    else:
        if Util.note_types_list[note_type_input - 1] == "LaneSwap":
            return {"noteType": "LaneSwap", "laneChanges": set_lane_swap()}

        return {"noteType": Util.note_types_list[note_type_input - 1]}


# given the desire to perform a lane swap
# prompt and gather how many lanes the user would like the swap to have
def set_lane_swap():
    print("\nAvailable Lane Sizes:")
    lane_names = [value[0] for value in Util.lane_swap_types_dict.values()]
    Util.dropdown_for_user_input(lane_names)

    lane_swap_lane_count = (
        input("Enter the number of lanes in the new lane configuration? "))

    lane_swap_lane_count = (
        Util.validate_dropdown_input(lane_swap_lane_count, len(lane_names)))
    if lane_swap_lane_count is None:
        return set_lane_swap()
    else:
        return set_lane_style(lane_swap_lane_count)


# given the desired lane swap count, display the art for the different styles
# allow the user to select which one
def set_lane_style(lane_swap_lane_count):
    lane_type_keys = (
        list(Util.lane_swap_types_dict.get(lane_swap_lane_count)[1].keys()))

    print("\nAvailable Lane Styles:")
    Util.dropdown_for_user_input(lane_type_keys)

    lane_type_input = (
        input("Enter the " + str(lane_swap_lane_count) + "-lane style: "))

    lane_type_input = (
        Util.validate_dropdown_input(lane_type_input, len(lane_type_keys)))

    if lane_type_input is None:
        return set_lane_style(lane_swap_lane_count)
    else:
        global current_lane_configuration, current_lane_count
        current_lane_configuration = list(lane_type_keys)[lane_type_input - 1]
        current_lane_count = lane_swap_lane_count

        lane_configuration = (Util.lane_swap_types_dict.get(
            lane_swap_lane_count)[1].get(current_lane_configuration))

        return set_lane_variation(lane_configuration)


# given the desired lane format, display the art for the different variations
# allow the user to select which one
def set_lane_variation(lane_configuration_list):
    lane_configuration_art_list = []
    for lane_configuration in lane_configuration_list:
        lane_configuration_art_list.append("\n" + lane_configuration[0])

    print("\nAvailable Lane Variations:")
    Util.dropdown_for_user_input(lane_configuration_art_list)
    lane_configuration_input = (
        input("Enter the number of the lane variations you want to swap to: "))

    lane_configuration_input = Util.validate_dropdown_input(
        lane_configuration_input, len(lane_configuration_art_list))

    if lane_configuration_input is None:
        return set_lane_variation(lane_configuration_list)
    else:
        selected_lane_list = (
            lane_configuration_list)[lane_configuration_input - 1][1]

        lane_changes_list = []
        for i in range(5):
            lane_changes_list.append(
                {"lane": i, "newLanePosition": selected_lane_list[i]})

        global current_lane_configuration_art
        current_lane_configuration_art = (
            lane_configuration_list)[lane_configuration_input - 1][0]

        return lane_changes_list


# populate the laneEvents segment which is used for starting lane configuration
def set_lane_event():
    Util.fancy_print_box(
        "⚠ You do not have the initial lane setup configured! "
        "Let's do that now ⚠")
    return [{"startBeat": 0, "lanes": set_lane_swap()}]


# when the song is saved, fetch what was previously stored in the length field
# if the highest beat in the current beatmap is greater than the current length
# then update length to reflect that value
def set_song_note_length(song_name, notes):
    with open('beatmaps/' + song_name + "/" + song_name + "Data.json", "r") \
            as beatmap_data_read:
        json_data = json.loads(beatmap_data_read.read())
        song_length = json_data["length"]
    beatmap_data_read.close()

    if not notes:
        last_note_beat = 0
    else:
        last_note_beat = notes[-1]["startBeat"]

    if last_note_beat > song_length:
        json_data["length"] = last_note_beat
        with open('beatmaps/' + song_name + "/" + song_name + "Data.json",
                  "w") as beatmap_data_write:
            json.dump(json_data, beatmap_data_write, indent=4)
        beatmap_data_write.close()


# shift all notes from a user supplied amount
def shift_all_notes(notes):
    shift_input = input("Enter the count to shift all the beats "
                        "(prefix with `-` for shift left or `+` to shift right): ").strip()

    if shift_input[0] != "+" and shift_input[0] != "-":
        print("Please include a '+' or '-' before the amount to shift")
        shift_all_notes(notes)
    try:
        shift_amount = float(shift_input[1:])
        if shift_input[0] == '-':
            shift_amount = -1 * shift_amount

        for note in notes:
            note["startBeat"] = note["startBeat"] + shift_amount

        return notes
    except ValueError:
        print("Please enter only a number after the '+' or '-'")
        shift_all_notes(notes)


# shift notes within the user supplied range a user supplied amount
def shift_some_notes(notes):
    shift_start_input = input("Enter the beat where the shift begins: ").strip()
    try:
        shift_start_input = float(shift_start_input)
    except ValueError:
        print("Please enter valid number for the start beat")
        shift_some_notes(notes)

    shift_end_input = input("Enter the beat where the shift ends: ").strip()
    try:
        shift_end_input = float(shift_end_input)
        if shift_end_input < shift_start_input:
            print("Please ensure that the end beat count is the same or later"
                  " than the start beat count")
            shift_some_notes(notes)
    except ValueError:
        print("Please enter valid number for the end beat")
        shift_some_notes(notes)

    shift_input = input("Enter the count to shift the beats between "
                        + str(shift_start_input) + " and "
                        + str(shift_end_input) +
                        "(prefix with `-` for shift left or `+` to shift right): ").strip()

    if shift_input[0] != "+" and shift_input[0] != "-":
        print("Please include a '+' or '-' before the amount to shift")
        shift_all_notes(notes)
    try:
        shift_amount = float(shift_input[1:])
        if shift_input[0] == '-':
            shift_amount = -1 * shift_amount

        for note in notes:
            if shift_start_input <= note["startBeat"] <= shift_end_input:
                note["startBeat"] = note["startBeat"] + shift_amount

        return notes
    except ValueError:
        print("Please enter only a number after the '+' or '-'")
        shift_all_notes(notes)


# add a note to the beatmap
def add_note(notes):
    global current_beat

    beat = input(
        "Enter beat for the note you want to add: ")

    try:
        beat = float(beat)
        lane = set_lane(beat)
        note_data = set_note_data(beat, lane)
        note_json_object = {"startBeat": beat,
                            "lane": lane,
                            "noteData": note_data}
        notes.append(note_json_object)
        current_beat = beat

        return notes
    except ValueError:
        print("\n Please enter a number.")
        add_note(notes)


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


# copy a subset of notes and place them at a different beat
def copy_note_segment(notes):
    start_copy_note = input(
        "Enter first beat of the segment you want to copy: ")
    try:
        start_copy_note = float(start_copy_note)
    except ValueError:
        print("\n Please enter a number.")
        copy_note_segment(notes)

    end_copy_note = input(
        "Enter last beat of the segment you want to copy: ")
    try:
        end_copy_note = float(end_copy_note)
    except ValueError:
        print("\n Please enter a number.")
        copy_note_segment(notes)

    if start_copy_note > end_copy_note:
        print("\n Please ensure that the last beat comes after the first beat")
        copy_note_segment(notes)

    copied_location = input(
        "Enter beat where the copied segment will begin: ")
    try:
        copied_location = float(copied_location)
    except ValueError:
        print("\n Please enter a number.")
        copy_note_segment(notes)

    notes_subset = copy.deepcopy(list(filter(lambda x: start_copy_note <= x.get("startBeat") <= end_copy_note, notes)))

    note_shift_distance = copied_location - start_copy_note
    for note in notes_subset:
        note["startBeat"] += note_shift_distance

    notes.extend(notes_subset)


# update the difficulty of an existing beatmap in the root Data.json file
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
            os.rename(
                beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json"),
                beatmap_directory + (song_name_pascal + "_" + str(updated_difficulty) + ".json"))

            if os.path.exists(beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json")):
                os.remove(beatmap_directory + (song_name_pascal + "_" + str(current_difficulty) + ".json"))

            break

    if already_exists:
        print("\n Difficulty", updated_difficulty, "already exists for "
              + current_song + ". Please choose a different difficulty")
