import os
import pygame
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3

# the base folder of the music
base_folder = "I:/Music"

# ask the user what song they want
song_name = input("Enter a song name: ").lower()
artist_name = input("Enter the artist's name: ").lower()

# search the folders for the requested song and artist
matching_files = []
for dirpath, dirnames, filenames in os.walk(base_folder):
    for filename in filenames:
        if song_name in filename.lower() and artist_name in filename.lower():
            matching_files.append(os.path.join(dirpath, filename))

if matching_files:
    # remove pycharm's errors about undefined variables
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
