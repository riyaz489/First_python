# types of array in languages
# 1. fixed size arrays : whose sized is fixe like in C language
# 2. dynamic size array: whose size changes according to items we push in it. like list in python
# so in dynamic size arrays size increases automatically, when list of full, and it copy data from old array to
# new large array


# rotate array by d places:
# reverse first d elements and d+1 to n elements separately
# then reverse whole list
# exaple: d=2, [1,2,3,4]
# step 1: [2,1,4,3]
# step2 : [3,4,1,2]

# find numbers of leaders in list (leader is number which greater than next occuring elements in list)
# example: [1,2,6,3]
# here 6 and 3 are leaders
# soltion : traverse list from last and if current elements is greater than last leader then add is to answer


# find max dff x[j]-x[i] where as j>i
# traverse from left to right
# initialized diff as x[1]-x[0]
# inside loop:
# res = max(res,arr[j]-minvalue)
# minvalue = min(minvalue,arr[j])
# in above line we are simply updating min_values we have seen so far. and updating it in minvalue
# so that next j index items can perform subtraction from it.

# find max freq elem in given ranges
# example: range_start = [2,4] ; range_end = [4,5]
# so our ranges would be -> [2,3,4] and [4,5]
# so max occurring elem is 4, because it occurs in both ranges
# to solve this we first create a array 'freq' of size max(range_end)+2 and initialize all elem in it with 0.
# then we run loop for len(start_range):
# inside loop we will do freq[start_range[j]] +=1 and freq[end_range[j]+1] -=1
# So after this uur array will look like this[0,0,1,0,1,-1,0,-1]
# here basically we are increment freq element by 1 which present in range_start index and
# whenever range ends, at that index we are decrementing by one.
# then in next loop which we run for all elements for freq array, we will do
# freq[i] = freq[i-1]+freq[1]
# then this will give frequency of all elements.
# [0,0,1,1,2,1,0]-> here index will represent out number and values will be its frequency.
# like for 4 freq is 2 and for 6 freq is 0.


####### Matrix #####

## addition and subtraction is simple each element of both matrix will add/subtract with each other
# [1,2]   + [1,2]  = [2,4]
# [3,4]     [3,4]    [6,8]

## multiplication:
# Am*n and Bn*p gives a matrix Cm*p; where In A matrix m is number of rows and n is number of columns
# for example first element of c will be sum of multiplcation of first row elements of A and first column of B.
# for i in 1 to m
#    for j in 1 to p
#       cij = 0
#       for k in 1 to n
#          cij += aik*bkj

## Transpose : col become ros and rows become cols
# for (int i = 0; i < cols; i++) {
#   for (int j = 0; j < rows; j++) {
#       cout << matrix[j][i] << " ";
# }

## Rotate array anticlockwise 90 degree
# first do a transpose of given array.
# then make first row as last row and last row as first, similarlay second row as second last and second last as second
# and so on.

# a = [ [1,2],[3,4],]
# c=[[0,0],[0,0]]
# # transpose
# for j in range(len(a[0])):
#     for i in range(len(a)):
#         c[j][i] = a[i][j]
#
# # swap rows, make first as last and last as first.
# low=0
# high = len(a)-1
# while high>low:
#     c[low], c[high] = c[high], c[low]
#     low+=1
#     high-=1


## Spiral traversal: here we will keep 4 pointers, left, right, top, bottom
# and we start traversal from top row then increment top pointer.
# then we traverse right column elements and decrement right pointer.
# then we traverse bottom row and decrement bottom pointer and then left column and
# increment left ointer.
# and keep repeating these steps till all elements traversed.

# top = 0
# bottom = len(a)-1
# left = 0
# right = len(a[0])-1
#
# while top<=bottom and left<=right:
#     # print top elements
#     print(*a[top][left:right+1])
#     top+=1
#
#     # print right elements
#     for i in range(top, bottom+1):
#         print(a[i][right],end=' ')
#     right-=1
#     print()
#
#     # print bottom elements
#     for i in range(right,left-1,-1):
#         print(a[bottom][i], end=' ')
#     bottom-=1
#     print()
#
#     # print left items
#     for i in range(bottom, top-1, -1):
#         print(a[i][left], end=' ')
#     left+=1
#     print()


## Find element in row sorted and column sorted matrix
# idea is simple, we start traversal from top-right corner element.
# if element is equal we return result
# else if x is smaller than element then move left
# else if x is greater than element found then move bottom.
# In this algo we can choose bottom-left element as well, but rules will reverse for that.
# time complexity is O(row+column)


## Find median in row sorted array
# we simply first calculate middle position and then we will perform binary search between min and max element
# and find out which element satisfies middle position.
# To identify which element satisfies middle position we will check how many elements comes after current
# calculated middle, if our array was linear instead of 2d.
# for example [1,2,9],[4,5,8] -> [1,2,4,5,8,9] so for number 5, only 2 elements comes after, which is 8 and 9.
# so number of elements after current number should be equal to
# numbers of elements comes after middle pos.(which is middle_pos -1)
# like in above example mid is 4 so number of elements after is 3. so our calculated middle also
# satisifies this condition.
a = [
    [5,10,12],
    [1,2,3],
    [4,20,31],
]

def bin_search_for_first_max(data, x):
    if x >= data[-1]:
        return 0
    l = 0
    r = len(data)-1
    current_max = 0
    while l<=r:
        mid = (l+r) // 2
        if data[mid] <= x: # anything in this range will not be our result
            l = mid+1
        else:
            r = mid-1
            current_max = mid
    return len(data) - current_max


def find_median_in_sorted_arr(data):

    tmin = data[0][0]

    for i in data[1:]:
        t_min = min(tmin, i[0])

    t_max = data[0][1]
    for i in data[1:]:
        t_max = max(t_max, i[-1])

    total_elem = len(a)*len(a[0])
    middle_pos = ((total_elem + 1)//2)
    numbers_should_be_greater_than_middle_pos = middle_pos - 1

    # when t_min equal to t_max then we got our result
    while t_min<t_max: # O(log(max-min)) as we are doing binary search between min and max.
        mid = (t_min+t_max) // 2
        elements_after_mid = 0
        # now we need to find how many elements are larger than this calculated number.
        for i in data:   #O(rows)
            elements_after_mid+= bin_search_for_first_max(i, mid) # O(log(columns))

        if elements_after_mid > numbers_should_be_greater_than_middle_pos:
            # this means our calculated middle is too small, due to which we got more greater numbers.
            t_min = mid+1
        else:
            # we are not doing mid+1,as this mid can be our possible answer.
            t_max = mid

    # we can return anything t_min or t_max as both will be equal
    return t_min
# time complexity will be O(log(max-min)*r*log(c))

print(find_median_in_sorted_arr(a))