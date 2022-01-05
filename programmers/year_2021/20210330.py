# https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3
def solution(phone_number):
    length = len(phone_number)
    return ''.join(['*' if i < (length - 4) else phone_number[i] for i in range(0, length)])