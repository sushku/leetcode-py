from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        i = 0
        j = len(height) - 1
        while i < j:
            base = j - i
            ht = min(height[i], height[j])
            area = base * ht
            if area > maxA:
                maxA = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxA

# Main
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))