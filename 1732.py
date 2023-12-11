nums = [2,1,-1]


def pivotIndex(nums: list[int]) -> int:
    left = 0
    rigt = sum(nums)
    for i in range(len(nums)):
        rigt -= nums[i]
        if left == rigt:
            return i
        left += nums[i]
    return -1

print(pivotIndex(nums))
