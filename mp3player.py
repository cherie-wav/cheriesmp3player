import time
import pygame
import tkinter as tk
from PIL import Image, ImageTk
pygame.mixer.init()
poop = tk.Tk()
playlist = {"chaos construct": "chaos_construct.mp3",
           "animals": "animals.mp3",
            "kahoot lobby music": "Lobby_Music.mp3",
            "uptown funk": "Uptown_Funk.mp3",
            "seven nation army": "seven nation army.mp3",
            "dance the night": "dance the night.mp3"
}
art_library = {"chaos construct": "chaos_construct.jpg",
               "animals": "animals.jpg",
               "kahoot lobby music": "kahoot.png",
               "uptown funk": "uptown_funk.png",
               "seven nation army": "seven nation army.jpg",
               "dance the night": "dance the night.png"
}
poop.title("cherie's mp3 player")
poop.geometry("1000x800")
poop.configure(bg="#9b2525")
tk.Label(poop, text="what song do you wanna play", bg="#cc6969", font=("Helvetica")).pack(pady=10)
list_frame = tk.Frame(poop)
list_frame.pack(pady=15, padx=20, fill=tk.BOTH, expand=True)
playlist_box = tk.Listbox(
    list_frame,
    bg="#cf6b6b",
    fg="#420303",
    selectbackground="#b83939",
    font=("Helvetica", 12)
)
playlist_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
for title in playlist.keys():
     playlist_box.insert(tk.END, title)
song_search = tk.Entry(poop, font=("Helvetica", 14))
song_search.pack(pady=10)
song = ""
art_label = tk.Label(poop, bg="#9b2525")
art_label.pack(pady=10)
queue = []
def check_songs():
    if pygame.mixer.music.get_busy():
        poop.after(100, check_songs)
    else:
         play_next()
def play_next():
    if not queue:
        return
    current_song = queue.pop(0)
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play()
    image = Image.open(art_library[current_song])
    image = image.resize((300, 300))
    tk_image = ImageTk.PhotoImage(image)
    art_label.config(image=tk_image)
    art_label.image = tk_image
    check_songs()
def start():
    global queue
    song = song_search.get().lower()
    queue = (
    [song] + [s for s in playlist if s != song]
    if song in playlist
    else list(playlist.keys())
    )
    play_next()
tk.Button(poop, text="play", command=start, font=("Helvetica", 14)).pack(pady=10)
def skip_song(event=None):
    pygame.mixer.music.stop()
    play_next()
skip_button = tk.Button(poop, text="skip", command=skip_song, font=("Helvetica", 14))
skip_button.pack(pady=10)
def quit(event=None):
    pygame.mixer.music.stop()
    poop.destroy()
quit_button = tk.Button(poop, text="quit", command=quit, font=("Helvetica", 14))
quit_button.pack(pady=10)
poop.mainloop()
pygame.init()
art_label = tk.Label(poop, "#9b2525")
art_label.pack(pady=10)
pygame.quit()