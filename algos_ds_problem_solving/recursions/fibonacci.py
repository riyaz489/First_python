# 0 1 1 2 3 5 8

def loop_fib(x):
    first = 0
    second = 1
    print(first)
    for i in range(x):
        print(second)
        c = first + second
        first = second
        second = c

loop_fib(5)


x = 5
z = [-1 for i in range(x+1)]
def fib_recur_dp(x):
    if x <=1:
        return x

    # if we have first item in our global list then just take it, otherwise calculate it
    if z[x-2] != -1:
        first = z[x-2]
    else:
        first = fib_recur_dp(x-2)
        z[x-2] = first

    if z[x - 1] != -1:
        second = z[x - 1]
    else:
        second = fib_recur_dp(x - 1)
        z[x - 1] = second

    z[x] = first+second
    # notice in fibonacci we are doing unnecessary calculations, which we have already done
    #  f(3)
    #  /  \
    # f(2) f(1)
    # |
    # f(1)
    # see for f(1) we are doing  times, so to avoid that we have used DP with our recursion approach.
    # otherwise fib simple recursive code will look like this ->
    # def fib(x):
    # if x<=1:
    #   return x
    # return fib(x-1) + fib(x-2)

    return z[x]

# so recursion with dp has complexity of O(n) but without dp it will O(2^n)

fib_recur_dp(5)
print(z)