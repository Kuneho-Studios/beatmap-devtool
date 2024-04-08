###
# Contains the flow for when a user would like to update an existing beatmap. This does the bulk of that work.
# Fetches the desired song and difficulty beatmap then provides prompts to the user to aid in editing the beatmap.
###
import json
import laneArt
import util

CURRENT_LANE_COUNT = 2
CURRENT_LANE_CONFIGURATION = "Two Lanes Left to Right"
CURRENT_LANE_CONFIGURATION_ART = laneArt.TWO_LANES_RIGHT_LEFT[0][0]


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

    notes_filled = edit_beatmap_input(notes)
    sorted_notes_filled = sorted(notes_filled, key=lambda note: (
        note['startBeat'], note['lane']))

    with open('beatmaps/' + song_name + "/"
              + song_name + "_" + song_difficulty + ".json",
              "w") as beatmap_write:
        json.dump({"notes": sorted_notes_filled, "laneEvents": lane_events},
                  beatmap_write, indent=4)
    beatmap_write.close()
    print(
        util.border + "\t\t✨ " + song_name + " on " + song_difficulty + " difficulty updated! ✨" + util.border)


# obtain the beat for the current note to be added to the beatmap
def edit_beatmap_input(notes):
    beat = input(
        "What is the beat for the note you want to add? (type 'exit' to leave editor) ")
    if beat.lower() == "exit":
        return
    else:
        try:
            beat = float(beat)
        except ValueError:
            print("Either enter a number or 'exit'!")
            edit_beatmap_input(notes)
        lane = set_lane(beat)
        note_data = set_note_data(beat, lane)
        note_json_object = {"startBeat": beat, "lane": lane, "noteData": note_data}
        notes.append(note_json_object)

        edit_beatmap_input(notes)
    return notes


# set the lane that the current beat will reside on
def set_lane(beat):
    print("\nCurrent Lane Configuration: " + CURRENT_LANE_CONFIGURATION)
    print(CURRENT_LANE_CONFIGURATION_ART)
    for i in range(CURRENT_LANE_COUNT):
        print(str(i + 1) + ") Lane " + str(i + 1))
    lane = input("What lane is beat " + str(beat) + " on? ")
    try:
        lane = int(lane)
    except ValueError:
        print("Enter a number!")
        set_lane(beat)

    if lane < 1 or lane > CURRENT_LANE_COUNT:
        print(
            str(
                lane) + " is not included in the above range. Please enter again.\n")
        set_lane(beat)

    return lane


# set the note type. if is a "laneSwap" then call methods to determine what to swap to
def set_note_data(beat, lane):
    print("\nAvailable Note Types:")
    util.dropdown_for_user_input(util.note_types_list)
    note_type_input = int(input(
        "Enter the number of beat " + str(beat) + " lane " + str(
            lane) + "'s note type: "))

    if note_type_input < 1 or note_type_input > len(util.note_types_list) + 1:
        print(
            note_type_input + " is not included in the above range. Please enter again.")
        set_note_data(beat, lane)

    if util.note_types_list[note_type_input - 1] == "LaneSwap":
        return {"noteType": "LaneSwap", "laneChanges": set_lane_swap()}

    return {"noteType": util.note_types_list[note_type_input - 1]}


# given the desire to perform a lane swap, prompt and gather how many lanes the user would like the swap to have
def set_lane_swap():
    print("\nAvailable Lane Sizes:")
    util.dropdown_for_user_input(util.lane_swap_types_dict.keys())
    lane_swap_lane_count = input(
        "Enter the number of lanes in the new lane configuration? ")
    try:
        lane_swap_lane_count = int(lane_swap_lane_count)
    except ValueError:
        print("Enter a number!")
        set_lane_swap()
    if lane_swap_lane_count not in util.lane_swap_types_dict.keys():
        print(lane_swap_lane_count + " is not a valid lane size configuration." +
              " Your options are: " + str(util.lane_swap_types_dict.keys()))
        set_lane_swap()
    return set_lane_variation(lane_swap_lane_count)


# given the desired lane swap count, display the art for the different variations and allow the user to select which one
def set_lane_variation(lane_swap_lane_count):
    lane_type_keys = util.lane_swap_types_dict.get(lane_swap_lane_count).keys()

    print("\nAvailable Lane Variations:")
    util.dropdown_for_user_input(lane_type_keys)
    lane_type_input = int(
        input("Enter the " + str(lane_swap_lane_count) + "-lane variation: "))

    if lane_type_input > len(lane_type_keys):
        print(
            lane_type_input + " is not included in the above range. Please enter again.")
        set_lane_variation(lane_swap_lane_count)

    global CURRENT_LANE_CONFIGURATION
    CURRENT_LANE_CONFIGURATION = list(lane_type_keys)[lane_type_input - 1]

    lane_configuration = util.lane_swap_types_dict.get(lane_swap_lane_count).get(
        CURRENT_LANE_CONFIGURATION)

    return set_lane_changes(lane_configuration)


# given the desired lane format, display the art for the different changes and allow the user to select which one
def set_lane_changes(lane_configuration_list):
    lane_configuration_art_list = []
    for lane_configuration in lane_configuration_list:
        lane_configuration_art_list.append(lane_configuration[0])

    print("\nAvailable Lane Positions:")
    util.dropdown_for_user_input(lane_configuration_art_list)
    lane_configuration_input = int(input(
        "Enter the number of the lane configuration you want the swap to be: "))
    selected_lane_list = lane_configuration_list[lane_configuration_input - 1][1]

    lane_changes_list = []
    for i in range(5):
        lane_changes_list.append(
            {"lane": i, "newLanePosition": selected_lane_list[i]})

    global CURRENT_LANE_CONFIGURATION_ART
    CURRENT_LANE_CONFIGURATION_ART = \
        lane_configuration_list[lane_configuration_input - 1][0]

    return lane_changes_list
