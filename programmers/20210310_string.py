# https://programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    return True if (s.isnumeric() and (len(s) == 4 or len(s) == 6)) else False