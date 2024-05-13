# there are 2 ways to verfiy bst.
# first way is to traverse bst in inorder fashion and check if prev node is > current
# if it is then it means bst is invalid.
# because in inorder bst always print in sorted manner.

# another ways is to assign -infinity and plus infinity  range to root node
# as when we traverse left side we change the right side range with root node and
# and for right child we will replace left range with root data.
# if current node lies in given range then tree is valid otherwise tree is invalid.
# example:

#       -infi <(5)< +infi
#         /          \
#   -infi <(3)< 5    5< (10)< +infi
#                      /
#                    5<(8)<10

class Tree:
    def __init__(self, data):
        self.data = data
        self.right, self.left = None, None




root = Tree(7)
left = Tree(5)
right = Tree(10)
root.left = left
root.right = right

left_left = Tree(1)
left.left = left_left

prev = Tree(float('-inf'))
def verify_bst_1(root):
    global prev
    if root is None:
        return True

    # according to inroder fashioin first we traverse left side
    if not verify_bst_1(root.left):
        return False

    # on last iteration left most node will be compared with -inf
    if root.data <= prev.data:
        return False
    # updating prev with left trav node
    prev = root

    # checking for right node.
    return verify_bst_1(root.right)


def verify_bst2(root, range1, range2):
    if root is None:
        return True
    if not(range1<root.data<range2):
        return False

    res = verify_bst2(root.left, range1, root.data)
    res &= verify_bst2(root.right,root.data, range2 )

    return res

# print(verify_bst2(root, float('-inf'), float('inf')))
# print(verify_bst_1(root))


# another similar problem will be that a  binary tree has 2 nodes which are not in correct order so we have to fix the
# the tree by identifying those 2 nodes and swap them.
# to identify those nodes we can again traverse tree in inorder fashion.


root2 = Tree(7)
left = Tree(5)
right = Tree(10)
root2.left = left
root2.right = right

left.left = Tree(1)
left.right = Tree(9)

right.left = Tree(6)
right.right = Tree(11)

# in this tree 9 and 6 are in wrong position
# pre is used to store previous node while traversal. which we will use to compare current and prev node while inorder
# traversal
pre, first, second = Tree(float('-inf')),None,None
def fix_binary_tree(root):
    global pre,first,second
    if root is None:
        return
    # inorder traversal, so left call will come first
    fix_binary_tree(root.left)
    if root.data <= pre.data:
        # this means we found our corrupted node, but corrupted node can be prev or it can be current node.
        # there will be 2 scenarios for corrupted nodes.
        # scenario 1: when corrupted nodes are continues.
        # 1,5,6,9,7,10,11 -> like in this case 7 and 9 are corrupted.
        # so to fix it we will simply make first as prev and second as current root.
        # and later we will swap first and second node data.
        # scenario 2 : when corrupted nodes are not contigues
        # 1,5,10,7,9,6,11 -> 10 and 6 are corrupted.
        # so cur_data< prev will be triggered 2 times.
        # in this case when first time triggered, prev node was the corrupted one, so we will store it in first.
        # second time when 6<9 (cur_item<prev) this time current node is corrupted one, so we will store root into
        # second. by using this we derived below logic.
        if first is None:
            first = pre
        # if we update second everytime less than condition is triggered then we will cover both above mentioned
        # scenarios.
        second = root

    # update prev value
    pre = root

    # traverse right side according to inorder.
    fix_binary_tree(root.right)


fix_binary_tree(root2)
# after calling this function it will store corrupted nodes in first and second

# swap the corrupted nodes.
if first is not None and second is not None:
    first.data, second.data = second.data, first.data


print(verify_bst_1(root2))