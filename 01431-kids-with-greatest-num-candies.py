class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        boolList = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                boolList.append(True)
            else:
                boolList.append(False)
        return boolList

# Main
candies = [12, 1, 12]
extraCandies = 10
print(Solution().kidsWithCandies(candies, extraCandies))