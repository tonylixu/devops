def length_of_longest_substr2(s):
    length = len(s)
    s2 = set()
    max_len = i = j = 0
    while i < length and j < length:
        if s[j] not in s2:
            s2.add(s[j])
            j += 1
            max_len = max(max_len, j-i)
        else:
            s2.remove(s[i])
            i += 1
    print max_len

if __name__ == '__main__':
    s = 'abcabcbb'
    length_of_longest_substr2(s)
