import json
import os

file_location_root = "/Game/WwiseAudio/Events/Beatmaps/Music/mx_"
file_path_root = "Content/ProjectRadiance/Data/"
border = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

note_types_list = [
    "Tap",
    "Hold",
    "LaneSwap"
]

two_lane_swap_types_list = [
    "Two Lanes Left to Right",
    "Two Lanes Right to Left",
]

three_lane_swap_types_list = [

]

four_lane_swap_types_list = [
    "Four Lanes Top to Bottom",
    "Four Lanes Bottom to Top",
    "Four Corners",
    "Four Lanes Left to Right",
    "Four Lanes Right to Left"
]

five_lane_swap_types_list = [
    "Five Lanes Top to Bottom",
    "Five Lanes Right to Left",
    "Five Lanes Left to Right",
    "Four Corners and Middle Top to Bottom",
]

lane_swap_types_dict = {
    2: two_lane_swap_types_list,
    3: three_lane_swap_types_list,
    4: four_lane_swap_types_list,
    5: five_lane_swap_types_list
}


def main():
    print(border + "   ✨ Welcome To Project Radiance's Beatmap Dev Tool ✨" + border)
    get_user_purpose()


def get_user_purpose():
    create_or_edit = input("Would you like to create a new beatmap or edit an existing one? (create/edit) ")
    if create_or_edit.lower() == "create" or create_or_edit.lower() == "c":
        get_user_input()
    elif create_or_edit.lower() == "edit" or create_or_edit.lower() == "e":
        name, difficulty = get_beatmap()
        edit_beatmap(name, difficulty)
    else:
        print("Please only enter 'create' or 'edit'")
        get_user_purpose()


def get_user_input():
    song_name = input("What's the song name? ").strip()
    album_name = input("What's the album name? ").strip()
    artist_name = input("What's the artist name? ").strip()
    bpm = int(input("What's the song's beats per minute? "))
    length = int(input("How many total beats in the song? "))
    genre = input("What's the song's genre? ").strip()
    difficulty_count = int(input("How many difficulties are there? "))
    difficulties = []
    count = 0
    while count < difficulty_count:
        new_difficultly = input("What's difficulty " + str(count + 1) + "? ").strip()
        difficulties.append(new_difficultly)
        count += 1
    fill_data_template(song_name, album_name, artist_name, bpm, length, genre, difficulties)


def fill_data_template(song_name, album_name, artist_name, bpm, length, genre, difficulties):
    with open('template/data_json_template.json', 'r') as template_file:
        template = json.load(template_file)
    template_file.close()

    song_name_pascal = string_to_pascal_case(song_name)

    template["songName"] = song_name
    template["album"] = album_name
    template["artist"] = artist_name
    template["fileLocation"] = file_location_root + song_name_pascal
    template["bpm"] = bpm
    template["length"] = length
    template["genre"] = genre

    difficulty_data = []

    os.makedirs('beatmaps/' + song_name_pascal)

    for difficulty in difficulties:
        data = {
            "tier": difficulty,
            "filePath": file_path_root
                        + song_name_pascal + "_" + string_to_pascal_case(difficulty) + ".json"
        }
        difficulty_data.append(data)

        with open('beatmaps/' + song_name_pascal + "/"
                  + song_name_pascal + "_" + string_to_pascal_case(difficulty) + ".json",
                  "x") as difficulty_file:
            json.dump({"notes": [], "laneEvents": []}, difficulty_file, indent=4)
        difficulty_file.close()

    template["difficulty"] = difficulty_data

    with open('beatmaps/' + song_name_pascal + "/" + song_name_pascal + "Data.json", "x") as data_file:
        json.dump(template, data_file, indent=4)
    data_file.close()

    print("\nYour beatmap's root file for \""
          + song_name
          + "\" by "
          + artist_name
          + " has been created in the \"beatmaps/\" directory along with empty files for your "
          + str(len(difficulties))
          + " difficulties.")


def get_beatmap():
    beatmap = (get_stored_difficulties(get_stored_songs()))
    beatmap_file_name = beatmap.split("_")
    beatmap_song_name = beatmap_file_name[0]
    beatmap_song_difficulty = beatmap_file_name[1].split(".json")[0]
    print(border + "\t\t✨ Editing " + beatmap_song_name + " on " + beatmap_song_difficulty + " difficulty ✨" + border)
    return beatmap_song_name, beatmap_song_difficulty


def edit_beatmap(song_name, song_difficulty):
    with open('beatmaps/' + song_name + "/"
              + song_name + "_" + song_difficulty + ".json",
              "r") as beatmap_read:
        jsonData = json.loads(beatmap_read.read())
        notes = jsonData["notes"]
        laneEvents = jsonData["laneEvents"]
    beatmap_read.close()

    notes_filled = edit_beatmap_input(notes)
    sorted_notes_filled = sorted(notes_filled, key=lambda note: (note['startBeat'], note['lane']))

    with open('beatmaps/' + song_name + "/"
              + song_name + "_" + song_difficulty + ".json",
              "w") as beatmap_write:
        json.dump({"notes": sorted_notes_filled, "laneEvents": laneEvents}, beatmap_write, indent=4)
    beatmap_write.close()
    print(border + "\t\t✨ " + song_name + " on " + song_difficulty + " difficulty updated! ✨" + border)


def edit_beatmap_input(notes):
    beat = input("What is the beat for the note you want to add? (type 'exit' to leave editor) ")
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


def set_lane(beat):
    lane = input("What lane is beat " + str(beat) + " on? ")
    try:
        lane = int(lane)
    except ValueError:
        print("Enter a number!")
        set_lane(beat)
    return lane


def set_note_data(beat, lane):
    note_types_list_index = 1

    for note_type in note_types_list:
        print(str(note_types_list_index) + ") " + note_type)
        note_types_list_index += 1

    note_type_input = int(input("\nEnter the number of beat " + str(beat) + " lane " + str(lane) + "'s note type: "))

    if note_type_input < 1 or note_type_input > len(note_types_list) + 1:
        print(note_type_input + " is not included in the above range. Please enter again.")
        set_note_data(beat, lane)

    if note_types_list[note_type_input - 1] == "LaneSwap":
        return {"noteType": "LaneSwap", "laneChanges": set_lane_swap()}

    return {"noteType": note_types_list[note_type_input - 1]}


def set_lane_swap():
    lane_swap_lane_count = input("How many lanes for the new lane configuration? ")
    try:
        lane_swap_lane_count = int(lane_swap_lane_count)
    except ValueError:
        print("Enter a number!")
        set_lane_swap()
    if lane_swap_lane_count not in lane_swap_types_dict.keys():
        print(lane_swap_lane_count + " is not a valid lane size configuration." +
              " Your options are: " + str(lane_swap_types_dict.keys()))
        set_lane_swap()
    set_lane_variation(lane_swap_lane_count)


def set_lane_variation(lane_swap_lane_count):
    lane_type_list = lane_swap_types_dict.get(lane_swap_lane_count)

    lane_type_list_index = 1
    for lane_swap in lane_type_list:
        print(str(lane_type_list_index) + ") " + lane_swap)
        lane_type_list_index += 1

    lane_type_input = int(input("\nEnter the " + str(lane_swap_lane_count) + "-lane variation: "))

    if lane_type_input > len(lane_type_list):
        print(lane_type_input + " is not included in the above range. Please enter again.")
        set_lane_variation(lane_swap_lane_count)

    set_lane_changes(lane_type_list[lane_type_input - 1])


def set_lane_changes(lane_variation):
    print("setting lane changes for", lane_variation)
    # {
    #     "startBeat": 39.5,
    #     "lane": 4,
    #     "noteData": {
    #         "noteType": "LaneSwap",
    #         "laneChanges": [
    #             {
    #                 "lane": 0,
    #                 "newLanePosition": "FourLaneTB_0"
    #             },
    #             {
    #                 "lane": 1,
    #                 "newLanePosition": "FourLaneTB_1"
    #             },
    #             {
    #                 "lane": 2,
    #                 "newLanePosition": "None"
    #             },
    #             {
    #                 "lane": 3,
    #                 "newLanePosition": "FourLaneTB_2"
    #             },
    #             {
    #                 "lane": 4,
    #                 "newLanePosition": "FourLaneTB_3"
    #             }
    #         ]
    #     }
    # },

def get_stored_songs():
    song_directories = os.listdir('beatmaps/')
    song_directories.remove("EMPTY_BEATMAP_DO_NOT_DELETE.json")
    song_directory_index = 1

    for directory in song_directories:
        print(str(song_directory_index) + ") " + directory)
        song_directory_index += 1

    directory_input = int(input("\nEnter the number of the song you would like to beatmap: "))
    song_name = song_directories[directory_input - 1]
    return song_name


def get_stored_difficulties(song_name):
    difficulty_beatmaps = os.listdir('beatmaps/' + song_name + "/")
    difficulty_beatmaps = [element for element in difficulty_beatmaps if "Data.json" not in element]
    difficulty_directory_index = 1

    for directory in difficulty_beatmaps:
        print(str(difficulty_directory_index) + ") " + directory)
        difficulty_directory_index += 1

    directory_input = int(input("\nEnter the number of the difficulty you would like to beatmap: "))
    difficulty_name = difficulty_beatmaps[directory_input - 1]
    return difficulty_name


def string_to_pascal_case(string_to_convert):
    words = string_to_convert.split()
    pascal_case_words = [word.capitalize() for word in words]
    return ''.join(pascal_case_words)


main()
