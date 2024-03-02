import sys
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        sumNums = sum(nums[:k])
        maxAvg = sumNums / k
        for i in range(k, len(nums)):
            sumNums = sumNums + nums[i] - nums[i-k]
            avg = sumNums / k
            if avg > maxAvg:
                maxAvg = avg
            i += 1
        return maxAvg

# Main
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(Solution().findMaxAverage(nums, k))