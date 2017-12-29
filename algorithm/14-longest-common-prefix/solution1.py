def longest_common_prefix(strs):
    if not strs:
        return ""
    s = strs.pop(0)
    # For each s[index]
    for i in range(len(s)):
        for string in strs:
            if len(string) <= i or string[i] != s[i]:
                return s[:i]
    return s

if __name__=='__main__':
    strs = ["heallo", "heaven", "headf"]
    print longest_common_prefix(strs)