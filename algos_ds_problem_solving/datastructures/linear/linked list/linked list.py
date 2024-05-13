# why linked list over array:
# 1. array is if fixed size
# 2. insertion and deletion from middle is costly, as we have to move right side elements. and also while insertion if
# if array size is lower then, our compiler will allocate new continues space and move all the elements there which
# will be O(n)
# 3. implementation of queue and deque is easier.
# 4. for merging smaller arrays into larger sorted array(basically merge sort), we don't need auxiliary space in case
# of linked list, we can shuffle same elements without needing extra auxiliary space.
# 5. worst case for insertion/deletion at beginning is O(1).
# and worst for end and middle element is also O(1) if we knew the previous node pointer.

# Disadvantages of Linked Lists:
# 1. Random access is not allowed in Linked Lists. We have to access elements sequentially starting from the first node.
# So, we cannot do a binary search with linked lists efficiently with its default implementation.
# Therefore, lookup or search operation is costly in linked lists in comparison to arrays.
# 2. Extra memory space for a pointer is required with each element of the list.
# 3. Not cache-friendly. Since array elements are present at contiguous locations, there is a locality of reference
# which is not there in the case of linked lists.
# locality of reference -> the tendency of a processor to access the same set of memory locations repetitively over a
# short period of time.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def insert(self, data, index=-1):
        # index = -1 represent insertion at last
        cur = self.head
        curr_index = 0

        if index == 0:
            # insert at the beginning
            new_node = Node(data)
            new_node.next = cur
            self.head = new_node
            return

        while cur.next is not None and (index == -1 or curr_index < index-1):
            cur = cur.next
            curr_index += 1
        new_node = Node(data)
        new_node.next = cur.next
        cur.next = new_node

    def search(self, x):
        cur = self.head
        index = 0
        while cur is not None:

            if cur.data == x:
                return index, cur
            cur = cur.next
            index += 1
        return -1

    def print(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def reverse(self):
        # just making next of current element to prev element
        cur = self.head
        prev = None
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            if temp is None:
                self.head = prev

    def delete(self, index=-1):
        cur = self.head
        cur_index = 0
        # removing first node
        if index == 0:
            self.head = self.head.next
            return
        # -1 case is for last node
        while cur.next.next is not None and (cur_index < index-1 or index == -1):
            cur = cur.next
            cur_index += 1
        cur.next = cur.next.next

    def sort(self, head):
        # merge sort
        if head.next is None:
            return head

        mid = self.get_middle_elem(head)
        left = head
        right = mid.next
        # breaking the linked list
        mid.next = None
        new_left = self.sort(left)
        new_right = self.sort(right)
        self.head = self.merge_sort(new_left, new_right)
        return self.head

    def merge_sort(self, left:Node, right:Node):
        # just compare and left and right elements and merge them on the basis of condition
        # creating a temp node as head, later we will remove it from result
        temp_head = Node(-1)
        cur = temp_head
        while left is not None and right is not None:
            if left.data < right.data:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        # adding remaining elements. note: at this point either left or right list has some elements, not both.
        if left is None:
            cur.next = right # adding right chain remaining elements.
        else:
            cur.next = left # adding left chain remaining elements.

        # removing temp head we created
        return temp_head.next

    def get_middle_elem(self, head):
        # using fast and slow pointer approach, or we can say tortoise and hase approach
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def delete_node_with_given_pointer(self, node):

        # to delete node in O(1) we can simple its next value in given node then delete the next node.
        node.data = node.next.data
        node.next = node.next.next
        # note: but this won't work if given node is last node. so for that we have to traverse all the way
        # to second last elem and change its next.

    def get_kth_node_from_end(self, k):
        # use 2 pointers which will move with same speed. but second pointer will start from kth node.
        # as distance between i and j is k, so when j reach to last element n,  then i will be at n-k element.
        # 0,      1 ,  2,  ....  k       ...   k from end  ...  n
        # i start              j start         i end           j end

        # todo: check k should be less than lenght of list.
        count = 1
        first_pointer = self.head
        # first move first pointer
        while count <k:
            first_pointer = first_pointer.next
            count+=1

        second_pointer = self.head
        while first_pointer.next is not None:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        print(second_pointer.data)

    def reverse_recursive(self):
        # idea is simple first traverse frm left to right.
        # then while coming back from recursive calls from right to left change returned_item.next = current elements.
        # where returned item was next item of current item in original list.
        # to reverse the list.

        # handled all exceptional case
        if self.head is None or self.head.next is None:
            return

        def recursive_rev(cur):

            if cur.next is None:
                # making last node as head
                self.head = cur
                # that means we reached to last node. we will return it.
                return cur

            # first we traverse left to right
            next_node = recursive_rev(cur.next)

            #now we have started all recursive calls and
            # now we are going back from right to left.
            # now we have next node and current node.
            # so we will simply have to make next of next_node to current node, to reverse the list.
            next_node.next = cur
            # making curr element as last element by making it next as null.
            # now if we have further parent stack calls remaining then its next will be assigned, which will be previous
            # element , otherwise its next will be remained null only.
            cur.next = None
            return cur

            # recursive call stack
            # 1
            # 2 # if we are here then here cur will be 2 and next will be 3 which is returned from bottom function
            #  3

        recursive_rev(cur=self.head)

    def reverse_groups_of_size_k(self, k):
        # for exmaple: 1,2,3,4,5,6,7 ; k=2 -> 2,1, 4,3, 6,5, 7

        if k<1 or self.head is None:
            # if k is greater than list size then we will simply reverse whole list,
            # instead of raising exception
            return

        # this will be used to re-assign head for the first pass, like in above example first pass is 1,2 and
        # head become 2 now
        first_pass = True

        cur = self.head

        # this will be used to join current and previous grp which is now reversed
        previous_first_node = None

        while cur != None:
            # keeping track of current first node, so that we can update previous_first_node for next iteration
            current_first_node = cur
            prev = None
            counter = 0
            while counter < k and cur !=None:
                # same logic is singly linked list reverse method; extra part iis below if else condition
                # which is used to change head and join grps after reversing sub-lists.
                next_item = cur.next
                cur.next = prev
                prev = cur
                cur = next_item
                counter+=1

            # if just start of the list then justchange head
            if first_pass:
                # current group last element(which now becomes first element)
                self.head = prev
                first_pass = False
            else: # else if we are in middle of list then join previous and current grp.
                # joining prev first node first element (which is now last element )with current group
                # last element(which now becomes first element)
                previous_first_node.next = prev

            previous_first_node = current_first_node

    def detect_and_remove_loop(self):
        # we will use floyds algo (details in one note notes)

        # to detect we will run 2 pointers slow and fast, here fast will move as 2 as speed of slow.
        # if those 2 match then it means we have loop
        slow = self.head
        fast = self.head

        while fast!= None and fast.next !=None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break
        else:
            # as loop is not breaked and fast become none.
            # that means there is no loop.
            return

        # in next step to remove the loop, to do that first we have to start point of loop. let say start point of loop
        # is m, after finding m we have to go m-1 node and set its next to null, instead of m node to remove the loop.
        # for example:
        # a->b->c->d->e->f->f->g->h   =>   a->b->c->d->e->f->g->h-> null;
        #             |___________|
        # so as you can see if loop start at e then e-1 are two nodes d and h.
        # to remove the loop we have to set next of h to null.

        # exceptional case when head is the starting point of the loop.
        if slow == self.head:
            # according to the algo we need to skip m nodes to reach to the starting point of the loop. here m
            # is the distance between head and the point where fast and slow pointer meet again.
            # but this distance will be 0 when starting point of loop is head only.
            # that means we already reach to the starting point, if fast == last and these 2 are also equal to head.
            # so we don't have to run below `while slow.next != fast.next:` while loop in this case as we can modify
            # list here only.

            # Now we have to go to the last element and make its next as null.
            # as we already reached to the starting point of loop and  slow is already equal to
            # fast pointer which is then equal to head. but we don't want that, we wanted
            # m(starting point of loop) - 1 node. which we will achieve using below loop.
            while slow.next != self.head:
                slow = slow.next
            slow.next = None
            print(f'cycle detected at Head of the list, changing last {slow.data} next to fix the list')
            return


        # to find the start point of loop, just set of the pointer to head node value again.
        # and now move both of them at same speed, when again they become equal that means we got the loop starting
        # point.
        slow = self.head

        # note: here instead of comparing slow and next direct we are checking their next values.
        # as we want to reach nodes before starting point (as discussed above), so that we can remove the loop.
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

        # as we changes slow with head, so according to above example
        # slow will be equal to d and fast will be equal to h

        fast.next = None
        print(f'cycle detected at {slow.next.data}, changing {fast.data} next to fix the list')

    def segregate_even_odd_numbers(self):
        # in -> 1,2,3,4,5,6,7; out-> 2,4,6,1,3,5,7 ; put all even elems first then odd ones in list.
        # idea is simple, we will create 2 sub list one for odd and another one for even, traverse  input list
        # and populate even odd sub lists. (as in linked list we have nodes which can we can move easily, so we don't
        # need extra space to store sublists, we can move original list nodes into these ub lists.)
        even_start, odd_start, even_end, odd_end = None, None, None, None
        cur = self.head
        while cur is not None:
            if cur.data % 2 == 0:

                if even_start is None:
                    even_start, even_end = cur
                else:
                    # adding cur to even list
                    even_end.next =cur
                    # updatng even end to latest element.
                    even_end = cur
            else:
                if odd_start is None:
                    odd_start, odd_end = cur
                else:
                    # adding cur to even list
                    odd_end.next =cur
                    # updatng even end to latest element.
                    odd_end = cur

            if even_start is None:
                # that means we have all odd elements
                self.head = odd_start
            elif odd_start is None:
                # that means we don't have odd elements
                self.head = even_start
            else:
                # otherwise we will join the 2 lists.
                self.head = even_start
                even_end.next = odd_start

    def check_palindrome(self):
        # naive approach is to first traverse list from left to right and put all elements into stack
        # the traverse again from left to right and then check element from stack top elements.
        # if it matches then remove top elem and move to next element in linked list
        # else return false

        # another approach is to find middle element and then reverse list nodes after mid element.
        # then start from 0th item and another pointer from mid+1 item and compare the nodes, if same then proceed further
        # else return false.

        if self.head is None or self.head.next is None:
            return True

        # first find mid
        fast, slow = self.head, self.head

        while fast != None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next

        # now break the list and reverse half of the list, which start from next of slow
        temp_head = slow.next
        breaking_point = slow
        slow.next = None
        temp_cur = temp_head
        prev = None
        while temp_cur!=None:
            temp_next = temp_cur.next
            temp_cur.next = prev
            prev = temp_cur
            temp_cur = temp_next
        temp_head = prev
        fast = temp_head
        slow = self.head
        # now check the reversed and first half of the list
        while fast!=None:
            if fast.data != slow.data:
                # now if we want to get original list again then simple reverse the temp_head list again
                # then join breaking_point.next = temp_head
                return False
            else:
                fast = fast.next
                slow = slow.next
        # now if we want to get original list again then simple reverse the temp_head list again
        # then join breaking_point.next = temp_head
        return True

    def  removeDuplicatesFromSortedList(self):
        cur = self.head

        # as after last elements there will be no duplicates that why we are running loop till last element
        # where last element is not included
        while cur.next != None:
            # if we found similar element then don't mve cur and keep removing duplicates.
            # as list is sorted so all duplicates will be next to each other.
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            # if we find different element, then move the cur to next elem.
            else:
                cur = cur.next

head = LinkedList(1)
head.insert(1)
head.insert(1)
head.insert(2)
head.insert(2)
head.insert(3)
head.removeDuplicatesFromSortedList()
head.print()



