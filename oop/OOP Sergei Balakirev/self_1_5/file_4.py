import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

elements = []

for i in range(218):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 100)
    d = random.randint(1, 100)

    random_class = random.choices([Ellipse, Rect, Line])[0]
    elements.append(random_class(a, b, c, d))
print(elements)

# s('[data-qa=applicant-card]').all('[data-qa=applicant_vacancy]')[0].element('[data-qa=log_items] [data-qa=attachmentButtons]').element('.vue-icon-survey'): click

