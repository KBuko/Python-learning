# A function that takes a string and counts the number of upper and lower case characters in it

def up_n_low(your_string):
    up = 0
    low = 0
    for i in your_string:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
    return f'The number of uppercase letters: {up}\nThe number of lowercase letters: {low}'


your_string = input('Enter your text here. ')
print(up_n_low(your_string))
