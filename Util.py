###
# Contains utility methods that can be used in any class throughout the repository
###

import os

import LaneArt

file_location_root = "/Game/WwiseAudio/Events/Beatmaps/Music/mx_"
file_path_root = "Content/ProjectRadiance/Data/"
border = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

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
    dropdown_for_user_input(song_directories)
    directory_input = input("Enter the number of the song you would like to beatmap: ")

    try:
        directory_input = int(directory_input)

        if 0 < directory_input < len(song_directories) + 1:
            return song_directories[directory_input - 1]
        else:
            print("\nPlease enter a number from the dropdown list.")
            input_stored_songs(song_directories)

    except ValueError:
        print("\nPlease enter a number from the dropdown list.")
        input_stored_songs(song_directories)


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

    try:
        directory_input = int(directory_input)

        if 0 < directory_input < len(difficulty_beatmaps) + 1:
            return difficulty_beatmaps[directory_input - 1]
        else:
            print("\nPlease enter a number from the dropdown list.")
            input_stored_difficulties(difficulty_beatmaps)

    except ValueError:
        print("\nPlease enter a number from the dropdown list.")
        input_stored_difficulties(difficulty_beatmaps)


def extract_and_sort_difficulties(difficulty_list):
    difficulty_list = [s[:-5] for s in difficulty_list]
    difficulty_list = [s.rsplit('_', 1)[1] for s in difficulty_list]
    difficulty_list = [int(difficulty) for difficulty in difficulty_list]
    return sorted(difficulty_list)
