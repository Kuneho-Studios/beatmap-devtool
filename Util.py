###
# Contains utility methods that can be used in any class throughout the repository
###
import json
import os
import LaneArt

BEATMAPS_DIRECTORY = 'beatmaps/'

FILE_LOCATION_ROOT = "/Game/WwiseAudio/Events/Beatmaps/Music/mx_"
FILE_PATH_ROOT = "Content/ProjectRadiance/Data/"

note_types_list = [
    "Tap",
    "Hold",
    "LaneSwap"
]

one_lane_swap_types_dict = {}

two_lane_swap_types_dict = {
    "Two Lanes Left to Right": LaneArt.TWO_LANES_RIGHT_LEFT,
    "Two Lanes Right to Left": LaneArt.TWO_LANES_LEFT_RIGHT
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


# helper method that given a list.
# creates the prompt menu which displays all elements in the list for the user to pick from
def dropdown_for_user_input(list_to_print):
    display_index = 1

    for item in list_to_print:
        print(str(display_index) + ") " + str(item))
        display_index += 1


# reads from the beatmaps directory to return all the saved songs
# if directory does not exist, return an empty list
def get_stored_songs():
    if not os.path.exists('beatmaps/'):
        return []
    song_directories = os.listdir('beatmaps/')
    return song_directories


# given a list of songs, display them for the user to input which they would like to edit
def input_stored_songs(song_directories):
    print("\nAvailable Songs:")

    song_name_list = []
    for song in song_directories:
        song_name_list.append(get_song_name(str(song)))

    dropdown_for_user_input(song_name_list)
    directory_input = input("Enter the number of the song you would like to beatmap: ")

    directory_input = validate_dropdown_input(directory_input, len(song_name_list))
    if directory_input is None:
        return input_stored_difficulties(song_name_list)
    else:
        return song_directories[int(directory_input) - 1]


# reads from the given song name directory to return all the saved difficulties
# doesn't display the ...Data.json file that is present for every song
def get_stored_difficulties(song_name):
    difficulty_beatmaps = os.listdir('beatmaps/' + song_name + "/")
    return [element for element in difficulty_beatmaps if
            "Data.json" not in element]


# given a list of difficulties for a select song, display them for the user to input which they would like to edit
def input_stored_difficulties(difficulty_beatmaps):
    print("\nAvailable Difficulties:")
    dropdown_for_user_input(difficulty_beatmaps)
    directory_input = input("Enter the number of the difficulty you would like to beatmap: ")

    directory_input = validate_dropdown_input(directory_input, len(difficulty_beatmaps))
    if directory_input is None:
        return input_stored_difficulties(difficulty_beatmaps)
    else:
        return difficulty_beatmaps[int(directory_input) - 1]


# takes the name of the beatmap and extracts the difficulty as the number immediately before the .json and after the
# last, and more often than not, only "_"
def extract_and_sort_difficulties(difficulty_list):
    difficulty_list = [s[:-5] for s in difficulty_list]
    difficulty_list = [s.rsplit('_', 1)[1] for s in difficulty_list]
    difficulty_list = [int(difficulty) for difficulty in difficulty_list]
    return sorted(difficulty_list)


# when a dropdown is presented to the user, verify that they entered not only a number,
# but also one that is present in the list
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
            BEATMAPS_DIRECTORY + song_save_name + "/" + song_save_name + "Data.json",
            "r") as root_data_file:
        song_name = json.load(root_data_file)['songName']
    root_data_file.close()
    return song_name


# box to put information regarding the last note entered
def note_report(current_lane_configuration, current_lane_configuration_art, last_beat):
    lane_configuration_line = " Lane Configuration: " + current_lane_configuration
    lane_configuration_art_line = " Lane Configuration Art: " + current_lane_configuration_art
    last_beat_line = " Last Beat: " + last_beat[0]['beat']

    last_notes_line = " Last Note(s): "
    for note in last_beat:
        print(note)
        last_notes_line = last_notes_line + "\n\tLane " + note['lane'] + " (" + note['noteType'] + ")"

    # print("LONGEST ", max(lane_configuration_line, last_beat_line, last_notes_line,
    #                       key=len))
    # longest_line = len(max(lane_configuration_line, last_beat_line, last_notes_line,
    #                        key=len))
    # print("LONGEST LINE ", longest_line)
    box_width = len(lane_configuration_line) + 4
    print("┌" + ("-" * (box_width - 2)) + "┐")
    print(" " + lane_configuration_line + " ")
    print(" " + lane_configuration_art_line + " ")
    print(" " + last_beat_line + " ")
    print(" " + last_notes_line + " ")
    print("└" + "-" * (box_width - 2) + "┘")


# fetches last beat from the current beatmap that's being edited
def get_last_beat_difficulty():
    # todo implement fetching last beat from the current file that's being edited
    return [{"beat": "not implemented", "lane": "not implemented", "noteType": "not implemented"}]


# fetches highest last beat from the current song (not the specific beatmap) that's being edited
# to be used in getting the totalBeats field for the Data.json file for a given song
def get_last_beat_song():
    # todo implement fetching last beat amongst all the files in a given song
    return ""
