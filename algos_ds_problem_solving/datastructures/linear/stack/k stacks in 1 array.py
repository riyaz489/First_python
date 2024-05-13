# idea is simple we will be having 3 arrays, one of n size to store our data
# second will be k size to store top item of k stacks and third array of size n is to store next available index.
# and that third array will also store previous top values for each stack once next_available values is used.
# because it will help us to go back list.

# let say n=5 and k=3
# so our k array will look like this -1,-1,-1
# and our next array will look like this 1,2,3,4,-1; as after 4th index list will be full that's why last item is -1
# and variable next_available_index = 0
# now let say we do below operations:
# push; stack1; data=1 -> k=[0,-1,-1] -> next = [-1,2,3,4,-1] -> data = [1,] ; next_available_index = 1
# as you can notice we update
# then we updated next array, here 0th index is updated with previous top value of stack1
# (so that we can go back in list for given stack)
# then we updated stack1 top with current utilized next_available_index which was 0;
# then we updated data array at index 0 ( index came from next_available_index)
# then we updated next_available_index from 0 to 1 which we took from next 0th index. (to store next item for any stack)

# push; stack2;data 2 -> k=[0,1,-1] -> next = [-1,-1,3,4,-1] -> data = [1,2] ; next_available_index = 2
# push; stack2;data 3 -> k=[0,2,-1] -> next = [-1,-1,1,4,-1] -> data = [1,2,3] ; next_available_index = 3
# push; stack3;data 4 -> k=[0,2,0] -> next = [-1,-1,1,-1,-1] -> data = [1,2,3, 4] ; next_available_index = 4
# push; stack1;data 5 -> k=[4,2,0] -> next = [-1,-1,1,-1,0] -> data = [1,2,3, 4 ,5] ; next_available_index = -1

# pop; stack2; -> top of stack 2 is 2->k=[4,1,0] ->  next = [-1,-1,-1,-1,0] -> data = [1,2, 4 ,5] ; next_available_index = 2
# during pop time we first poped data from top index of stack 2
# then we figured out what was the previous top for index at 2 and it was 1(with the help of next array);
# so we changed its values in k array to 1.
# then we put current next_available_index into next array at same index 2.
# because we can use next_available_index later, that's we put it into next array
# changed next_available to 2 as 2 is now available.


# if you notice here k size array and next array make a link here which helps us to retrieve old items for each stack.
# but getting index from next array to push data is random, as it will return whatever is next available.
# but for 2nd top item for a given stack we can simply visit top index in next array then it will give us the
# prev top index. i.e
# top_index_of_stack2 = k[1]
# prev_top_index_of_stack2 = next[k[1]] # as in next we are storing prev top index whenever we are utilizing new index.

class KStacks:
    def __init__(self, total_array_capacity, number_of_stacks, ):
        self.capacity = total_array_capacity
        self.num_of_stacks = number_of_stacks
        self.top = [-1]*self.num_of_stacks
        self.data = [None]*self.capacity
        self.next = [i for i in range(1,self.capacity)]
        # putting -1 on last index of next, as after second last index in next,
        # we don't have any new next index to put data
        self.next.append(-1)
        # this variable will keep pulling next available indices from next array
        self.next_available_index = 0

    def push(self, stack_no, x):
        # taking backup of current avaiable index
        current_available_index = self.next_available_index # it will become 0
        # updating var from next array for next iteration
        self.next_available_index = self.next[self.next_available_index] # it will become 0 to 1
        # updating next index which is utilized right now, with previous top value
        # 0th index of next is utilized by -1 of current stack
        self.next[current_available_index] = self.top[stack_no] # next[0] will become -1
        # updating stack top with newly utilized index
        self.top[stack_no] = current_available_index # top[stack_no] = 0
        # updating data in list
        self.data[current_available_index] = x

    def pop(self, stack_no):
        current_stack_top = self.top[stack_no]

        # first remove the data from array
        print(self.data[current_stack_top])
        self.data[current_stack_top] = None

        # then update stack top with previous top index
        self.top[stack_no] = self.next[current_stack_top]

        # then put currently available index back to next array, as we got one more free index now
        # and we will put it on current_stack_top index, as it is free now
        self.next[current_stack_top] = self.next_available_index
        # now we will use current_stack_top(which is free now) for next push operation
        self.next_available_index = current_stack_top

    def is_full(self):
        # if it is equal to -1 then it means no next space available to fill data
        return self.next_available_index == -1

    def is_empty(self, stack_no):
        # if given stack top is -1 then it means it is empty.
        return self.top[stack_no] == -1

k = KStacks(number_of_stacks=3, total_array_capacity=5)
k.push(0,1)
k.push(0,2)
k.push(1,4)
k.push(1,5)
# k.push(0,1)
print(k.is_empty(1))
print(k.is_full())
k.pop(0)
k.pop(0)
k.pop(1)
