def inc():
    global x
    x += 1
    print(f"Количество вызовов функции равно {x}.")


x = 0
inc()
inc()
inc()
