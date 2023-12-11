nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]


def longestSubarray(nums: list[int]) -> int:
    left = 0
    zeros = 0
    res = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        res = max(res, right - left)
    return res


print(longestSubarray(nums))

# идем в право считаем нули что мы встретили, если их становится больше 1 то начиваем считать где слева был последний
# нуль, максимальная разница между правым шагом и последним нулем и есть ответ
