class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        remIndexDict = {}
        for i, n in enumerate(nums):
            rem = target - n
            if n in remIndexDict:
                return [remIndexDict[n], i]
            else:
                remIndexDict[rem] = i

# Main
nums = [2, 7, 11, 14]
target = 9
print(Solution().twoSum(nums, target))