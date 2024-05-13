from itertools import permutations

# permutation -> arrange in particular order.
#                   sort n numbers in r ways
#                   example : numbers=[1,2,3]; permutation-> [123,132,213,312,321,231]
#                   formula = p(n,r) = n!/(n-r)!
#                   if numbers can repeat then -> n^r

# example: frame 3 letter word from SWING (5 letter word)
# x = 5!/(5-3)! = 60

# example, let n = 3 (A, B, and C) and r = 2 (All permutations of size 2). Then there are 3P2 such permutations,
# which is equal to 6. These six permutations are AB, AC, BA, BC, CA, and CB

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
        # cutting string len to k
        print(x[0:k])

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
# For example, let n = 3 (A, B, and C) and r = 2 (All combinations of size 2). Then there are 3C2 such combinations,
# which is equal to 3. These three combinations are AB, AC, and BC.



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

# 1. all combinations O(n^k), where k is length of combinations.
# fix one element then make combination with other elements one by one
#                            [1,2,3], 2   -> ([1,2],[1,3], [2,3])  -> formula (prev result +current first)
#    /  (1)  (current first)                           | (2)                           \ (3)
# [2,3],1 ->  ([[2], [3]])                           [3],1 -> ([[3]])                   [], 1
#   /   (2)             \ (3)
# [2],0 ->([[]])     [3],0 ->([[]])

def combinations(l:list, r:int): # O(n^k)
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



# 2. all subarray
# complexity n2
def allSubarray(a):
    x = []
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            x.append(a[i:j])
    return x



# 3. subarray having sum less than k
# let us take an example:
# for input [1,2,3]
# subarrays will be 1, 2, 12, 3, 23, 123.
# total subarray count is 6
# now if you notice
# subarray ending with 1 is 1 => 1
# subarray ending with 2 is 2   => 2, 12
# subarray ending with 3 is 3  => 3, 23, 123

# similarly subarray ending with n will be n.

# and total number of subarrays will be
# 1 + 2+ 3+ ...n
# AP sum = n/2(2*1 + (n-1)*1) =(n/2)(1+n) => total number of subarrys.


# that means with every new element we are making (prev length of array +1) new sub-arrays.
# like prev array was [1,2] and total subarrays with it was 3.
# now if we add 3 in array, then total possible subarrays will be  =
# (prev no. of subarrays) + (no.of subarrays after adding new elem) = 3 + (prev lenght of arr +1) = 3+3 = 6


# we will have 2 pointers, f and l, and both will start with 0
# now as long as sum of f to l pointer elements is <k we will add l-f+1 to res

# lets take an example:
# [2,3,4,5], k=8
# we will start with 2 and 2 is less than 8 so res is 1
# then we will increment l, now sub array is [2,3] and sum is again less than 8 so we will do res+= new subarray lenght
# so res will be 1+2 = 3
# now again l++ and sub array will be [2,3,4] but now sum is > 8, so we do f++ till sum <8 again
# now we left with [3,4], as we can see new element 4 is added, but now subarray lenght is 2.
# so new possible subarrays with addition of 4 will be 2. so res will be res+=2
def countSubarrays(arr, n, k):
    start = 0
    end = 0
    count = 0
    sum = arr[0]

    while (start < n and end < n):

        # If sum is less than k, move end
        # by one position. Update count and
        # sum accordingly.
        if (sum < k):
            end += 1

            if (end >= start):
                count += end - start # lenght of current subarray

            # For last element, end may become n
            if (end < n):
                sum += arr[end]

        # If sum is greater than or equal to k,
        # subtract arr[start] from sum and
        # decrease sliding window by moving
        # start by one position
        else:
            sum -= arr[start]
            start += 1

    return count


# Driver Code
if __name__ == "__main__":
    array = [1, 11, 2, 3, 15]
    k = 10
    size = len(array)
    print(countSubarrays(array, size, k))

# This code is contributed by ita_c

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


# Find number of ways a 5 digit number can be formed from 1,2,3,4,5 where 1 will always be left of 2.
# now if we fix 1 and 2 position then we will left with 3 numbers, whose positions we can change and generate
# different permutations.
# so possible permutation with 3 digit number will be 3!.
# now there are 5C2 =10 ways in which we can place 1 and 2.
# for combination think like, we have 5 positions and we have to get 2 different possible positions.
# [1,2,X,X,X,] => 3!
# [1,X,2,X,X,] => 3!
# [1,X,X,2,X,] => 3!
# [1,X,X,X,2] => 3!
# [X,1,2,X,X] => 3!
# [X,1,X,2,X] => 3!
# [X,1,X,X,2] => 3!
# [X,X,1,2,X] => 3!
# [X,X,1,X,2] => 3!
# [X,X,X,1,2] => 3!