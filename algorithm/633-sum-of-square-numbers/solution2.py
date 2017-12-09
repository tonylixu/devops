def judge_square_sum(c):
    for a in range(int(c ** 0.5) + 1):
        b2 = c - a ** 2
        if (int(b2 ** 0.5)) ** 2 == b2:
            return True
    return False

if __name__ == '__main__':
    c = 5
    print judge_square_sum(5)