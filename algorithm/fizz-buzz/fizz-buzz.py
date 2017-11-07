n = 15
for i in range(n):
    n = i+1
    if n % 3 == 0 and n % 5 != 0:
        print "Fizz"
    elif n % 5 == 0 and n % 3!= 0:
        print "Buzz"
    elif n % 15 == 0:
        print "FizzBuzz"
    else:
        print n