# is palindrome: https://leetcode.com/problems/valid-palindrome/

# sol 1 : faster than 5.08% of Python3 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        target = ""
        for val in s:
            target = target + val.lower() if val.isalnum() else target
        for i in range(0, len(target)//2):
            if target[i] != target[len(target)-i-1]:
                return False
        return True

# sol 2: faster than 5.08%
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = 0
        flag = False
        while True:
            if i >= (len(s)-1):
                flag = True
                break
            if not s[i].isalnum():
                i += 1
            elif not s[len(s)-j-1].isalnum():
                j += 1
            else:
                if s[i].lower() != s[len(s)-j-1].lower():
                    break
                i += 1
                j += 1
        return flag

