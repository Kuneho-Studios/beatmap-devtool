###
# Contains the flow for when a user would like to update an existing beatmap.
# This does the bulk of that work. Fetches the desired song and difficulty
# beatmap then provides prompts to the user to aid in editing the beatmap.
###
import json
import copy
import Util
from Help import *

lane_configurations = {}
initial_lane_events = None

current_lane_count = None
current_lane_configuration = None
current_lane_configuration_art = None

current_song = None
current_difficulty = None
current_beat = None

available_actions_list = [
    HELP_ACTION,
    BACK_ACTION,
    # Enter any new commands after back
    SET_BEAT_ACTION,
    ADD_NOTE_ACTION,
    EDIT_NOTE_ACTION,
    DELETE_NOTE_ACTION,
    SHIFT_SOME_NOTES_ACTION,
    SHIFT_ALL_NOTES_ACTION,
    SHOW_ALL_LANE_CHANGES_ACTION,
    COPY_SOME_NOTES_ACTION,
    SAVE_ACTION
]


# open the existing beatmap for editing. then calls method edit_beatmap_input
# to loop through the editing/adding process obtain the laneEvents since it
# will not be changed here. paste it at the end of the editing process to
# ensure it remains.
def edit_beatmap(song_name, song_difficulty):
    global current_song, current_difficulty, current_beat, initial_lane_events
    current_song = song_name
    current_difficulty = song_difficulty
    current_beat = 0

    notes, lane_events = Util.read_beatmap(song_name, song_difficulty)

    if not lane_events:
        lane_events = set_lane_event()
        Util.fancy_print_box("✨ Initial lane configuration set!"
                             " You can proceed to beatmapping now! ✨")
        save_beatmap(notes, song_name, song_difficulty, lane_events)

    else:
        global lane_configurations, current_lane_count, current_lane_configuration, \
            current_lane_configuration_art

        if len(notes) > 0:
            current_beat = notes[-1]["startBeat"]

        update_lane_configuration(current_beat, notes)

    initial_lane_events = lane_events
    notes = edit_beatmap_input(notes)

    save_beatmap(notes, song_name, song_difficulty, lane_events)


# obtain the beat for the current note to be added to the beatmap
def edit_beatmap_input(notes):
    global current_beat

    action_input = ""
    while action_input != 1:
        Util.note_report(current_lane_configuration, current_lane_configuration_art,
                         Util.get_last_beat(current_beat, notes), current_beat)

        print("\nAvailable Beatmap Actions:")
        Util.dropdown_for_user_input(available_actions_list, True)

        action_input = (
            input("Enter the number of the action you'd like to perform: "))

        action_input = (
            Util.validate_dropdown_input(action_input, len(available_actions_list), True))

        if available_actions_list[action_input] == HELP_ACTION:
            edit_beatmap_input_help()
        elif available_actions_list[action_input] == SHOW_ALL_LANE_CHANGES_ACTION:
            Util.show_lane_changes(notes, current_song, current_difficulty)
        elif available_actions_list[action_input] == SHIFT_ALL_NOTES_ACTION:
            shift_all_notes(notes)
        elif available_actions_list[action_input] == SHIFT_SOME_NOTES_ACTION:
            notes = shift_some_notes(notes, current_beat)
        elif available_actions_list[action_input] == ADD_NOTE_ACTION:
            lane = set_lane(current_beat)
            notes = add_note(notes, current_beat, lane)
        elif available_actions_list[action_input] == COPY_SOME_NOTES_ACTION:
            copy_note_segment(notes)
        elif available_actions_list[action_input] == SET_BEAT_ACTION:
            current_beat = set_beat()
            update_lane_configuration(current_beat, notes)
        elif available_actions_list[action_input] == DELETE_NOTE_ACTION:
            notes = delete_note(notes, current_beat)
        elif available_actions_list[action_input] == EDIT_NOTE_ACTION:
            notes = edit_note(notes, current_beat)
        elif available_actions_list[action_input] == SAVE_ACTION:
            save_beatmap(notes, current_song, current_difficulty, initial_lane_events)

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

    note_type_input = Util.validate_dropdown_input(note_type_input, len(Util.note_types_list))
    if note_type_input is None:
        return set_note_data(beat, lane)
    else:
        if Util.note_types_list[note_type_input - 1] == "LaneChange":
            return {"noteType": "LaneChange", "laneChanges": set_lane_change()}

        return {"noteType": Util.note_types_list[note_type_input - 1]}


# given the desire to perform a lane change
# prompt and gather how many lanes the user would like the swap to have
def set_lane_change():
    print("\nAvailable Lane Sizes:")
    lane_names = [value[0] for value in Util.lane_change_types_dict.values()]
    Util.dropdown_for_user_input(lane_names)

    lane_change_lane_count = (
        input("Enter the number of lanes in the new lane configuration? "))

    lane_change_lane_count = (
        Util.validate_dropdown_input(lane_change_lane_count, len(lane_names)))
    if lane_change_lane_count is None:
        return set_lane_change()
    else:
        return set_lane_configuration(lane_change_lane_count)


# given the desired lane change count, display the art for the different configurations
# allow the user to select which one
def set_lane_configuration(lane_change_lane_count):
    lane_change_list_values = list(Util.lane_change_types_dict.values())
    lane_configuration_size, lane_configuration_options = lane_change_list_values[lane_change_lane_count - 1]

    lane_type_keys = (
        list(lane_configuration_options.keys()))

    print("\nAvailable Lane Configurations:")
    Util.dropdown_for_user_input(lane_type_keys)

    lane_type_input = (input("Enter the " + lane_configuration_size + " configuration: "))

    lane_type_input = (
        Util.validate_dropdown_input(lane_type_input, len(lane_type_keys)))

    if lane_type_input is None:
        return set_lane_configuration(lane_change_lane_count)
    else:
        global current_lane_configuration, current_lane_count

        lane_configuration = lane_configuration_options.get(list(lane_type_keys)[lane_type_input - 1])

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

        return lane_changes_list


# populate the laneEvents segment which is used for starting lane configuration
def set_lane_event():
    Util.fancy_print_box(
        "⚠ You do not have the initial lane setup configured! "
        "Let's do that now ⚠")
    return [{"startBeat": 0, "lanes": set_lane_change()}]


# when the song is saved, fetch what was previously stored in the length field
# if the highest beat in the current beatmap is greater than the current length
# then update length to reflect that value
def set_song_note_length(song_name, notes):
    with open(Util.BEATMAPS_DIRECTORY + song_name + "/" + song_name + "Data.json", "r") \
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
        with open(Util.BEATMAPS_DIRECTORY + song_name + "/" + song_name + "Data.json",
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
def shift_some_notes(notes, beat):
    shift_end_input = input("Enter the beat where the shift ends: ").strip()
    try:
        shift_end_input = float(shift_end_input)
        if shift_end_input < beat:
            print("Please ensure that the end beat count is the same or later"
                  " than the start beat count")
            shift_some_notes(notes, beat)
    except ValueError:
        print("Please enter valid number for the end beat")
        shift_some_notes(notes, beat)

    shift_input = input("Enter the count to shift the beats between "
                        + str(beat) + " and "
                        + str(shift_end_input) +
                        " (prefix with `-` for shift left or `+` to shift right): ").strip()

    if shift_input[0] != "+" and shift_input[0] != "-":
        print("Please include a '+' or '-' before the amount to shift")
        shift_some_notes(notes, beat)
    try:
        shift_amount = float(shift_input[1:])
        if shift_input[0] == '-':
            shift_amount = -1 * shift_amount

        for note in notes:
            if beat <= note["startBeat"] <= shift_end_input:
                note["startBeat"] = note["startBeat"] + shift_amount

        return notes
    except ValueError:
        print("Please enter only a number after the '+' or '-'")
        shift_some_notes(notes, beat)


# add a note to the beatmap
def add_note(notes, beat, lane):
    note_data = set_note_data(beat, lane)

    if note_data["noteType"] == "Chain":
        note_data = chain_notes_note_data(lane)
    if note_data["noteType"] == "Hold":
        note_data = hold_notes_note_data(beat, lane, note_data, notes)

    note_json_object = {"startBeat": beat,
                        "lane": lane,
                        "noteData": note_data}
    notes.append(note_json_object)

    return sorted(notes, key=lambda note: (note['startBeat'], note['lane']))


# handle which lanes get chained with the original supplied beat
def chain_notes_note_data(lane):
    chained_lanes_input = ""
    chained_lanes = []
    vacant_lanes = []
    for i in range(1, current_lane_count + 1):
        if i != lane:
            vacant_lanes.append(i)
    while chained_lanes_input != 0 and vacant_lanes:
        print("0) Done")
        for j, lane_number in enumerate(vacant_lanes):
            print(str(j + 1) + ") Lane " + str(lane_number))
        chained_lanes_input = (
            input("Enter the number of the lane you'd like to chain: "))
        chained_lanes_input = (
            Util.validate_dropdown_input(chained_lanes_input, len(vacant_lanes), True))
        if chained_lanes_input is not None and chained_lanes_input != 0:
            chained_lanes.append(vacant_lanes[chained_lanes_input - 1])
            vacant_lanes.pop(chained_lanes_input - 1)

    chained_lanes_data = []
    for k in chained_lanes:
        chained_lanes_data.append({"lane": k})
    return {"noteType": "Chain", "chainedLanes": chained_lanes_data}


# handle how long the hold note gets held for
def hold_notes_note_data(beat, lane, note_data, notes):
    hold_note_duration = input(
        "Enter the duration of the hold note in beats: ")

    while isinstance(hold_note_duration, str) or float(hold_note_duration) <= 1.0:
        try:
            hold_note_duration = float(hold_note_duration)
            if hold_note_duration <= 1:
                print("\nPlease enter a length greater than 1\n")
                hold_note_duration = input(
                    "Enter the duration of the hold note in beats: ")
        except ValueError:
            print("\nPlease enter a number.\n")
            hold_note_duration = input(
                "Enter the duration of the hold note in beats: ")

    note_data = {"noteType": "Hold", "endBeat": beat + (hold_note_duration - 1)}
    return note_data

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


# sets the current beat
def set_beat():
    beat = input("Enter the beat to jump to: ")

    try:
        return float(beat)
    except ValueError:
        print("\n Please enter a number.")
        set_beat()


# given a beat, update the lane configuration to reflect it
def update_lane_configuration(beat, notes):
    global current_song, current_difficulty, current_lane_configuration, current_lane_configuration_art, \
        current_lane_count
    lane_changes = Util.get_lane_changes(notes, current_song, current_difficulty)

    current_lane_count = lane_changes[0][0]
    current_lane_configuration = lane_changes[0][1]
    current_lane_configuration_art = lane_changes[0][2]

    if len(lane_changes) > 1:
        for dict_beat, dict_configs in lane_changes.items():
            if dict_beat < beat:
                current_lane_count = lane_changes[dict_beat][0]
                current_lane_configuration = lane_changes[dict_beat][1]
                current_lane_configuration_art = lane_changes[dict_beat][2]
            else:
                break


# given a beat, delete a specific a note
def delete_note(notes, beat):
    current_beat_notes_list = Util.get_last_beat(beat, notes)

    if not current_beat_notes_list:
        print("\nThere are no notes at this beat. Nothing to delete.\n")
    else:
        note_list = []
        for note in current_beat_notes_list:
            note_list.append(note['noteType'] + " (" + "Lane " + str(note['lane']) + ")")

        print("\nNotes at Beat " + str(beat) + ": ")
        Util.dropdown_for_user_input(note_list)

        note_to_delete_input = (
            input("Enter the number of the note you'd like to delete: "))

        note_to_delete_input = (
            Util.validate_dropdown_input(note_to_delete_input, len(note_list)))

        if note_to_delete_input is None:
            return delete_note(notes, beat)
        else:
            notes = [note for note in notes if note.get("startBeat") != beat or
                     note.get("lane") != current_beat_notes_list[note_to_delete_input - 1]['lane']]

    return notes


# given a beat, allow the user to edit it
def edit_note(notes, beat):
    current_beat_notes_list = Util.get_last_beat(beat, notes)

    if not current_beat_notes_list:
        return notes
    else:
        note_list = []
        for note in current_beat_notes_list:
            note_list.append(note['noteType'] + " (" + "Lane " + str(note['lane']) + ")")

        print("\nNotes at Beat " + str(beat) + ": ")
        Util.dropdown_for_user_input(note_list)

        note_to_edit_input = (
            input("Enter the number of the note you'd like to edit: "))

        note_to_edit_input = (
            Util.validate_dropdown_input(note_to_edit_input, len(note_list)))

        if note_to_edit_input is None:
            return edit_note(notes, beat)
        else:
            print("Current note is a " + str(current_beat_notes_list[note_to_edit_input - 1]['noteType']) + " on Lane "
                  + str(current_beat_notes_list[note_to_edit_input - 1]['lane']))
            lane = set_lane(beat)

            # remove old note
            notes = [note for note in notes if note.get("startBeat") != beat or
                     note.get("lane") != current_beat_notes_list[note_to_edit_input - 1]['lane']]

            # add new note
            return add_note(notes, beat, lane)


# save the current beatmap
def save_beatmap(notes, song_name, song_difficulty, lane_events):
    with open(Util.BEATMAPS_DIRECTORY + song_name + "/" + song_name + "_" + song_difficulty
              + ".json", "w") as beatmap_write:
        json.dump({"notes": notes, "laneEvents": lane_events},
                  beatmap_write, indent=4)
    beatmap_write.close()

    set_song_note_length(song_name, notes)

    Util.fancy_print_box("✨ " + song_name + " on " + song_difficulty
                         + " difficulty updated! ✨")
