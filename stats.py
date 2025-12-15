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


def sort_on(items):
    return items["num"]


def get_sorted_count(total):
    dict_list = []
    for char, count in total.items():
        d = {"char": char, "num": count}
        dict_list.append(d)

    # Now that we have a sortable list, we can sort
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
