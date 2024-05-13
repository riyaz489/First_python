# here each node will have prev and next pointer address.
# its can be traversed in both direction
# also we can delete/insert/traverse prev nodes in O(1)
# but in normal linked if we want to delete prev node of a given node, then it will need traversal again.

# like when we are storing browser history and we have to go back and forward, in that case we can use
# double linked list.
# but its disadvantage is it is more complex and need more space than single linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    # insert at 0
    # first check if head exists, if it is then mark head.prev = new node and next of new_node as head
    # and mark new node as head.
    def insert_at_begin(self, data):
        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    # insert at end
    # go to the last element. make last element next as new node and new node prev as last elem.
    def insert_at_end(self, data):
        new_node = Node(data)
        head = self.head
        # exceptional case if head is None
        if head is None:
            self.head = new_node
            return
        while head.next is not None:
            head = head.next

        head.next = new_node
        new_node.prev = head

    # reverse
    # simple replace prev and next pointer. prev become next and next node become prev.
    def reverse(self):
        if self.head is None:
            return None
        cur = self.head
        while True:
            cur.next, cur.prev = cur.prev, cur.next

            # As prev represent next elem now so we use prev to find if this is the last element
            # if it is then update head and break the loop
            if cur.prev is None:
                self.head = cur
                break
            # going to next elem, which is prev now
            cur = cur.prev

    # delete head
    # fetch next element of head and make its prev as null
    def delete_from_begining(self):
        if self.head is None:
            return -1 # nothing to delete
        self.head = self.head.next
        self.head.prev = None

    # delete from end
    # fetch  last elem and make its prev elem next as null
    def delete_from_end(self):
        if self.head is None:
            return -1 # nothing to delete
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.prev.next = None

    def traverse(self):
        cur = self.head
        if cur is None:
            print('empty')
            return
        while cur is not None:
            print(cur.data)

            cur = cur.next

dlk = DoublyLinkedList()
dlk.insert_at_begin(2)
dlk.insert_at_begin(1)
dlk.insert_at_end(3)
dlk.reverse()
dlk.traverse()
dlk.delete_from_begining()
dlk.delete_from_end()
dlk.traverse()