# complexity all are nlogn(O)
# here first we built maxheap (in max heap parent has bigger element than its children )
# then by this way we will got max element as root parent, we will replace root parent with last element
# and again heaify it to get 2 max at root and so on.
# array representation is cheap for space complxity, so thats why we are usg array
# get childs of node in array
# for index i childs will be l = 2*i+1  r = 2*i+2
def heapify(data, n, i):
# it will heapify top to bottom
# for this function we assume that we have already a given max heap and only top element is manipulated.
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and data[l]> data[i]:
        largest = l
    if r < n and data[r]> data[largest]:
        largest = r

    if largest!=i:
        data[i], data[largest] = data[largest], data[i]
        # now heapify the node which we just changed (means replaced with i)
        heapify(data,n, largest)

def sorting(data):
    # first heapify from bottom to top
    # n/2-1 element will be the last root node
    for x in range(len(data)//2-1, -1, -1):
        heapify(data, len(data), x)

    # now move largest elements to end one by one
    for y in range(len(data)-1, 0, -1):
        data[y], data[0] = data[0], data[y]
        # we will ignore last elements which is already moved, that's why total elements passed is y instead of len(data)
        # now because we changes the 0th element we will heapify again to get max again at top
        heapify(data, y, 0)


x = [1, 2, 5, 1, -4, 9, 3]
sorting(x)
print(x)
