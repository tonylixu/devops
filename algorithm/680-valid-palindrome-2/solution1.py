def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

def validate(s):
    if is_palindrome(s):
        return True
    else:
        for i in range(len(s)):
            s2 = s[:i] + s[i+1:]
            if is_palindrome(s2):
                return True
    return False

if __name__ == '__main__':
    s = 'cbbcc'
    print validate(s)
