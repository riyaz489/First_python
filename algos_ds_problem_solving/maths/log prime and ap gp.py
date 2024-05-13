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

# check prime numbers -> first we will check if number is 1, then simply return true.
# then we check if number is divisible by 2 or 3, if it is then return false. (as this will save lot of iterations)
# Now we have to check if our number is divisible any other prime number or not(like 121). to do so we will
# start loop from 5 to till sqrt of(n) (we ran loop till sqrt of n because, because all multiples
# comes in pair -> (1,30) (2,15) (3,10) (5,6)). now inside loop we check if current iteration or
# current iteration+2 is divisible by n or not. then increment current iteration by 6
# (as prime numbers can be represented as 6n-1 or 6n+1)


# all divisors of n:
# run loop till sqrt(n) and now if iteration x perfectly divides 'n' then we will print x and n/x


# all prime factors of a number
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


# find all prime numbers till n:
# Sieve of Eratosthenes -> all non-prime numbers are multiple of prime numbers.
# so in this algo first we create a array of numbers 2 to n. then one by one
# we pick one number and if its  mulitple present in given array. if it is there then we will mark it as non-prime.
n = 10
is_prime = [True] * (n+1)
for i in range(2, n+1):
    if is_prime[i]:
    # we can start from i square because lower values will be covered in lower prime number multiples.
        j = i*i
        while j <= n:
            is_prime[j] = False
            # j+i is also next multiple of i
            j += i

for i in range(1,n+1):
    if is_prime[i]:
        print(i)


# find power of a number-> break power by 2 recursively
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

# we can use same approach with iterations instead of recursion, but the problem is how we are going to
# divide power into multiple of 2s. So for that we will use binary numbers.
# we will convert power into binary representation.
# for example: 19 as power can be equal to 16+2+1
# and its binary representation is: 10011 -> here each position represent power of 2. so at 1st place we have 2 power 0
# 2 place we have 2power 1 and at 5th place we have 2 power 4.
# So if you notice all 1 bits are present power of 2s whose sum is equal to our required power.
# for example -> for 10011, if we only consider one 1 bit at a time then we get -> 10000 which is 16,
# 10 which is 2 and 1 is 1 and their sum is 19

# so this will help us to divide power into multiple of 2s.
# n=3
# x = 4
# res = 1
# while n>0:
#     if n%2 !=0:
#         # that means we got 1 bit and now we have to multiple the number with result
#         # we will multiply res so far with x, where x is  n^(some multiple of 2 we got so far).
#         res *= x
#         x-=1 # subtract by one to replace 1 at the end with 0
#     else:
#         # that means we got 0 so calculate the power of 2, but don't add this into result.
#         # as this is going to be used later.
#         x *= x
#         n/=2 # remove one 0 from last
#         # or n = n>>1
# print(res)