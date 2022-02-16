# two pointer 까진 캐치했으나 풀이는 결국 책을 참고했다.
# 바깥에서부터 축소보단 안에서 확장하며 검증하는 생각을 해야함
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or (s == s[::-1]):
            return s
        def expand(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1:right-1]
        result = ""
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result