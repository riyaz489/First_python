# 1. In-Place Sorting: An in-place sorting algorithm uses constant extra space for producing the output
# (modifies the given array only). It sorts the list only by modifying the order of the elements within the list.

# algos:
# Insertion Sort
# Selection Sort
# Bubble Sort
# quick sort

# 2. A sorting algorithm is said to be stable if two objects with equal keys appear in the same
# order in sorted output as they appear in the input data set.
# algos:
# Bubble Sort,
# Insertion Sort,
# Merge Sort,
# Count Sort,


# Find minimum diff in array.
# sort the array
# and then find diff between adjacent elements
# and return whichever is minimum.


# Merge overlapping intervals
# for example [(1,3), (2,4)] output -> [(1,4)] ; here first item in tuple is start time of interval and second
# item is end time.
# data = data.sort() on the basis of start time of intervals.
# index = 0
# result = data[index]
# for i in range(1, len(data)):
#    if result[index][1] >= data[i][0]:
#    #if first interval end is greater than start of next interval then it means
#    #they are overlapping, because we already sorted on the basis of start time so start of first will always be <= to
#    #next interval.
#    # now we will merge it.by updating end of result interval
#    result[index][1] =   max(data[i][1], result[index][1])
#   else:
#      index+=1
#      result[index] = data[i]
#

# Find maximum guests at a given point
# arr[]  = {1, 2, 10, 5, 5}
# dep[]  = {4, 5, 12, 9, 12}
#  Time     Event Type         Total Number of Guests Present
# ------------------------------------------------------------
#    1        Arrival                  1
#    2        Arrival                  2
#    4        Exit                     1
#    5        Arrival                  2
#    5        Arrival                  3    // Max Guests
#    5        Exit                     2
#    9        Exit                     1
#    10       Arrival                  2
#    12       Exit                     1
#    12       Exit                     0
# like in this case maximum guests will be at 5
# idea is simple we will sort arr and dep array. and then we will kee a counter so whenever a guest arrvied we will
# increment the counter and whenever guests leave we will decrement the counter.

# sort both the arrays
# then we do:
# curr = 0
# i=0
# j=0
# while i<len(arr) and j<len(dep):
#   if(arr[i]<dep[j]){
#             curr++;i++;
#         }
#   else{
#             curr--;j++;
#         }
#   res=Math.max(curr,res);
