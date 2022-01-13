# The Captain's Room

from collections import Counter
K = int(input())
key_dict = Counter([int(i) for i in input().split(" ")])
for (key, val) in key_dict.items():
    if val == 1:
        print(key)
        break