class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def print(self, head):
        cur = head
        while cur is not None:
            print(f'cur -> {cur.data} | random-> {cur.random.data}')
            cur = cur.next

    def insert(self, data):
        cur = self.head

        new_node = Node(data)
        new_node.next = cur
        self.head = new_node


    # this random pointer linked list, has one more pointer, which is random pointer.
    # here next will give item but random can point to any pointer, it can be prev node, next node or current node.

    # for example:
    #             __
    #            |  |
    # 1-> 2-> 3->4 <-
    # ^       |
    # |_______|
    # here 3 random pointer points to 1 and 4 random pointer points to itself .

    # and clone means, nodes will be new but data will be same.

    def clone_random_pointer_list(self):
        # simple way is to first traverse list from left to right and we will store data into dict, here in dict
        # key will be current node and value will be new_node with same data.
        # then when we again traverse data from left to right, we will update next and random pointer of new nodes.
        # but the problem is not every type of node can be hashable, because for dict key items should be able to
        # hashable.

        # so what we can do, for each node, instead of storing clone nodes in hash we can simply store, new values
        # as its next node. so always cur.next will be its clone item. so it will look like this
        # 1-> clone_1 -> 2 -> clone_2
        # once nodes are created and mapping is done we can simply, remove clone nodes and make new clone list.
        # so here clone1.next = clone1.next.next
        # and clone1.random = 1.random.next # as next items are clone ones

        cur = self.head

        # adding new nodes next to current nodes
        while cur!=None:
            new_node = Node(cur.data)
            # we can not do random mapping yet, as random node can be last node, for which new node is not added yet
            new_node.next = cur.next
            cur.next = new_node

            cur = cur.next.next

        # adding random mapping
        cur = self.head
        while cur!=None:
            # adding new node random as next item of cur.random
            cur.next.random = cur.random.next
            # can not remove new items from list yet, as next new node random can point to prev new node nodes.
            cur = cur.next.next

        # removing new nodes and creating new list
        new_head = self.head.next
        prev_clone_node = new_head
        cur = self.head
        cur.next = prev_clone_node.next
        cur = cur.next
        while cur!=None:
            # link prev and curr clone node
            cur_clone_node = cur.next
            prev_clone_node.next = cur_clone_node
            # remove new node
            cur.next = cur_clone_node.next

            # updating vars for next iteration
            cur = cur.next
            prev_clone_node = cur_clone_node
        return new_head

l1 = LinkedList(3)
th = l1.head
l1.insert(2)
tw = l1.head
l1.insert(1)
on = l1.head
l1.insert(0)
ze = l1.head

on.random = on
tw.random = on
th.random = tw
ze.random = ze
l1.print(l1.head)

l2 = l1.clone_random_pointer_list()

print()
l1.print(l2)
print()
l1.print(l1.head)
