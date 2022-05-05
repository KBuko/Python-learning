"""
Creation of an abstract class "Progression" with methods for calculating the i-th element and the sum of the
progression. Implementation of the derived classes "Arithmetic progression" and "Geometric progression" with their
own methods for calculating the i-th element and the sum
"""
from abc import ABC, abstractmethod


class Progression(ABC):
    def __init__(self, start_num, step):
        self.start_num = start_num
        self.step = step

    @abstractmethod
    def find_number(self, i_num):
        pass

    @abstractmethod
    def sum_progression(self, i_num):
        pass


class Arithmetic_progression(Progression):

    def find_number(self, i_num):
        return self.start_num + self.step * (i_num - 1)

    def sum_progression(self, i_num):
        final_num = self.find_number(i_num)
        return int(((self.start_num + final_num) / 2) * i_num)


class Geometric_progression(Progression):

    def find_number(self, i_num):
        return self.start_num * self.step ** (i_num - 1)

    def sum_progression(self, i_num):
        return int((self.start_num * (1 - self.step ** i_num)) / (1 - self.step))


new_arithmetic = Arithmetic_progression(1, 3)
print(f'The latest number of arithmetic progression is {new_arithmetic.find_number(5)}.')
print(f'The sum of all elements of the sequence is {new_arithmetic.sum_progression(5)}.')

print('-' * 50)

new_geometric = Geometric_progression(2, 2)
print(f'The latest number of arithmetic progression is {new_geometric.find_number(3)}.')
print(f'The sum of all elements of the sequence is {new_geometric.sum_progression(3)}.')

