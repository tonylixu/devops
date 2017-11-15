def length_of_longest_substr(s):
    length = len(s)
    s3 = ''
    max_len = 0
    for i in range(length):
        for j in range(i+1, length+1):
            s2 = []
            for k in range(i, j):
                s2.append(s[k])
                length = len(s2)
            if max_len < len(s2) and len(set(s2)) == len(s2):
                max_len = len(s2)
                s3 = ''.join(s2)
    print s3

if __name__ == '__main__':
    s = 'abcabcbb'
    length_of_longest_substr(s)