# https://programmers.co.kr/learn/courses/30/lessons/12935
# 제일 작은 수 제거하기
def solution(arr):
    min_val = min(arr)
    arr = [elem for elem in arr if elem != min_val]
    return arr if len(arr) > 0 else [-1]