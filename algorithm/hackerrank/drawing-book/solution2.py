def solve(n, p):
    flips_from_head = p/2
    flips_from_tail = (n-p)/2
    print min(p/2, (n-p)/2)
n = 9
p = 3
solve(n,p)