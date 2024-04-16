line: str = input()

chars: set = set(line)
print(*chars, sep='')

# Option №2
print(''.join(set(line)))
