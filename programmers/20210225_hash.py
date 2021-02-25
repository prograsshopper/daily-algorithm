# https://programmers.co.kr/learn/courses/30/lessons/42576
import unittest

def solution(participant: list, completion: list) -> str:
    from collections import defaultdict
    from itertools import zip_longest
    
    result_dict: dict = defaultdict(lambda:0)
    
    for person in zip_longest(participant, completion):
        result_dict[person[0]] += 1
        result_dict[person[1]] -= 1
    
    for val in result_dict:
        if result_dict[val] == 1:
            return val


if __name__ == "__main__":
    participant: list = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
    completion: list = ['josipa', 'filipa', 'marina', 'nikola']

    print(solution(participant, completion) == 'vinko')