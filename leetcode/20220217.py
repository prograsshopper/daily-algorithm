# sol 1
# 4116 ms, faster than 22.02% of Python3 online submissions
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            cur = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == cur:
                    result.append(i)
                    result.append(j)
                    return result
        return result

# sol 2
# 687 ms, faster than 35.31% of Python3 online submissions
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {nums[i]: i for i in range(0, len(nums))}
        for i, num in enumerate(nums):
            if (target - num) in nums[i+1:] and i != nums_dict[target-num]:
                return nums.index(num), nums_dict[target-num]