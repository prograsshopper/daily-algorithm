# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    return True if x % sum([int(elem) for elem in str(x)]) == 0 else False