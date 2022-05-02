# https://programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    answer = []
    for elem1, elem2 in zip(arr1, arr2):
        mid_ans = []
        for i, j in zip(elem1, elem2):
            mid_ans.append(i+j)
        answer.append(mid_ans)
    return answer