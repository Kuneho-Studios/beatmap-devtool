###
# Contains the flow for when a user would like to update an existing beatmap.
# This does the bulk of that work. Fetches the desired song and difficulty
# beatmap then provides prompts to the user to aid in editing the beatmap.
###
import json

import Util

current_lane_count = None
current_lane_configuration = None
current_lane_configuration_art = None

current_song = None
current_difficulty = None
current_beat = None

available_actions_list = [
    "Add Notes",
    # "Edit Note",
    # "Delete Note",
    "Shift All Notes",
    "Shift Some Notes",
    "Show All Lane Swaps",
    # Enter any new commands before exit
    "Exit"
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
        shift_input = input("Enter the count to shift all the beats "
                            "(prefix with `-` for shift left or `+` to shift right): ").strip()

        if shift_input[0] != "+" and shift_input[0] != "-":
            print("Please include a '+' or '-' before the amount to shift")
            edit_beatmap_input(notes)
        try:
            float(shift_input[1:])
            notes = shift_all_notes(shift_input, notes)
            edit_beatmap_input(notes)
        except ValueError:
            print("Please enter only a number after the '+' or '-'")
            edit_beatmap_input(notes)
    elif available_actions_list[action_input - 1] == "Shift Some Notes":
        # todo give option to shift a subset of notes opposed to every note
        print("Shifting some notes")
        edit_beatmap_input(notes)
    elif available_actions_list[action_input - 1] == "Add Notes":
        notes = add_note(notes)
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
def shift_all_notes(shift_input, notes):
    shift_amount = float(shift_input[1:])
    if shift_input[0] == '-':
        shift_amount = -1 * shift_amount

    for note in notes:
        note["startBeat"] = note["startBeat"] + shift_amount

    return notes

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
