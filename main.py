import json

fileLocationRoot = "/Game/WwiseAudio/Events/Beatmaps/Music/mx_"
filePathRoot = "Content/ProjectRadiance/Data/"


def main():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" +
          "   Welcome To Project Radiance's Beatmap Dev Tool <3" +
          "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    get_user_purpose()


def get_user_purpose():
    create_or_edit = input("Would you like to create a new beatmap or edit an existing one? (create/edit) ")
    if create_or_edit.lower() == "create" or create_or_edit.lower() == "c":
        get_user_input()
    elif create_or_edit.lower() == "edit" or create_or_edit.lower() == "e":
        print("Editing an existing beatmap is not yet a feature. Please restart and select 'create' or come back later")
    else:
        print("Please only enter 'create' or 'edit'")
        get_user_purpose()


def get_user_input():
    song_name = input("What's the song name? ")
    album_name = input("What's the album name? ")
    artist_name = input("What's the artist name? ")
    bpm = int(input("What's the song's beats per minute? "))
    length = int(input("How many total beats in the song? "))
    genre = input("What's the song's genre? ")
    difficulty_count = int(input("How many difficulties are there? "))
    difficulties = []
    count = 0
    while count < difficulty_count:
        new_difficultly = input("What's difficulty " + str(count + 1) + "? ")
        difficulties.append(new_difficultly)
        count += 1
    fill_data_template(song_name, album_name, artist_name, bpm, length, genre, difficulties)


def fill_data_template(song_name, album_name, artist_name, bpm, length, genre, difficulties):
    with open('template/data_json_template.json', 'r') as template_file:
        template = json.load(template_file)
    template_file.close()

    template["songName"] = song_name
    template["album"] = album_name
    template["artist"] = artist_name
    template["fileLocation"] = fileLocationRoot + string_to_pascal_case(song_name)
    template["bpm"] = bpm
    template["length"] = length
    template["genre"] = genre

    difficulty_data = []
    for difficulty in difficulties:
        data = {
            "tier": difficulty,
            "filePath": filePathRoot
            + string_to_pascal_case(song_name) + "_" + string_to_pascal_case(difficulty) + ".json"
        }
        difficulty_data.append(data)

    template["difficulty"] = difficulty_data

    with open('beatmaps/' + string_to_pascal_case(song_name) + "Data.json", "w") as data_file:
        json.dump(template, data_file, indent=4)
    data_file.close()

    print("\nYour beatmap's root file for \""
          + song_name
          + "\" by "
          + artist_name
          + " has been created in the \"beatmaps/\" directory")


def string_to_pascal_case(string_to_convert):
    words = string_to_convert.split()
    pascal_case_words = [word.capitalize() for word in words]
    return ''.join(pascal_case_words)


main()
