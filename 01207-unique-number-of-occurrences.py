
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if d.get(i):
                d[i] += 1
            else:
                d[i] = 1
        return len(d.values()) == len(set(d.values()))

# Main
arr = [1, 2, 2, 1, 1, 3]
print(Solution().uniqueOccurrences(arr))