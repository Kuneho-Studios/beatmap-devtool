import json
import os

import util

file_location_root = "/Game/WwiseAudio/Events/Beatmaps/Music/mx_"
file_path_root = "Content/ProjectRadiance/Data/"


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
  fill_data_template(song_name, album_name, artist_name, bpm, length, genre,
                     difficulties)


def fill_data_template(song_name, album_name, artist_name, bpm, length, genre,
    difficulties):
  with open('template/data_json_template.json', 'r') as template_file:
    template = json.load(template_file)
  template_file.close()

  song_name_pascal = util.string_to_pascal_case(song_name)

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
                  + song_name_pascal + "_" + util.string_to_pascal_case(
          difficulty) + ".json"
    }
    difficulty_data.append(data)

    with open('beatmaps/' + song_name_pascal + "/"
              + song_name_pascal + "_" + util.string_to_pascal_case(
        difficulty) + ".json",
              "x") as difficulty_file:
      json.dump({"notes": [], "laneEvents": []}, difficulty_file, indent=4)
    difficulty_file.close()

  template["difficulty"] = difficulty_data

  with open(
      'beatmaps/' + song_name_pascal + "/" + song_name_pascal + "Data.json",
      "x") as data_file:
    json.dump(template, data_file, indent=4)
  data_file.close()

  print("\nYour beatmap's root file for \""
        + song_name
        + "\" by "
        + artist_name
        + " has been created in the \"beatmaps/\" directory along with empty files for your "
        + str(len(difficulties))
        + " difficulties.")
