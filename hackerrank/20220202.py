from collections import Counter
nums = int(input())
counter = Counter([input() for num in range(0, nums)])
print(length)
print(" ".join([str(elem[1]) for elem in counter.items()]))