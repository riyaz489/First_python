# https://wiki.python.org/moin/TimeComplexity

### python datatypes ######

# List: mutable. it uses 2 block of memory, one to store data and another one to object info.
# list add extra space in it to perform append operation in O(1) time complexity.
# and to keep trace of extra space it use more block. that's why it consumes more data than tuple.
# Insert: O(n)
# append: O(1)
# Get Item: O(1)
# Delete Item:O(n)
# Iteration: O(n)
# equal: O(n)
# copy: O(n)
# sort: O(nlog(n))
# Get Length: O(1)  (list already stored count of elements in object info, so that's why it's O(1))

# Dictionary
# Get Item: O(1)
# Set Item: O(1)
# Delete Item: O(1)
# length: O(1)
# Iterate Over Dictionary: O(n)
# dict takes lot of space in memory its 4.7 times in comaprsion to list of tuples
# i.e dict() is 4.7 times of [()].

# Set: does not store duplicates. it uses hash tables, so checking if element is exists is faster, but traversing all elements are slow than list.
# it does not preserve the insertion order.so we can not use indexes here for fetching elements.
# Check for item in set: O(1)
# Difference of set A from B: O(length of A)
# Intersection of set A and B: O(minimum of the length of either A or B)
# Union of set A and B: O(length(A) + length(B))
# pop and add: O(1)

# Tuples: not mutable. so it uses 1 block of memory only to store data.
# so tuples are faster than list and consume less memory.

# ordered dict: it uses doubly linked list and keep order of insertion.

# class objects are also mutable

# note: there are amortzied(very bad or once in while)  cases where time-complexity is more than the average/worst case,
# because in few operations like deletion and addition of data we need to change size of given data-structre. due to which
# we have to copy all existing data to new allocated memory. but we usually ignore this!



# In python, we have bisect and insort library,
# bisect will give index where we can place new element in list, so that list will remain sorted.
# example: l = [1,2,3,4,4,4,5] ; bisect.bisect(l, 4); output: 6 #right most index
#       bisect.bisect_left(l,4); output:4 # left most index
# it works on concept of binary search, so complexity is log(n)
# similarly bisect.insort() will insert new data, instead of returning index
