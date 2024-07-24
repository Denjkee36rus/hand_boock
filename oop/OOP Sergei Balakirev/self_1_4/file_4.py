class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f'Воспроизведение {self.filename}')


if __name__ == '__main__':
    media1 = MediaPlayer()
    media2 = MediaPlayer()

    media1.open('filemedia1')
    media2.open('filemedia2')

    # print(media1.__dict__)
    # print(media2.__dict__)

    media1.play()
    media2.play()
