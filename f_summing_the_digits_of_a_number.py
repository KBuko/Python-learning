'''
the function forms a sequence, each element of which is equal to the sum of the digits
of the corresponding element of the original number.
The function also finds the sum of the digits of the new sequence
'''

def count_nums(l):
    """
    adds up the digits of the number

    :param l: number or sequence element
    :return:  the stacked digits of the element
    """
    summa = 0
    while l > 0:
        summa += l % 10
        l //= 10
    return summa

n = map(int, input('Enter a few numbers separated by a space ').split())
new_nums = []
for i in n:
    new_nums.append(count_nums(i))
    
nums_correct = ', '.join(map(str, new_nums))
print(new_nums, sum(new_nums))
