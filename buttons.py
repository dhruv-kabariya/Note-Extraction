
from logging import root
import tkinter as tk
from tkinter import Button
from tkinter.filedialog import askopenfilename


from note.note_recognition import (
    main
)

from graphFrame import (
    plot
)


def open_file(frame, note, music):
    open_file_button = askopenfilename(
        #     filetypes=(
        #     ("audio files", "*.mp3", "*.wav", "*.m4a"), ("All files", "*.*")
        # )
    )
    print(open_file_button)
    predicted_notes, starts, volumn, segment_ms = main(open_file_button)
    note.setNotes(predicted_notes, starts)
    music.playMusic(open_file_button)

    plot(frame, volumn, segment_ms, starts)


def openButton(frame, music, note):
    """
    This button for choose audio file fro directory and process the operation
    """

    button = tk.Button(
        master=frame,
        text="Open",
        command=lambda: open_file(frame, note, music)
    )
    button.grid(row=0, column=0)


def playButton(frame):
    """
    This is for music play 
    """

    button = Button(master=frame, text="Play")
    button.grid(row=0, column=1)


def pauseButton(frame):
    """
    This button for stop music and graph and all activity
    """

    button = tk.Button(master=frame, text="Pause")
    button.grid(row=0, column=2)
