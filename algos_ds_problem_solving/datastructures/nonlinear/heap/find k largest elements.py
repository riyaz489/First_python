from algos_ds_problem_solving.datastructures.nonlinear.heap.heap import MinHeap

# we have to find k largest items (for getting kth largest/smallest also we can use same approach)
# one way to solve is to use max heap and extract top items k items
# but its time complexity will be O( n+ k(Log(n)) )
# other way is to create a min heap of first k elements and start traversing from k+1 element
# and whenever we found current element is greater than min heap top.
# just replace it with heap top item and heapify it again.
# as we are removing the lowest element everytime, so in final heap we will left with only k largest elements.
# time complexity will be O(k + (n-k)Logk )
# which is better than max heap. and takes less auxiliary space.

def k_largest_element(data, k):
    mh = MinHeap()
    # build minheap of k elements
    mh.build_heap_from_random_array(data[:k])

    for i in range(k, len(data)):
        if data[i]> mh.heap[0]:
            # replace smallest element with current item, if it is greater.
            mh.heap[0] = data[i]
            # heapify to get smallest value in heap to top again
            mh.heapify(0)

    return mh.heap

print(k_largest_element([7,5,2,9,12,56,3], 3))