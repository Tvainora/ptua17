from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    def __init__(self, file_name):
        self.file_name = file_name

    @abstractmethod
    def play(self):
        pass


class AudioPlayer(MediaPlayer):
    def play(self):
        print(f"Playing audio file: {self.file_name}")


class VideoPlayer(MediaPlayer):
    def play(self):
        print(f"Playing video file: {self.file_name}")