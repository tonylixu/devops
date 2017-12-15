def is_palindrome(s):
    queue = []
    stack = []
    is_palindrome = True
    for i in s:
        # Push into queue and stack
        queue.insert(0, i)
        stack.insert(0, i)
    for i in range(len(s)/2):
        a = stack.pop(0)
        b = queue.pop(-1)
        if a != b:
            is_palindrome = False
            break
    return is_palindrome

def validate(s):
    s2 = [x for x in s]
    if is_palindrome(s2):
        return True
    else:
        for i in range(len(s2)):
            temp = s2.pop(i)
            if is_palindrome(s2):
                return True
            s2.insert(i, temp)
    return False

if __name__ == '__main__':
    s = 'cbbcc'
    print validate(s)
