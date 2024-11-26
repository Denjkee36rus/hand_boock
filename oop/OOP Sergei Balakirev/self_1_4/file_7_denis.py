class StreamData:
    def create(self, fields, lst_values):


class StreamReader:

    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData
        res = sd.create(self.FIELDS, lst_in)
        return sd, res





se = StreamReaderO
data, result = sr.readlines





