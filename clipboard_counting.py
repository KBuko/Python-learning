import pyperclip

s = pyperclip.paste()
print('here\'s what you copied:\n' + s)
s = s.replace('/n', '').replace('/r', '')
n1 = len(s)
s = s.replace(' ', '')
n2 = len(s)

print('-'*40)
print('with spaces there are ' + str(n1) + ' characters.')
print('without spaces there are ' + str(n2) + ' characters.')
print('-'*40)
