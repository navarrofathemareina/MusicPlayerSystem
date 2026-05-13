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

# ---------------- HEADER ---------------- #
header = Frame(root, bg="#f5f5f5")
header.pack(fill=X, pady=20)

Label(
    header,
    text="Music Player",
    bg="#f5f5f5",
    fg="#111",
    font=("Helvetica", 24, "bold")
).pack()

# ---------------- ALBUM ART ---------------- #
album_frame = Frame(root, bg="#f5f5f5")
album_frame.pack(pady=20)

album_art = Canvas(
    album_frame,
    width=260,
    height=260,
    bg="#d9d9d9",
    bd=0,
    highlightthickness=0
)

album_art.create_text(
    130,
    130,
    text="ALBUM ART",
    fill="#666",
    font=("Helvetica", 18)
)

album_art.pack()

# ---------------- SONG INFO ---------------- #
info_frame = Frame(root, bg="#f5f5f5")
info_frame.pack(pady=20)

Label(
    info_frame,
    textvariable=current_song,
    bg="#f5f5f5",
    fg="#111",
    font=("Helvetica", 20, "bold"),
    wraplength=340
).pack()

Label(
    info_frame,
    text="Artist Name",
    bg="#f5f5f5",
    fg="#777",
    font=("Helvetica", 14)
).pack(pady=5)

# ---------------- PROGRESS BAR ---------------- #
progress = Scale(
    root,
    from_=0,
    to=100,
    orient=HORIZONTAL,
    length=320,
    bg="#f5f5f5",
    fg="#111",
    troughcolor="#d9d9d9",
    highlightthickness=0,
    bd=0
)
progress.pack()

# ---------------- CONTROLS ---------------- #
controls = Frame(root, bg="#f5f5f5")
controls.pack(pady=30)

btn_style = {
    "bg": "#ffffff",
    "fg": "#111",
    "font": ("Helvetica", 18),
    "bd": 0,
    "activebackground": "#e5e5e5",
    "cursor": "hand2",
    "width": 3,
    "height": 1
}

# LOAD
Button(
    controls,
    text="📁",
    command=load_music,
    **btn_style
).grid(row=0, column=0, padx=10)

# PLAY
Button(
    controls,
    text="▶",
    command=play_music,
    **btn_style
).grid(row=0, column=1, padx=10)

# PAUSE
Button(
    controls,
    text="⏸",
    command=pause_music,
    **btn_style
).grid(row=0, column=2, padx=10)

# RESUME
Button(
    controls,
    text="⏵",
    command=resume_music,
    **btn_style
).grid(row=0, column=3, padx=10)

# STOP
Button(
    controls,
    text="■",
    command=stop_music,
    **btn_style
).grid(row=0, column=4, padx=10)

# ---------------- PLAYLIST ---------------- #
playlist_container = Frame(root, bg="#ffffff")
playlist_container.pack(
    fill=BOTH,
    expand=True,
    padx=20,
    pady=25
)

Label(
    playlist_container,
    text="QUEUE",
    bg="#ffffff",
    fg="#777",
    font=("Helvetica", 12, "bold")
).pack(anchor="w", padx=10, pady=10)

playlist = Listbox(
    playlist_container,
    bg="#ffffff",
    fg="#111",
    selectbackground="#111",
    selectforeground="white",
    font=("Helvetica", 12),
    bd=0,
    highlightthickness=0,
    activestyle="none"
)

playlist.pack(fill=BOTH, expand=True, padx=10, pady=10)

# ---------------- STATUS BAR ---------------- #
status = Label(
    root,
    textvariable=song_status,
    bg="#ffffff",
    fg="#555",
    font=("Helvetica", 11)
)
status.pack(fill=X)

# ---------------- RUN ---------------- #
root.mainloop()