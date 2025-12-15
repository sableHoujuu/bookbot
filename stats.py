def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_count(words):
    total = {}
    for word in words:
        lower = word.lower()
        for i in range(0, len(lower)):
            char = lower[i]
            if char in total:
                total[char] += 1
            else:
                total[char] = 1

    return total
