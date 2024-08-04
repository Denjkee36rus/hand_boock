class TriangleChecker:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def _is_all_fields_number(self, fields: list) -> bool:
        for field in fields:
            if not isinstance(field, (int, float)):
                return False
        return True
        # return all(
        #     [isinstance(field, (int, float)) for field in fields]
        # )

    def _is_all_fields_natural_number(self, fields: list) -> bool:
        for field in fields:
            if field <= 0:
                return False
        return True

        # return all(
        #     [field <= 0 for field in fields]
        # )

    def _is_valid_triangle(self) -> bool:
        return (self.a + self.b > self.c
                and self.a + self.c > self.b
                and self.b + self.c > self.a)

    def is_triangle(self) -> int:
        fields = [self.a, self.b, self.c]
        if not (self._is_all_fields_number(fields) and
                self._is_all_fields_natural_number(fields)):
            return 1
        elif not self._is_valid_triangle():
            return 2
        return 3


if __name__ == '__main__':
    x, y, z = map(int, input().split())
    triangle = TriangleChecker(x, y, z)
    print(triangle.is_triangle())
