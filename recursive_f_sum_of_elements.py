'''
A recursive function that calculates the sum of the elements of a list
whose elements can also be a list
'''

my_list = [1, 2, [3, 4], [5, 6]]


def summa(a):
    s = 0
    for x in a:
        if type(x) is list:
            s += summa(x)
        else:
            s += int(x)
    return s


print(summa(my_list))
