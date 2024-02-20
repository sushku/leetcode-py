class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        totLen = len1 + len2
        midIndex = totLen // 2
        i, j, count = 0, 0, 0
        mergedList = []
        while count <= midIndex:
            p1 = nums1[i] if i < len1 else None
            p2 = nums2[j] if j < len2 else None
            if (i < len1 and j < len2 and p1 < p2) or (i < len1 and j >= len2):
                mergedList += [p1]
                i += 1
            else:
                mergedList += [p2]
                j += 1
            count += 1

        print(mergedList)
        if totLen % 2:
            median = mergedList[-1]
        else:
            median = (mergedList[-1] + mergedList[-2]) / 2
            
        return median

 # Main
nums1 = [-1]
nums2 = [-3, -1, 0]

print(Solution().findMedianSortedArrays(nums1, nums2))