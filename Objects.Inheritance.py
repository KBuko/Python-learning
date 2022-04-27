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
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        if x1 == x2 == x3 == x4 or y1 == y2 == y3 == y4:
            print('this object does not exist')
            self.__del__()

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

        print('!the new object was created\n')

    def __del__(self):
        print('the object was deleted')
        print('-' * 50)

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

    def check_figure(self):
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
        square = round(math.sqrt(part1 - part2 * part3), 2)
        if square > 0:
            print(f'the square of the figure is - {square:.2f}')
            return square
        else:
            print('such a quadrilateral is distorted. it is not convex')


class parallelogram(Figure):

    def check_parallels(self):
        if self.x1 == self.x2 and self.x3 == self.x4:
            print('this is parallelogram')
        else:
            print('this is not a parallelogram')
            self.__del__()

    def get_parallels(self):
        return f'has points: {self.x1}, {self.y1}, {self.x2}, {self.y2}, ' \
               f'{self.x3}, {self.y3}, {self.x4}, {self.y4}'


newObject = [Figure(0, 20, 4, 18, 0, 20, 0, 4), Figure(12, 0, 4, 18, 2, 20, 0, 4)]

newObject2 = [parallelogram(12, 3, 12, 18, 2, 20, 2, 4), parallelogram(5, 8, 12, 0, 3, 5, 3, 9),
              parallelogram(0, 0, 12, 3, 9, 30, 100, 53)]

if newObject[0].check_figure() and (not newObject[0].calculate_square()):
    newObject[0].__del__()
else:
    newObject[0].get_sides()
    newObject[0].calculate_perimeter()
    print('-' * 50)

if newObject[1].check_figure() and (not newObject[1].calculate_square()):
    newObject[1].__del__()
else:
    newObject[1].get_sides()
    newObject[1].calculate_perimeter()
    print('-' * 50)

if newObject2[0].check_figure() and (not newObject2[0].calculate_square()):
    newObject2[0].__del__()
else:
    newObject2[0].check_parallels()
    newObject2[0].calculate_perimeter()
    print('-' * 50)

# max_square = max(newObject2, key=lambda sq: sq.calculate_square())

# print('*'*50)
# print(f'The parallelogram with max square {max_square.get_parallels()}.')
