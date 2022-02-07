def check_strict_superset(set_a, set_b):
    result = False
    if set_a.issuperset(set_b) and (len(set_a) > len(set_b)):
        result = True
    return result

set_a = set([int(num) for num in input().split(" ")])
set_nums = int(input())

final_result = True
for num in range(set_nums):
    cur_set = set([int(num) for num in input().split(" ")])
    if not check_strict_superset(set_a, cur_set):
        final_result = False
        break
print(final_result)