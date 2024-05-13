# For every bar 'x', we calculate the area with 'x' as the smallest bar in the rectangle.
# If we calculate the such area for every bar 'x' and find the maximum of all areas, our task is done.
# one naive way to do it is, traverse array from left to right and then for each element find left most min element
# and right most min element. and then calculate area for current data.
# for example
# data = 1,5,6,4,8,9,10,3
# current element is 4 and element on left side which is less than 4 is after 2 nodes
# and similarly on right side is after 3 nodes.
# then max area for current element will be 4*(2(left_side)+3(right_side)+1(current_node))
# as to form as rectangle heights of all bars should be same, that's why we are taking current node as min.
# and time complexity will be n^2
# but we can solve this in O(3n). If we can use stocks span approach to find leftmost and rightmost min element.

# but we make it more efficient using stocks span approach again
# like for stock span problem our stack gives us the previous greater number.
# and as we go down in stack we will get more greater elements which were present in more left side.
# but in this case we want smaller elements so stack will look little bit opposite.
# stack [i
#         j
#         k
#         l]
# so here j is lower than i and k is lower than k and so on.
# example: 10, 20,40,30,50,60
# when we are at 30 then our stack will look like this.
# stack = [
#           40
#           20
#           10
#           ]
# i=30
# we can see top of stack is greater than i, that means we found lower element for 40 on right side,
# so we will pop top of stack and find its index
# which is 2; so 3-2 is 1 and multiplied by 40 will give area = 40
# as you can notice here we calculated area of stack top element which was 40.
# because smaller element was just next to it ,due to which we can't increase it's width.
# and 30 was it's next smaller which was just next to it.

# now when we at i=50;
# stack = [
# #           30
# #           20
# #           10
# #           ]
# as stack top is smaller we will just add 50 into stack
# # now when we at i=60;
# # stack = [   50
# # #           30
# # #           20
# # #           10
# # #           ]
# # again as stack top is smaller we will just add 60 into stack

# now list traversal is complete we will remove items from stack. in this case i will be n
# so for 60 prev smaller was 50; so area will be 60
# for 50 prev smaller was 30 so area will be n-index_of(30) = 5-3 *50 = 100
# for 30 prev was 20
# similarly 10 was the smallest element so its area will be n*10

def find_max_area(data):
    res=0
    stack = []

    for i in range(len(data)):

        # whenever current data becomes less than stack top item, that means we found the rightmost lower element for
        # stack top item.
        while len(stack)>0 and data[i] < data[stack[-1]]:
            # we will check iteratively , that current item i is lower right, for how many items present in stack.
            # because let say i is 10 and stack is like [70, 40,20]
            # so i will be right most shortest element for 70, then 40 and then 20 also.
            # so i will be helpful to calculate area for all of these items.
            top_item = stack.pop()

            # if stack is empty then it means current element is lowest in list
            # otherwise we will check how far perv lower is from current item
            # (which is lower on right side for stack top item)

            width = i if len(stack)==0 else i-stack[-1]-1
            # as we are calculating area for top item in stack;
            height = data[top_item]
            # cal area
            area = height*width
            # find max area
            res = max(res, area)

        stack.append(i)

    # for remaining elements in stack
    while len(stack) > 0:

        # now we traversed all the elements in above list, then means the remaining items in stack does not have greater
        # values on their right side, that's why now i become len of list here.

        top_item = stack.pop()

        # if stack is empty then it means current element is lowest in list
        # otherwise we will check how far perv lower is from end of list.
        width = len(data) if len(stack) == 0 else len(data) - stack[-1]-1
        # as we are calculating area for top item in stack;
        height = data[top_item]
        # cal area
        area = height * width
        # find max area
        res = max(res, area)
    return res
# its time complexity will be 2n as one n to add data into stack another n to remove data form stack.

find_max_area([10,50,40,60,70,10])


######## max area rectangle in matrix of 1 and 0 #########################
# for example => [0,0,1,1,0]
#                [0,0,1,1,0]
# max rectangle area is 4 for middle  1's
# this is simple, using above max area rectangle in histogram, we can simply solve this
# for each row we have to simply add 1's of previous rows to find the actual height
# but if any col for current row has 0 then we won't add prev rows. as now continuity of 1' break.
# and for height and width we need continues 1's, otherwise it won't form rectangle
# for example -> [0,0, 1,1]
#                [1,1, 0,0]
#                [1,1, 1,1]
#                [0,0, 1,1]
# after doing sums of prev rows
#                [0,0,1,1]
#                [1,1,0,0]
#                [2,2,1,1]
#                [0,0,2,2]-> now from each row we can see the actual heights

# next step is to simply call find_max_area for each row and that will give us result.

def find_max_area_rect_in_matrix_of_0_1(data):
    res = 0
    temp = 0

    for row in range(len(data)):

        # add prev row heights
        for col in range(len(data[row])):
            if data[row][col] == 1 and row!=0:
                data[row][col] += data[row-1][col]
            res = max(res, find_max_area(data[row]))

    return res

# time complexity is O(r*c)
data = [[0,0, 1,1],
               [1,1, 0,0],
               [1,1, 1,1],
               [0,0, 1,1]]

print(find_max_area_rect_in_matrix_of_0_1(data))