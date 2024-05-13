# we will simply maintain a min heap of k size. each node in heap will store.
# current array name, current array current index, and current data of current array.
# intially we will store first item of each k array into heap, then we will extract min from heap.
# and add same array next item into.
# idea is there should be at max one element from each heap, it should not be more than 1.

# algo :
# Create a min-heap of size k and insert 1st element in all the arrays into the heap
# Repeat the following steps while the priority queue is not empty.
# .....a) Remove the minimum element from the heap (minimum is always at the root) and store it in the output array.
# .....b) Insert the next element from the array from which the element is extracted. If the array doesn’t
#         have any more elements, then do nothing.

# node in heap will look like this
class HeapNode:
    def __init__(self, data, arr_ind, index_in_arr):
        self.data=data
        # it will tell us which array this data belongs to
        self.arr_pos = arr_ind
        # it will tell use index of current data in its array.
        self.index_in_arr = index_in_arr