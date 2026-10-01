text = "leetcode"

char_count = {}


def firstNonRepeatingCharc(text):
    for t in text:
        char_count[t] = char_count.get(t, 0) + 1

    for t in text:
        if char_count[t] == 1:
            return char_count[t]


print(firstNonRepeatingCharc(text))
