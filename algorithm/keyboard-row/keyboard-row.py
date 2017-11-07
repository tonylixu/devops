def findWords(words):
    # We define keyboard rows
    keyboard_rows = [
        ['e', 'i', 'o', 'p', 'q', 'r', 't', 'u', 'w', 'y'],
        ['a', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 's'],
        ['b', 'c', 'm', 'n', 'v', 'x', 'z']
    ]
    # We sort and eliminate the duplicate
    # because if you can type one, you can type many
    words_new = []
    re = []
    for i in words:
        words_new.append(''.join(set(sorted(i.lower()))))
    position = 0
    for w in words_new:
        list_w = list(w)
        # The number of characters can be typed in each row
        counter_1 = counter_2 = counter_3 = 0
        length = len(list_w)
        for i in list_w:
            if i in keyboard_rows[0]:
                counter_1 += 1
            elif i in keyboard_rows[1]:
                counter_2 += 1
            elif i in keyboard_rows[2]:
                counter_3 += 1    
        if counter_1 == length or counter_2 == length or counter_3 == length:
            re.append(words[position])
        position += 1
    print re


if __name__ == "__main__":
    words = ["Hello", "Alaska", "Dad", "Peace"]
    findWords(words)