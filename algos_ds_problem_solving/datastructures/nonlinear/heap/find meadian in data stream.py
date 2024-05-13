# we need to find medians for a given data steam.
# for exmaple: [5,10,5,4, ...]
# After reading 1st element of stream - 5 -> median - 5
# After reading 2nd element of stream - 5, 15 -> median - 10
# After reading 3rd element of stream - 5, 15, 1 -> median - 5
# After reading 4th element of stream - 5, 15, 1, 3 -> median - 4, so on...
import math


# naive way to sort array everytime new item is added and then find median.

# another way is to solve it using bin search tree. there we implemented a bst to find kth smallest element.
# we will simply find the median element using this approach, where k will be (lenght of current stream) //2.
# so time complexity to find median will be log(n).
# and for stream of n size total complexity will be n(log(n)), but this time-complexity is not guaranteed.

# another way to solve it using 2 heaps which will guarantee n(log(n)).
# one will be max heap and another will be min heap.
# max heap will store smaller items and min heap will store larger items.
# also we  have to make sure that max heap always contains same number of items or one extra item than min heap.

# so now we have four conditions:
# 1. if max heap has more items than min heap:
#   a. if current item is greater than max item in maxheap then simply add it into min heap.
#   b. else add new item into max heap and then remove top item from max heap and then add removed item into imn heap.
# 2. else if max and min heap has same items:
#   a. if item is smaller than top item in max heap simpy insert into max heap.
#   b. add new item into min heap but now min heap size is larger, so remove top item from minheap and add it into
#   max heap.
# 3. 3rd case will never arise as whenere both heap size is same we are trying to push new items in smaller_items heap.


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def get_left_child(self, parent_index):
        lft_index = 2*parent_index+1
        if lft_index < self.size:
            return lft_index
        return None

    def peek(self):
        return self.heap[0]

    def get_right_child(self, parent_index):
        rgt_index = 2*parent_index+2
        if rgt_index < self.size:
            return rgt_index
        return None

    def get_parent_index(self, child_index):
        if child_index == 0:
            return None
        return math.floor((child_index-1)/2)

    def insert(self, data):
        self.heap.append(data)
        self.size+=1
        current_parent = self.get_parent_index(self.size-1)
        current_node = self.size-1
        while current_parent is not None and self.heap[current_parent]>self.heap[current_node]:
            self.heap[current_node], self.heap[current_parent] = self.heap[current_parent], self.heap[current_node]
            current_node = current_parent
            current_parent = self.get_parent_index(current_node)

    def heapify(self, node_position):
        left_child = self.get_left_child(node_position)
        right_child = self.get_right_child(node_position)
        min_pos = node_position
        if left_child is not None and self.heap[left_child] < self.heap[min_pos]:
            min_pos = left_child
        if right_child is not None and self.heap[right_child] < self.heap[min_pos]:
            min_pos = right_child
        if min_pos !=node_position:
            self.heap[min_pos],  self.heap[node_position] = self.heap[node_position],  self.heap[min_pos]
            self.heapify(min_pos)

    def extract_min(self):
        self.heap[0], self.heap[self.size-1] = self.heap[self.size-1], self.heap[0]
        self.size-=1
        self.heapify(0)
        return self.heap.pop()

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def get_left_child(self, parent_index):
        lft_index = 2 * parent_index + 1
        if lft_index < self.size:
            return lft_index
        return None

    def peek(self):
        return self.heap[0]

    def get_right_child(self, parent_index):
        rgt_index = 2 * parent_index + 2
        if rgt_index < self.size:
            return rgt_index
        return None

    def get_parent_index(self, child_index):
        if child_index == 0:
            return None
        return math.floor((child_index - 1) / 2)

    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        current_parent = self.get_parent_index(self.size - 1)
        current_node = self.size - 1
        while current_parent is not None and self.heap[current_parent] < self.heap[current_node]:
            self.heap[current_node], self.heap[current_parent] = self.heap[current_parent], self.heap[current_node]
            current_node = current_parent
            current_parent = self.get_parent_index(current_node)

    def heapify(self, node_position):
        left_child = self.get_left_child(node_position)
        right_child = self.get_right_child(node_position)
        min_pos = node_position
        if left_child is not None and self.heap[left_child] > self.heap[min_pos]:
            min_pos = left_child
        if right_child is not None and self.heap[right_child] > self.heap[min_pos]:
            min_pos = right_child
        if min_pos != node_position:
            self.heap[min_pos], self.heap[node_position] = self.heap[node_position], self.heap[min_pos]
            self.heapify(min_pos)

    def extract_max(self):
        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        self.size -= 1
        self.heapify(0)
        return self.heap.pop()


def find_median_of_stream(data):
    smaller_items_heap = MaxHeap()
    bigger_item_heap = MinHeap()

    # insert first item and print it explicitly
    smaller_items_heap.insert(data[0])
    print(data[0])

    for i in range(1, len(data)):

        if smaller_items_heap.size > bigger_item_heap.size:
            # that means we will try to push new items in bigger items heap.
            if data[i] > smaller_items_heap.peek():
                bigger_item_heap.insert(data[i])
            else:
                # new item is smaller so we will insert it in smaller items heap and remove largest item from
                # smaller heap and move it to bigger items heap. to maintain size of both heaps.
                smaller_items_heap.insert(data[i])
                x = smaller_items_heap.extract_max()
                bigger_item_heap.insert(x)
        else:
            # we will try to add new item into smaller items heap
            if data[i]< smaller_items_heap.peek():
                smaller_items_heap.insert(data[i])
            else:
                bigger_item_heap.insert(data[i])
                x = bigger_item_heap.extract_min()
                smaller_items_heap.insert(x)

        # now time to print median for stream data seen so far.
        # If total size numbers seen for far is odd that means our median is, top item of
        # smaller items heap.
        if (smaller_items_heap.size+bigger_item_heap.size) %2!=0:
            print(smaller_items_heap.peek())
        # else we have to find avg of both heap top items.
        else:
            print((smaller_items_heap.peek()+bigger_item_heap.peek())/2)

find_median_of_stream([12,15,10,5,8,7,16])
