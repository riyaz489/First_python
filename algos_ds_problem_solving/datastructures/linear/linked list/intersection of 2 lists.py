class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def insert(self, data):
        cur = self.head

        new_node = Node(data)
        new_node.next = cur
        self.head = new_node
# intersection point of 2 list
# 1->2->3->5->6->7
#          |
#       8->9
# so here 5 is intersection point where 2 lists merges.
# one way is to traverse one list and put its nodes into hash set, then traverse second list
# and check hashset each time, if we found similar element then just print that element as result.
# another way is to find difference between lenght of 2 lists.
# let say difference is m. then we will skip m nodes from longest list and then traverse both the list
# with same speed, whenever we found similar element that will be or result.

# above approach will always work, as we know if 2 lists intersect then their last elements
# will always be common. in above example 5,6,7 is common. now we know first list has 1 more elements than second list.
# now if we start first list from 2 and second from 8 then we will reach to 5 on both lists at the ame time.
# which is our result.

def find_intersction_point(l1, l2):
    len_l1 = 0
    len_l2 = 0

    c1 = l1.head
    c2 = l2.head
    while c1 is not None:
        len_l1 += 1
        c1 = c1.next
    while c2 is not None:
        len_l2 += 1
        c2 = c2.next

    nodes_to_skip = abs(len_l1-len_l2)
    c1 = l1.head
    c2 = l2.head
    # let make c1 always bigger list
    if len_l1 < len_l2:
        c1, c2 = c2, c1
    while nodes_to_skip != 0:
        c1 = c1.next
        nodes_to_skip -= 1

    while c1!=c2 and c1 !=None:
        c1=c1.next
        c2 = c2.next

    if c1 !=None:
        print(c1.data)

l1 = LinkedList(6)
l1.insert(5)
temp = l1.head
l1.insert(4)
l1.insert(3)
l1.insert(2)
l1.insert(1)

l2 = LinkedList(9)
t2 = l2.head
l2.insert(8)
t2.next = temp

find_intersction_point(l2,l1)




