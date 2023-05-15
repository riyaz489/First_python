# for log notation we use this format just to types in .py files
# log_2(n) it means log with base 2

# log_b(n) = x
# above n will be equivalent to; n= b^x
# i.e; n = b^(lob_b(n))

# we can count digits using this, like for decimal numbers base will be 10 and for binary base will be 2
# floor(log_b(n) + 1) = number of digits


# ap
# ln = a+(n-1)d
# sn = n/2 (2a+(n-1)d)

# gp
# sn = a((r^n) -1)/(r-1)
# ln = a (r^(n-1))

# prime numbers -> 6n-1 or 6n+1

# prime factors: i) run loop to i<= square_root(n)
# because all multiples comes ni pair -> (1,30) (2,15) (3,10) (5,6)


def primeFactors(n):
    c = 2
    while (n > 1):

        if (n % c == 0):
            print(c, end=" ")
            n = n / c
            # print till we can divide with small numbers completely.
            # if we can not divide with samll number anymore then increment it with one.
            # note: because we directly incrementing c with so we can get non-prime numbers as well like 4,6,etc
            # but we already divided our n with 2 and 3 repeatedly, so n%4 or n%6 will never return zero. similarly
            # for other numbers as well, because their prime factor already divided n.
        else:
            c = c + 1

# find power of a number-> break power into by 2 recursively
# then computer smaller power
# then merge result

def power(x,n):
    if n==0:
        return 1
    temp = power(x,int(n/2))
    temp *= temp

    if  n%2!=0:
        temp*=x

    return temp