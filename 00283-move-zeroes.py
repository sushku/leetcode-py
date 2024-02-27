from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0
        lastIndex = len(nums) - 1
        while True:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                lastIndex -= 1
                count += 1
            else:
                i += 1
            if i > lastIndex:
                break

# Main
nums = [0, 1, 0, 3, 0, 12, 0, 0]
Solution().moveZeroes(nums)