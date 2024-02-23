from typing import List

class Solution:
    def getNumFlowers(self, consecutiveZeroes: int):
        consecutiveZeroes = consecutiveZeroes if consecutiveZeroes % 2 else consecutiveZeroes - 1
        return consecutiveZeroes // 2

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        consecutiveZeroes = 1
        totalFlowers = 0
        for k in flowerbed:
            if k == 0:
                consecutiveZeroes += 1
            else:
                if consecutiveZeroes:
                    totalFlowers += self.getNumFlowers(consecutiveZeroes)
                    consecutiveZeroes = 0
        if consecutiveZeroes:
            consecutiveZeroes += 1
            totalFlowers += self.getNumFlowers(consecutiveZeroes)

        return n <= totalFlowers

# Main
flowerbed = [0, 0, 0, 1, 0, 0]
n = 2
print(Solution().canPlaceFlowers(flowerbed, n))