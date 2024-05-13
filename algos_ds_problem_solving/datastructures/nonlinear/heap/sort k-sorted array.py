import math
from algos_ds_problem_solving.datastructures.nonlinear.heap.heap import MinHeap

# we have given a partially array, where current index i correct postion can lie i-k or i+k index.
# and now task is to sort the array.

# for example:
# d = [2,4,3,5,6]; if k =1 and i is 2 currently, then 3s correct index will i-1 or i+1
# i.e 3 correct position can be in 1 to 3 index.
# as we can see its correct position is 1.

# simple way is to use insertion sort or selection sort.
# it will sort array in n*k complexity.
# like in case of selection sort.
# we will start from first item, and we will scan only next k elements as we know 0th item has be present in k+i/k-i
# indices. as there is nothing on left side, so we will only check right k elements.
# and once we find min we will replace it.
# similarly for second element as we know left side data is already sorted so no need to check there,
# so again we will scan only next k items.
# and we will going like this.
# Also you have noticed we are doing swapping, so it might effect i-k/i+k property of current list.
# but in actual its not. as for ith position we did swapping within i to i+k range. to data present earlier at
# ith position also destined to be put in i to i+k range. so as we did swapping within this range.
# so list k-i/k+i property still holds.

# but n*k complexity can go higher if k is higher.
# so another way to solve it using heap.
# we will build heap of size k. O(k)
# then we will run a loop till i=k+1 to n. O(n-k)
# and inside loop we will remove min element and push next element (k+i index) in heap.O(log(k))
# so total time complexity will be O(k)+ O(n-k)*log(k)
def sort_array(data, k):
    # first build minheap for first k items
    mp = MinHeap()
    mp.build_heap_from_random_array(data[0:k+1])
    index = 0
    for i in range(k+1, len(data)):
        data[index] = (mp.extract_min())
        mp.insert(data[i])
        index+=1

    # print reaming k elements present in heap
    while mp.size:
        data[index] = mp.extract_min()
        index+=1
    return data

print(sort_array([9,8,7,18,19,17], 2))