###
# Contains the flow for when a user would like to update an existing beatmap. This does the bulk of that work.
# Fetches the desired song and difficulty beatmap then provides prompts to the user to aid in editing the beatmap.
###
import json

import LaneArt
import Util

current_lane_count = 2
current_lane_configuration = "Two Lanes Left to Right"
current_lane_configuration_art = LaneArt.TWO_LANES_RIGHT_LEFT[0][0]


# open the existing beatmap for editing. then calls method edit_beatmap_input to loop through the editing/adding process
# obtain the laneEvents since it will not be changed here.
# paste it at the end of the editing process to ensure it remains.
def edit_beatmap(song_name, song_difficulty):
    with open('beatmaps/' + song_name + "/"
              + song_name + "_" + song_difficulty + ".json",
              "r") as beatmap_read:
        json_data = json.loads(beatmap_read.read())
        notes = json_data["notes"]
        lane_events = json_data["laneEvents"]
    beatmap_read.close()

    sorted_notes_filled = sorted(edit_beatmap_input(notes), key=lambda note: (note['startBeat'], note['lane']))

    with open('beatmaps/' + song_name + "/" + song_name + "_" + song_difficulty + ".json", "w") as beatmap_write:
        json.dump({"notes": sorted_notes_filled, "laneEvents": lane_events}, beatmap_write, indent=4)
    beatmap_write.close()

    Util.fancy_print_box("✨ " + song_name + " on " + song_difficulty + " difficulty updated! ✨")


# obtain the beat for the current note to be added to the beatmap
def edit_beatmap_input(notes):
    Util.note_report(current_lane_configuration, current_lane_configuration_art, Util.get_last_beat_difficulty())
    beat = input(
        "What is the beat for the note you want to add? ")

    if beat.lower() == "exit":
        return
    else:
        try:
            beat = float(beat)
            lane = set_lane(beat)
            note_data = set_note_data(beat, lane)
            note_json_object = {"startBeat": beat, "lane": lane, "noteData": note_data}
            notes.append(note_json_object)

            edit_beatmap_input(notes)
        except ValueError:
            print("Either enter a number or 'exit'!")
            edit_beatmap_input(notes)
    print()
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


# set the note type. if is a "laneSwap" then call methods to determine what to swap to
def set_note_data(beat, lane):
    print("\nAvailable Note Types:")
    Util.dropdown_for_user_input(Util.note_types_list)

    note_type_input = input("Enter the number of beat " + str(beat) + " lane " + str(lane) + "'s note type: ")

    note_type_input = Util.validate_dropdown_input(note_type_input, len(Util.note_types_list))
    if note_type_input is None:
        return set_note_data(beat, lane)
    else:
        if Util.note_types_list[note_type_input - 1] == "LaneSwap":
            return {"noteType": "LaneSwap", "laneChanges": set_lane_swap()}

        return {"noteType": Util.note_types_list[note_type_input - 1]}


# given the desire to perform a lane swap, prompt and gather how many lanes the user would like the swap to have
def set_lane_swap():
    print("\nAvailable Lane Sizes:")
    lane_names = [value[0] for value in Util.lane_swap_types_dict.values()]
    Util.dropdown_for_user_input(lane_names)

    lane_swap_lane_count = input("Enter the number of lanes in the new lane configuration? ")

    lane_swap_lane_count = Util.validate_dropdown_input(lane_swap_lane_count, len(lane_names))
    if lane_swap_lane_count is None:
        return set_lane_swap()
    else:
        return set_lane_style(lane_swap_lane_count)


# given the desired lane swap count, display the art for the different styles and allow the user to select which one
def set_lane_style(lane_swap_lane_count):
    lane_type_keys = list(Util.lane_swap_types_dict.get(lane_swap_lane_count)[1].keys())

    print("\nAvailable Lane Styles:")
    Util.dropdown_for_user_input(lane_type_keys)

    lane_type_input = input("Enter the " + str(lane_swap_lane_count) + "-lane style: ")

    lane_type_input = Util.validate_dropdown_input(lane_type_input, len(lane_type_keys))
    if lane_type_input is None:
        return set_lane_style(lane_swap_lane_count)
    else:
        global current_lane_configuration
        current_lane_configuration = list(lane_type_keys)[lane_type_input - 1]

        lane_configuration = Util.lane_swap_types_dict.get(lane_swap_lane_count)[1].get(
            current_lane_configuration)

        return set_lane_variation(lane_configuration)


# given the desired lane format, display the art for the different variations and allow the user to select which one
def set_lane_variation(lane_configuration_list):
    lane_configuration_art_list = []
    for lane_configuration in lane_configuration_list:
        lane_configuration_art_list.append(lane_configuration[0])

    print("\nAvailable Lane Variations:")
    Util.dropdown_for_user_input(lane_configuration_art_list)
    lane_configuration_input = input("Enter the number of the lane variations you want to swap to: ")

    lane_configuration_input = Util.validate_dropdown_input(lane_configuration_input, len(lane_configuration_art_list))
    if lane_configuration_input is None:
        return set_lane_variation(lane_configuration_list)
    else:
        selected_lane_list = lane_configuration_list[lane_configuration_input - 1][1]

        lane_changes_list = []
        for i in range(5):
            lane_changes_list.append(
                {"lane": i, "newLanePosition": selected_lane_list[i]})

        global current_lane_configuration_art
        current_lane_configuration_art = lane_configuration_list[lane_configuration_input - 1][0]

        return lane_changes_list

