# applications:
# single resource ad multiple consumers.
# synchronization between fast and slow devices.
# used in OS for scheduling jobs.


# impementation:
# in case of deque its O(1), as we simply remove rear element from array.
# but in case of enqueue we will insert new element at first index of array, so now we have to right shift
# all the remaining elements. So enqeue will become O(n).
# so make it big(1), we can use circular array.
# in case of enqueue we will add element towards rear and incase of dequeue we will remove element from front.
# now while removing from front we will simply change the head of queue to next index.


class LQueue():
    # insert at end and remove from front
    def __init__(self, capacity):
        self.start = 0
        self.size = 0
        self.data = [-1]*capacity
        self.capacity = capacity

    def enqueue(self, data):

        if self.size == self.capacity:
            print('overflow')
            return False
        # getting rear index
        rear_index = (self.start + self.size) % self.capacity
        self.data[rear_index] = data
        self.size+=1

    def dequeue(self):

        if self.size == 0:
            print('underflow')
            return False
        data = self.data[self.start]
        # moved the head
        self.start = (self.start + 1) % self.capacity
        print(data)
        self.size-=1
        return data

q = LQueue(3)
q.enqueue(1)
q.enqueue(2)
q.dequeue()
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.dequeue()
q.dequeue()

# for linked list implementation, maintain 2 pointers in linked list one is head and noather one is rear(which is last
# node in linkedlist).
# now for insertion add new node next to rear pointer and update rear pointer as new node.
# in case of deletion make head.next node as head. both operations are O(1)
# (insert at end and delete from front approach)


# implement stack using queue
# create 2 empty queue of same size.
# In case of push first we move a the items of q1 to q2.
# then insert new item to q1, then again move all items from q2 to q1.
# by doing so, when you perform dequeue on q1 then it will remove newly_added item only.
# notice at the time of insertion q2 will be empty initially.

# similarly we can implement queue using 2 stack, for every new item first move all data to stack to
# stack 2 then add new data to stack1 then again move all data frm stack2 to stack1, this will ensure
# new data will at bottom of stack1, which will be popped at last.

# reverse a queue
# simply first add all items to stack, then from stack push all items back to queue.

# reverse k items of a queue
# Create an empty stack.
# One by one dequeue items from a given queue and push the dequeued items to stack.
# Enqueue the contents of stack at the back of the queue.
# Reverse the whole queue.

# generate numbers with given digits in ascending order.
# for example with 5 and 6 generate 8 numbers -> [5,6,55,56, 65,66,555, 556]
# its simple create a queue then add digits given in ascending order let say digits are 3 and 6
# then 3 will be added first then 6 to queue -> [3, 6]
# then dequeue items from queue one by one and append given digits, and then push it back to queue
# for example, after dequeue we will get 3, and given digits are 3 and 6, so we will append 3 to 3 and 6 to 3
# so after one iteration queue will look like -> [6, 33, 36]
# similarly 6 will be popped and 3&6 will be added to it simultaneously and added to queue.
def sort_digits(digits):
    # using counting sort as we have only 0-9 digits
    digits = set(digits)
    res = []
    for i in range(10):
        if str(i) in digits:
           res.append(str(i))
    return res


def generate_numbers(digits, k):
    digits = sort_digits(digits)

    queue = [*digits]
    i=2
    while i <=k:
        cur_number = queue.pop(0)
        print(cur_number)
        for j in digits:
            queue.append(cur_number + j)
            i+=1
            if i>=k:
                break

    for i in queue:
        print(i)

generate_numbers(['8','3'], 10)

# max number in a k size subset of contiguous elements of a given sequence.
# for example: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
# k = 3
# Output :
# 3 3 4 5 5 5 6
# create a queue of k size and maintain only useful numbers.
#  An element is useful if it is in current window and is greater than all other elements on left side of
#  it in current window. so our queue front will always have largest numbers and queue rear will have lowest number.

def find_max_in_a_window(data, k):
    queue = [] # data will be stored in decreasing order from front to rear; so front will have max element
    # queue will store indicies only, and here indicies will be stored in ascending order. and data of those indicies will be decending order.
    front = 0
    rear = -1
    # do first k element iterations manually
    for i in range(k):

        # removing all item which are smaller than current item from rear
        while len(queue) != 0 and data[i] >= data[queue[rear]]:
            queue.pop(rear)
        queue.append(i)
    for i in range(k, len(data)):

        # first print prev window result
        print(data[queue[front]])

        # remove prev window data
        if queue[front] <= i-k:
            queue.pop(front)

        # removing all item which are smaller than current item from rear
        while len(queue) != 0 and data[i] >= data[queue[rear]]:
            queue.pop(rear)
        # pushing current index at the back
        queue.append(i)

    # print last window data
    print(data[queue[front]])

d = [1, 2, 3, 1, 4, 5, 2, 3, 6]
find_max_in_a_window(d,3)