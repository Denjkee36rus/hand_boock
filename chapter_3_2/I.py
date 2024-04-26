string = input()
location = {}

while string:
    words = string.split()

    for word in words:
        # if word not in location:
        #     location[word] = 1
        # else:
        #     location[word] += 1

        location[word] = location.get(word, 0) + 1

    string = input()

for key, value in location.items():
    print(key, value)
