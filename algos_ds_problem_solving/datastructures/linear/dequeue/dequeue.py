# here we can insert and delete from both end front and rear.

# Applications of Deque: Since Deque supports both stack and queue operations, it can be used as both.
# The Deque data structure supports clockwise and anticlockwise rotations in O(1) time which can be useful in
# certain applications. Also, the problems where elements need to be removed and or added to both ends can be
# efficiently solved using Deque.

# Some Practical Applications of Deque:
# 1. Applied as both stack and queue, as it supports both operations.
# 2. Storing a web browser’s history.
# 3. Storing a software application’s list of undo operations.
# 4. Job scheduling algorithm

# to perform push_rear, push_front, remove_rear, remove_front in O(1) we have to use circular array.
# otherwise we will face similar issues which we faced in deleteion of head in normal queue. as in that case we have
# to shift all remaining elements. so to avoid that we will circular array.

class LDequqe:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.data = [-1]*capacity
        # rear will be calculated, so that's why we didn't stored it here.

    def push_front(self,x):
        if self.size == self.capacity:
            print('overflow')
            return False
        # moving one position back and inserting new data there and making it as new head.
        new_front = (self.front - 1) % self.capacity
        self.data[new_front] = x
        self.front = new_front
        self.size += 1

    def push_rear(self, x):
        if self.size == self.capacity:
            print('overflow')
            return False
        # finding end of list and pushing new node there.
        rear = (self.front+self.size)%self.capacity
        self.data[rear] = x
        self.size += 1

    def remove_rear(self):
        if self.size == 0:
            print('underflow')
            return False
        # just reduce the size
        rear = (self.front+self.size-1)%self.capacity
        print(self.data[rear])
        self.size -= 1

    def remove_front(self):
        if self.size == 0:
            print('underflow')
            return False
        print(self.data[self.front])
        # moving head to right
        self.front = (self.front+1)%self.capacity
        self.size -= 1

d = LDequqe(3)
d.push_rear(8)
d.push_front(4)
d.push_front(3)
d.push_front(2)

d.remove_rear()
d.remove_rear()
d.remove_rear()
d.remove_rear()


# min max operations, ket say we have two functions insert min and insert max
# in which user will always provide min and max values.
# now our task is to find and remove min max values
# so we will simply use dequeue for this, for min elements insert them in front
# and for max elements insert them at end.
# and while deletion user front and rear again, only these positions we will find min and max items.


# circular tour ##
# we have given 2 lists as input first contains petrol quantity and second contains distance to reach from current
# petrol pump to next petrol pump. and all these petrol pumps in circular path
# The task is to find the index of the first starting point such that the truck can visit all the petrol
# pumps and come back to that starting point.
# Input: arr1[6,3,7]
#        arr2[4,6,3]
# Output: 2

# naive approach: simply start from all points and check from which point we can do complte traersal
# efficient appraoch would be to create queue and then for each point check
# prev_petrol + currnt_petrol-current_distance >= 0 then push current petrol pump index to queue
# and update prev_petorl, otherwise if result is -ve then remove first item from queue
# and then recalculate prev_petrol.
# if queue front reaches to n+1 index then such traversal does not exists.
# or if queue size matches with array size and front ==rear then traversal exists.

# another efficient approach is :
# traverse all points
# If in the middle, at any petrol pump, the amount of petrol is less than the distance to be covered to reach
# the next petrol pump, then we can say we cannot complete the circular tour from start.
# Now we will ignore all previously travelled points and traverse next elements to find new start of petrol pump where
# the amount of petrol is
# greater than or equal to the distance to be covered
# and we mark it as start. Continue this process till all points are visited or a starting point is found.

def find_starting_point(data):
    prev_sum = 0
    current_sum = 0
    start_point = 0
    for i in range(len(data)):
        current_sum = current_sum + data[i][0] - data[i][1]

        # this is basically an observation, that if we found
        # negative now, that means its prev values could have +ve.
        # and current point need more petrol, which can be accumulated from pervious points
        # so now we have to make starting point from next to it.
        # because that's the only possibility now.
        if current_sum < 0:
            start_point = i + 1
            prev_sum += current_sum
            current_sum = 0

        # now check if prev remaining petrol and currently accumulated petrol is positive or not
        # if it is not,then it means no path is possible to traverse all pumps
    return start_point if current_sum + prev_sum >= 0 else -1


print(find_starting_point([[6, 4], [3, 6], [7, 3]]))