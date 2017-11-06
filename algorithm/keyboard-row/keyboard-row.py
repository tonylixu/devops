def findWords(words):
    # We define keyboard rows
    keyboard_rows = [
        'eiopqrtuwy',
        'adfghjkls',
        'bcmnvxz'
    ]
    # We sort and eliminate the duplicate
    words_new = []
    re = []
    for i in words:
        words_new.append(''.join(set(sorted(i.lower()))))
    print words_new
    for i in words_new:
        for j in i:
            if j in keyboard_rows[0]:
                break
            elif j in keyboard_rows[1]:
                break
            elif j in keyboard_rows[2]:




if __name__ == "__main__":
    words = ["Hello", "Alaska", "Dad", "Peace"]
    findWords(words)