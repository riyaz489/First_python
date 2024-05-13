from heap import MinHeap
# find k close elements; to measure closeness of 2 items we will do abc(item1-item2).
# the smaller the result the closer they are.

# to solve this we will create a min heap again and in minheap instead of storing actual value we will
# store difference of current item and given k.
# to optimize it further we can use the max-heap. like we used min-heap to find k-largest items.
# also we have to change comparator in max-heap. instead of simply compare 2 values
# we have to do somethign like abs(a-k)< abs(b-k).
# python does not have maxheap lib and I also don't have max heap code.
# so i will skip its implementaiont. buts same as find-k-largest-items, but in this case heap comparator will be
# modified.
