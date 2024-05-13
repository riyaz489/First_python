# example:
# 1,5,2,7,4,8,9
# output is 1,2,7,8,9 or 1,5,7,8,9 or 1,2,4,8,9; but  1,5,8,9 is also increasing subsequence but it is not longest.

# one way to solve it using an auxiliary array which will keep track of lenght LIS of 0 to ith index
# like for above input array will look like
# 1,2,2,3,3,4,5
# and our answer will max item from this array.
# now to generate array, let say we are at 4th index for 4 item.
# now in aux array we will check from 0 to i-1 index:
# for 0th index LCS is 1 and input[0] is also < input[i] i.e 1<4, so we will do lcs =1+1 = 2
# for 1th index LCS is 2 and input[1] is  > input[i] i.e 5>4, so we will skip its lcs and mark it as 0+1 for now.
# for 2th index LCS is 2 and input[2] is also < input[i] i.e 2<4, so we will do lcs =2+1 = 3
# for 3rd index LCS is 3 and input[3] is > input[i], i.e 7>4, so we will keep lcs so far as 0 and do 0+1 for now.
# now we will check what is max out of these operations, and we will put max value in current index of aux arr.
# which is 3 in our case.

# but time complexity is n^2 for this algo.

# a better solution would be, if we can store minimum item for each lenght of LIS.

# for exmaple: 1, 40,50,60,4,80
# for lcs of lenght 1 minimum item is 1
# for lcs of lenght 2 minimum item is 40
# for lcs of lenght 3 minimum item is 50
# for lcs of lenght 4 minimum item is 60
# now, for lcs of lenght 2 we have new minimum item is 4, so we will replace it with 40.
# for lcs of lenght 4 minimum item is 80

# as you can notice if current item is bigger than last item in LIS list then we will simply append it to LIS arr.
# otherwise we will find its correct position in LIS array and swap it.
# swapping position will be closest ceil value of current element.
# like in 4 case, 1 was smaller than 4 and next greater item in list was 40, so that's why we replaced with 40.
# and final result will be LIS array size.

# now as you can notice items in LIS array will always be sorted. so we can use binary search here to figure out the
# swapping position

# data=[ 1 , 3, 4, 5, 6]
# k=2
# we will get 3 index as output which is 1
def search_ceil_value(data, k):
    l = 0
    r = len(data)-1
    res = 0
    while l<=r:
        mid = (l+r)//2

        if k <= data[mid]:
            r = mid - 1 # reduce right range to get more lower values.
            res = mid  # last max value we have seen.
        else:
            l = mid + 1

    return res

def findLIS(data):
    aux = [1] # as for first elelement lenght will be 1

    for i in range(1,len(data)):
        if data[i]>aux[-1]:
            aux.append(data[i])
        else:
            new_index = search_ceil_value(aux, data[i])
            aux[new_index] = data[i]

    return len(aux)

print(findLIS([1,5,2,7,4,8,9]))


### VAriations of LIS ###

# 1. delete minimum elements to make a array sorted.
# 2. Max sum increasing subseqeunce.
# here we will not use binary search apporach instead we use first approach which was of n2 complexity.
# in aux array instead of maintain LIS lenght we will maintain max sum of LIS.

def max_sum_lis(data):
    arrr = [0] * len(data)
    arrr[0] = data[0]
    for i in range(1, len(data)):
        # initializing with current array value
        arrr[i] = data[i]

        for j in range(0, i):
            if data[i] > data[j]:
                # if item is smaller then only we will consider of adding prev min item LIS.
                # and we will keep whatever max value we found so far for item i.
                arrr[i] = max(arrr[i], arrr[j] + data[i])

    print(max(arrr))

# 3. maximum lenght bitonic subsequence. bitomic sequence  is first increasing then decreasing.
# if array is sorted and we only have increasing or decreasing elements then answer would be lenght of increasing or
# decrease subsequence only.
# idea is simple, first create an aux array of increasing LIS
# then traverse data from right to left and populate new LIS array also from right to left. this will give us
# longest decreasing subsequence from left to right.
# now for each index do sum of aux1 and aux2 item, and return whatever is max.
# for example: [1, 11,2,10,4,5,2,1]
# LIS =         [1,2,2,3,3,4,2,1]
# LongestDecreasingSubsequence =         [1,5,2,4,3,3,2,1]

# LongestBitonicSubsequence =         [1+1-1, 2+5-1, ... 1+1-1]
# doing -1 as current element is repeated on LIS and LDS
# this currently n2 complexity

# 4. build bridges: [(6,2), (4,3), (2,6), (1,5)]
# we have give starting point and endpoint of bridges in each tuple and we have to build max bridges by making sure
# so 2 bridges cross each other.
# like if we build (2,6) then we can't build (1,5) and 1,5 will now overlap.
#   1 2 3 4 5 6
#     |
#     ________
#             |
#   1 2 3 4 5 6

# idea is simple sort data by first key and if first key is same then use second key.
# then find the LIS using second key, if second key is same for few bridges then include it in LIS.
# because to avoid overlap starting and ending point should be in increasing order.
# time complexity is 2*(nlog)

# 5. Find the longest chain of pairs
# here we have given starting and ending points in tuple, and we have to build longest chain.
# and 2 pairs (a,b) and (c,d) will be only included in chain if c>b.
# example: (5,24), (15,28), (39,60)
# so here possible chains can be [(5,24), (39,60)] and [(15,28), (29,60)]

# to solve it first we have to sort data using first key.
# then we have to use modified lis code on new sorted pairs list.
# like in case of max sum LIS we modified LIS condition. similarly here
# also we will consider any item for LIS only when that pair ending is smaller than starting of current pair.
# i.e c>b as mentioned above.
