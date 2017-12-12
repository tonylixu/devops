def length_of_last_word(s):
    """
    :type s: str
    :rtype: int
    """
    s2 = [x for x in s.split(' ') if x]
    if s2:
        return len(s2[-1])
    else:
        return 0

if __name__ == '__main__':
    s = "hello world"
    print(length_of_last_word(s))