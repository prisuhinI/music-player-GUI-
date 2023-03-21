from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")
        self.music_file = None
        self.playing = False
        mixer.init()
        self.create_widgets()

    def create_widgets(self):
        self.music_label = Label(self.root, text="No music loaded")
        self.music_label.pack(pady=10)
        self.load_button = Button(self.root, text="Load Music", command=self.load_music)
        self.load_button.pack(pady=5)
        self.play_button = Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)
        self.pause_button = Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=5)

    def load_music(self):
        self.music_file = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("Music Files", "*.mp3"), ("All Files", "*.*")])
        if self.music_file:
            self.music_label.config(text=f"Loaded: {self.music_file}")
            mixer.music.load(self.music_file)

    def play_music(self):
        if self.music_file:
            mixer.music.play()
            self.playing = True

    def pause_music(self):
        if self.playing:
            mixer.music.pause()
            self.playing = False

root = Tk()
app = MusicPlayer(root)
root.mainloop()

