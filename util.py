import os

import laneArt

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
  "Two Lanes Left to Right": laneArt.two_lanes_left_right,
  "Two Lanes Right to Left": laneArt.two_lanes_right_left
}

three_lane_swap_types_dict = {}

four_lane_swap_types_dict = {
  "Four Lanes Top to Bottom": laneArt.four_lanes_top_bottom,
  "Four Lanes Bottom to Top": laneArt.four_lanes_bottom_top,
  "Four Corners": laneArt.four_lanes_corners,
  "Four Lanes Left to Right": laneArt.four_lanes_left_right,
  "Four Lanes Right to Left": laneArt.four_lanes_right_left
}

five_lane_swap_types_dict = {
  "Five Lanes Top to Bottom": laneArt.five_lanes_top_bottom,
  "Five Lanes Bottom to Top": laneArt.five_lanes_bottom_top,
  "Five Lanes Right to Left": laneArt.five_lanes_right_left,
  "Five Lanes Left to Right": laneArt.five_lanes_left_right,
  "Four Corners and Middle Top to Bottom": laneArt.five_lanes_corner_middle_top_bottom,
  "Four Corners and Middle Bottom to Top": laneArt.five_lanes_corner_middle_bottom_top,
}

lane_swap_types_dict = {
  1: one_lane_swap_types_dict,
  2: two_lane_swap_types_dict,
  3: three_lane_swap_types_dict,
  4: four_lane_swap_types_dict,
  5: five_lane_swap_types_dict
}


def string_to_pascal_case(string_to_convert):
  words = string_to_convert.split()
  pascal_case_words = [word.capitalize() for word in words]
  return ''.join(pascal_case_words)


def dropdown_for_user_input(list_to_print):
  display_index = 1

  for item in list_to_print:
    print(str(display_index) + ") " + str(item))
    display_index += 1


def get_stored_songs():
  song_directories = os.listdir('beatmaps/')
  song_directories.remove("EMPTY_BEATMAP_DO_NOT_DELETE.json")
  return song_directories

def input_stored_songs(song_directories):
  print("\nAvailable Songs:")
  dropdown_for_user_input(song_directories)
  directory_input = int(
      input("Enter the number of the song you would like to beatmap: "))
  return song_directories[directory_input - 1]


def get_stored_difficulties(song_name):
  difficulty_beatmaps = os.listdir('beatmaps/' + song_name + "/")
  return [element for element in difficulty_beatmaps if
          "Data.json" not in element]


def input_stored_difficulties(difficulty_beatmaps):
  print("\nAvailable Difficulties:")
  dropdown_for_user_input(difficulty_beatmaps)
  directory_input = int(
      input("Enter the number of the difficulty you would like to beatmap: "))

  difficulty_name = difficulty_beatmaps[directory_input - 1]
  return difficulty_name
