# first sol
#  faster than 84.48% of Python3 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        word_dict = defaultdict(list)
        for elem in strs:
            sort_elem = "".join(sorted(elem))
            word_dict[sort_elem].append(elem)
        return word_dict.values()