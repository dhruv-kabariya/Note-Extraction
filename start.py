from display_note import NoteDisplay
from music_controll import MusicControll

from math import fabs, trunc
import tkinter as tk
from tkinter import Label


from graphFrame import (
    plot
)

from note_show import (
    draw,
    drawLine,
)

from buttons import (
    openButton,
    playButton,
    pauseButton
)


root = tk.Tk()
# root.attributes("-fullscreen", True)

root.title("Note Detector")


# defing frame

# graph frame
graph_frame = tk.Frame(master=root, width=800, height=500)

# pygame frame
note_frame = tk.Frame(master=root, width=800, height=500)

# button frame
button_frame = tk.Frame(
    master=root,
    height=100,  # height=root.winfo_screenheight()*0.10,
    width=800  # width=root.winfo_screenwidth()
)

screen = draw(note_frame)


music_controller = MusicControll()
note_display = NoteDisplay(screen)


# open button
openButton(button_frame, music_controller, note_display)
playButton(button_frame)
pauseButton(button_frame)
button_frame.pack(side=tk.TOP)


graph_label = Label(
    text="Graph of Music", master=graph_frame
)
graph_label.pack()
plot(graph_frame)
# graph_frame.pack()


# button frame buttons

note_frame.pack()


while True:

    screen.fill((255, 255, 255))
    drawLine(screen)
    note_display.displyNote(music_controller)
    root.update()
