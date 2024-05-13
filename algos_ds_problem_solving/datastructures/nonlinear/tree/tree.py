# Basic Tree Terminologies:
import math


# Root: The root of a tree is the first node of the tree. In the above image, the root node is the node 30.

# Edge: An edge is a link connecting any two nodes in the tree. For example,
# in the above image there is an edge between node 11 and 6.

# Siblings: The children nodes of same parent are called siblings.
# That is, the nodes with same parent are called siblings. In the above tree, nodes 5, 11, and 63 are siblings.

# Leaf Node: A node is said to be the leaf node if it has no children.
# In the above tree, node 15 is one of the leaf nodes.

# Level: The level of a node is the number of edges on the path from the root node to

# Height of a Tree: Height of a tree is defined as the total number of levels in the tree or the length of the path
# from the root node to the node present at the last level. The below tree is of height 2.
# note: height is equal to level
#           1
#           /\
#          2  3
#         /\  /\
#        5 6  7 8

# we will learn about binary trees as they have most of the applications in real world#####

### nodes and level/height relations in binary trees ####
# In below formula height and levels are considered for counting edges not nodes.
# 1. max number of nodes at level l ->
# 2. max number of nodes in a tree of  height h will be  -> (2^(h+1))-1
# 3. minimum possible height/levels for n nodes -> log2(n+1) -1
# 4. in perfect binary tree number of leaf nodes = (total number of nodes in tree+1) /2;
# that means all nodes present before leaf are just half in number than leaf nodes =>
# nodes before leaf +1 = number of nodes in leaf
# 5. minimum possible levels/height with l leaves nodes -> log2(l)


# types of binary trees:
# 1. full binary tree:  A Binary Tree is full if every node has either 0 or 2 children.
# we can say except leaf nodes all nodes has 2 childs
# example:
#                  18
#                 |  \
#                15   30
#                / \
#               30  50


# 2. Complete Binary tree: all nodes has 2 childs except last level.
# and all nodes at last level are filled from left to right.
# i.e all nodes in the last level are as far left as possible.
# example:
#    18
#   /   \
#  15   30
#  /\    | \
# 40 50  100 40
# / \  \
# 8  7  9
# as you can see last level 50 node has only one child.

# 3. Perfect binary tree: here all nodes has 2 child except leaf nodes and all leaf nodes will be at same level.
#                  18
#               /     \
#              15     30
#            /   \   /  \
#           40   50 100  40

class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):

        if data > self.data:
            if self.right is None:
                self.right = Tree(data)
            else:
                # it will recursively adjust itself
                self.right.insert(data)
        elif data < self.data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.insert(data)

def find_height(root):
    # note: in this implementation we are counting max nodes from top to bottom, instead of edges.
    # that's why result is max_level+1, instead of equal to it.
    # if we are considering edges for height calculation then final result will be subtracted by 1.
    # if current node is null that means we reached to end
    if not root:
        return 0
    # traverse both sides of tree and find where we can find max depth of tree, that will be height
    return max(find_height(root.left), find_height(root.right))+1 # adding 1, because we are considering current node for height 1

def get_size(root):
    # gives total number of nodes
    if root is None:
        return 0
    return 1 + get_size(root.left) + get_size(root.right) # recursively get size of left and right subtree.

def get_max_node(root):
    # gives total number of nodes
    if root is None:
        return float('-inf')
    return max(root.data, get_size(root.left), get_size(root.right)) # recursively find max value from left and right subtree.

# check if sum of child nodes is equal to parent node data
def check_child_sum_property(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True # if no child then current node will be true

    sum = 0
    if root.left:
        sum+= root.left
    if root.right:
        sum+= root.right

    return sum == root.data and check_child_sum_property(root.left) and check_child_sum_property(root.right)
    # check current sum and check recursively if child nodes also applies same property

# balanced tree is a tree for which each node, left and right subtree height difference should be 0 or 1.
def check_tree_balanced(root):
    # height will be 0 for last nodes and it will be balanced.
    if root is None:
        return True, 0

    # we will check height and balanced status for left sub stree
    res = check_tree_balanced(root.left)
    # if left subtree is not balanced then return false.
    if res[0] is False:
        return False
    # adding 1 to height to include current node.
    left_height = res[1]+1

    # same procedure for right subtree
    res = check_tree_balanced(root.right)
    if res[0] is False:
        return False
    right_height = res[1] + 1

    # checking if current root node is balanced and generating height by choosing max of left and right subtree heights
    return abs(left_height-right_height) <= 1, max(left_height, right_height)


## Convert binary tree into double linked list
# here left child become prev node of root and right child will become next of root
# example:
#     10
#    /\
#   5  20
#       /\
#      30 35
# => null<-5<->10<->30<->20<->35-> null
def convert_to_doubly_linked_list(root):
    head = None
    prev = None

    def con_dbl(root):
        nonlocal prev
        nonlocal head
        if root is None:
            return root

        # do left traversal first
        con_dbl(root.left)
        if prev is None:
            # that means we reached to left most child and now make it as head
            head = root
        else:
            # now update prev node next and current node prev
            prev.next = root
            root.prev = prev

        prev = root
        # traverse right child
        con_dbl(root.right)

    con_dbl(root)
    return head

def find_diameter(root):
    # diameter is just longest path possible from one node to any other node.
    # to solve this, we will calculate sum of height of left and right child for each node and then we will print
    # max of those sums.
    global res
    if root is None:
        return 0
    left_height = find_diameter(root.left)
    right_height = find_diameter(root.right)
    res = max(res, 1+left_height+right_height)# calculating diameter for current subtree.
    return 1+max(left_height, right_height) # returning current subtree height

def find_closest_common_ancestor(root, a, b):

    if root is None:
        return None

    # if we found a or b
    if root.data == a or root.data ==b:
        return root

    # if both a and b found in childs of root
    left_child = find_closest_common_ancestor(root.left, a, b)
    right_child = find_closest_common_ancestor(root.right, a, b)

    if left_child and right_child:
        return root

    # if right child is null, that means either only a or b present in  left child or both present in left child.
    if left_child:
        return left_child
    else:
        # else we will check in right child, if right also not contains a and b then this will automatically
        # return None
        return right_child

def count_nodes_in_complete_b_tree(root):
    # idea is simple we have to check which subtree is perfect b tree. and whenever we found perfect b tree.
    # we calculates its nodes using formula log2(l)-1.
    # to check if sub complete tree is perfect tree we will check height of left most leaf and right most leaf.
    # if it matches then we can say it is perfect tree as complete tree start filling from left most leaf.
    # and if it is not perfect tree then we check subtrees if they are perfect b tree or not.
    global res
    cur = root
    left_h = 0
    right_h = 0
    while cur is not None:
        left_h+=1
        cur = cur.left
    cur = root
    while cur is not None:
        right_h+=1
        cur = cur.right

    if right_h == left_h:
        return math.pow(2,right_h)-1
    # else we will consider current root by doing +1 and check if its subtrees are perfect b tree.
    return 1+  count_nodes_in_complete_b_tree(root.left) + count_nodes_in_complete_b_tree(root.right)

def check_symmeteric(root1, root2):
    # a tree is symmetric if we flip its left over right half then, it should exactly match.
    #    5
    #  /   \
    #  1    1
    #/  |   / \
    #3  4  4  3

    # we will make 2 recursive calls one for left tree and one for right sub tree and we recursively compare them.
    if root1 is None and root2 is None:
        return True

    if root1 is None and root2 is not None:
        return False
    if root2 is None and root1 is not None:
        return False
    if root1.data !=root2.data:
        return False

    return check_symmeteric(root1.left, root2.right) and check_symmeteric(root1.right, root2.left)




root = Tree(5)
left = Tree(1)
right = Tree(1)
l_left = Tree(2)
r_right = Tree(2)
root.left = left
root.right = right
right.left = r_right
left.left = l_left

# print(find_height(root))

print(check_symmeteric(root, root))