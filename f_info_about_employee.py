# A function that accepts info about an employee and outputs this information according to a template

def info(name, last_name, **kwargs):
    print('Name:', name)
    print('Last name:', last_name)
    if kwargs != 0:
        print()
    for i in kwargs:
        print(i+':', kwargs[i])
    print('-' * 30)

info('Kate', 'Smith', Age=22, locality='USA', Email='ggg@ttt.com')