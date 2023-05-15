# worst -> O(nlogn)
# average -> theta(nlogn)
# auxilary space -> n

# divide and conquer
# while merging do sorting
# while merging start comparing from first element of each sub list


def sorting(data):
    # when l and r hae one-one element then this recursion will return and l and r array with one element to above
    # caller stack.
    # then that above function will sort those and return new updated l and r to its above caller stack ad so on.
    if len(data)>1:
    # divide
        mid = len(data)//2
        r = data[mid:]
        l = data[:mid]
        # get the sored left array
        sorting(l)
        # get the right sorted array
        sorting(r)

        i = j = t = 0
        # sort and merge
        while i< len(l) and j<len(r):
            # we will append whatever is smaller
            if l[i]<r[j]:
                data[t]=l[i]
                i+=1
            else:
                data[t]=r[j]
                j+=1
            t+=1
        # adding remaining elements
        while i < len(l):
            data[t] = l[i]
            i += 1
            t += 1
        while j < len(r):
            data[t] = r[j]
            j += 1
            t += 1

# because list is mutable so it is passed by reference


x = [1, 2, 5, 1, -4, 9, 3]
sorting(x)
print(x)
y = [1, 2, 5, 1, -4, 9]
sorting(y)
print(y)