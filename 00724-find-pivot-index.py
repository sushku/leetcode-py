from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumNums = 0
        for n in nums:
            sumNums += n
        left, right = 0, sumNums
        prev_n = 0
        for i, n in enumerate(nums):
            left += prev_n
            right -= n
            if left == right:
                return i
            prev_n = n
        return -1
# Main
nums = [1, 7, 3, 6, 5, 6]
print(Solution().pivotIndex(nums))