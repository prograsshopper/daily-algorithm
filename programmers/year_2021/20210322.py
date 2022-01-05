# https://programmers.co.kr/learn/courses/30/lessons/12934
# first solution
import math
def solution(n):
    if math.sqrt(n).is_integer():
        return (int(math.sqrt(n)) + 1) ** 2
    else:
        return -1