


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print(f"Area = {area}")

    def __str__(self):
        pass



triangle_one = Triangle(25, 36)
triangle_one.calculate_area()