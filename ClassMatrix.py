"""
Creation of the "Matrix" class with dynamic and static properties. The class includes methods:
- setting matrix values by the user
- displaying the resulting matrix on the screen
- checking the matrix for type (identity, zero, diagonal, mixed)
I also added the ability to count the total number of created matrices and calculate the number of matrices of each type
"""


class Matrix:
    matrix_counter_general = 0
    matrix_counter_zero = 0
    matrix_counter_identity = 0
    matrix_counter_diagonal = 0
    matrix_counter_other = 0

    @classmethod
    def matrix_counter(cls):
        cls.matrix_counter_general += 1

    @classmethod
    def matrix_type_counters(cls, a, b):  # 'a' would be list_diagonal, b - list_other
        if b == a == {0}:
            print('Zero matrix')
            cls.matrix_counter_zero += 1
        elif a == {1} and b == {0}:
            print('Identity matrix')
            cls.matrix_counter_identity += 1
        elif b == {0} and a != {0}:
            print('Diagonal matrix')
            cls.matrix_counter_diagonal += 1
        else:
            print('Mixed matrix')
            cls.matrix_counter_other += 1

    @staticmethod
    def output(matrix):
        for i in matrix:
            print(i)

    def new_matrix(self, rows, cols):
        self.rows = rows  # the number of lists inside the main list
        self.cols = cols  # the number of elements inside lists
        self.elems = []
        rows_i = 0
        cols_i = 0
        while rows_i < int(rows):
            self.row_m = []
            while cols_i < int(cols):
                a = int(input('enter a new element for your matrix '))
                self.row_m.append(a)
                cols_i += 1
            self.elems.append(self.row_m)
            rows_i += 1
            cols_i = 0
        Matrix.matrix_counter()
        Matrix.output(self.elems)

    def define_matrix(self):
        list_other = []  # the list for elements off diagonal
        list_diagonal = []  # the list for numbers on the diagonal
        for i in range(0, len(self.elems)):
            for j in range(0, len(self.elems[i])):
                if i != j:
                    list_other.append(self.elems[i][j])
                else:
                    list_diagonal.append(self.elems[i][j])

        list_diagonal, list_other = set(list_diagonal), set(list_other)

        Matrix.matrix_type_counters(list_diagonal, list_other)


# Creating a new object. It can be any number of objects of different sizes.
myMatrix = Matrix()
myMatrix.new_matrix(3, 3)
myMatrix.define_matrix()

myMatrix2 = Matrix()
myMatrix2.new_matrix(2, 2)
myMatrix2.define_matrix()

print(f'The total number of matrices you created: {Matrix.matrix_counter_general}\n'
      f'Zero matrices: {Matrix.matrix_counter_zero}\n'
      f'Identity matrices: {Matrix.matrix_counter_identity}\n'
      f'Diagonal matrices: {Matrix.matrix_counter_diagonal}\n'
      f'Other matrices: {Matrix.matrix_counter_other}')
