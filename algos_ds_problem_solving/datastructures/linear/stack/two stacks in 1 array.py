# we will store 2 tack in array
# one will put data from front another one will put data from end in single array
class TwoStacks:
# this is cache friendly due to locality of reference
    def __init__(self, capacity):
        self.capacity = capacity
        self.top1 = -1
        self.top2 = capacity
        # initializing array
        self.data = [0]*capacity

    def push1(self, x):
        # incase stack is empty then it will check for full capacity as top2 initialized as capacity.
        if self.top1+1 >= self.top2:
            raise ' stack overflow exception'
        else:
            # for stack1 we could have simply maintained insert and deletion from index 0 only, but that is not O(1)
            # as we have to move remaining elements to right. but incase of linkedlist we could have done that
            # and for second stack always delete and insert from last. but in case f linked list we cold have lost the
            # benefit of locality of refernce for caching, as new nodes will take new memory.
            self.top1+=1
            self.data[self.top1] = x

    def pop1(self):
        if self.top1 == -1:
            raise ' underflow exception'
        else:
            res = self.data[self.top1]
            self.top1 -= 1
            return res


    def push2(self, x):
        # here we will move from right to left while insertion
        # in case stack 1 is empty, then it will check for -1
        if self.top2 - 1 <= self.top1:
            raise ' stack overflow exception'
        else:
            self.top2 -= 1
            self.data[self.top2] = x


    def pop2(self):
        # while deletion we will move towards right
        if self.top2 == self.capacity:
            raise ' underflow exception'
        else:
            res = self.data[self.top2]
            self.top2 +=1
            return res

t = TwoStacks(3)
t.push1(1)
t.push1(2)
t.push2(3)
print(t.pop2())
# print(t.pop2())
print(t.pop1())