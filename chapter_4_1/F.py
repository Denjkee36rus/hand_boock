my_list = []


def modern_print(string):
    global my_list
    if string not in my_list:
        print(string)
        my_list.append(string)


modern_print("Hello!")
modern_print("Hello!")
modern_print("How do you do?")
modern_print("Hello!")
