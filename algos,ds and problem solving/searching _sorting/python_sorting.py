# for list we can use sort(), it will sort existing list
# but sorted() will return new list and here we can pass key for sorting as well if our list elements are iterable
# with the help of this we can so rt dict as well
# sorted(x.items(), key=lambda item: (item[1], item[0]))
# above code will return list of tuples,
# which is sorted by dict values(item[1]) and if value is same then sorted by key(item[0])

# we can implement above   function easily,so basically to do sorting on the basis of multiple items,
# like we did in above exmample,
# simply concatenate those items, create new list and sort it.
# similarly we can do it for lambda function  based sorting, first apply lambda function on each
# item of list and create new list, then sort it.,z
# to optimise it we can avoid creating new list and calculated values with provided lambda function,
# while we are doing sorting.

# python used tim sort behind the scene which is combination of insertion sort and merge sort.
# its complexity is o(nlog(n))
# idea is insertion sort works well with small array,
# so here we divide array in chunk of length 64 using merge sort and sort it using insertion sort
# so if size of array is less than 64 then we algo will simply use insertion sort.


