'''
Creation of a class "figure" with properties: coordinates of 4 points. The class contains methods
for checking the existence of the created quadrilateral, calculation and output of information
about a figure: lengths of sides, diagonals, perimeter, area of a figure.
The class has a check of the figure for convexity.
Added derived class "parallelogram". The class provides a check whether the figure is a parallelogram.

Below is a commented out program that analyzes quadrilaterals to find the maximum area among objects.
'''
import math


class Figure:
    def __init__(self, num_of_points):
        i = 0
        dots = []
        while i < num_of_points:
            dot = []
            x = int(input(f'enter X value for the {i + 1} point '))
            y = int(input(f'enter Y value for the {i + 1} point '))
            dot.append(x)
            dot.append(y)
            dots.append(dot)
            i += 1
        self.dots = dots

        self.x1 = self.dots[0][0]
        self.y1 = self.dots[0][1]
        self.x2 = self.dots[1][0]
        self.y2 = self.dots[1][1]
        self.x3 = self.dots[2][0]
        self.y3 = self.dots[2][1]
        self.x4 = self.dots[3][0]
        self.y4 = self.dots[3][1]
        print('the new object was created!\n')

    def __del__(self):
        print('the object was deleted')

    def check_figure(self, to_print=True):
        try:
            k0 = (self.y2 - self.y1) / (self.x2 - self.x1)
            k1 = (self.y3 - self.y4) / (self.x3 - self.x4)
            k2 = (self.y3 - self.y2) / (self.x3 - self.x2)
            k3 = (self.y4 - self.y1) / (self.x4 - self.x1)
        except ZeroDivisionError:
            k0, k1, k2, k3 = 0, 0, 0, 0
        if k0 == k1 == k2 == k3 and to_print:
            print('this is not a figure, it is a line')
            return False
        return k0, k1, k2, k3

    def side(self, a1, b1, a2, b2):
        return round(math.sqrt(math.pow((a2 - a1), 2) + math.pow((b2 - b1), 2)))

    def get_sides(self, to_print=True):
        side1 = self.side(self.x1, self.y1, self.x2, self.y2)
        side2 = self.side(self.x2, self.y2, self.x3, self.y3)
        side3 = self.side(self.x3, self.y3, self.x4, self.y4)
        side4 = self.side(self.x4, self.y4, self.x1, self.y1)
        if to_print:
            print(
                f'the sides of this object are: 1st - {side1}, 2nd - {side2}, 3rd - {side3}, 4th - {side4}')
        return side1, side2, side3, side4

    def check_figure_sides(self):
        sides = self.get_sides(to_print=False)
        if (sides[0] < sides[1] + sides[2] + sides[3]) \
                and (sides[1] < sides[0] + sides[2] + sides[3]) \
                and (sides[2] < sides[1] + sides[0] + sides[3]) \
                and (sides[3] < sides[1] + sides[2] + sides[0]):
            print(f'the object with points {self.x1}, {self.y1}, {self.x2}, {self.y2}, '
                  f'{self.x3}, {self.y3}, {self.x4}, {self.y4} exists')
            return True

        print(f'this object does not exist')
        return False

    def calculate_diagonals(self, to_print=True):
        diagonal1 = round(math.sqrt(math.pow((self.x3 - self.x1), 2) + math.pow((self.y3 - self.y1), 2)))
        diagonal2 = round(math.sqrt(math.pow((self.x4 - self.x2), 2) + math.pow((self.y4 - self.y2), 2)))
        if to_print:
            print(
                f'diagonal 1 = {diagonal1}, diagonal 2 = {diagonal2}')
        return diagonal1, diagonal2

    def calculate_perimeter(self, to_print=True):
        sides = self.get_sides(to_print=False)
        perimetr = sides[0] + sides[1] + sides[2] + sides[3]
        if to_print:
            print(f'perimetr is {perimetr}')
        return perimetr

    def calculate_square(self):
        sides = self.get_sides(to_print=False)
        diagonals = self.calculate_diagonals(to_print=False)
        perimetr = self.calculate_perimeter(to_print=False)
        angle1 = math.acos((sides[3] ** 2 + sides[2] ** 2 - diagonals[0] ** 2) / (2 * sides[3] * sides[2]))
        angle2 = math.acos((sides[0] ** 2 + sides[1] ** 2 - diagonals[0] ** 2) / (2 * sides[0] * sides[1]))
        part1 = ((perimetr / 2 - sides[0]) * (perimetr / 2 - sides[1]) * (perimetr / 2 - sides[2]) *
                 (perimetr / 2 - sides[3]))
        part2 = sides[0] * sides[1] * sides[2] * sides[3]
        part3 = ((math.cos((math.degrees(angle1) + math.degrees(angle2)) / 2)) ** 2)
        if part1 - part2 * part3 > 0:
            square = round(math.sqrt(part1 - part2 * part3), 2)
            print(f'the square of the figure is - {square:.2f}')
            return square
        else:
            print('such a quadrilateral is distorted. it is not convex')
            return False


class Parallelogram(Figure):

    def check_parallels(self):
        sides = self.get_sides(to_print=False)
        if sides[0] == sides[2] and sides[1] == sides[3]:
            k0, k1, k2, k3 = self.check_figure(to_print=False)
            if k0 == k1 and k2 == k3:
                print('this is a parallelogram')
        else:
            print('this is not a parallelogram')

    def get_parallels(self):
        return f'has points: {self.x1}, {self.y1}, {self.x2}, {self.y2}, ' \
               f'{self.x3}, {self.y3}, {self.x4}, {self.y4}'


#creating an object to test methods of the "Figure" class
obj = Figure(4)
if (not obj.check_figure()) or (not obj.check_figure_sides) or (not obj.calculate_square()):
    pass
else:
    obj.get_sides()
    obj.calculate_perimeter()
print('-' * 50)

#creating an object to test methods of the "Parallelogram" class
obj2 = Parallelogram(4)
if (not obj2.check_figure()) or (not obj2.check_figure_sides) or (not obj2.calculate_square()):
    pass
else:
    obj2.check_parallels()
    obj2.get_sides()
    obj2.calculate_perimeter()