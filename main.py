import os
import tkinter as tk
from tkinter import filedialog, ttk
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("400x300")

        self.playlist = []
        self.current_song = None

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Create buttons
        self.btn_add = tk.Button(self.master, text="Add Songs", command=self.add_songs)
        self.btn_play = tk.Button(self.master, text="Play", command=self.play)
        self.btn_stop = tk.Button(self.master, text="Stop", command=self.stop)
        self.btn_next = tk.Button(self.master, text="Next", command=self.next_song)
        self.btn_pause = tk.Button(self.master, text="Pause", command=self.pause_resume)

        # Create a volume slider
        self.volume_slider = ttk.Scale(self.master, from_=0, to=1, orient="horizontal", command=self.set_volume)
        self.volume_slider.set(0.5)  # Set default volume to 50%

        # Create a label to display the currently playing song
        self.current_song_label = tk.Label(self.master, text="")

        # Add widgets to the window
        self.btn_add.pack(pady=10)
        self.btn_play.pack(pady=10)
        self.btn_stop.pack(pady=10)
        self.btn_next.pack(pady=10)
        self.btn_pause.pack(pady=10)
        self.volume_slider.pack(pady=10)
        self.current_song_label.pack(pady=10)

    def add_songs(self):
        files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
        self.playlist.extend(files)

    def play(self):
        if self.playlist:
            if self.current_song is None:
                self.current_song = 0
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()
            self.update_current_song_label()

    def stop(self):
        pygame.mixer.music.stop()

    def next_song(self):
        if self.playlist:
            pygame.mixer.music.stop()
            self.current_song = (self.current_song + 1) % len(self.playlist)
            self.play()

    def pause_resume(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def set_volume(self, value):
        pygame.mixer.music.set_volume(float(value))

    def update_current_song_label(self):
        if self.playlist:
            self.current_song_label.config(text=f"Now Playing: {os.path.basename(self.playlist[self.current_song])}")
        else:
            self.current_song_label.config(text="")

def main():
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
