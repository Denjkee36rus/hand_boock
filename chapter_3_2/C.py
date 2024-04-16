unique: set = set()

for _ in range(int(input())):
    unique.update(input().split())

print(*unique, sep='\n')
