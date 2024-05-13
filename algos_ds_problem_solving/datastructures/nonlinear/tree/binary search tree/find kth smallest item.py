# idea is simple for each node we will keep a count of how many elements are smaller than them.
# while insertion of new node we will increase count of its larger ancestors.
# and while finding results we just have to check if current node smaller_count == k-1 (as when
# we consider current node also then count will become k)

class BSTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.smaller_than_current_count = 0

def insert(root, data):
    # todo: validate before insertion of node exists or note.
    #  otherwise our smaller elements counter will unnecessarily incremented

    if root is None:
        return BSTree(data)

    if data > root.data:
        root.right = insert(root.right, data)
    elif data < root.data:
        # as new data is smaller, so we are increasing count of smaller elements for current node.
        root.smaller_than_current_count+=1
        root.left = insert(root.left, data)
    return root

def successor(root):
    root = root.right
    while root.left:
        root = root.left
    return root

def delete(root, data):
    # todo: add a validation before deletion to check if node we are trying to delete exists or not
    #  otherwise our smaller elements counter will unnecessarily decremented
    if root is None:
        return None

    if data > root.data:
        root.right = delete(root.right, data)
    elif data < root.data:
        # decreasing count as we increased in insert
        root.smaller_than_current_count-=1
        root.left = delete(root.left, data)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            suc = successor(root)
            root.data = suc.data
            root.right = delete(root.right, suc.data)

def find_kth_smaller_node(root, k):
    # now while insertion you must have noticed we have incrementing count only if new node is going on left sub tree.
    # but this will only give us the correct count for new node ancestors, but what about right subtree.
    # as they are already greater, but we are not changing their count.
    # for example:  [5,3,14]
    # if we create tree with above nodes it will look like this
    #        5  (1)
    #     /     \
    #    3 (0)    14 (0)
    # if you notice count at 14 is 0 but ideally it should be 2.
    # so to fix while searching for kth smaller node. whenever we have to go to right subtree
    # we will first subtract k with the count of parent node +1 (including parent node).
    # let say if k was 3 and then k will be 1 after traversing 5 node and
    # when we compare k-1 == current node count
    # which is 1-1 == 0; so this will be true as 14 is 3rd smallest node.

    if root is None:
        return None # result not exists

    if root.smaller_than_current_count == k-1:
        return root
    elif k-1 > root.smaller_than_current_count:
        # as k is much greater then we have to go to right side.
        return find_kth_smaller_node(root.right, k-1-root.smaller_than_current_count)
    else:
        return find_kth_smaller_node(root.left, k)


root = insert(None, 20)
insert(root, 18)
insert(root, 19)
insert(root, 15)
insert(root, 10)
insert(root, 70)
insert(root, 60)
insert(root, 50)
insert(root, 65)


print(find_kth_smaller_node(root, 7).data)
delete(root, 19)
print(find_kth_smaller_node(root, 7).data)

