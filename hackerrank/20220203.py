test_num = int(input())
for num in range(0, test_num):
    a_num = int(input())
    set_a = set([int(num) for num in input().split(" ")])
    b_num = int(input())
    set_b = set([int(num) for num in input().split(" ")])
    print(set_a.issubset(set_b))