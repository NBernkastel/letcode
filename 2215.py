nums1 = [1, 2, 3]
nums2 = [2, 4, 6]


def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    return [list(set(nums1).difference(set(nums2))), list(set(nums2).difference(set(nums1)))]


print(findDifference(nums1, nums2))
