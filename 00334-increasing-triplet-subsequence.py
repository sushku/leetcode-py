import sys
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = sys.maxsize
        min2 = sys.maxsize
        for n in nums:
            if n < min1:
                min1 = n
            elif n > min1 and n < min2:
                min2 = n
            elif n > min2:
                return True
        return False

# Main
nums = [2, 1, 5, 0, 4, 6]
print(Solution().increasingTriplet(nums))