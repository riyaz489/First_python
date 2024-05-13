class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def dfs_recursive_trav(root):
        print(root.data)
        if root.left:
            dfs_recursive_trav(root.left)

        if root.right:
            dfs_recursive_trav(root.right)

# build tree from postorder & inorder or preorder & inorder lists.
# note we can not get tree from postorder and preorder combination, we need inorder to find left and right child.


# idea is simple
# preorder  -> Root, left, right
# inorder -> left, root, right
# in preorder first item seen in list always a root
# now first we look in preorder we found that first item is root.
# now we find root node in in_order list. lets say it present on k index.
# then items on left side of k index will be left child subtree and items on right side will be right child subtree.
# if we traverse preorder list in preorder way we could have got generated complete tree. but resultant tress will be
# skewed on left side. so to find where right and left subtree ends we used inorder list.

def generate_tree_from_pre_inorder(inorder, preorder):
    st = 0
    en = len(inorder)-1

    inorder_dict_map = {} # this will give us key of data in O(1)
    for i in range(len(inorder)):
        inorder_dict_map[inorder[i]] = i
    preorder_ind = 0

    def rec_gen_tree(inorder, preorder, st, en):
        nonlocal preorder_ind
        if st>en:
            return None
        # as we are running in preorder way then we can simply do preorder index ++;
        node = Tree(preorder[preorder_ind])
        preorder_ind+=1

        # now look for data index in inorder to find left and right items.
        root_index = inorder_dict_map[node.data]

        # add left and right child recursively
        # we reduced the lenght of preorder list using key index found in inorder.
        node.left = rec_gen_tree(inorder, preorder, st,root_index-1)
        node.right = rec_gen_tree(inorder, preorder, root_index+1, en)

        return node
    return rec_gen_tree(inorder,preorder,st,en)

# as in postorder last items are root, so we will traverse postorder list from right to left.
def generate_tree_from_post_inorder(inorder, preorder):
    st = 0
    en = len(inorder) - 1

    inorder_dict_map = {}  # this will give us key of data in O(1)
    for i in range(len(inorder)):
        inorder_dict_map[inorder[i]] = i
    preorder_ind = en

    def rec_gen_tree(inorder, preorder, st, en):
        nonlocal preorder_ind
        if st > en:
            return None
        # as we are running in preorder way then we can simply do preorder index ++;
        node = Tree(preorder[preorder_ind])
        preorder_ind -= 1

        # this means current node has no child
        if (st == en):
            return node
        # now look for data index in inorder to find left and right items.
        root_index = inorder_dict_map[node.data]

        # add left and right child recursively
        # we reduced the lenght of preorder list using key index found in inorder.

        # now as we reversed the list so right child comes first.
        node.right = rec_gen_tree(inorder, preorder, root_index + 1, en)
        node.left = rec_gen_tree(inorder, preorder, st, root_index - 1)


        return node

    return rec_gen_tree(inorder, preorder, st, en)

in_order = [20,10,40,30,50]
pre = [10,20,30,40,50]
post_order = [20,40,50,30,10]
t = generate_tree_from_post_inorder(in_order, post_order)
dfs_recursive_trav(t)