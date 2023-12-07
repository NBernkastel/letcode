nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3


def longestOnes(nums: list[int], k: int) -> int:
    j = 0
    i = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            k -= 1
        if k < 0:
            if nums[j] == 0:
                k += 1
            j += 1
    return i - j + 1


print(longestOnes(nums, k))
