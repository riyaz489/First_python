# worst n2 (as in worst case selected pivot will be either smallest or largest, or our list will be divided into
# (1,n-1) elements)
# best/average nlogn (best case is when pivot occurs in middle)
# space complexity - O(n) only for recursion calls not for array.
# here we will choose a pivot (random,first or last) (random pivot is ost efficient, as it reduce chances of
# having worst case)
# then move all smaller elements than pivot value to left and greater will be on the right side
# so here we basically do  things find correct position of pivot and
# move all other greater element to right and smaller elements to left and return new pivot position

# quick sort is also divide and conqur algo like merge sort, difference is pivot function in quicksort and merge
# function in merge sort.

# this is inplace algo but not stable, as partition function change same element position.
# there is a way to make it stable using naive partition but that is not efficient and makes this algo slower.

# quick sort implementation using lomuto_partition (different partition functions are mentiond below)
def pivot(f,l,ar):
    pi = ar[l]
    i = f-1
    for j in range(f,l):
        # moving all greater element to right side of ith index
        if ar[j]< pi:
            i += 1
            ar[j], ar[i] = ar[i], ar[j]

    # swapping i th and last element
    ar[l], ar[i+1] = ar[i+1 ], ar[l]
    return i+1

def sorting(f,l,ar):
    if f<l:
        pi = pivot(f,l,ar)
        sorting(f, pi-1, ar)
        sorting(pi+1, l, ar)

# similarly we can implement for hoare partition only pivot function will change.


x = [1, 2, 5, 1, -4, 9, 3]
sorting(0, len(x)-1,x)
print(x)


# Lomuto partition
# here we try to move all smaller elements to left side.
# and once all elements smaller than pivot moved to left side we move pivot also next to last smaller element
# such that all smaller elements will be on left side and all greater elements is on right side.
# --- smaller elements -- , pivot, --larger elements --

# Algo
# we take pivot as last element.
# here we will be having i and j pointers.
# we run a loop for j from 0 to n-1
# then inside loop we check data[j] < pivot then we increment i and replace data[i] with data[j]
# here i represents smaller elements traversed so far and j is current element.
# all elements till i index will be smaller than pivot.

def lomuto_partition(data):
    i = -1
    pivot = data[-1]
    # if pivot is not last element then swap pivot with last element. as this algo only works with pivot as last element
    # pivot = data[pivot_index]
    # data[-1], data[pivot_index] = data[pivot_index] , data[-1]
    for j in range(len(data)-1):
        if data[j] < pivot:
            i += 1
            # move smaller element to left side.
            data[j], data[i] = data[i], data[j]
    if i == -1:
        # this means all elements are greater than pivot, as no swapping happens.
        # so just swap first elem with last.
        data[0], data[-1] = data[-1], data[0]
    else:
        # place pivot in its correct position
        data[i+1], data[-1] = data[-1], data[i+1]

data = [4,5,6,3]
lomuto_partition(data)
# print(data)

# Hoare_partition
# This partition is faster than lomuto partition as we have less swaps operations here.
# here pivot element will not goes to its correct position like we did last swap in lomuto partition
# to move pivot its correct position, instead here it will just return an index where all elements on left side are
# lower and right side is greater.

# here pivot can be any element.
# here also we will be having 2 points i and j. but in this case i move towards right side and j move towards
# left side and whenever we found larger element on i pointer traversal and smaller element on j pointer traversal.
# we will simply swap them.
def Hoare_partition(data):
    i = -1
    j = len(data)
    # we just took pivot first element, but we can take something else as well.
    pivot = data[0]
    while True:
        while True:
            i+=1
            if data[i]>= pivot:
                break
        while True:
            j-=1
            if data[j]<= pivot:
                break

        if i>=j:
            break

        data[i], data[j] = data[j], data[i]
    return j

data = [5, 1,2,3,4]
j = Hoare_partition(data)
# print(j)
# print(data)

# there is one more partition called naive partition which maintains stability of elements.
# but it is very slower. as it uses 2-3 loops and O(n) extra space for partition.



## Find Kth smallest element in array:
# here we use pivot function
# if pivot location == k-1 then it means it is our answer.
# pivot is < k-1 ; then we need to go to right side, so we will repeat same steps with
# low = pivot+1
# if pivot > k-1 then we will do high=pivot-1

## segregate two dfferent types of elements in array
# for example segregate even and odd elements.
# [5,2,1,6,4] -> output [5,1,2,6,4]  first odd elements then even.
# here we can simply use partition algorithm. to move 1 type of element to left side and other type of elements
# to right side.

## segregate three different types of element in array.
# here we will have 3 different pointers
# low, mid, high
# where values between o to low have one type of values
# low to mid have other type of values
# mid and high become equal after segregation is complete. so mid to high len will be 0.
# high to n-1 will have third type of values.
# for example segregate all 0s,1s, and 2s in given list. [2,1,0,0,1,2,1,0]
# low and mid start from 0 and high will start from n-1
# we run a loop till mid<=high
# then if we encounter 0 at mid, we will swap low and mid pointer items and increment low and mid
# if we get 1 at mid then increment mid
# if we get 2 then we will swap mid and high and decrement high pointer
