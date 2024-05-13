# we need to find a pair whose sum is equal to k
# one way to do it to create ordered list by traversing tree in inorder way.
# and then se 2 pointers approach to find it.

# another way is to use a set. this approach also we have used with list as well.
# but now we will use it with tree.
# we will traverse whole tree. and as we are traversing we will keep pushing complement of current node into
# set . k-curren_node_data . before inserting data to dict, we will check if
# current node data is already present in set.
# if yes then we will return the result.

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


def find_pairs(root, k, set_data=set()):
    if root is None:
        # if we reach here, that means we encountered leaf node of any branch.
        # if we would have found result, then we wouldn't have reached to leaf. we would have gone towards upwards to
        # return found pairs. but we reached here, that means we didn't found result yet, so we can sfely return empty
        # result.
        return ()

    res = find_pairs(root.left, k, set_data)
    if len(res)!=0:
        # if we found result in left traversing already then return result
        return res

    if root.data in set_data:
        res = (root.data, k-root.data)
        return res
    else:
        set_data.add(k-root.data)

    return find_pairs(root.right, k, set_data)


root = bst_insert(None, 20)
root = bst_insert(root, 70)
root = bst_insert(root, 18)
root = bst_insert(root, 15)
root = bst_insert(root, 19)
root = bst_insert(root, 10)
root = bst_insert(root, 60)
root = bst_insert(root, 65)
root = bst_insert(root, 50)

print(find_pairs(root, 75))