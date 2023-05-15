from itertools import permutations

# permutation -> arrange in particular order.
#                   sort n numbers in r ways
#                   example : numbers=[1,2,3]; permutation-> [123,132,213,312,321,231]
#                   formula = p(n,r) = n!/(n-r)!
#                   if numbers can repeat then -> n^r

# example: frame 3 letter word from SWING (5 letter word)
# x = 5!/(5-3)! = 60

# algo: The idea is to one by one extract all elements, place them at first position and recur for remaining list.
# Python function to print permutations of a given list
def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list. remLst is
        # remaining list
        remLst = lst[:i] + lst[i+1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


# Driver program to test above function
data = list('123')
for p in permutation(data):
    print(p)

## permutation using recursion:
def swap(x, i, j):
    temp = ''
    for z in range(len(x)):
        if z == i:
            temp += x[j]
        elif z == j:
            temp += x[i]
        else:
            temp += x[z]
    return temp


def per(x, k=0):
    if len(x) == k:
        print(x)

    for i in range(k, len(x)):
        # we are doing swap,because we want to set all the existing elements one by one in each position
        x = swap(x, i, k)
        # fix one item by increasing k with 1
        per(x, k+1)
        # reversing the swap operation, so that previous recursion stack will get original string
        x = swap(x, k, i)



# combination : select/pick items from list.
#           formula: n!/(r!(n-r)!) ; r! in denominator is used to delete different permutations
#           so all these permutations [123,132,213,312,321,231] will be considered sa single combination as all these
#           have same digits


# fix one element then make combination with other elements one by one
# complexity n2
# all combinations formula (all subsets): 2^n

# SUBARRAY/substring: A subarray is a contiguous part of array and maintains relative ordering of elements.
# For an array/string of size n, there are n*(n+1)/2 non-empty subarrays/substrings.

#
# SUBSEQUENCE: A subsequence maintain relative ordering of elements but may or may not be a contiguous part of an array.
# For a sequence of size n, we can have 2^n-1 non-empty sub-sequences in total.
#
# SUBSET: A subset does not maintain relative ordering of elements and is neither a contiguous part of an array.
# For a set of size n, we can have (2^n) sub-sets in total.

# example: l = [1,2,3,4,5,6,7]
# subset: [7,4] (not contiguous and doesn't have order as original one)
# subarray=[1,2,3] (contiguous elements from original list in same order as original list)
# subsequence=[2,4,6] (even though we don't have contiguous elements, but still they maintain original list order)

# 1. all combinations
def combinations(l:list, r:int):
    # note: for specific length only r will reach to 0 and if r is 0 that means we got our intial combination [[]]
    # but r is not 0 and l already become empty then it will return empty list [] and not [[]], i.e no combination
    # this is what avoid getting combination of lesser value
    if r ==0:
        return [[]]
    ls = []
    # to get all combinations replace ls=[] with ls=[[]]
    for x in range(0,len(l)):
        first = l[x]
        rem = l[x+1:]
        comb = combinations(rem, r-1)

        for y in comb:
            ls.append([first]+y)

    return ls
# specific length combinations
print(combinations([1,2,3,4],4))


#                            [1,2,3], 2   -> ([1,2],[1,3], [2,3])  -> formula (prev result +current first)
#    /  (1)  (current first)                           | (2)                           \ (3)
# [2,3],1 ->  ([[2], [3]])                           [3],1 -> ([[3]])                   [], 1
#   /   (2)             \ (3)
# [2],0 ->([[]])     [3],0 ->([[]])

# 2. all subarray
# complexity n2
def allSubarray(a):
    x=[]
    for i in range(len(a)):
        x.append([a[i]])
        for j in range(i+1,len(a)):
            x.append([*x[-1], a[j]])
    return x



# 3. subarray having sum less than k
#Let us take an example array is 1 2 3
# Subarrays will be 1 2 3 12 123 23.
#
# Total :6 .
#
# With 1 at first  , 3 subarrays are formed.
#
# With 2 at first , 2 are formed.
#
# With 3 , only 1 is formed.
#
# 1+2+3=6
#
# Similary, for input size n, using sum of first n natural numbers.
#
# Total subarrays would be 1+2+…..+n
# so we use sum of AP formula and get below eqution
# i.e n*(n+1)/2
# same thing applies for backward story
# with 3 at last, 3 subarrays are formed
# with 2 at last, 2 subarrays are formed
# with 1 at last, 1 subarrays are formed
#  using this technique, we can create a formula to find number of subarrays formed at current index i
# formula: [last index - first index +1]
# example: total subarrays formed with elements only 1 and 2 from array [1,2,3]
# so for 1 , 0-0+1 = 1
# and for 2, 1-0+1 = 2
# so total count will be 3
# note this algo will not work for -ve numbers
# this is sliding window problem: here we find subsets whose sum is lesser, then using above technique
# we will find number of  subssets generated when current elements at last position.
def countMinSumSubArray(a,k,n):
    sum=0
    f =0
    l=0
    res =0
    while l<n:
        sum+=a[l]
        if sum < k:
            res = l-f+1
            l+=1

        while sum>=k and f<=l:
            f+=1
            sum-=a[f-1]
    return res


if __name__ == "__main__":
    array = [1,0,1]
    k = 1
    size = len(array)
    print(countMinSumSubArray(array, size, k))

# similarly for greater count we can subtract lower sum count  with total subsets counts.



# all subsets
# complexity will be 2^n, because here we will take 2 decision for ech element, wither we should include it or not.

# [1,2]   ->    (1) either null or 1-> [none]/[1]  ==> (2) add either null or 2 in previous array -> [none,none]/[none,2]/[1,2]/[1,none]

res = []
def allSubsets(data,k,myarr):

    # in our case all subsets will have same length, or original list because we are adding None for empty data.
    # so if k match the original array list size it means current subset is completed
    if k == len(data):
        res.append(tuple(myarr))
    else:

        # decision 1: if we do not include current element
        myarr[k]=None
        allSubsets(data,k+1, myarr)

        # decision 2: if we include current element
        myarr[k]=data[k]
        allSubsets(data,k+1, myarr)

allSubsets([1,2,3], 0, [None]*3)
print(res)

### another way ####

res = []
def allSubsets(data,k,myarr):

    # in our case all subsets will have same length, or original list because we are adding None for empty data.
    # so if k match the original array list size it means current subset is completed
    if k == len(data):
        res.append(tuple(myarr))
    else:

        # decision 1: if we  include current element
        myarr.append(data[k])
        allSubsets(data,k+1, myarr)

        # decision 2: if we not include current element
        # there is a magic here, by the time we reach to below allSubstes call, the element we are removing below,
        # is already added by above function call.
        # for example, if data[k] is 1, then it will give all scenarios where 1 is excluded from subset
        myarr.remove(data[k])
        allSubsets(data,k+1, myarr)

allSubsets([1,2,3], 0, [])
print(res)