text = input().split()
text_2 = input().split(' ')

print(text)  # ['Python', 'is', 'fun']
print(text_2)  # ['Python', '', '', '', 'is', 'fun']
s = 'PYTHON'

print(' '.join([char * 2 for char in s]))
# Python    is fun
