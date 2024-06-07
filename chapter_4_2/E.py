def to_string(*data, sep=' ', end='\n'):
    return sep.join(map(str, data)) + end


print(to_string([7, 3, 1, "hello", (1, 2, 3)]))


def to_string(*args, sep=" ", end="\n"):
    n: int = len(args)

    result: str = ""
    for i in range(n):
        result += str(args[i])
        if i != n - 1:
            result += sep

    result += end

    return result
