# 344. Reverse String : https://leetcode.com/problems/reverse-string/
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