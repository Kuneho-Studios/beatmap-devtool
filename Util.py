###
# Contains utility methods that can be used in any class
###
import json
import os

import LaneArt

BEATMAPS_DIRECTORY = 'beatmaps/'

FILE_LOCATION_ROOT = "/Game/WwiseAudio/Events/Beatmaps/Music/mx_"
FILE_PATH_ROOT = "Content/ProjectRadiance/Data/"

MAX_LANE_SIZE = 5

note_types_list = [
    "Tap",
    "Hold",
    "LaneSwap"
]

one_lane_swap_types_dict = {}

two_lane_swap_types_dict = {
    "Two Lanes Left to Right": LaneArt.TWO_LANES_LEFT_RIGHT,
    "Two Lanes Right to Left": LaneArt.TWO_LANES_RIGHT_LEFT,
}

three_lane_swap_types_dict = {}

four_lane_swap_types_dict = {
    "Four Lanes Top to Bottom": LaneArt.FOUR_LANES_TOP_BOTTOM,
    "Four Lanes Bottom to Top": LaneArt.FOUR_LANES_BOTTOM_TOP,
    "Four Corners": LaneArt.FOUR_LANES_CORNERS,
    "Four Lanes Left to Right": LaneArt.FOUR_LANES_LEFT_RIGHT,
    "Four Lanes Right to Left": LaneArt.FOUR_LANES_RIGHT_LEFT
}

five_lane_swap_types_dict = {
    "Five Lanes Top to Bottom": LaneArt.FIVE_LANES_TOP_BOTTOM,
    "Five Lanes Bottom to Top": LaneArt.FIVE_LANES_BOTTOM_TOP,
    "Five Lanes Right to Left": LaneArt.FIVE_LANES_RIGHT_LEFT,
    "Five Lanes Left to Right": LaneArt.FIVE_LANES_LEFT_RIGHT,
    "Four Corners and Middle Top to Bottom": LaneArt.FIVE_LANES_CORNER_MIDDLE_TOP_BOTTOM,
    "Four Corners and Middle Bottom to Top": LaneArt.FIVE_LANES_CORNER_MIDDLE_BOTTOM_TOP,
}

lane_swap_types_dict = {
    1: ("One Lane", one_lane_swap_types_dict),
    2: ("Two Lanes", two_lane_swap_types_dict),
    3: ("Three Lanes", three_lane_swap_types_dict),
    4: ("Four Lanes", four_lane_swap_types_dict),
    5: ("Five Lanes", five_lane_swap_types_dict)
}


# converts a string to PascalCase
def string_to_pascal_case(string_to_convert):
    words = string_to_convert.split()
    pascal_case_words = [word.capitalize() for word in words]
    return ''.join(pascal_case_words)


# converts a string to Space Case
def camel_case_to_space_case(string_to_convert):
    space_case_string = string_to_convert[0].upper()  # Add the first character as it is
    for char in string_to_convert[1:]:
        if char.isupper():
            space_case_string += " " + char
        else:
            space_case_string += char
    return space_case_string


# helper method that given a list.
# creates the prompt menu which displays all elements
# in the list for the user to pick from
def dropdown_for_user_input(list_to_print):
    display_index = 1

    for item in list_to_print:
        print(str(display_index) + ") " + str(item))
        display_index += 1


# gets the specified beatmap that the user would like to edit
def get_user_beatmap():
    song_list = get_stored_songs()

    if len(song_list) == 0:
        fancy_print_box(
            "⚠ There are no beatmaps present. Please create one first ⚠")
        return None
    else:
        return get_beatmap(song_list)


# reads from the beatmaps directory to return all the saved songs
# if directory does not exist, return an empty list
def get_stored_songs():
    if not os.path.exists(BEATMAPS_DIRECTORY):
        return []
    song_directories = os.listdir(BEATMAPS_DIRECTORY)
    return song_directories


# given a list of songs, display them for the user to input which they edit
def input_stored_songs(song_directories):
    print("\nAvailable Songs:")

    song_name_list = []
    for song in song_directories:
        song_name_list.append(get_song_name(str(song)))

    dropdown_for_user_input(song_name_list)
    directory_input = input(
        "Enter the number of the song you would like to beatmap: ")

    directory_input = validate_dropdown_input(
        directory_input, len(song_name_list))
    if directory_input is None:
        return input_stored_difficulties(song_name_list)
    else:
        return song_directories[int(directory_input) - 1]


# reads from the given song name directory to return all the saved difficulties
# doesn't display the ...Data.json file that is present for every song
def get_stored_difficulties(song_name):
    difficulty_beatmaps = os.listdir(BEATMAPS_DIRECTORY + song_name + "/")
    return [element for element in difficulty_beatmaps if
            "Data.json" not in element]


# given a list of difficulties for a select song,
# display them for the user to input which they would like to edit
def input_stored_difficulties(difficulty_beatmaps):
    print("\nAvailable Difficulties:")
    dropdown_for_user_input(difficulty_beatmaps)
    directory_input = input(
        "Enter the number of the difficulty you would like to use: ")

    directory_input = validate_dropdown_input(
        directory_input, len(difficulty_beatmaps))
    if directory_input is None:
        return input_stored_difficulties(difficulty_beatmaps)
    else:
        return difficulty_beatmaps[int(directory_input) - 1]


# takes the name of the beatmap and extracts the difficulty as the number
# immediately before the .json and after the last  "_"
def extract_and_sort_difficulties(difficulty_list):
    difficulty_list = [s[:-5] for s in difficulty_list]
    difficulty_list = [s.rsplit('_', 1)[1] for s in difficulty_list]
    difficulty_list = [int(difficulty) for difficulty in difficulty_list]
    return sorted(difficulty_list)


# when a dropdown is presented to the user, verify that they entered a number,
# and also one that is present in the list
def validate_dropdown_input(user_input, list_length):
    try:
        user_input = int(user_input)

        if 0 < user_input <= list_length:
            return user_input
        else:
            print("\nPlease enter a number from the dropdown list.")
            return None

    except ValueError:
        print("\nPlease enter a number from the dropdown list.")
        return None


# box to put headers in
def fancy_print_box(text):
    length = len(text) + 3
    print("\n" + "~" * length)
    print(" " + text + " ")
    print("~" * length)


# gets the song name from the Data.json file
def get_song_name(song_save_name):
    with open(
            BEATMAPS_DIRECTORY + song_save_name + "/"
            + song_save_name + "Data.json", "r") as root_data_file:
        song_name = json.load(root_data_file)['songName']
    root_data_file.close()
    return song_name


# box to put information regarding the last note entered
def note_report(current_lane_configuration, current_lane_configuration_art, last_beat):
    lane_configuration_line = (
            " Lane Configuration: " + current_lane_configuration)
    lane_configuration_art_line = (
            " Lane Configuration Art: \n" + current_lane_configuration_art)

    if not isinstance(last_beat, list):
        last_beat_line = " Last Beat: " + str(last_beat)
        last_notes_line = " Last Note: None"
    elif not last_beat:
        last_beat_line = " Last Beat: None"
        last_notes_line = " Last Note: None"
    else:
        if len(last_beat) == 1:
            last_notes_line = " Last Note: "
        else:
            last_notes_line = " Last Notes: "
        last_beat_line = (
                " Last Beat: " + str(last_beat[0]['beat']))

        for note in last_beat:
            last_notes_line = (str(last_notes_line) + "Lane " + str(note['lane'])
                               + " (" + note['noteType'] + "), ")
        last_notes_line = last_notes_line.removesuffix(", ")

    max_length_line = max(lane_configuration_line, last_notes_line, key=len)
    box_width = len(max_length_line) + 4
    print("\n┌" + ("-" * (box_width - 2)) + "┐")
    print(" " + lane_configuration_line + " ")
    print(" " + lane_configuration_art_line + " ")
    print(" " + last_beat_line + " ")
    print(" " + last_notes_line + " ")
    print("└" + "-" * (box_width - 2) + "┘\n")


# fetches last beat from the current beatmap that's being edited
def get_last_beat(current_beat, notes_list):
    if len(notes_list) == 0:
        return []

    last_lane_list = []
    i = 1
    is_found = False
    while i < len(notes_list) + 1:
        this_note = notes_list[-i]
        if this_note["startBeat"] == current_beat:
            last_lane_list.append({"beat": current_beat,
                                   "lane": this_note["lane"],
                                   "noteType": this_note["noteData"]["noteType"]})
            is_found = True
        elif is_found or this_note["startBeat"] < current_beat:
            break
        i += 1

    if not last_lane_list:
        return []
    else:
        return sorted(last_lane_list, key=lambda note: (note['lane']))


# reads the laneEvents at the bottom of the beatmap
# sets global current lane variables to match those
def get_initial_lane_configuration(lanes_list):
    lane_positions = []
    none_count = 0

    for lane in lanes_list:
        this_lane = lane['newLanePosition']
        lane_positions.append(this_lane)
        if "None" in this_lane:
            none_count = none_count + 1

    return get_current_lane_values((MAX_LANE_SIZE - none_count), lane_positions)


# reads the noteData for each note. if noteType is swap
# then determine the art and plaintext name of the swap
def get_lane_swaps(notes_list, song_name, song_difficulty):
    lane_positions = []
    none_count = 0

    # get original lane configuration
    notes, lane_events = read_beatmap(song_name, song_difficulty)
    original_lane_configuration = \
        get_initial_lane_configuration(lane_events[0]['lanes'])
    swaps_dict = {0: (original_lane_configuration[0], original_lane_configuration[1], original_lane_configuration[2])}

    for note in notes_list:
        if note["noteData"]["noteType"] == "LaneSwap":
            lanes_list = note["noteData"]['laneChanges']
            for lane in lanes_list:
                lane_positions.append(lane["newLanePosition"])
                if "None" in lane["newLanePosition"]:
                    none_count = none_count + 1

            lane_count, lane_config, lane_art = \
                get_current_lane_values((MAX_LANE_SIZE - none_count), lane_positions)
            swaps_dict[note["startBeat"]] = ((MAX_LANE_SIZE - none_count), lane_config, lane_art)
            none_count = 0
            lane_positions = []

    return swaps_dict


# given the amount of lanes and the lane positions
# loop through the art to determine which variation is used
# as well as the plaintext name of the variation
def get_current_lane_values(lane_count, lane_positions):
    lane_dictionary = get_lane_swap_dictionary(lane_count)

    current_lane_configuration = None
    current_lane_configuration_art = None

    # loop through the various configurations
    # outer-loop used to get the plain text name once position array matches
    for i in lane_dictionary.items():
        # loop through the art for a given configuration
        # if the lane position array's match, then return this art and break
        for j in i[1]:
            if lane_positions == j[1]:
                current_lane_configuration_art = j[0]
                break
        # a check to ensure that the inner loop is "break"ed and not just done
        if current_lane_configuration_art is not None:
            current_lane_configuration = i[0]
            break

    return lane_count, current_lane_configuration, current_lane_configuration_art


# helper method to determine which dictionary to loop through
def get_lane_swap_dictionary(lane_count):
    if lane_count == 1:
        return one_lane_swap_types_dict
    elif lane_count == 2:
        return two_lane_swap_types_dict
    elif lane_count == 3:
        return three_lane_swap_types_dict
    elif lane_count == 4:
        return four_lane_swap_types_dict
    elif lane_count == 5:
        return five_lane_swap_types_dict
    else:
        print("CURRENT COUNT OF " + str(lane_count)
              + " NOT FOUND. PLEASE REPORT")


# method to fancy print and display the gathered lane swap events
def show_lane_swaps(notes_list, song_name, song_difficulty):
    # get lane swap events
    lane_swaps_dict = get_lane_swaps(notes_list, song_name, song_difficulty)

    box_width = 34
    print("\n┌" + ("-" * (box_width - 2)) + "┐")

    dict_index = 0
    for dict_beat, dict_configs in lane_swaps_dict.items():
        print(" Beat\n" + "\t" + str(dict_beat))
        print(" Lane Swap Name\n" + "\t" + dict_configs[1])
        print(" Lane Swap Art\n" + dict_configs[2])
        if dict_index < len(lane_swaps_dict) - 1:
            print("~" * box_width)
            dict_index += 1

    print("└" + "-" * (box_width - 2) + "┘\n")


# reads the beatmap and returns the notes and lane events elements
def read_beatmap(song_name, song_difficulty):
    with open(BEATMAPS_DIRECTORY + song_name + "/"
              + song_name + "_" + song_difficulty + ".json",
              "r") as beatmap_read:
        json_data = json.loads(beatmap_read.read())
        notes = json_data["notes"]
        lane_events = json_data["laneEvents"]
    beatmap_read.close()
    return notes, lane_events


# given a list of songs, determine which song the user wants
# then return the song name and difficulty number of their selected song
def get_beatmap(song_list):
    song = input_stored_songs(song_list)
    difficulty_list = extract_and_sort_difficulties(
        get_stored_difficulties(song))
    difficulty = str(input_stored_difficulties(difficulty_list))
    return song, difficulty


# given a list of json items, replace a specific element in a the json object
def replace_field_in_json_list(json_list, field_name, old_substring, new_substring):
    updated_list = []
    for json_obj in json_list:
        if field_name in json_obj:
            json_obj[field_name] = json_obj[field_name].replace(old_substring, new_substring)
        updated_list.append(json_obj)
    return updated_list
