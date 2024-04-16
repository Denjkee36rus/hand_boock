s = 'python world python python java programming'

nums = {1, 'java', 6, 8}
words = s.split()
print(words)
# Слияние

print(nums.update(words))
print(nums)

print('Исходное множество:', id(nums))

nums = nums.union(words)
print('Union множество:', id(nums))
