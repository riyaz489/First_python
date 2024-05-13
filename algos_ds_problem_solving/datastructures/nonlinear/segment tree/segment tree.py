from types import FunctionType
# Let say if we  have to perform multiple range based operations on given list then.
# for example to get sum of items from 2nd index to 5th index.
# in that case normally we will traverse from 2nd to 5th index and we will so sum.
# basically it will be O(n) in worst case.

# to optimize it we can create an aux array which will keep sum of items 0 to i index, for index i.
# so now we can find sum of ranged items in O(1), by doing aux[end_range]-aux[start_range].
# but the problem with this approach is whenever we update an element, we again have to update whole
# aux array with new sums. that will be O(n) operation.

# So better approach is to segment tree, which will perform range based and update queries in O(log(n)).
# Segment Trees are Binary Tree which is used to store intervals or segments. That is each node in a
# segment tree basically stores the segment of an array. Segment Trees are generally used in problems
# where we need to solve queries on a range of elements in arrays.
# we can solve prefix problems also using this tree. for prefix of n size range would be (0,n)

# Segment trees are full binary tree not complete tree like heap, so we need to put someplace holders for empty nodes.
# so that we can represent it in array.
# a sample Segment tree for data [5,3,7,1,9] array length is 5
# here in segement tree leaf nodes contains actual data and internal nodes contains range based operation results
# like for above case our operation will be sum
#                             (0-5) 25
#                           /         \
#                  (0-2) 15          (3-4) 10
#                   /      \          /     \
#              (0-1) 8  (2-2) 7   (3-3)1  (4-4) 9
#                /   \
#           (0-0)5   (1-1) 3
# here brackets values specify range and non-bracket items are sum of values for given range.
# now if we want to find sum of values if range (0-2) then I can simply go to that node and find the result.

# Now to store it in array we have to figure out how many max nodes our tree possibly can have.
# So can you can notice we are dividing range on each next level by 2 and tree will go on till we left with only 1 node.
# so tree max height can be log2(lenght of input array)
# now formula to find max possible nodes for given height is 2^(height+1) -1
# so lenght of array to store tree nodes will  be = 2^(log2(n)+1)  - 1
# it will be approximately equal to 4n, so we cna use 4n instead of above complex formula.

# note: segment tree works in fixed size array, i/e deletion and insertion is not possible in log(n) as we have to
# recalculate all the nodes and balance tree, so its better to build new tree instead of doing deletion/insertion.

# now we will construct the tree using array.
def build_tree(data): # time and space complexity will be O(4n)
    tree = [None] * 4 * len(data)

    def build_tree_inner(data, range_start, range_end, current_index):
        # we will build tree from bottom to top
        if range_start == range_end:
            # as you can notice in above tree example
            # at leaf nodes, start and end range become equal and those ranges also represent item current index in original
            # input array.
            # so that's why we are putting range_start as index to get correct item.
            # and current_index is new calculated index which will be its new index in tree.
            tree[current_index] = data[range_start]
            return tree[current_index]

        mid = (range_start+range_end)//2 # finding mid of range, to make 2 recursive calls
        left_child_pos = 2*current_index + 1 # arr position for left child for complete tree
        right_child_pos = 2*current_index+2

        # reducing range for left and right calls and passing new current_index, to assigning next left and right childs
        # to their correct position
        # also adding sum of below 2 calls to current node. as we are building bottom to top
        tree[current_index] = build_tree_inner(data, range_start, mid, left_child_pos) + \
                              build_tree_inner(data, mid+1, range_end, right_child_pos)
        return tree[current_index]

    build_tree_inner(data, 0, len(data)-1, 0)
    return tree


# Range query can be of 3 types in nature.
# 1. in case our node is fully covered in given range then, we will add current node value in current result.
# for example: current node contains range of 3-4 and input is 1-5 then we will current node value in result.
# 2. in case our current node range is partially covered in given range then we will go to left or right child.
# till it is fully covered in given range.
# for example: given range in  1-5 and current range is 3-7.
# for will break current node range by traversing its child till we found 3-5 range which lies completely within
# 1-5 range.
# 3. if current node is completely outside of given range, do a early return with 0.
# exmaple: input is 7-9 and current node is 2-4, as we know tree below its will contains only range withing 2-4
# so we will never get 7-9 value so we will return 0 from here.


# so we will go from top to bottom in tree, and try to traverse both childs of each node. to find the required ranges
# and then sum them.
def range_query(tree, in_start, in_end, rg_start, rg_end, current_index): # O(log(n))
    # we might be trying to traverse all the nodes, but even in worst case scenario we will end up beeing traversing
    # only 2 branches. which is 2logn.

    # completely lies within given range
    if rg_start>= in_start and rg_end<= in_end:
        return tree[current_index]
    # if completely out side ouf given range
    if (rg_end<in_start) or (rg_start > in_end):
        return 0

    # trying to divide partially overlapping ranges, bu traversing left and right child
    # for non overlapping part we will get result 0 and for overlapping part we will get node value.
    range_divider = (rg_start+rg_end)//2
    left_index = current_index*2 +1
    right_index = current_index*2 +2
    return range_query(tree, in_start, in_end, rg_start, range_divider, left_index) +\
           range_query(tree, in_start, in_end, range_divider+1, rg_end, right_index)

# update query is simple, we will be given an index where update happened, new value which we need to update and
# original old input array.
# now to update new value we will find the diff between old and new value.
# let;s say diff is 5, so we will add 5 to all the nodes in which current index lies, recursively.
def update_query(tree, old_array, new_data, index):

    def update_query_inner(tree, in_index, start, end, current_ind, diff):
        if in_index>= start and in_index<=end:
            # updated item lies in current node range, so we will update it
            tree[current_ind]+=diff


            # also we have to make sure we will break the recursion, to going infinite.
            # so we will add condition to break, when we reached to leaf node
            if start>=end:
                return

            # update its child recursively
            mid = (start+end) //2
            left_index = current_ind*2 + 1
            right_index = current_ind*2 + 2

            update_query_inner(tree, in_index,start, mid, left_index, diff)
            update_query_inner(tree, in_index,mid+1, end, right_index, diff)


    update_query_inner(tree, index, 0, len(old_array)-1, 0, new_data-old_array[index])
    return tree

data =[4,3,6,8,1]
tree = build_tree(data)
tree = update_query(tree, data, 2, 4)
print(range_query(tree, 1,4,0,len(data)-1,0 ))