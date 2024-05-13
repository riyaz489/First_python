# worst complexity n2
# best complexity n

# it is inplace and stable algo.
# this is best algo for small sized array. because as you can notice it simple algo which do some swaps operations
# and when few of the data is already sorted, then internal loop is also skipped.
# whereas quicksort uses recursion and extra partitions which create some overhead
# so at some point or array length insertion sort is faster but when array length exceeds some
# threshold after that point quicksort will always be faster.


# here we keep taking elements from left  and put tem into its correct position.
# for example: in 3,2,1
# we start with 3, as one element is already sorted then nothing needs to be done.
# then we pick 2 so now we have 3,2 elements, as we can see 2 is not in its correct position.
# so we move it to left side to make it sorted.
# then we pick 1, at that moment array will look like this 2,3,1. as you can notice left side of 1 is already sorted.
# so when we pick 1 we again move it to its correct position, then our complete array will be sorted.
def sorting(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1

        # shifting elements
        while key < data[j] and j>=0:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data

print(sorting([1, 2, 5, 1, -4, 9, 3]))
print(sorting([1, 2, 5, 1, -4, 9]))