# A heap is complete tree.
# heap is not bst, as in bst we have ordered data, but in heap only current node should be min/max of
# its left and right child.
# and bst is also necessarily a complete tree.
import math

# we can create priority queue using heap class, as in priority queue also top item having max/min priority.

# we can simply store complete tree in an array.
# and we can use these formula to access children and parent.
# left child  = 2*parent_index+1
# right child = 2*parent_index+2
# parent = floor((child_index-1)/2)

# we will do array representation here, as it is easy and save space.
class MinHeap:
    def __init__(self):
        # if we traverse tree horizontally then position of node in tree is same as index in heap array.
        # for example :
        #      0
        #    1    2
        #  3  4  5 6
        # as you can notice 2nd node in tree is present in 2nd index in array. as this is complete tree.
        self.heap = []
        self.size = 0

        # in heap we have only 2 major operations insert and heapify.
        # in case of insert we fix tree from bottom to top.
        # and in case of heapify we fix tree from top to bottom.
        # now other operations like change node_value, delete kth node, extract_min, build heap from random arr,
        # will use approaches from above insert and heapify methods.

    def get_left_child(self, parent_index):
        lft_index = 2*parent_index+1
        if lft_index < self.size:
            return lft_index
        return None

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
        # we will first insert new data as a last node, then we wil move it towards top recursively,
        # if it smaller then its current parent node.
        # to save space we will do it iteratively.
        self.heap.append(data)
        self.size+=1

        current_parent = self.get_parent_index(self.size-1)
        current_node = self.size-1
        while current_parent is not None and self.heap[current_parent]>self.heap[current_node]:
            # current_parent will be none when current node become root of tree
            # and as soon as we found a prent which is smaller than current node, then we will stop the loop.

            # swap items
            self.heap[current_node], self.heap[current_parent] = self.heap[current_parent], self.heap[current_node]
            # update current and parent
            current_node = current_parent
            current_parent = self.get_parent_index(current_node)

    def heapify(self, node_position):
        # heapify -> only one node is violating heap property. that means subtree below it follows heap property.
        # that means smallest/greatest element either its right or left child. because in min/max heap
        # top most item is smallest/greatest item ,so if current root does not have that means
        # its left or right child have that min/max.

        # so to fix tree we will move top to bottom. first we will fix current node.
        # then after fixing current node, below tree is messed up so we have to fix it recursively as well.

        # note: once we swap child and root nodes, only one branch will be effected so we just to fix one branch.
        left_child = self.get_left_child(node_position)
        right_child = self.get_right_child(node_position)
        min_pos = node_position
        if left_child is not None and self.heap[left_child] < self.heap[min_pos]:
            min_pos = left_child
        if right_child is not None and self.heap[right_child] < self.heap[min_pos]:
            min_pos = right_child
        # we are checking which one out of these 3 has min value to reduce swap operations.
        if min_pos !=node_position:
            self.heap[min_pos],  self.heap[node_position] = self.heap[node_position],  self.heap[min_pos]
            self.heapify(min_pos)

        # else current node is in its right position, no need to do perform any other operation


    def extract_min(self):
    # extract-> we replace last node wth root and remove last node from tree. then we will heapify tree.
    # we replaced with last node because its easier to remove last nodes as last node does not have childrens.
    # plus heap is complete tree also. so if we just chose node from anywhere to replace with root.
    # then it will put a hole in complete tree. and now to fill the left side of tree we can't guarantee in
    # Log(n) operations.

        # replace last node with root
        self.heap[0], self.heap[self.size-1] = self.heap[self.size-1], self.heap[0]
        # reduce the size first, so that heapify function won't include last node
        self.size-=1

        # heapify tree again
        self.heapify(0)
        # remove last element from heap which is min now.
        return self.heap.pop()

    def decrease_key(self, key, new_value):
        self.heap[key] = new_value
        # now we will heapify tree from current node towards top. same thing we did in insert.
        current_node = key
        current_parent = self.get_parent_index(current_node)
        while current_parent is not None and self.heap[current_node] < self.heap[current_parent]:
            self.heap[current_node], self.heap[current_parent] = self.heap[current_parent],  self.heap[current_node]
            current_node = current_parent
            current_parent = self.get_parent_index(current_node)

    def increase_key(self, key, new_value):
        self.heap[key] = new_value
        self.heapify(key)

    def delete(self, key):
        res = self.heap[key]
        # frst move current key to the top
        self.decrease_key(key, float('-inf'))
        # then remove it.
        self.extract_min()
        return res

    def build_heap_from_random_array(self, list_data):
        # new list data will be our new heap array now we have to fix it.
        # its time complexity is O(n). there is some mathematical proof.

        # to fix array we have to hepaify from last level to top level nodes.
        # also heapify function replaces root with child nodes, as leaf nodes does not have child
        # so we will skip leaf nodes and start from second last level.
        self.heap = list_data
        self.size = len(list_data)
        for i in range(self.get_parent_index(self.size-1), -1, -1):
            self.heapify(i)

    def sort_arr_using_heap(self, list_data):
        self.build_heap_from_random_array(list_data)
        for i in range(self.size):
            print(self.extract_min())

mh = MinHeap()
mh.sort_arr_using_heap([6,5,3,4,7,1])
# print(mh.insert(2))


# sample problem

## buy maximum possible items with given sum
# let say data= [1,12,5,111,200]; sum =10.
# we have to fetch as much items as possible from list. but sum all items should not exceed 10.
# output is 1,5; because 6<10.
# we can simply sort it and then return items from left side.
# but its time compolexity will be nlog(n).
# we can use min heap instead.
# building min heap with O(n).
# then extract min items log(n).
# so final time-complexity will be O(n)+ (len of result array, [like 2 in above case])*log(n).
# => res_len*(logn)