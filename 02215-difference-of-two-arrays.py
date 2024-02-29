from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1).difference(set(nums2))), list(set(nums2).difference(set(nums1)))]

# Main
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
print(Solution().findDifference(nums1, nums2))