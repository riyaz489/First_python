# Think recursively:

# 1. assume your function is working and it's already solving sub problem
# 2. then think about base case(exit condition)
# 3. dry run with smallest problem possible.
# 4. leaf node in tree is base case for exit condition.
# 5. if we do more than one recursion call then it will become tree.
#


# tail recursive functions: these are those function where recursive function is called at the very end of function
# example:
def a(n):
    if n==0:
        return
    print(n)
    a(n-1)

# modern compiler are smart they can detect the tail recursive function and avoid creating new stack frame for new
# recursive function, as parent function has nothing else to do once child function is completed, so there is no need
# to store parent function state.
# so in conclusion tail function are more optimised than not tail recursive functions.


# but below exaple is not tail recursive
def a(n):
    if n==0:
        return 1
    print(n)
    return n*a(n-1)
# as here parent function need to do some multiplication on child function result

# now to make it tail recursive, we will add one more argument
# (we usually take help of extra agrs to make function tail recursive)

def a(n,k=1):
    if n==1:
        return k
    return a(n-1, n*k)
# so k will be like for input 3: 3x1, 2x3, 1x6
# and once n become 1, it will return k which is 6 now.




### find sum in subsets of a list

x = [1,2,3,5,6]
z = 8
# we can optimize it using DP, by storing already computed data
def find_sum(x, z, k,sub):
    # it means we reach to leaf node
    if k+1 == len(x):
        print(sub)
        if sum(sub) == z:
            return 1
        return 0
    # we did sub+[] (it will create a new list object, instead of passing same list),
    # to avoid passing same list in all recursive methods
    temp1 = find_sum(x, z, k+1, sub+[])
    temp2 = find_sum(x, z, k+1, sub+[x[k+1]])
    return temp1 + temp2


print(find_sum(x, z, k=0, sub=list()))