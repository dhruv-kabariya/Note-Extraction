from pygame import mixer


class MusicControll:

    def __init__(self):
        mixer.init()
        self.play = False
        self.music = None

    def playMusic(self, file):
        self.music = mixer.music.load(file[0:-4] + ".mp3")
        self.play = True
        mixer.music.play()

    def paushMusic(self):

        self.play = False
        mixer.music.pause()

    def resumeMusic(self):

        self.play = True
        mixer.music.unpause()

    def currentTime(self):
        # print(mixer.music.get_pos())
        return mixer.music.get_pos()
