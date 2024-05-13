# worst -> O(nlogn)
# average -> theta(nlogn)
# auxilary space -> n

# it is stable but not in-place algo it uses O(n) space for sorting.
# also in general it is slower tha quicksort.

# well in array memory allocation is contigues, which helps us to access random index elements at o(1) time complexity.
# but this is not true for linked list. due to this reason quick sort is only preferred for arrays.
# and merge sort is preferred for linkedlist. also merge sort with linked list does not take extra O(n) space.
# As, unlike arrays, in linked lists, we can insert items in the middle in O(1) extra space and O(1) time if we are
# given a reference/pointer to the previous node. Therefore, we can implement the merge operation in the merge
# sort without using extra space.

# It is useful for external sorting. For massive arrays, where the full array
# doesn't fit in a single page of memory, this means that you can load a small subset of the array into memory,
# sort it, switch to another subset, sort it, etc.
# The merge sort algorithm can be easily parallelized, which means it can take advantage of multiple
# processors or cores to sort the data more quickly.

# divide and conquer
# first divide array into sub array till length of arr become 1.
# while merging do sorting
# while merging start comparing from first element of each sub list


def merging(l,r,data):
    # when first this function is called at that time data will break into some smaller array. which is combination of
    # l and r subarrays. for example input: [4,3,2,1]. when l=4 and r = 3 then data will be [4,3].
    # as list is passed by reference in python. so we don't have to return anything in ths function.
    # the previous sort who called merge by passing data as 4,3 input will be modified to 3,4.

    i = j = t = 0
    # sort and merge
    while i < len(l) and j < len(r):
        # we will append whatever is smaller
        if l[i] < r[j]:
            data[t] = l[i]
            i += 1
        else:
            data[t] = r[j]
            j += 1
        t += 1
    # adding remaining elements
    while i < len(l):
        data[t] = l[i]
        i += 1
        t += 1
    while j < len(r):
        data[t] = r[j]
        j += 1
        t += 1


def sorting(data):
    # when l and r hae one-one element then this recursion will return and l and r array with one element to above
    # caller stack.
    # then that above function will sort those and return new updated l and r to its above caller stack ad so on.
    if len(data)>1:
    # divide
        mid = len(data)//2
        r = data[mid:]
        l = data[:mid]
        # get the sored left array
        sorting(l)
        # get the right sorted array
        sorting(r)
        merging(l,r,data)


x = [1, 2, 5, 1, -4, 9, 3]
sorting(x)
print(x)
y = [1, 2, 5, 1, -4, 9]
sorting(y)
print(y)



## Sort a array who is partially sorted.
# for example we have an array [1,3,5,7,2,4,8]
# we have given a index k, where values left side of k are sorted and values
# right of k are sorted. like in above example k is 4.
# now we have to sort complete array.

# to solve this in O(n) time and space complexity
# first we will store left and right half of array into different small arrays
# then remaining algo is similar as merge to sorted array.
# where we traverse both arrays from left to right and whatever element is lower we will
# add that into original array.
# this similar logic is also foundation of merge sort.

# def sort_partially_sorted_array(data, k):
#     left = data[0:k+1]
#     right = data[k+1:]
#     i = 0
#     j = 0
#     counter = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             data[counter] = left[i]
#             i += 1
#         else:
#             data[counter] = right[j]
#             j += 1
#         counter += 1
#     # now for remaining elements we will add the into list.
#
#     while i< len(left):
#         data[counter] = left[i]
#         i += 1
#         counter += 1
#
#     while j< len(right):
#         data[counter] = right[j]
#         j += 1
#         counter += 1
#
#     print(data)
#
# sort_partially_sorted_array([1,3,5,7,2,4,6,8], 3)

# Print union of 2 sorted array. i.e print unique element in both arrays
# for example: a = 1,2,2,3,4,4 b= 2,3,3,4,5; output = 1,2,3,4,5
# we will use same function which we used to merge 2 sorted arrays (merge function of merge sort algo).
# now in this case only difference is we will add new equality conditions.
# whenever left[i] == right[j] then we will print element once and increment both i and j.
# and whenever i or j same as its previous element then we will increment i or j respectively and then `continue`
# in loop without printing anything.

# Print intersection of 2 sorted array.
#  a = 1,2,2,3; b= 2,3,4,5; output = 2,3
# its code is also similar to merge function, only difference is in case of > or < we will just increment i and j
# indices respectively. and in case element is equal in both array then we will print it.
# and if current element is same as prev then we will skip current element by incrementing i or j pointer respectively,
# instead of printing it.

## Count Inversions in a array.
# here if i< j and data[i]> data[j] then it is inversion pair.
# example: 2,8,3; so here 8,3 is one pair.

# here again we will use merge sort algo. while sorting we will count pairs.
# data = 4,3,1,5

# 4,3,1,5
# /    \
# 4,3   1,5
#  |   |  |  |
#   4   3  1  5

# so while merging on first iteration we will get 4 on left side and 3 on right side.
# then we will first sort it and as 4 > 3 so we add 1 pair to count.
# on 1,4, as it is already sorted so here pair count is 0.
# next we will get 3,4 on left side and 1,5 on right side.
# when we will traverse elements one by one in both array, we will get 3 from left side and 1 from right side.
# now 3>1. but as we know both left and right side array already sorted so all elements on left array after 3
# will be greater than 1. so here we will increment result count by len(left)-current_element_index.
# next time when we at 5 from right side, as it is greater than both 3 and 4 then we will skip the count.


def sort_and_count(data, l, r):
    i = 0
    j = 0
    t = 0
    res = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:

            data[t] = l[i]
            i += 1
        else:
            res += len(l) - i
            data[t] = r[j]
            j += 1

        t += 1
    while i < len(l):
        data[t] = l[i]
        i += 1
        t += 1
    while j < len(r):
        data[t] = r[j]
        j += 1
        t += 1

    return res


def count_pairs(data):
    res = 0
    if len(data) > 1:
        l = data[0: len(data) // 2]
        r = data[len(data) // 2:]

        # result from previous sub arrays
        res += count_pairs(l)
        res += count_pairs(r)

        # result after merging and sorting of l and r part.
        res += sort_and_count(data, l, r)

    return res


print(count_pairs([8, 4, 2, 1]))