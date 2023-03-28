import os
import pygame
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3

# the base folder of the music
base_folder = "I:/Music"

# ask the user what song they want
input_text = input("Enter a song name: ")

# search the folders for the requested song
matching_files = []
for dirpath, dirnames, filenames in os.walk(base_folder):
    for filename in filenames:
        if input_text in filename:
            matching_files.append(os.path.join(dirpath, filename))

if matching_files:
    # get the song's name, artist, and album
    audio = None
    track_name = None
    artist_name = None
    album_name = None

    # check if the file is a FLAC or MP3 and use the appropriate method to get the metadata
    if matching_files[0].endswith('.flac'):
        audio = FLAC(matching_files[0])
        track_name = audio['title'][0]
        artist_name = audio['artist'][0]
        album_name = audio['album'][0]
    elif matching_files[0].endswith('.mp3'):
        audio = EasyID3(matching_files[0])
        track_name = audio['title'][0]
        artist_name = audio['artist'][0]
        album_name = audio['album'][0]

    # print the track information
    print(f"Playing {track_name} by {artist_name} from {album_name}")

    # play the song
    pygame.init()
    pygame.mixer.music.load(matching_files[0])
    pygame.mixer.music.play()

    # wait for the song to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.quit()

else:
    print("No matching music file found.")
