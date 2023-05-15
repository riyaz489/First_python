
def max_area_histogram(heights):
    # max area will always be one of the height in given list
    # so we will take height one by one as minimum, find left and right range for it and calculate area

    # we will use stack to get left and right limit
    # if height is grater then current height then pop stack top  and when we got smaller elem then take current index as limit and push current elem
    # this will give closest min value from current value in a given list with O(1) complexity

    right_stack = []
    right_limits = [0]*(len(heights))

    max_elem = 0
    for i in range(len(heights)):

        right_limit = len(heights)-1
        # getting right limit
        while  len(right_stack)>0 and heights[right_stack[-1]] >= heights[len(heights)-i-1] :
            right_stack.pop(-1)
        if right_stack.__len__() !=0:
            right_limit = right_stack[-1] -1
        right_stack.append(len(heights)-i-1)


        right_limits[len(heights)- 1-i]=right_limit

    # using same list for saving memory
    right_stack = []

    # now calculate area and find max one
    for i in range(len(heights)):
        left_limit = 0


        # getting left limit
        while len(right_stack) > 0 and heights[right_stack[-1]] >= heights[i]:
            right_stack.pop(-1)
        if right_stack.__len__() != 0:
            left_limit = right_stack[-1] + 1
        right_stack.append(i)



        width =  right_limits[i]-left_limit +1
        area = width* heights[i]
        max_elem = max_elem if max_elem > area else area

    return(max_elem)


max_area_histogram([1,2,5,3,4])