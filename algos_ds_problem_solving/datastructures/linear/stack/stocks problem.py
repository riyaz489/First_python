# basically in Stock span problem, we have to found out number of continues previous days where sotcks
# price were less than current day stocks price. and in result current day will also be included.
# for example: 50,10,20,40, 10 ,60
# for 50 it is only 1. as there is no days before it.
# for 40 it will be 3 as its previous days are 10 and 20 and including 40 will be 3 days
# similarly for 60 it will be 6 days.
# basically we have to find nearest(index-wise) greater element from left side.
# this problem variant is the nearest previous greatest element.

# well naive way to do it, if we simply traverse all left side elements again and again till we found greater element
# and time complexity.
# but we can optimize it if we can ignore smaller elements on left of side of current elements.

# for example -> 50, 5,4,3,2,1, 10 , 40, 30, 60
# like when we at 10 we know that its next greater element is 50, so if somehow we can skip these middle elements check
# So Idea is simple we will use stack to store the max values we have seen so far
# let say if we start with 50 ; stack was empty then we will simply add 50 to stack
# 5; 5< 50 -> so we will not pop 50 from stack and we will simply put 5 in stack
# 4; 4<5 -> 5 will not be poped out; and we will add 4 into stack
# 3; stack -> [3,4,5,50]
# 2; stack -> [2, 3,4,5,50]
# 1; stack -> [1,2, 3,4,5,50]

# 10 ; now 10 > stack top. so we will pop 1,2,3,4,5; and when we reach to 50 we found 50>10 so we will not pop 50
# and insert 10 to stack
# so as you can see for next element 40, we can find next greatest element very quickly
# because now 5,4,3,2,1 is removed from stack and we simply have to compare with 10 and 50.
# so at 40 our stack will look like this [50, 40]
# now what does that means, it means that elements between 40 and 50 is less than 40. because that was the reason
# we popped them from stack
# so basically in stack we are keeping track of right most greatest element we found so far.
# then below it will be the value which is greater than top
# and as we go down we will keep getting greater values.

# so using this we can skip lot of checks.
# also you may be thinking that its worst case time complexity will be O(n^2), but its not.
# as we are traversing array only once and at the same time we are pushing data to stack
# and also we are popping each element only once.
# that means it's time complexity is O(2n)

def find_stock_span(data):
    stack =[0]
    print(1)
    for i in range(1, len(data)):

        while len(stack)>0 and data[i]>data[stack[-1]]:
            # removing lower elements
            stack.pop()

        if len(stack) == 0:
            # if stack is empty then, its means it is the greatest element seen so far and there is no
            # lower element on left side
            print(i+1)
        else:
            # else we will get the number of days by subtracting current index and left most greatest element
            # simialry we can find the left most greatest element by simply printing stack top item.
            print(i-stack[-1])
        stack.append(i)


# find_stock_span([50, 5,4,3,2,1, 10 , 40, 30, 60])

#### Find nearest greater element from right side #####

def find_greater_right_neighbour(data):
    # similar approach as above, but here we will traverse from right to left.
    stack = [len(data)-1]
    print(-1)# -1 for not exists
    for i in range(len(data)-2, -1, -1):

        while len(stack) > 0 and data[i] > data[stack[-1]]:
            # removing lower elements
            stack.pop()

        if len(stack) == 0:
            # if stack is empty then, then there is no greater element
            print(-1)
        else:
            print(data[stack[-1]])
        stack.append(i)

find_greater_right_neighbour([90, 30,80, 10,20,40,])