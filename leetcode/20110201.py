# 344. Reverse String : https://leetcode.com/problems/reverse-string/
"""
투 포인터

- 리스트에 순차적으로 접근해야할때 두 개의 점을 이용해 위치를 기록하면서 처리하는 기법

1. 시작점과 끝점이 첫번째 원소의 인덱스(0)을 가리키도록 한다
2. 현재 부분 합이 M과 같다면 카운트한다
3. 현재 부분 합이 M보다 작거나 같다면 end를 1 증가시킨다.
4. 현재 부분 합이 M보다 크다면 start를 1 증가시킨다
5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.
"""
# sol 1
# 38.11% faster 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

# sol 2
# faster than 10.45% of Python3 online submissions 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s)-1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1