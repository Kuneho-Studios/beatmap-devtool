import json
import os

file_location_root = "/Game/WwiseAudio/Events/Beatmaps/Music/mx_"
file_path_root = "Content/ProjectRadiance/Data/"
border = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"


def main():
    print(border + "   ✨ Welcome To Project Radiance's Beatmap Dev Tool ✨" + border)
    get_user_purpose()


def get_user_purpose():
    create_or_edit = input("Would you like to create a new beatmap or edit an existing one? (create/edit) ")
    if create_or_edit.lower() == "create" or create_or_edit.lower() == "c":
        get_user_input()
    elif create_or_edit.lower() == "edit" or create_or_edit.lower() == "e":
        get_beatmap()
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
            json.dump({}, difficulty_file, indent=4)
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
