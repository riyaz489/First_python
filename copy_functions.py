# in python '=' will just copy the reference of current object to new one
x = 10
y = x
# if some some immutable type value already stored in memory then python will use same memory address for
# new variable as well, to speed up the memory allocation process. that's why z also have same id
z = 10
print(id(x), id(y), id(z))

# now if we just want to copy only value not reference then we can use python's 'copy' module
# in copy module also we have 2 kinds of copy, deep and shallow
import copy

# 1. shallow copy: it will copy value of current object to new object,
# but for object's children, it will copy reference only. that's why it is called one-level-deep copy only
groups = [[1,2,3],[4,5,6]]
shallow_copy = copy.copy(groups)
# main object id's are different
print(id(shallow_copy), id(groups))
# child object id's are same same, becuase for child objects it copies reference not value
print(id(groups[0]), id(shallow_copy[0]))

# 2. deep copy: here it will create new object for main and its child objets as well.
# it creates completely independent copy of original object

deep_copy = copy.deepcopy(groups)
# main object id's are different
print(id(deep_copy), id(groups))
# here child id's are also different
print(id(groups[0]), id(deep_copy[0]))
