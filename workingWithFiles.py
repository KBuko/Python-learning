#a program that creates alphabetical text files (A.txt, B.txt, etc.) in a given directory.
# Each file contains a corresponding letter of the alphabet

from string import ascii_uppercase

dir = './new_folder'

for let in ascii_uppercase:
    with open(f'{dir}/{let}.txt', 'w') as f:
        f.write(f'{let}')
        f.close()

print('Done!')

