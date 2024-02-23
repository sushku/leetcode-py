from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        numZeroes = 0
        for n in nums:
            if n != 0:
                product *= n
            else:
                numZeroes += 1
        if numZeroes > 1:
            return [0] * len(nums)
        else:
            newList = []
            for n in nums:
                if n != 0:
                    if numZeroes == 1:
                        newList.append(0)
                    else:
                        newList.append(product // n)
                else:
                    newList.append(product)
            return newList

# Main
nums = [3, 5, 5, -4]
print(Solution().productExceptSelf(nums))