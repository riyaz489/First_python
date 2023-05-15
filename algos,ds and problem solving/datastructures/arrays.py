# types of array in languages
# 1. fixed size arrays : whose sized is fixe like in C language
# 2. dynamic size array: whose size changes according to items we push in it. like list in python
# so in dynamic size arrays size increases automatically, when list of full, and it copy data from old array to
# new large array


# rotate array by d places:
# reverse first d elements and d+1 to n elements separately
# then reverse whole list
# exaple: d=2, [1,2,3,4]
# step 1: [2,1,4,3]
# step2 : [3,4,1,2]

# find numbers of leaders in list (leader is number which greater than next occuring elements in list)
# example: [1,2,6,3]
# here 6 and 3 are leaders
# soltion : traverse list from last and if current elements is greater than last leader then add is to answer


# find max dff x[j]-x[i] where as j>i
# traverse from left to right
# initialized diff as x[1]-x[0]
# inside loop:
# res = max(res,arr[j]-minvalue)
# minvalue = min(minvalue,arr[j])

# find max freq elem in given rnages
# example: range_starts = [2,4] ; rnages_end = [4,5]
# so our ranges would be -> [2,3,4] and [4,5]
# so max occurring elem is 4, because it ccrs n both ranges
# to solve this we will create a single array and intialize it with 0;
# intitaly set_value will be 0
# for starting index we will increament set_value by one nd one we reach anges_end indicies we will subtract it by one
# it will look lke this:
# [0,0,1,1,2,1]-> then we will smply find max and return it;s index as output.


