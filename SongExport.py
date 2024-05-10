###
# Contains the work to export a song onto the user's machine in a destination of their choosing
###


import os
import tkinter
import zipfile
from tkinter import filedialog
import Util


# export a zip of the song containing the beatmaps for it
def export_song():
    print("\nSelect the song to export")
    song_list = Util.get_stored_songs()

    if len(song_list) == 0:
        Util.fancy_print_box(
            "⚠ There are no songs present to export ⚠")
    else:
        selected_song = Util.input_stored_songs(song_list)
        directory_to_zip = "beatmaps/" + selected_song
        with zipfile.ZipFile(os.path.join(choose_directory(), selected_song + ".zip"), 'w',
                             zipfile.ZIP_DEFLATED) as zip_file:
            # Iterate over all the files in the directory
            for root, dirs, files in os.walk(directory_to_zip):
                for file in files:
                    # Construct the full file path
                    file_path = os.path.join(root, file)
                    # Add the file to the zip
                    zip_file.write(file_path, os.path.relpath(file_path, directory_to_zip))

        print(selected_song + " has been exported")


# gives the pop-up save dialogue to allow the user to choose save location
def choose_directory():
    root = tkinter.Tk()
    root.withdraw()
    return filedialog.askdirectory()
