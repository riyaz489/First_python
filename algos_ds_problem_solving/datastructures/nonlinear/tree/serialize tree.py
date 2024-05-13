
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
def dfs_recursive_trav(root):
    print(root.data)
    if root.left:
        dfs_recursive_trav(root.left)
    if root.right:
        dfs_recursive_trav(root.right)
root = Tree(10)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(8)
root.insert(13)
root.insert(16)
root.insert(2)
root.insert(4)
root.insert(6)


def serialize(root, res=[]):
    # serailize means to convert tree into string/array

    # idea is simple we will simply traverse in preorder fashion and whenever we found a node does not have right/left
    # child we will simply place None in list.
    # None in list will signify that current node does not have right/left child.

    if root is None:
        res.append(None)
        return res
    res.append(root.data)

    serialize(root.left, res)
    serialize(root.right, res)

    return res

data = serialize(root)

def deserailize(data):
    # converting list into tree
    # we will again traverse list into preorder fashion

    if len(data)==0:
        return None
    if data[0] is None:
        data.pop(0)
        return None
    root = Tree(data[0])
    data.pop(0)

    root.left = deserailize(data)
    root.right = deserailize(data)
    return root


root = deserailize(data)

dfs_recursive_trav(root)