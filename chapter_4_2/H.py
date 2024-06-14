# string = 'Яндекс использует Python во многих проектах'
# result = sorted(string.split(), key=lambda x: len(x) )
# print(result)

def snring(args: str):
    return args.upper()[::-1]
print(snring("hello world"))
