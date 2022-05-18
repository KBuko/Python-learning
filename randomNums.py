'''
Using the random module, generate a random matrix. Find the maximum element of the matrix located
on the perimeter of the matrix, as well as the minimum element inside the perimeter
'''
import random


def fill_matrix(cols, rows):
    my_matrix = []
    for m in range(int(rows)):
        myRows = []
        for c in range(int(cols)):
            myRows.append(random.randrange(100))
        my_matrix.append(myRows)
    return NewMatrix(my_matrix)


class NewMatrix:

    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def data_output(self):
        for line in self.my_matrix:
            print(line)

    def find_perimetr(self, calculate_min_elem=False):
        nums_in_perimetr = []
        for num in self.my_matrix[0] + self.my_matrix[-1]:
            nums_in_perimetr.append(num)

        for num in range(1, len(self.my_matrix) - 1):
            nums_in_perimetr.append(self.my_matrix[num][0])
            nums_in_perimetr.append(self.my_matrix[num][-1])
        if calculate_min_elem:
            return max(nums_in_perimetr)
        return nums_in_perimetr

    def nums_inside_perimetr(self, calculate_min_elem=False):
        nums_inside_perimetr = []
        if len(self.my_matrix) <= 2 or len(self.my_matrix[0]) <= 2:
            return 'not defined. This matrix is too small'
        else:
            for num in self.my_matrix[1:-1]:
                for m in num:
                    if m is not num[0] and m is not num[-1]:
                        nums_inside_perimetr.append(m)
            if calculate_min_elem:
                return min(nums_inside_perimetr)
            return nums_inside_perimetr


matrix = fill_matrix(4, 4)
matrix.data_output()
print(f'The maximum element of the matrix located on the perimeter is '
      f'{matrix.find_perimetr(calculate_min_elem=True)}')
print(f'The minimum element inside the perimeter of this matrix is '
      f'{matrix.nums_inside_perimetr(calculate_min_elem=True)}')

