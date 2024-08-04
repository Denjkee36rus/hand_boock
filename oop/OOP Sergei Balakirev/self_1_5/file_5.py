class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_tiangle(self):
        if not isinstance(self.a, (int, float)) or self.a <= 0:
            return -1
        if not isinstance(self.b, (int, float)) or self.b <= 0:
            return -1
        if not isinstance(self.c, (int, float)) or self.c <= 0:
            return -1

        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 0


        return 1


