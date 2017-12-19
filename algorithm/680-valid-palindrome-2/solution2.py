def valid_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            s1 = s[:lo] + s[lo+1:]
            s2 = s[:hi] + s[hi+1:]
            return self.is_palindrome(s1) or self.is_palindrome(s2)
        lo += 1
        hi -= 1
    return True
        
        
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    s = 'cbbcc'
    print valid_palindrome(s)