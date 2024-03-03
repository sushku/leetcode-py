from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currAlt = 0
        altitudes = [currAlt]
        for n in gain:
            currAlt += n
            altitudes.append(currAlt)
        return max(altitudes)

# Main
gain = [-5, 1, 5, 0, -7]
print(Solution().largestAltitude(gain))