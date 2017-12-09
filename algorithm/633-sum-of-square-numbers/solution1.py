def judge_square_sum(c):
    nums = [i for i in range(1, c)]
    length = len(nums)
    i = 0
    while i*i <= c:
        j = 0
        while j*j <= c:
            if i*i + j*j == c:
                return True
            j += 1
        i += 1
    return False

if __name__ == '__main__':
    c = 5
    print judge_square_sum(5)