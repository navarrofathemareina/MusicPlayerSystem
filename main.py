from tkinter import *
from tkinter import filedialog
import pygame
import os

# ---------------- INIT ---------------- #
pygame.mixer.init()

root = Tk()
root.title("Minimal Music Player")
root.geometry("430x820")
root.config(bg="#f5f5f5")
root.resizable(False, False)

# ---------------- VARIABLES ---------------- #
playlist_songs = []

current_song = StringVar()
current_song.set("No song selected")

song_status = StringVar()
song_status.set("Stopped")

# ---------------- FUNCTIONS ---------------- #
def load_music():
    folder = filedialog.askdirectory()

    if folder:
        playlist.delete(0, END)
        playlist_songs.clear()

        for file in os.listdir(folder):
            if file.endswith(".mp3"):
                playlist.insert(END, file)
                playlist_songs.append(folder + "/" + file)


def play_music():
    try:
        selected_song = playlist.curselection()[0]
        song = playlist_songs[selected_song]

        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

        current_song.set(playlist.get(selected_song))
        song_status.set("Playing")

    except:
        song_status.set("Select a song")


def pause_music():
    pygame.mixer.music.pause()
    song_status.set("Paused")


def resume_music():
    pygame.mixer.music.unpause()
    song_status.set("Playing")


def stop_music():
    pygame.mixer.music.stop()
    song_status.set("Stopped")
