# Hash table is where we store our data and index of each row is identified by hash function.
# requirements for hash function:
# 1. It should be fast to generate hash value.
# 2. It should uniformly distribute the keys (Each table position be equally likely for each key).
# 3. It should always return values withing given range of hash table. i.e if has table has only m rows then
#    it should return values from 0 to m-1; it will be handled by % operator.

# Collision: As we know user can input anything in hash table to store, so its nearly impossible to generate unique
# hash for each row for limited sized hash table. So when we get same hash values for different inputs then its called
# collision.


# How to generate hash numbers for strings:
# As we know we each character has some ascii values ranging from 97 to 122. so we can convert string into numbers.
# by converting each char into its ascii value. and to reduce the size of result we can do sum of all each
# individual characters. but the problem is different permutation of same string will result same numbers.
# for example abc and bac will result same number.
# So to solve this issue we will use weighted sum in hash function.
# char1*x^0+ char2*x^1 + char3*x^2 ...
# here x can be any integer value.

# Load factor = number of items we are going to store in hash table / number of slots exists in hash table.

## Collision Handling:

# 1. Chaining: here each row of hash table is dynamic list or linked list,
#   so whenever we have collision we append entry in same row. So that means each row contains multiple entries
#   for inputs which has same hash function results.
#   for example:
#                ## Hash table ##
#                    0, 4
#                     <empty linked list>
#                    <empty linked list>
#                    3
#   so for input 0,4,3 for hash table of size 4. 0%4=0 inserted in first row. 4%4=0 which is again first row
#   which is collision, so we append this entry in 0th row linked list. and 3%4=3, so it will stored on 4th row.

#   Datatypes to store chains:
#      1.lists,linkedlist -> search,delete,insert will be O(1+ size of chain) # [O(1) is to calculate
#                            hash function and go to correct hash table row]
#      2. self balancing bst ->  search,delete,insert will be O(1+log(size of chain))# [O(1) is to calculate
#                            hash function and go to correct hash table row]

#   we have also notices that avg chain length will be equal to load factor
#   this means avg search, delete, insert time will be (1+ load factor) in case of linked list.

# 2. Open Addressing: In Open Addressing, all elements are stored in the hash table itself. So at any point, the size
# of the table must be greater than or equal to the total number of keys
#   a. linear probing: In linear probing we will first try to insert data into location of hash, if that is already
#                       filled then we will go down linearly and try to find next available slot in table and insert
#                       value there. If we reached to bottom then we will start from top again and if we reached to
#                       original hash value slot again then we return false. which means table is full and
#                       we can't insert new value.
#                       so hash function will remain same but rehash function will look like
#                       this ->  rehash(key) = (n+i)%(table_size)
#                       where n is original hash function result( i.e hash(input) = n)
#                       and i will increment on every insert failure.
#
#                       during deletion we start loop from original hash value and move down sequentially like insert.
#                       we will run loop till we reached to same original hashed value again
#                       or we found an empty slot. if reached to these states that means element does not exists.
#                       If we found element then we will simply replace data with some empty node.
#                       instead of deleting element we are replacing it with empty node because it will help us
#                       distinguish if that row was empty or deleted. because during search we are breaking our loop
#                       on empty row not on deleted row.
#                       Search logic already covered in delete.
#
#                       Clustering: The main problem with linear probing is clustering, many consecutive elements
#                       form groups and it starts taking time to find a free slot or to search an element.
#                       let say if we have k elements which results to same hash value then k consecutive rows of
#                       hash table will be blocked.
#   b. quadratic probing: quadratic probing is similar to linear probing. only difference is
#                          here we will increment i by 1 and then square it.
#                          so rehash formula will look like this (n+(i^2))%(table_size)
#                          this algo also has clusterting issue but instead of taking consecutive rows it blocks i^2
#                          rows which saves our time to find free slot for different elements.which is slightly better.
#
#                           Now there is one more problem with quadratic probing,that even if we have free slot.
#                           sometimes we are not able to find free slot as we are moving quadratically.
#                           but there is an observation, whenever table size is prime number then only it will be
#                           guarantee to insert elements as long as any free slot available at any position.
#   c. double hashing: We use another hash function hash2(x).
#                       So rehash formula will look like this  (hash(x) + i*hash2(x)) % table_size
#                       here i is slot search attempt number.
#                       here first hash function would be like x%table_size
#                       second hash function would be y -or+ (x%y).
#                       here we are doing plus or minus with y because we don't want result of second hash function .
#                       to be 0. otherwise we will be keep traversing on the same row again and again.
#                       and here y could be any number which is co-prime with table_size.
#                       for example if table size is 7 then y could be 6. if we go with subtraction.
#                        then formula will look like
#                         ( (x%7) + 6-(x%6) ) %7.
#                       So table size should be prime and y should be a co-prime number of table_size. then only
#                       above hash function will consider all the rows. otherwise sometimes we will not be able to
#                       find empty row even if empty row is available.


# Load factor in open addressing:
# m = Number of slots in the hash table
# n = Number of keys to be inserted in the hash table
#  Load factor α = n/m  ( < 1 )
# it should be always less than 1 because number of slots will always be greater than the keys to be inserted.
# otherwise we will not be able to insert extra keys.

# so let say load factor is 0.8 for some arrangement. that means hash table is 80% full and 20% rows are empty.
# now in ideal scenario double hashing will uniformly distribute collision keys within hash table.
# that means avg unsuccessful search time (worst case; when element does not exists in hash table )  for above
# arrangement will be 5 traversal. because 20% free means every 1/5 th row is free. so on 4 traversal we will find
# booked rows and on every fifth traversal we will find free row
# for 0.9 load factor we will find empty row at 10th traversal. and as we know our search stops whenever we find empty
# row (not deleted) or same original hash row.

# so this observation leads to this formula  => 1/(1-α)
# So Search, Insert and Delete take (1/(1 – α)) time


# Comparison of above three:
# 1.Linear probing has the best cache performance but it suffers from clustering. One more advantage
# of Linear probing that it is easy to compute.
# 2. Quadratic probing lies between the two in terms of cache performance and clustering.
# 3. Double hashing has poor cache performance but no clustering. Double hashing requires more computation
# time as two hash functions need to be computed.

# Chaining vs Open Addressing
# 1.	Chaining is Simpler to implement. Open Addressing requires more computation.
# 2.	In chaining, Hash table never fills up, we can always add more elements to chain. In open addressing, table
#       may become full.
# 3.	Chaining is Less sensitive to the hash function or load factors.
#       Open addressing requires extra care to avoid clustering and load factor.
# 4.	Chaining is mostly used when it is unknown how many and how frequently keys may be inserted or deleted.
#       Open addressing is used when the frequency and number of keys is known.
# 5.	Cache performance of chaining is not good as keys are stored using linked list.
#       Open addressing provides better cache performance as everything is stored in the same table.
# 6.	Wastage of Space (Some Parts of hash table in chaining are never used).
#       In Open addressing, a slot can be used even if an input doesn’t map to it.
# 7.	Chaining uses extra space for links.	No links in Open addressing.


## Union of two lists:
# simply add both lists data into new set. it will result in union

## intersection:
# first add list A data into new set. then traverse B list items and whichever item of B
# exists in new A set we will print that.

## Return pair whose sum is equal to k in unsorted array:
# we create a new empty set and traverse original array
# if k-current_element not exists in new set then we will add current_element in new set
# else we return true.
# def find_pair_for_k(data, k):
#     new_set = set()
#     for i in data:
#         if k-i in new_set:
#          # we are checking if complement exists in elements added so far.
#             return i, k-i
#         else:
#             new_set.add(i)
#     else:
#         return -1


## Check if any subset returns sum as 0 in unorderded list.
def find_pair_for_k(data):
    new_set = set()
    prefix_sum = 0
    for i in data:
        prefix_sum+=i
        # if current prefix sum is equal to prefix sum we have seen earlier, then that means sum of elements which
        # lies between these same prefix sum must be 0.
        # for example: [1,2,3,-4,1,-3,4]
        # so prefix sum will look like this  [1,3,6,2,3,0,4]
        # so as you notice here prefix sum 3 occurs 2 times one element 2 at 1st index and another for element 1 at
        # 4th index. so that means sum from 2nd index to 4th index is 0.
        # also we can 0 on the 5th index that means sum from 0th to fifth index is also 0.
        if prefix_sum in new_set:
            return True
        if prefix_sum == 0:
            return True
        new_set.add(prefix_sum)

## Check if any subset returns sum as k in unorderded list.
# logic will be same as above but instead of checking if current prefix sum exists in old prefix sum
# we will check if current_prefix_sum-required_sum exists in previous prefix sum or not.
#     new_set = set()
#     prefix_sum = 0
#     for i in data:
#         prefix_sum+=i
#         # we are checking if its pair exists in previous sums, whose sum equal to required sum.
#         if prefix_sum-required_sum in new_set:
#             return True
#         if prefix_sum == required_sum:
#             return True
#         new_set.add(prefix_sum)


## Longest subarray with given sum
# logic is same as above only thing extra will be, we will count the length of subarray and the return the max one
#     def lenOfLongSubarr(self, arr, n, k):
#
#         result = 0
#         temp_sum = 0
#         # this will contains prefix sum as key and index number as value.
#         sub_aar_sum = dict()
#         for i in range(n):
#             temp_sum += arr[i]
#               # if complement found in dict then we will find its index from sub_arr_dict
#             if temp_sum - k in sub_aar_sum:
#                 # calculate length of subarr by subtracting current index with complement prefix sum element index.
#                 result = max(result, i - sub_aar_sum[temp_sum - k])
#             if temp_sum == k:
#             # if prefix sum so far is equal to k then we will simply do i+1,as index start from 0.
#             # so i+1 will result number of elements.
#                 result = i + 1
#             # if prefix_sum already exists in sub_arr_sum then that means previously we have seen similar prefix sum
#             # so in that case we will not update sub_arr_sum, because we wanted longest subarray. as pervious
#             # value of i and current value of i results in same sum. so we can start array from previous value i, as
#             # it will not change in sum.
#             if temp_sum not in sub_aar_sum:
#                 sub_aar_sum[temp_sum] = i
#         return result

## Longest subarray with same number of 0s and 1s
# for example [1,1,0,0,1,1,0] so answer will be 6 -> [1,0,0,1,1,0] here 3 0s and 3 1s
# idea is simple, we will first replace all 0 with -1 and then we will use code to find longest subarray
# whose sum is equal to k where k will be 0 this time.


## Check longest subarray in 2 binary arrays whose sum is equal
# example: a=[1,0,0,1,1,0]; b = [0,0,1,0,0,1]; so answer would be 5 and sum would be 2 which is [0,0,1,1,0] from A and
# [0,1,0,0,1] from B.
# here subarray will be common which means starting and ending of both subbarys should be same.
# so naive solution is to generate all subsets of both arrays with same start and ending indiceis and check the max sum.
# for i in range(len_of a or b):
#   sum1=0; sum2=0
#   for j in range(i,len_of a or b):
#       sum1+=a[j]
#       sum2+=b[j]
#      if sum1==sum2:
#          result = max(max, j-i+1)

# Efficient solution will be to create a new array C which is result of A-B array elements.
# now we can simply use `longest subarray whose sum equal to 0` logic.
# because when both array has 0 or 1 then c will also contains 0. so this will not impact our prefix sum
# but when either A or B has 1 and other array has 0 then it effect our sum. So in this case
# C will have weather 1 or -1. so we have to find same number of 1s and -1s to make result 0.

## Longest consecutive subsequence
# Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are
# consecutive integers, the consecutive numbers can be in any order.
# for example: [4,8,9,1,3,2] -> output will be [4,1,3,2] as it contains consecutive elements.
# consecutive are : i, i+1, i+2 ...
# and subsequence elements will be in same sequence but we can skip elements in the middle. example: [1,4,3] -> [1,3]
# can be one.
# naive approach will be to sort the array and then traverse from left to right to find the length of max consecutive
# elements.
# efficient approach is discussed below:
# idea is simple we will insert list data int set, then we traverse element from list one by one.
# for that particular element we will move in left and right direction and check if that element exists in set or not.
# for example in list [2,1,4,5,3]. if i is 2 then we will check if 1 is there in set or not. if we found 1 then we will
# check for 0 and so on. we move on left side till we found starting of sequence.
# similarly we will move on right side till we reach to 5 (last element of sequence).
# and while traversing elements we will remove them from set, to avoid traversing same sequence again.
#     def longestConsecutive(self, nums: List[int]) -> int:
#         h_map = set(nums)
#         res = 0
#         # we will pick one value and move in left and right direction
#         for i in nums:
#             if i not in h_map:
#                 # it means i is already traversed and removed from h_map
#                 continue
#             h_map.remove(i)
#             count = 1
#             left = i - 1
#             right = i + 1
#             while left in h_map:
#                 h_map.remove(left)
#                 left -= 1
#                 count += 1
#             while right in h_map:
#                 h_map.remove(right)
#                 right += 1
#                 count += 1
#
#             res = max(res, count)
#
#             # if hmap is empty then there is no need to continue the loop.
#             if not h_map:
#                 break
#         return res


## Count distinct element in every windows of size k
# for example: [1,3,1,2,4,5,6,5]; k=3
# so first window will be [1,3,1] and size of distinct elements will be 2
# second window will be [3,1,2] and size will be 3
# similarly last window will be [5,6,5] and size will be 3.

# it naive solution will be to use set for each window to find distinct element size.
# but its time complexity will be O((n-K)*k). because for each window we will be creating new set of size k.
# and there will be n-k windows.

# efficient solution will be to use a dict to count freq of all elements in a window
# and whenever we move our window we will decrease frequency of first element(element which is going to be removed
# from window) or remove it from freq dict if freq become zero.
# and increase freq or add new element(which is going to be addded in new window.) in freq dict
# for example [1,2,1,3] for k=3.
# in first window our freq dict will look like {1:2, 2:1}
# and in next window freq dict will be {1:1, 2:1, 3:1}. freq of 1 is reduced and 3 is added into dict.

def distinct_counter_in_k_size_window(data,k):
    d = {}

    # creating initial map
    for i in data[0:k]: # O(k)
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    print(len(d))
    for i in range(1, len(data)-k+1): #O(n-k)
        # removing previous data
        d[data[i-1]] -= 1
        # if freq becomes 0 then removing it from dict.
        if d[data[i-1]] == 0:
            d.pop(data[i-1])

        if data[i+k-1] in d:
            d[data[i+k-1]]+=1
        else:
            d[data[i + k - 1]] = 1

        print(len(d))


# time complexity is O(n) and space is O(k)
distinct_counter_in_k_size_window([1,2,1,3,3,4,5], 3)

