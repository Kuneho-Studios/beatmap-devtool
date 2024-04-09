###
# Contains the flow for when a user would like to create a new beatmap. This does all that work and creates the root
# ...Data.json file as well as a file for each beatmap difficulty.
###

import json
import os

import Util

BEATMAPS_DIRECTORY = 'beatmaps/'

FILE_LOCATION_ROOT = "/Game/WwiseAudio/Events/Beatmaps/Music/mx_"
FILE_PATH_ROOT = "Content/ProjectRadiance/Data/"


# gather all user data about the basic song info
def get_user_input():
    song_name = input("What's the song name? ").strip()
    album_name = input("What's the album name? ").strip()
    artist_name = input("What's the artist name? ").strip()
    bpm = get_bpm_input()
    length = int(input("How many total beats in the song? "))
    genre = input("What's the song's genre? ").strip()
    difficulty_count = get_difficulty_count_input()
    difficulties = get_difficulties_input(difficulty_count)
    create_root_data_file(song_name, album_name, artist_name, bpm, length, genre, difficulties)


def get_bpm_input():
    bpm = input("What's the song's beats per minute? ")
    try:
        bpm = float(bpm)
    except ValueError:
        print("\"BPM\" must be a number. Please enter a number")
        get_bpm_input()
    return bpm


def get_difficulty_count_input():
    difficulty_count = input("How many difficulties are there? ")
    try:
        difficulty_count = int(difficulty_count)
    except ValueError:
        print("\"Difficulty Count\" must be a number. Please enter a number")
        get_difficulty_count_input()
    return difficulty_count


def get_difficulties_input(difficulty_count):
    difficulties = []
    count = 0
    print("Difficulty is a rating between 1 and 10 (inclusive)")
    # todo add a cli command to explain how the rating system works - help the user accurately set the difficulty rating
    while count < difficulty_count:
        new_difficultly = input(
            "What's difficulty " + str(count + 1) + "? ").strip()

        try:
            new_difficultly = int(new_difficultly)

            if 0 < new_difficultly < 11:
                difficulties.append(new_difficultly)
                count += 1
            else:
                print("\nDifficulty must be a whole number between 1 and 10 (inclusive). Please enter again.\n")
        except ValueError:
            print("\nDifficulty must be a whole number. Please enter a number.\n")

    return difficulties


# creates the ...Data.json file containing all the basic information that is requested for the song
def create_root_data_file(song_name, album_name, artist_name, bpm, length, genre, difficulties):
    song_name_pascal = Util.string_to_pascal_case(song_name)

    create_directories(song_name_pascal)

    data_file = {
        "songName": song_name,
        "album": album_name,
        "artist": artist_name,
        "fileLocation": FILE_LOCATION_ROOT + song_name_pascal,
        "bpm": bpm,
        "length": length,
        "genre": genre,
        "difficulty": create_difficulty_files(difficulties, song_name)
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
            "filePath": FILE_PATH_ROOT + song_name + "_" + str(difficulty) + ".json"
        }
        difficulty_data.append(data)

        with open(BEATMAPS_DIRECTORY + song_name + "/"
                  + song_name + "_" + str(difficulty) + ".json",
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
