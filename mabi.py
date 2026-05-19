from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pygame
import os

# ---------------- INIT ---------------- #
pygame.mixer.init()

root = Tk()
root.title("Music Player")
root.geometry("450x850")
root.config(bg="#121212")
root.resizable(False, False)

# ---------------- STYLE ---------------- #
style = ttk.Style()
style.theme_use("clam")

style.configure("TButton",
                font=("Helvetica", 12, "bold"),
                padding=8)

style.configure("TLabel",
                background="#121212",
                foreground="white",
                font=("Helvetica", 12))

# ---------------- VARIABLES ---------------- #
playlist_songs = []

current_song = StringVar(value="No song selected")
song_status = StringVar(value="Stopped")

# ---------------- FUNCTIONS ---------------- #
def load_music():
    folder = filedialog.askdirectory()
    if folder:
        playlist.delete(0, END)
        playlist_songs.clear()

        for file in os.listdir(folder):
            if file.endswith(".mp3"):
                full_path = os.path.join(folder, file)
                playlist_songs.append(full_path)
                playlist.insert(END, file)


def play_music():
    try:
        index = playlist.curselection()[0]
        song = playlist_songs[index]

        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

        current_song.set(playlist.get(index))
        song_status.set("Playing")

    except:
        song_status.set("Select a song first")


def pause_music():
    pygame.mixer.music.pause()
    song_status.set("Paused")


def resume_music():
    pygame.mixer.music.unpause()
    song_status.set("Playing")


def stop_music():
    pygame.mixer.music.stop()
    song_status.set("Stopped")

# ---------------- HEADER ---------------- #
header = Frame(root, bg="#121212")
header.pack(pady=20)

Label(header,
      text="🎵 Music Player",
      bg="#121212",
      fg="white",
      font=("Helvetica", 22, "bold")).pack()

# ---------------- SONG DISPLAY ---------------- #
display = Frame(root, bg="#121212")
display.pack(pady=15)

Label(display,
      textvariable=current_song,
      wraplength=380,
      justify="center",
      font=("Helvetica", 14, "bold")).pack()

Label(display,
      textvariable=song_status,
      fg="#bbbbbb",
      font=("Helvetica", 11)).pack(pady=5)

# ---------------- ALBUM ART (MODERN CARD) ---------------- #
album = Frame(root, bg="#1e1e1e", width=280, height=280)
album.pack(pady=20)
album.pack_propagate(False)

Label(album,
      text="ALBUM ART",
      bg="#1e1e1e",
      fg="#888",
      font=("Helvetica", 16, "bold")).pack(expand=True)

# ---------------- CONTROLS ---------------- #
controls = Frame(root, bg="#121212")
controls.pack(pady=20)

def make_btn(text, cmd):
    return ttk.Button(controls, text=text, command=cmd, width=6)

make_btn("📂", load_music).grid(row=0, column=0, padx=6)
make_btn("▶", play_music).grid(row=0, column=1, padx=6)
make_btn("⏸", pause_music).grid(row=0, column=2, padx=6)
make_btn("⏵", resume_music).grid(row=0, column=3, padx=6)
make_btn("⏹", stop_music).grid(row=0, column=4, padx=6)

# ---------------- PLAYLIST ---------------- #
playlist_frame = Frame(root, bg="#121212")
playlist_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

Label(playlist_frame,
      text="QUEUE",
      fg="#bbbbbb",
      bg="#121212",
      font=("Helvetica", 11, "bold")).pack(anchor="w")

playlist = Listbox(
    playlist_frame,
    bg="#1e1e1e",
    fg="white",
    selectbackground="#333333",
    selectforeground="white",
    font=("Helvetica", 11),
    bd=0,
    highlightthickness=0
)

playlist.pack(fill=BOTH, expand=True, pady=10)

# ---------------- STATUS ---------------- #
status_bar = Frame(root, bg="#1e1e1e")
status_bar.pack(fill=X)

Label(status_bar,
      textvariable=song_status,
      bg="#1e1e1e",
      fg="#bbbbbb",
      font=("Helvetica", 10)).pack(pady=5)

# ---------------- RUN ---------------- #
root.mainloop()