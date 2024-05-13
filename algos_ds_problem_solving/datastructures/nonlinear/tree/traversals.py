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

    def dfs_recursive_trav(self):
        print(self.data)
        if self.left:
            self.left.dfs_recursive_trav()
        if self.right:
            self.right.dfs_recursive_trav()

    def dfs_iterative_trav(self):
        # we will use stack as stack represent recursions
        # this is preroder traversal
        stack = [self]
        while len(stack):
            x = stack.pop(-1)
            if x:
                print(x.data)
                stack.append(x.right)
                stack.append(x.left)

    def dfs_iterative_trav_in_order(root):
        stack = []
        cur = root
        while True:

            # first append all left nodes
            if cur is not None:
                stack.append(cur)
                cur = cur.left

            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done

            # when cur become none that means we rached to lft most child for current subtree
            # now its time to print data and add right childs
            elif len(stack) != 0:
                cur = stack.pop()
                print(cur.data)
                # now in next iteration we will explore this right subtree.
                cur = cur.right

            else:
                # stack is empty and cur is also none that means we traversed complete tree
                break

    def bfs_iter_trav(self):
        queue = [self]
        while len(queue):
            # #### To find max width of binary tree just return the max temp value seen so far.
            # because queue will have all nodes of same level  before starting of x loop.
            temp = len(queue)
            for x in range(temp):
                current = queue.pop(0)
                print(current.data)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)


# inorder, postorder, preorder are just different variants of DFS.
# In each of them we simply change the root traversal.
# like in Inorder -> Left, root, right
# preorder -> root, left,right
# postorder -> left,right,root
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data)
        in_order_traversal(root.right)
def pre_order_traversal(root):
    if root:
        print(root.data)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.data)

def print_nodes_at_level_k(root, k):
    # another way is to use BFS function
    if not root:
        return
    if k==0:
        print(root.data)
    else:
        print_nodes_at_level_k(root.left, k-1)
        print_nodes_at_level_k(root.right, k-1)


# print left view of tree and at certain level if left child not exists then print leftmost right child.
# for example:
#     5
#    / \
#    4  6
#        \
#         8
# output -> 5, 4, 8
def left_view_recursive(root):
    max_level = 0

    def left_view(root, level):
        nonlocal max_level
        if root is None:
            return
        if max_level < level:
            # that means we are first time visiting current level
            # we will make it same so that no other node of same level could visit it.
            max_level = level
            print(root.data)

        left_view(root.left, level+1)
        left_view(root.right, level+1)
    left_view(root, 1)

def left_view(root):
    # here we will simply use dfs traversal, only print first item in queue
    queue = [root]
    while queue:
        temp = len(queue)
        for i in range(temp):
            data = queue.pop(0)
            # only change is, we are printing only first item of current level.
            ### similarly for right view we will print only last item in queue
            if i==0:
                print(data.data)
            if data.left:
                queue.append(data.left)
            if data.right:
                queue.append(data.right)
            # we are forced to traverse all nodes, as we don't know at given level which is the leftmost node.

# print top view of tree
# to solve this we have to calculate horizontal distance of each node. let say root node is at 0.
# then its left child will be -1 and right child will be +1.
# using this we recursively we will calculate horizontal distance and then. we will print first
# seen unqiue horizontal distance node.

# for bottom view approach will be same only difference will be, instead of first seen unique horizontal distance
# we will print last seen node with given horizontal distance.
def print_top_view(root):
    queue = [(root, 0)]
    horzintal_dis_seen = set()
    while len(queue)>0:
        node_data = queue.pop(0)

        # if distance not seen then print it and add it to set
        if node_data[1] not in horzintal_dis_seen:
            print(node_data[0].data)
            horzintal_dis_seen.add(node_data[1])

        # adding left and right child to queue
        if node_data[0].left:
            queue.append((node_data[0].left, node_data[1]-1))
        if node_data[0].right:
            queue.append( (node_data[0].right, node_data[1]+1))
def print_bottom_view(root):
    queue = [(root, 0)]
    horzintal_dis_node_map = {}  # horizontal distance and node mapping
    while len(queue) > 0:
        node_data = queue.pop(0)

        # updating map with new node of same horizontal distance
        horzintal_dis_node_map[node_data[1]] = node_data[0]

        # adding left and right child to queue
        if node_data[0].left:
            queue.append((node_data[0].left, node_data[1] - 1))
        if node_data[0].right:
            queue.append((node_data[0].right, node_data[1] + 1))
    # printing all last nodes for given horizontal distance
    for i,j in horzintal_dis_node_map.items():
        print(j.data)

def vertical_traversal(root):
    # IF we draw a vertical line then whatever nodes lie in same line will have same horizontal positions (in mean
#  nodes with same x axis will lie on same vertical line).
    # now our task is to print all nodes with same x axis togeather.
    # for this we will traverse bfs ways and while traversing we will pass left child x axis values
    # parent x axis -1 and right will be plus 1.
    # same approach we followed for top view.
    if root is None:
        return
    res_dict = {}
    queue = [(root, 0)]
    min_height = float('inf')
    max_height = float('-inf')
    while queue:
        temp = len(queue)
        for i in range(temp):
            current_node = queue.pop(0)
            if current_node[0].left:
                queue.append((current_node[0].left, current_node[1]-1))
            if current_node[0].right:
                queue.append((current_node[0].right, current_node[1]+1))
            if current_node[1] in res_dict:
                res_dict[current_node[1]].append(current_node[0])
            else:
                res_dict[current_node[1]] = [current_node[0]]
            min_height = min(min_height, current_node[1])
            max_height = max(max_height, current_node[1])

    # for remaining items in queue
    for i in range(min_height, max_height+1):
        # similarly we can find vertical sum by doing sum of each list here
        print([j.data for j in res_dict[i]])

def spiral_traversal(root):
    # first traverse right to left for first row, then for next row left to right and so on.
    # we will use bfs approach with 2 stacks instead of single queue.
    # alternating level child will be stored in separate stacks. like level1 items in stack1, level2 in stack2
    # level3 in stack1 again and so on. as stack reverse the data, so this will help us to reverse the direction of
    # traversal on every level change.

    st1 = [root]
    st2 = []

    reversed = False

    while len(st1) or len(st2):

        if reversed:
            temp = len(st2)
        else:
            temp = len(st1)

        for i in range(temp):
            # pop from one stack and push its child into another stack to print child data in reverse order than of
            # parent.
            if reversed:
                item = st2.pop()
                if item.right:
                    st1.append(item.right)
                if item.left:
                    st1.append(item.left)
                print(item.data, end='')
            else:
                item = st1.pop()
                if item.left:
                    st2.append(item.left)
                if item.right:
                    st2.append(item.right)
                print(item.data, end='')

        # toggling reversed flag for next row
        reversed  = not reversed
        print('\n')

def find_path_for_node(root, data, path=[]):
    # find path from first ancestor to required data node.
    if root is None:
        return []
    if root.data == data:
        return path
    # adding current node in path
    path.append(root.data)
    # check data in left or right nodes
    # if not found in left and right subtree then we are returning empty list which is false in bool.
    if find_path_for_node(root.left, data, path) or find_path_for_node(root.right, data, path):
        return path

    # if node not found in left and right subtree
    # then remove current node from path
    path.pop(-1)
    return []


root = Tree(5)
root.insert(12)
root.insert(7)
root.insert(18)
root.insert(69)
root.insert(4)
root.insert(13)
left_view(root)