###
# Contains the flow for when a user would like to create a new beatmap. This does all that work and creates the root
# ...Data.json file as well as a file for each beatmap difficulty.
###

import json
import os

import util

BEATMAPS_DIRECTORY = 'beatmaps/'

FILE_LOCATION_ROOT = "/Game/WwiseAudio/Events/Beatmaps/Music/mx_"
FILE_PATH_ROOT = "Content/ProjectRadiance/Data/"


# gather all user data about the basic song info
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
        new_difficultly = input(
            "What's difficulty " + str(count + 1) + "? ").strip()
        difficulties.append(new_difficultly)
        count += 1
    create_root_data_file(song_name, album_name, artist_name, bpm, length, genre, difficulties)


# creates the ...Data.json file containing all the basic information that is requested for the song
def create_root_data_file(song_name, album_name, artist_name, bpm, length, genre, difficulties):
    song_name_pascal = util.string_to_pascal_case(song_name)

    create_directories(song_name_pascal)

    data_file = {
        "songName": song_name,
        "album": album_name,
        "artist": artist_name,
        "fileLocation": FILE_LOCATION_ROOT + song_name_pascal,
        "bpm": bpm,
        "length": length,
        "genre": genre,
        "difficulty": create_difficulty_files()
    }

    with open(
            BEATMAPS_DIRECTORY + song_name_pascal + "/" + song_name_pascal + "Data.json",
            "x") as root_data_file:
        json.dump(data_file, root_data_file, indent=4)
    root_data_file.close()

    print("\nYour beatmap's root file for \""
          + song_name
          + "\" by "
          + artist_name
          + " has been created with "
          + str(len(difficulties))
          + " difficulties.")


# creates the empty beatmap files for each of the difficulties the user plans on having for the given song
def create_difficulty_files(input_difficulties, song_name):
    difficulty_data = []
    for difficulty in input_difficulties:
        data = {
            "tier": difficulty,
            "filePath": FILE_PATH_ROOT + song_name + "_" + util.string_to_pascal_case(difficulty) + ".json"
        }
        difficulty_data.append(data)

        with open(BEATMAPS_DIRECTORY + song_name + "/"
                  + song_name + "_" + util.string_to_pascal_case(difficulty) + ".json",
                  "x") as difficulty_file:
            json.dump({"notes": [], "laneEvents": []}, difficulty_file, indent=4)
        difficulty_file.close()
    return difficulty_data


# creates 'beatmaps/` directory if not already existing.
# then creates the directory named after the song to hold all the beatmap files
def create_directories(song_name_pascal):
    if not os.path.exists(BEATMAPS_DIRECTORY):
        os.makedirs(BEATMAPS_DIRECTORY)

    os.makedirs(BEATMAPS_DIRECTORY + song_name_pascal)
