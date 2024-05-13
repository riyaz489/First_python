# In Circular linked list last node next points to head
# advantages: we can traverse whole list from any point; exmaple-> we can use it in round robin.

# we create doubly circular linked list as well, I mean its feasible to create one.
# we can get previous node  in O(1) without maintain tail pointer. in case of doubly circular linked list




class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # traversal -> we will check if we again reach to head or not.
    # empty list and only head in list will be exceptional case.
    def traverse(self):
        if self.head == None:
            return

        cur = self.head
        print(cur.data)
        cur=cur.next
        while cur != self.head:
            print(cur.data)
            cur = cur.next



    # insert at beginning- > first we have to add new node as head. but now the problem is now we have to
    # update last node next-pointer as well. because now head is changed and last node is still pointing to previous head.
    # well there is 2 ways to do it in O(1). if we maintain tail pointer then we can simply add new item after tail
    # and then make new last elem as head. or we can insert this item in second position and then replace data of first node
    # and second node. in below function we will use second approach as we ar not maintaining tail pointer.
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head

        # insert new node at 2nd place
        new_node.next = self.head.next
        self.head.next = new_node

        # now swap data, to make new node as head. and we don't have to change  next of tail of linked list.
        # as it already pointing to existing head. and we didn't changed head, we just changed its data.
        self.head.data, new_node.data = new_node.data, self.head.data

    # insert at end -> we insert data at second position, then we swap data of head and second element and then we mark
    # second element as head.
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head

        # so here first we are creating required chain, then pointing head to right place.
        # first insert at second pos again
        new_node.next = self.head.next
        self.head.next = new_node

        # swap data
        self.head.data, new_node.data = new_node.data, self.head.data

        # mark second node as head, as head will be same data node.
        self.head = new_node


    # DELETE HEAD -> take backup of second node, then delete second node and then replace head node data with second
    # node data
    def delete_head(self):
        if self.head is  None:
            return
        if self.head.next == self.head:
            # only 1 node is present
            self.head = None
            return

        # copying second node data into head, now second and head node has same data.
        self.head.data = self.head.next.data

        # delete second node
        self.head.next = self.head.next.next

    # delete end node or node between head and last node -> traverse to k-1 node, then do k.next = k.next.next
    def delete_end_or_k_node(self, k=-1):
        # k is greater than length of list then return -1

        # its logic same as singly linked list
        # k=-1 means last node
        if self.head is  None:
            return
        if self.head.next == self.head:
            # only 1 node is present
            self.head = None
            return

        if k == 1:
            self.delete_head()
            return

        cur = self.head
        i = 1
        while (k == -1 and cur.next.next != self.head) or i < k-1:
            cur = cur.next
            i += 1

        # now we are at previous element of k.
        cur.next = cur.next.next


cl = CircularLinkedList()
cl.traverse()
cl.insert_at_begin(1)
cl.insert_at_end(2)
cl.insert_at_end(3)
cl.insert_at_begin(0)
cl.traverse()
# cl.delete_head()
cl.delete_end_or_k_node(4)
cl.traverse()