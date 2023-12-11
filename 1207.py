arr = [1, 2, 2, 1, 1, 3]


def uniqueOccurrences(arr: list[int]) -> bool:
    uniq = {}
    for i in range(len(arr)):
        if arr[i] in uniq:
            uniq[arr[i]] += 1
        else:
            uniq[arr[i]] = 1
    vallist = list(uniq.values())
    if len(set(vallist)) == len(vallist):
        return True
    return False


print(uniqueOccurrences(arr))
