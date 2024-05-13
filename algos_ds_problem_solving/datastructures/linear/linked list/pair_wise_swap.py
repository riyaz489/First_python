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

    def pair_wise_swap(self):
        # here we have to 2 element pairs position
        # for exmaple: -> 1,2,3,4,5,6,7 -> 2,1,4,3,6,5,7
        # so we swapped 1 and 2 then 3 and 4 and so on.
        # simple solution is to traverse left to right and then swap the data instead of links
        # but incase of large data this is not ideal solution to swap data.

        # to change links we have to below mentioned algo.
        # again we will keep 3 pointers (prev, cur,next).
        # ... i-2, i-1,i,i+1, i+2 ...
        # let say these i are indicies in list
        # if i-2 and i-1 already processed then our list will like this
        # i-1, i-2,    i,     i+1, i+2
        #      prev  curr      next
        # now join prev pair with current pair using prev.next = curr.next
        # replace i and i+1 nodes
        # then make i as prev. i+2 as curr and i+3 as next.


        # basically if we talk about pair i and i+1 then lets how these 2 links will be modified.
        # first lets talk about i+1 its next will become its prev element which is i. but if we do that then we will lost reminaing list
        # that's why take a backup of next first.
        # once i+1 is updated, now we have to set next for i. as we know now list will look like this
        # i+1-> i ; next = i+2
        # next of i will be next of next which is i+3, why is it so ?
        # because in normal scenario it should be i+2, but as know i+2 and i+3 are also going to swap in future
        # so i+3 will definitely come on left side. that's why we make i->i+3
        # and we will repeat these steps for all pairs.

        # lets take exmaple of 1->2->3->4->5
        cur = self.head # data =1
        # change the head in advance
        self.head = cur.next  #  data = 2
        prev = self.head # data =2

        while cur!=None and cur.next!=None:
            # taking backup of next, so that remaining list will not lost
            next = cur.next.next # `iteration are divide using ;`-> 3; 5

            # joining prev pair with current pair; so basically
            # prev value was first element of prev pair but due to swapping it become last element;
            # to join list prev pair with current we have to join prev pair last elem with current pair last element
            # (current pair last element will become first after swapping)
            prev.next = cur.next # `iteration are divide using ;`=> 2->2; 1->4;
            # basically first of prev pair in original list will join with last element of next pair in original list

            # making current pair first element as next of, current pair second element.
            cur.next.next = cur # `iteration are divide using ;`=> 2->1; 4->3

            # changing values
            prev = cur # `iteration are divide using ;`-> 1; 3
            cur = next # `iteration are divide using ;`-> 3; 5

        # if list has odd number of elements then joining last element to new list.
        prev.next = cur # 3->5
        # so final list look like this => 2->1->4->3->5

    def print(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


l = LinkedList(7)
l.insert(6)
l.insert(5)
l.insert(4)
l.insert(3)
l.insert(2)
l.insert(1)
l.pair_wise_swap()
l.print()
