import cProfile

# Data
s = "abciiidef"
k = 3
Vowel = ['a', 'e', 'i', 'o', 'u']


# func
def maxVowels(s: str, k: int) -> int:
    count = 0
    for let in s[0:k]:
        if let in Vowel:
            count += 1
    max_count = count
    for i in range(k, len(s)):
        if s[i - k] in Vowel:
            count -= 1
        if s[i] in Vowel:
            count += 1
        if count > max_count:
            max_count = count
    return max_count


if __name__ == '__main__':
    print(maxVowels(s, k))
