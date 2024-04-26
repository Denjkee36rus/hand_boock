
string = input()
location = {}
while string !='':
    words = string.split()
    for i in words:
        if i not in location:
            location[i] = 1
        else:
            location[i] += 1
    string = input()
for result in location.items(): # вот эту строчку не понимаю !!!!
    print(result[0], result[1]) # вот эту строчку не понимаю !!!!
# print(*location.items(), sep='\n')





