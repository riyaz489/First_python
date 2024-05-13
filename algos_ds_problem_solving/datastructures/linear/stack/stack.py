# underflow: pop/peek operations done on empty stack
# overflow: push operation done on full stack

# its LIFO: as element last element will be out first.

# In linked list implementation simply insert new nodes as head (0th index)
# and while deletion remove data from head(0th index)
# and maintain a current_size and capacity variables in linked list to check overflow and underflow operations.


# Applications:
# 1. check balacned paranthesis -> {()} ; implementation without stacks will be very difficult as we have to
#    maintain opened brackets
# 2. reverse data
# 3. recursion calls use stacks
# 4. infix operations to postfix/prefix operations -> like a+b to +ab (prefix representation)
# 5. undo/redo operations. like we will maintain 2 stacks undo and redo. if do some undo
#   then we will move top item form undo operation
#   to redo stack and in case of redo we will move top item from redo to undo. and once we see that undo stack got
# new item which is not from redo, like user start doing some actions, which is then added to undo stack
# then we will clear redo stack.

# list stack example
l = []
l.append(1)
l.append(2)
l.append(3)
l.append(4)
print(l.pop())
# only capacity parameter is missing; that means we can put unlimited items. but len() is there to tell us current size




#### get_min in given stack in O(1) time complexity #######
# for example: stack = [5,4,8,6,1,9]
# get_min() -> 1 # it will not remove item fro stack, just show the current min value; pop()->9
# one naive way to do it in by creating a new auxiliary array.
# in new auxiliary array data will be filled together our original stack
# when stack is empty and we are pushing new element then same element will be pushed into auxiliary stack as well.
# next time we will push data into auxiliary stack only when new_data <= auxiallry_top
# and while popping item form original stack we will check if  popped item == auxiallry_top
# then we will pop data from aux array as well;
# so aux array will maintain min elements where top item will be current min and lower items are prev mins.
# but in worst case here we need O(n) aux space.

# another way to do in O(1) aux space
# here we will simply maintain a variable called current_min. and will modify original stack elements to
# get the previous min item. lets see how we do it using below algo.

# note: below algo only works if our stack items are >0.
# incase of first element, current_min will first item only.
# next time when we push data and new data <= current_min
# then this new data will be modified;
# modified_new_data = new_data - current_min
# then we will push this modified_new_data
# and our current_min will be new_data (unmodifed one)
# as you can notice modified_new_data will always be <=0 because when new_data <= current min then only we are doing
# this modification.

# so next time whenever we do pop oeration, we can simply check for -ve and 0 values. if popped item is <=0
# then we know it was the current_min value, because when we pushed it we knew it was <= current min
# that's why we modified and it ends up being -ve/0 value.
# now first we have to get back the original vlaue, so that we can show correct result to user.
# modified_poped_item = current_min
# and now as current min is removed from list so we have to fetch prev min.
# to do so we will simply do current_min = current_min - popped_item
# as popped_item = current_min - prev_min (push modification formula)
# => prev_min = current_min - popped_item


# now for if stack -ve items then we have to change the push and pop item modification.
# other things will remain same.
# push formula will be => new_modified_item = 2*new_item - current_min
# pop_formula will be  => prev_min = 2*current_min - popped_item
# also in pop condition will be changed, instead of checking for <=0 we will check if popped_item <= current_min
# now question is why popped_item <= current_min, when we see actual min value
# because while pushing as we know new_item <= current_min => new_item-current_min will always be <=0
# also push formula is modified_item = new_item + (new_item - current_min)
# => modified_item = new_item + (some negative value or zero)
# => modified_value will always be less than its original value.

# this approach only works for stack as only from one end we are doing pop/push, due to this
# we are able to maintain link between prev and current min. other wise in list case where we can insert anywhere
# below mentioned code will give random results.
class MinMaintainStack:
    def __init__(self):
        self.min_item = None
        self.data = []

    def push(self,x):
        if len(self.data) == 0:
            self.min_item = x
            self.data.append(x)
            return
        if x <= self.min_item:
            temp = 2*x - self.min_item
            self.min_item = x
            self.data.append(temp)
            return

        self.data.append(x)

    def pop(self):
        if self.peek() <= self.min_item:
            temp = self.min_item
            # updating min item
            self.min_item = 2*self.min_item - self.data.pop()
            # returning prev min item as popped item, as popped item was modified when pushed
            return temp
        else:
            return self.data.pop()

    def get_min(self):
        return self.min_item

    def peek(self):
        return self.data[-1]


s = MinMaintainStack()
s.push(5)
s.push(6)
s.push(7)
s.push(4)
s.push(1)
s.push(9)

print(s.get_min())
s.pop()
print(s.pop())
print(s.get_min())
