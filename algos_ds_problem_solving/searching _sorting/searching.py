  # complexity best -> o(1) and worst -> O(log(n))

def bin_search(data, x, f, l):
    mid = f + (l-f)//2
    if f > l:
        return -1
    if x == data[mid]:
        return mid
    elif data[mid] > x:
        return bin_search(data, x, f, mid-1)
    elif data[mid]< x:
        return bin_search(data, x, mid+1, l)


x = [1, 2, 3, 4, 5, 6,  7, 8, 9]
print(bin_search(x, 8, 0, 8))
print(bin_search(x, 12, 0, 8))
print(bin_search(x, 2, 0, 8))


## ternary search
# here we divide list into 3 part
# four points will be l ... mid1 ... mid2 ... r
# part one from l to mid1, part 2 from mid1 to mid2 and part3 from mid2 to r
# to calculate mid1 and mid2
# mid1 = l+(r-l)//3 # adding one-third part to left side
# mid2 = r-(r-l)//3 # removing one-third part from right side.

# algo is simple, first we check if elem present at mid1 or mid2.
# if not then we check if elem is less than mid1
# if it is then it means it lies between l and mid1

# otherwise we will check if elem is greater than mid2 elem
# if it is then it means elem lies in mid2 and r range.

# otherwise elem present between mid1 and mid2

# def t_search(data, x):
#
#     l = 0
#     r = len(data)-1
#
#     while (l<=r):
#         mid1 = l + (r - l) // 3
#         mid2 = r - (r - l) // 3
#         if x == data[mid1]:
#             return mid1
#         elif x == data[mid2]:
#             return mid2
#         elif x < data[mid1]:
#             r = mid1 - 1
#         elif x > data[mid2]:
#             l = mid2 + 1
#         else:
#             l = mid1+1
#             r = mid2-1
#
#     return -1



## find first and last occurance using binary search in sorted array:

# for last occurance, first part of code will remain same as binary search only below condition will be added:
# if arr[mid]>x:
# elif arr[mid]<x:
# # above is binary search code and below is new condition
# elif mid==n-1 || arr[mid] != arr[mid+1]:
#  # this condition means that, if we found the element at mid index and if mid index is last item or item after mid
#  # element is different than current element, that means we found our element last occurance.
#     return mid
# else:
# #else we will remove current element from our search range by doing f=mid+1
#     f = mid+1

# similarly for first occurrence
# elif mid == 0 || arr[mid] != arr[mid-1]:
# return mid
# else:
# l = mid-1

# note: In competitive programming we can use bisect lib instead of rewriting binarysearch
        # bisect.bisect_left() will give left most index in sorted list where we can place x and
        # list will be sorted after inserting x at index i.
        # a = [1, 3, 5, 6, 7, 9, 10, 12, 14]
        # x = 8
        # i = bisect.bisect_left(a, x, lo=2, hi=7) # [5, 6, 7, 9, 10] # now it will find index in given lo hi range only.
        # print(i)
        # output-> 5
        # similarly bisect_right will give right most index.


## binary search problems:
# 1. to find first occrance of 1 in sorted array of 0 and 1.
# 2. number of occrances in sorted list: using binary search find first and last occurance of each element.
#   then do last_occurance_index - first_ccurance_index + 1 to find freq. and repeat it for all elements.
# 3. find sqrt: initial values will be l=0 and r = x//2 (sqrt of number can not be greater than its half value,
#    1 is exception case) and do bin search to find element.
# 4. to find a peak element. peak element is elem whose neighbours elem are smaller than it.
# for example: [50, 2, 45, 3,1,23]
# here 50, 45 and 23 are peak elements.
# again we use binary search.

# first we find mid element = l+r//2

# if mid elem is greater than both mid-1 and mid+1 elem then we return this as peak elem.

# or if mid+1 is greater than mid elem then a peak element lies in right side of list.
# (but why it that so, let's understand it with different scenarios:
# if mid+1 is corner element then it is peak element.
# if mid+2 is less than mid+1 element then again mid+1 is peak element.
# if mid+2 is greater than mid+1 element then in that case we have again same condition for
# mid+2 which we had for mid+1. [like if mid+2 is corner elem then it is peak, and so on.])

# or if mid-1 is greater than mid elem then a peak element lies in left side of list.(same reason for right side.)



## Find number of elements greater than k in sorted array
def bin_search_for_first_max(data, x):
    if x >= data[-1]:
        return -1
    l = 0
    r = len(data)-1
    current_max = 0
    while l<=r:
        mid = (l+r) // 2

        if data[mid] <= x: # anything in this range will not be our result
            l = mid+1

        else:
            r = mid-1
            current_max = mid # index  of greater element found so far

    # current_max is index for first elements which is greater than x in sorted array.
    return len(data) - current_max



## in infinite array:
# keep multiplying index by 2 until elem <= item[index]
# then in case of elem < item[index], do binary search with start_index as index/2+1 (as we already knew
# item[index/2] < element) and end_index as index

def find_in_infinite_sized_arr(x, arr):
    # first find the index where elem is greater than our elem, that greater ele will be last ndex for our binary search
    if arr[0] == x:
        return 0
    i = 1
    while arr[i]< x:

        i*=2
    if arr[i] == x:
        return i

    return bin_search(arr, x, i//2, i-1)


## find elem in sorted rotated array
# like 30, 40, 50, 60, 1, 2, 3 is sorted rotated array here 3 rotations is done, due to which 1, 2 and 3 came at last.
# well in rotated sorted array one half form any point is always be sorted. using this idea we can solve this problem.
# for example in above list if we randomly pick element let say 40 so notice its left side is sorted.
# similarly if we pick 60, again its left side is sorted and for 2 its right side is sorted. So always, in rotated array
# one side for each element will be sorted.

#def find_in_r_arr(data, x):
    # f = 0
    # l = len(data)-1
    # while f<=l:
    #     mean = (l+f)//2
    #
    #     if x == data[mean]:
    #         return mean
    #     elif data[mean] >= data[f]:
    #         # left half is sorted, we will look for data here.
    #         if x < data[mean] and x >= data[f]:
    #             # that means x preset in left half range
    #             l = mean-1
    #         else:
    #             # otherwise it present in unsorted right half
    #             f = mean+1
    #
    #     else:
    #         # right half is sorted, we will look for data here.
    #         if x > data[mean] and x <= data[l]:
    #             # that means x preset in right half range
    #             f = mean + 1
    #         else:
    #             # otherwise it present in unsorted left half
    #             l = mean - 1
    # return -1


## find starting point or minimum in rotated sorted array
    # def findMin(self, nums: List[int]) -> int:
    #     # for rotated array, for any random element either left or right half is always sorted.
    #     f = 0
    #     l = len(nums) - 1
    #     # handling edge case when list already sorted
    #     mid = (f + l) // 2
    #     if nums[0] < nums[-1]:
    #         return nums[0]
    #
    #     while f < l:
    #         # if both neighbours elements are greater, then it means we found starting point of list.
    #         if nums[mid - 1] > nums[mid] and nums[mid + 1] > nums[mid]:
    #             return nums[mid]
    #
    #         if nums[l] < nums[mid]:
    #             # as we already know list is rotated, so smallest item is deifnitely not first item
    #             # and if left half is sorted, then it means smaller item exists on right side.
    #             f = mid + 1
    #         else:
    #             # if right half is sorted, then it means right half only contains greater elements,
    #             #  so we move towards left.
    #             l = mid - 1
    #         mid = (f + l) // 2
    #
    #     return nums[mid]


## find 2 numbers whose sum equal to k, in sorted array.
# here we will use 2 pointer approach first pointer start with 0 index and second will start from last index. and
# both these pointers will move towards each other and find pair.
# algo :
# p1, p2 = 0, len(arr)-1
# while p1 <= p2:
    # x = arr[p1]+ arr[p2]
    # if x > k:
        #p2-=1
    # elif x<k:
        #p1+=1
    # else return p1 and p2


## find 3 numbers whose sum equal to k in sorted array:
# here we will run a loop from 0 to n-1
# now for each number arr[i],  we try to find 2 number pairs in remaining list, whose sum equal to k-arr[i]
# to do so we again use 2 pointer approach.
# we run 2 pointer function, for each number where first pointer will be i+1 and last pointer will be len(arr)-1
# notice we start 2 pointer from i+1 as elements before i is already covered in previous iteration.
# algo:
# for i in range(len(arr)):
#     x = k - arr[i]
#     pair1, pair2 = find_two_pairs(data=arr, first_pointer=i+1, required_sum=x)
#     # find_two_pairs code is same which we discussed in 'find 2 number' problem


##### range checks ###
# if we have 2 ranges of fucntions and we have to find how they are overlapping
# then we can use below approach

# example -> range1 (20 to 40) and range2 (30 to 60)

# condition1 -> range1[0]<=range2[1] and range2[0]<=range1[1]
# this means range1 and range2 is overlapping. otherwise there is no overlapping.

# now to check how much they overlapped we check below condition:

# if range1[0] < range2[0] and range1[1] < range2[1]
# this means right half of range1 is overlapping left half of range2
# for above example this condition will be true

# elif range1[0] > range2[0] and range1[1] > range2[1]
# this means left half of range is overlapping with right half of range2
# example : range1(20 to 40) and range(10 to 30)

# elif range1[0]>= range2[0] and range1[1]<= range2[1]
# example -> range1(20-30) range2(10-40)
# range1 lies inside range2

# else range2 lies inside range1

## Inequality condition always returns range for x, instead of single value.
# for example
# 2x^2 + 5x + 10 >= 7
# to find values of x which results >=7 we will first move 7 to left side and make right side to 0
# 2x^2 + 5x +3 >=0
# now it looks like ax^2 + bx+ c = 0 quadratic equation which can be soled using.
# x = (-b ± √D)/2a, where D = b2 – 4ac
# now this will result 2 values which will be edge points, around those values
# our equation will change direction. for example if above equation returns 3,6 for x.
# then for x below 3 we will get results <7 and for value greater than 6 we will again get results less than 7.
# if above formula gives only one value for x then we have to find out by putting x-1 and x+1 as
# input, whether equation results >7 or < 7, using that we will decide in which direction we have to
# ether 3 to -infinity or 3 to + infinity.

## To find if a point lies inside closed loop or a polygon. we can use ray tracing alog.
# in ray tracing algo we draw a straight line from given point to any single direction.
# now we check if our straight line intersect polygon odd numbers of times then point lies inside polygon else
# it lies outside of polygon.
# in this algo If we are drawing horizontal line form point, then we will ignore all horizontal
# intersections with polygon which will overlap with our line. we will only consider vertical lines
# intersection of polygon. but for more complex shapes, which overlaps with itself, this algo will give incorrect results.
# in that case we will use winding number algo. where we represent direction of each egge in polygon.
# now again we draw a horizontal line like ray tracing.
# if the edge crosses the ray going "upwards", the winding number is incremented;
# if it crosses the ray "downwards", the number is decremented.
# A winding number of 0 means the point is outside the polygon; other values indicate the point is inside the polygon.
# check https://en.wikipedia.org/wiki/Point_in_polygon#:~:text=of%20the%20algorithm.-,Winding%20number%20algorithm,as%20the%20nonzero%2Drule%20algorithm.
# to understand better.




## Find median of 2 sorted array
# 1.  We know that median will always be at  (m+n+1 //2) index  for merged list and
#     if m+n is even then two medians will be (m+n+1)//2 and ((m+n+1)//2 +1) position
# 2.  Also we know that elements in left side of median will be lower in both lists and similarly
#     right side will be greater.

# using above 2 ideas we will generate  equations:
# 1. median_index_in_a + median_index_in_b = (len(a)+len(b))//2
# => median_index_in_a = (len(a)+len(b))//2 - median_index_in_b
# here median_index_in_b or median_index_in_a will be consecutive elements if both lists merged, so either of these
# can be our median, so to decide that we will take max elem out of these 2.
# 2. left_side_of_median_index_in_b < median_index_in_a and left_side_of_median_index_in_b < median_index_in_b
# now we will se binary search to find median_index_in_a and median_index_in_b will be calculated accordingly.

a = [2, 3, 5, 8,25, 24]
b = [10, 12, 14, 16, 18, 20]
def find_median(x,y):

    x, y = (x, y) if len(x) < len(y) else (y, x)
    # we will do binary search on smaller array to find result faster.
    start = 0
    end = len(x)-1
    median_pos = (len(x)+len(y)+1) // 2
    while start <= end:
        x_idx = (start + end + 1) // 2
        # as x index start from 0, so we are adding 1 to make its index start from 1.
        # as while calculating median_pos, we considered list whose index start from 1.
        x_idx += 1
        y_idx = median_pos - x_idx

        # doing -1 as index in python start from 0
        x_idx -= 1
        y_idx -= 1

        x_left = x[x_idx] if x_idx >-1 else float('-inf')
        y_left = y[y_idx] if y_idx >-1 else float('-inf')
        x_right = x[x_idx+1] if x_idx!=len(x)-1 else float('inf')
        y_right = y[y_idx+1] if y_idx!=len(y)-1 else float('inf')

        if x_left <= y_right and y_left <= x_right:
            t = len(x)+len(y)
            if t % 2 == 0:
                return (max(x_left, y_left) + min(x_right, y_right)) / 2
            else:
                return max(x_left, y_left)

        if x_left > y_right:
            end = x_idx-1
        else:
            start = x_idx+1

print(find_median(a,b))


## Find number in a list who is repeated most of the time.
# and our list contains  numbers only 0 to n-1 numbers, where n is size of array.
# for example: [1,2,3,2,6]; this list is illegal as it contains 6 which is greater 4 (which is n-1).
# also we have to do it in O(n) time complexity with O(1) space complexity.
# also our array is mutable but we have to keep original values in it.
data = [4,4,4,4,1,2,3,5,0,3,1,3, 5,5,5,5,5,5,5]

# 1. as elements will never be greater than n-1, so we can add any multiple of n to any element in list.
# because using  %n operation we can easily retrieve original value.
# 2. also as elements only lies within 0 to n-1, so can easily represent element as index.

# so using this trick we will add n to data[element], whenever element is traversed and whatever index
# has max multiple of n i.e data[element]//n. that index will be our answer.


def find_max(data):
    res = -1
    index = 0
    max_item = -1
    while index< len(data):
        temp_data = data[index]
        temp_data %= len(data) # retrieving original value, so that we can use it as index.
        data[temp_data] += len(data) # adding length, whenever current elements is traversed.

        if data[temp_data] // len(data) > max_item:
            res = temp_data  # updating value
            max_item = data[temp_data] // len(data) # updating max multiple of n, seen as of now.

        index += 1

    # not to retrieve original array just do %n operation for all elements. I am not doing it here,
    # as it is not required as of now.

    return res

print(find_max(data))


## Find repeated number in a mutable list.
# and our list contains  numbers only 0 to n-1 numbers, where n is size of array and only one number will
# be having duplicates.
# for example: [1,2,3,2,6]; this list is illegal as it contains 6 which is greater 4 (which is n-1).
# [1,2,3,2,3] this is also illegal as it contains multiple repeated elements.
# also we have to do it in O(n) time complexity with O(1) space complexity.

data = [1,3,2,3,4,3,0,0,0]
# we can use similar approach as we used in previous problem.
# but to simplify it, instead of adding len(n) at data[element], we will just multiply data[element] with -1 whenever
# it accessed.
def find_repeated_elem(data):
     i=0
     while i < len(data):

         # because 0 mutiplied with -1 will result 0, so we have to change it to something else.
         # that why we are replacing it with len(n) and later doing mod to find the correct value which is 0.
         if data[i] == 0:
             data[i] = len(data)
         temp = abs(data[i]%len(data))
         # negative means already accessed, as our array only contains 0 to n-1
         if data[temp]<0:
             return temp
         data[temp] *= -1
         i+=1

print(find_repeated_elem(data))


## Find repeated number in a non-mutable list.
# array size will always be n>=2
# only one element will repeat any number of times.
# all the elements from 0 to max(arr) will be present, i.e if 4 is max item in current array,
# then 0,1,2,3 has to present in array.
# therefore 0<=max(arr)<=n-2
# for example: [1,2,3,2,6]; this list is illegal as it contains 6 which is greater 3 (which is n-2).
# [1,2,3,2,3] this is also illegal as it contains multiple repeated elements.
# also we have to do it in O(n) time complexity with O(1) space complexity.

data = [0, 1, 3, 2, 4, 3]
# As here we can not modify the list, So we will follow different approach.
# Here we will jump from one element to another using -> current_element = data[current_element]
# basically we will use current element as index to fetch next element.
# array which has duplicates will certainly have loop, if we traverse it using above approach.
# now to find loop we will simply floyd's cycle finding algo.
# for example:
# data = [1,2,3,4,5,6,7,3]
# 1 -> 2 -> 3 -> 4 -> 5
#           |         |
#            <-7<- 6 <-

# to find where loop start we will divide algo in 2 phase.
# phase 1: we will move 2 pointers, slow and fast pointer. fast pointer will move at 2x speed.
#           and we will run this loop till slow and fast pointer matches.
# phase 2: now we will make one the pointer at data[0]. and then move both pointer as same speed, till slow and fast
#          pointer become same again.

# please find detailed explanation of floyds loop detection algo in one-notes.

def find_repeated_elem(data):
    slow = 0
    fast = 0
    while True:
        # note: we could have simply traversed array using slow = data[slow]. but here if you noticed
        # we did +1 to result. we did so to avoid self loops.
        # if we take example of 0,1,2,3,3 list. then slow =data[slow] will stuck on 0 only as data[0] is also 0
        # in given list. same goes for fast pointer, that also stuck in 0 only.so to avoid this we are doing +1
        slow = data[slow]+1
        fast = data[data[fast]+1]+1

        if slow == fast:
            break

    fast = 0
    while True:
        slow = data[slow]+1
        fast = data[fast]+1

        if fast == slow:
            # doing -1 to get original values of fast pointer
            return fast-1

print(find_repeated_elem(data))



## Allocate minimum pages:
# basically we have to find minimum possible maximum pages allocated to k students.
# also pages allocation should be continues.
# for example: [10,20,30, 40],  k=2
# so possible allocations are 10 and (90) 20+30+40; so here max allocation is 90
# next is 30, 70 ; here max is 70
# 60, 40; here max is 60
# here allocations should be contigues, so 10 and 30 & 20 and 40 pair is not possible.
# so minimum of max in above three arrangements is 60.

# naive approach is to create all possible pairs and minimum values there.
data = [10,20,30,40]
def find_all(data, n, k):

    if k==1:
        # this mean only 1 partition is remaining, so we are returning sum of remaining elements
        return sum(data[0:n])
    if n == 1:
        # this means only 1 element is remaining and other n-1 elements are already allocated.
        return data[0]

    res = float('inf')
    for i in range(1, n):
        # so here basically we make partition at every position possible.
        # like in first itertation we did sum of 1-n elements and in second we did sum for 2-n and so on.
        # and for remaining we just called find_all() to find sum recursively.
        temp = max(find_all(data, i, k-1), sum(data[i:n]))

        # above recursion will not do partition exactly k times, instead t will do partition k or less than k times.
        # like if we take example of first iteration. it will always do 2 partition only ( 0 and 1 to n-1 elements),
        # regardless of k.
        # but this is fine as lower values of partition will result in higher maximum, which will be filtered
        # out in below condition.

        res = min(res, temp)

    return res
# print(find_all(data, len(data), 2))

## In second optimized approach we will use binary search
# AS we know the largest answer we can get when k is 1 and lowest answer is when k==n
# because when k is 1 then we have to sum all the pages and when k==n then each student will get 1 page
# so maximum number in given list will be the answer.
# for example : [10,20,30] for k=1; result would be 60 and for k=3 result would be max of (10,20,30) which is 30.
# so now we know our result will lies between 30 and 60, regardless of k.
# as we know whenever we have to find a value between upper and lower bound we can imply use binary search.
# now we start from 30 and move towards 60 till we find a value, which is max of an arrangement, where
# that arrangement can be divided into k parts.
# for example [10,20,30,40] k=3; min is 40 and max is 100. so one value could be 50, because 50
# is part of an arrangement (10 | 20,30 | 40 ) which can be divide into 3 parts. and also 50 lies between 40 and 100.
# but 51 is not, as none of the arrangement can result max as 51. also 60 is not possible as, (10,20,30|40)
# this arrangement can be divide int 2 parts only.
# we will return or result once we find first minimum satisfying max number.


# so first function is to check if current arrangement is valid or not.
def is_arrangement_valid(data, max_number):
    sum_list = []
    temp = 0
    for i in data:

        # adding sum till temp_sum it is less than max_number
        if i+temp <= max_number:
            temp += i
        else:
            sum_list.append(temp)
            temp = i
    else:
        sum_list.append(temp)

    return len(sum_list)


def find_max_number(data, k):
    if len(data) < k:
        return -1
    max_possible_result = sum(data)
    min_possible_result = max(data)

    result = float('inf')
    while max_possible_result>=min_possible_result:
        mid_value = (min_possible_result + max_possible_result) // 2
        temp = is_arrangement_valid(data, mid_value)
        if temp <= k:
            # update the result we found so far, as there could be multiple arrangements possible so we have to find min
            # possible ,so we move pointer towards left side
            result = min(mid_value, result)
            max_possible_result = mid_value -1

            # here we are considering < condition also with equal to condition.
            # as we are already checking `len(data) < k` above. so if certain arrangement can be partition into
            # less than k, then that arrangement can also be partitioned into k partitions as well.
            # as number of elements are greater than equal to k.

        # now we have to decide in which direction pointer needs to be moved, decresing or increasing.
        # as we know more partition will leads to less maximum sum and less number of partition will leads to greater
        # max sum.
        # for example: 1,2,3,4,5; k=2 => max will be 12(3+4+5) and in same list for k=4 max possible sum will be 9 (4+5)
        # this implies k is inversely proportional to max sum.
        # so if we get k from is_arrangement_valid function greater than required k then it means current max_value
        # or we can say mid_value is very low. we have to increase mid_value so that we can reach closer ot our answer.


        elif temp > k:
            min_possible_result = mid_value+1


    return result


d = [15, 10, 19, 10, 5, 18, 7]
k  = 5
print(find_max_number(d, k))



### 2 eggs n floors ###
# we have to find a threshold floor below which egg will not break, but floors above it egg will break.
# if we have only 2 eggs then we can't use bin search. as we need need log(n) attempts.
# one way to solve is start from 0th floors and move towards top floor.
# as eggs will not break in lower floors so we will get multiple attempts.
# and we will stop once egg is broken.
# but in worst case we have to traverse n floors.
# another way is to skip start from 10th floor. if egg breaks then now we have only need to scan 0-9 floors
# from bottom to top. so it will take only 10 attempts in worst case.
# if egg didn;t break then we will go to 20th floor and so on.
# but if you notice, by every increasing floor our number of attempts are increasing.

# like for first 10 floors worst case attempts will be 10.
# for 20 floors it will be 11
# for 30 it will be 12, if threshold floor is 29.  (as we first tried on 10th, then 20th, then 30th,
# if egg breaks on 30th
# then we start with 21 and will try all the way to 29th  floor)

# so if we have 1000 stores building then this number of attempts will be keep increasing.
# so to keep number of attempts constant in case of worst case scenario. we can decrease floors skipping by 1
# for every next attempt.
# for example for 1 attempt we check 10 floors, then for 2nd attempt we will skip only 9 floors, instead of 10
# then for 3rd attempt we will skip 8 floor.(so here till 3rd attempt we have covered 10+9+8=27 floors.
# so worst case scenario for this will be , if threshold exists at 26th floor. then total attempts would be
# (floors skip attempts)3+ 7(if we start from 19th(excluding) floor till 26th(including), so total attempts is
# remained constant which is 10)
# but there is a problem here as well, if we start with skipping 10 floors
# then by the time of 9th attempt we will be skipping only 1 floor for next attempts. which
# will not result in 10 attempts anymore.
# let say floors we need to initially skip is x, instead of 10.
# now for every increasing attempt we are reducing value of x by 1.
# also to avoid above mistake we have to make sure, all the values we choose to skip floors should be equal
# to number of floors.
# x+(x-1)+(x-2)+ ... + 1 = 100
# |_____________________|
# lenght of this expression will be x, as we started with x and ending with 1. so if we reduce 1, x times from x
# then only we will get 1 at the end

# so basically we have to find x, if we decrease x by 1, x times, then sum of all floors we skipped should be 100.
# using AP formula we will get 100 = x(x+1)/2
# => x will be 14 in this case.
# so for 100 floors we will get result in 14 attempts max.
