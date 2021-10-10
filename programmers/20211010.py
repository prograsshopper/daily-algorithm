# https://programmers.co.kr/learn/courses/30/lessons/12925
# 문자열을 정수로 바꾸기
'''
단순히 int로 바꾸고 끝낼 문제가 아니라 다른 사람 풁이를 보고 나니 완전 잘못생각했다는 판단이 든 문제
너무 파이썬 언어에서 제공하는 편의에 의존한게 아닌가 하는 생각이 들었다
해당 풀이: 
def solution(s):
    result = 0
    for index, number in enumerate(s[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** index)
    return result
'''
def solution(s):
    return int(s)
