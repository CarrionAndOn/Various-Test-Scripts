import os
import pygame
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3

# the base folder of the music
base_folder = "I:/Music"

# ask the user what song they want
song_name = input("Enter a song name: ").lower()
# ask what artist in case of songs that have the same name as eachother
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
    year = None

    # check if the file is a FLAC or MP3 and use the appropriate method to get the metadata
    if matching_files[0].endswith('.flac'):
        audio = FLAC(matching_files[0])
        track_name = audio['title'][0]
        artist_name = audio['artist'][0]
        album_name = audio['album'][0]
        year = audio['date'][0]
    elif matching_files[0].endswith('.mp3'):
        audio = EasyID3(matching_files[0])
        track_name = audio['title'][0]
        artist_name = audio['artist'][0]
        album_name = audio['album'][0]
        year = audio['date'][0]
    # WAV file metadata is far too inconsistent to be able to check it, so skip metadata if it's a wav
    elif matching_files[0].endswith('.wav'):
        print("WAV file, method to get metadata is too inconsistent, skipping metadata check!")

    # print the track information
    if matching_files[0].endswith('.flac'):
        print(f"Playing {track_name} by {artist_name} from {album_name} ({year})")
    elif matching_files[0].endswith('.mp3'):
        print(f"Playing {track_name} by {artist_name} from {album_name} ({year})")
    # if it is a wav, just show the full filename as a compromise since the metadata is too inconsistent to grab
    elif matching_files[0].endswith('.wav'):
        print(f"Playing {matching_files}")

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
