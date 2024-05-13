# this tree is derived from binary search algorithm.
# we can use this to find smallest and greatest elements.
# we can use this to find ceil, floor , nodes  count of smaller/greater than k.
# note: we can not store duplicate items in BST, but we can modify implementation of BST to store duplicates.
# like each node can store the freq of data, with data value.
# then below tree node will have one more property which is called freq.
class Tree:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def inorder_trav(root):
    if root is not None:
        print(root.data)
        inorder_trav(root.left)
        inorder_trav(root.right)

def bst_insert(root, data):
    # we will insert in binary search way.; i.e  smaller nodes will be left child and greater nodes will be right child.

    if root is None:
        root = Tree(data)
        return root

    if data == root.data:
        # if data already exists in bfs then we will skip insert.
        return

    elif data > root.data:
        # insert on right subtree
        if root.right is not None:
            # root right is not none, then we will recursively find right place in right subtree to insert new data.
            bst_insert(root.right, data)
        else:
            # root right is none then we will insert new node as right child
            root.right = Tree(data)
    else:
        # insert on left subtree
        if root.left is not None:
            bst_insert(root.left, data)
        else:
            root.left = Tree(data)

    # if tree already has some data then we are only worried about original root, that's why we did return here only.
    # not in recursion calls.
    return root

def find_successor(root):
    # now new successor can be either closest smaller number or closest greater number.
    # to find the closest smaller number will be rightmost leaf node in left subtree.
    # and closest greater node can be leftmost  leaf node in right subtree.
    # here we will go with closes greater number.
    root = root.right
    while root.left is not None:
        root = root.left
    return root

def bst_delete(root, data):
    # here we will have three scenarios which we will discuss below

    # if requested node does not exists in search or root node is None
    if root is None:
        return root

    # first we have to find the node which we have to delete
    if data > root.data:
        root.right = bst_delete(root.right, data)
    elif data < root.data:
        root.left = bst_delete(root.left, data)

    else:
        # that means we found the exact node

        # now this if block and next elif block covers 2 scenarios:
        # scenario 1: if requested node does not have any child then in that case we can simply remove it
        # so if left and right child both are None then this first if block will return None
        # to is parent caller and that parent caller will set None for its left/right subchild.

        # scenario 2: if requested node has only 1 child either left or right.
        # then that case we will simply replace request node with left/right child (whichever exists)
        # so parent caller will set its left/right child with current node left/right child.

        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # we will inside this block when we have both left and right child.
        else:
            # scenarios 3: when we have both left and right child. now in this case we have to find closest smaller
            # or closest greater successor.
            # we use below function for that.
            suc = find_successor(root)
            # above function will always return leaf node. now we will simply replace leaf node data with current node
            # and remove leaf node.

            # replace successor and current root data
            root.data = suc.data

            # now we will delete successor node
            root.right = bst_delete(root.right, suc.data)
    return root # return newly modified root node to caller function

def search(root, data):
    # we will search in bin search manner.
    cur = root

    while cur is not None:
        if data> cur.data:
            cur = cur.right
        elif data<cur.data:
            cur = cur.left
        else:
            return cur
    # it will return NOne if we didn't find correct node.
    return cur

def floor(root, data):
    # we have to find biggest node which is smaller than requested node.
    # if there is nothing smaller than current node then return None.

    possible_candidate_for_floor = None
    # now whenver we go to right child that means we have seen a smaller element which may be closer to requested node.
    # that also means our answer does not exists in left subtree. as all nodes will be smaller then current node.

    while root is not None:

        if data > root.data:
            # whenever we see a smaller elements we will make it possible candidate.
            possible_candidate_for_floor = root
            root = root.right
        elif data < root.data:
            root = root.left
        else:
            # found exact match
            return root

    return possible_candidate_for_floor

def ceil(root, data):
    possible_candidate_for_ceil = None
    while root is not None:
        if data < root.data:
            possible_candidate_for_ceil = root
            root = root.left
        elif data > root.data:
            root = root.right
        else:
            # found exact match
            return root
    return possible_candidate_for_ceil




root = bst_insert(None, 20)
root = bst_insert(root, 70)
root = bst_insert(root, 18)
root = bst_insert(root, 15)
root = bst_insert(root, 19)
root = bst_insert(root, 10)
root = bst_insert(root, 60)
root = bst_insert(root, 65)
root = bst_insert(root, 50)

# inorder_trav(root)
root = bst_delete(root, 20)
inorder_trav(root)
