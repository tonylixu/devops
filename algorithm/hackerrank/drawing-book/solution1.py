def solve(n, p):
    # Edge cases
    # n == p or p is 1
    if n == p or p == 1:
        print 0
        exit(0)
    # n is even and p == n-1
    if n % 2 == 0 and p == n - 1:
        print 0
        exit(0)
    # Main solution
    flips_from_head = p/2
    flips_from_tail = (n-p)/2
    print min(flips_from_head, flips_from_tail)
n = 9
p = 3
solve(n,p)