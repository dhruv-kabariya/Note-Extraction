from note_class import Note

import pygame
from pygame.font import SysFont

pygame.font.init()
image = pygame.image.load('images\\whole_note.png')
image = pygame.transform.scale(image, (40, 40))
text = SysFont(None, 32)

dimentions = {
    "A": [790, 205],
    "A#": [790, 205],
    "B": [790, 200],
    "C": [790, 155],
    "C#": [790, 155],
    "D": [790, 150],
    "D#": [790, 150],
    "E": [790, 105],
    "F": [790, 75],
    "F#": [790, 75],
    "G": [790, 250],
    "G#": [790, 250]
}


class NoteDisplay:

    def __init__(self, screen):

        self.notes = []
        self.screen = screen

    def setNotes(self, predicted_notes, starts):

        for i in range(len(predicted_notes)):
            self.notes.append(
                Note(
                    predicted_notes[i],
                    starts[i],
                    dimentions[predicted_notes[i]][0],
                    dimentions[predicted_notes[i]][1]
                )
            )

    def displyNote(self, music):

        for note in self.notes:

            if(note.time < music.currentTime()):
                if(note.display):
                    self.screen.blit(image, (note.x, note.y))
                    letter = text.render(note.note, True, (25, 25, 112))
                    self.screen.blit(letter, (note.x, 350))
                    note.updateX()
        pygame.display.update()
