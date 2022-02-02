# Reorder Data in Log Files : https://leetcode.com/problems/reorder-data-in-log-files/
# sol 1
# faster than 17.59% of Python3 online submissions
"""
The value of the key parameter should be a function (or other callable) that takes a single argument and returns a key to use for sorting purposes.
"""
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        dig_logs = []
        for log in logs:
            if log.split()[1].isalpha():
                letter_logs.append(log)
            else:
                dig_logs.append(log)
        return sorted(letter_logs, key=lambda elem: (elem.split()[1:], elem.split()[0])) + dig_logs