example = input()
temp_count = 1
for i in range(len(example) - 1):
    if example[i] == example[i + 1]:
        temp_count += 1
    else:
        print(example[i], temp_count)
        temp_count = 1
print(example[-1], temp_count)

# Option 2
line = input()

length: int = len(line)
count: int = 1

for i in range(length):
    if i == length - 1:
        print(line[i], count)
        break
    if line[i] == line[i + 1]:
        count += 1
    else:
        print(line[i], count)
        count = 1
