class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in d:
                return [d[rem], i]
            d[nums[i]] = i

s = Solution()
res = s.twoSum([3, 9, 4, 8, 3], 6)
print(res)
