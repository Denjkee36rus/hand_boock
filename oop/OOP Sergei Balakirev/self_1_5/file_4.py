import random


class Shape:
    def __init__(self,
                 a: int,
                 b: int,
                 c: int,
                 d: int):
        self.sp: tuple[int, int] = (a, b)
        self.ep: tuple[int, int] = (c, d)

    def __str__(self) -> str:
        return (f'{self.__class__.__name__}'
                f'(sp={self.sp}, ep={self.ep})')


class Line(Shape):
    pass


class Rect(Shape):
    pass


class Ellipse(Shape):
    pass


if __name__ == '__main__':
    # кол-во аргументов конструктора класса
    ARGS_COUNT: int = 4
    elements = []

    for i in range(217):
        model = random.choice([Ellipse, Rect, Line])

        values = random.choices(range(1, 100), k=ARGS_COUNT)
        elements.append(model(*values))
        # elements.append(model(
        #     *random.choices(range(1, 100), k=ARGS_COUNT)
        # ))

    print(*elements)
# s('[data-qa=applicant-card]'
#   ).all('[data-qa=applicant_vacancy]'
#         )[0].element('[data-qa=log_items] [data-qa=attachmentButtons]'
#                      ).element('.vue-icon-survey'): click
