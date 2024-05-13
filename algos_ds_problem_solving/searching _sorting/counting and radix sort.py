# Counting sort
# it is used when elements present in list is of smaller range.
# for exmaple: [0,1,1,5,4,2,3,1,2,3,4,1,5,2,1,0,3]. in this array elements lies withing 0-5 range.
# let say range length is m and array length is n. So its time complexity is log(m+n).
# but for larger input range it is not efficient as it can end up taking lot of extra memory.

# it is not comparing based algo.

# here we simply count the frequency of all elements and place the frequency of elements into a new list.
# and minimum element freq will go to 0 index and next elements goes to 1st and max element goes to last index.
# then we simply traverse freq array and add elements into output arr on the basis of their freq.

def counting_sort(data):

    tmin = min(data) # O(n)
    tmax = max(data) # O(n)
    trange = tmax-tmin+1

    # first count freq and place freq in appropriate index of list.
    freq = [0]*trange
    for i in data:  # O(n)
        freq[i-tmin] += 1

    for i in range(1, len(freq)): # O(m)
        # now this will tell us how many elements exists before current element
        freq[i] += freq[i-1]

    output = [0]*len(data)
    for i in range(len(data)-1, -1, -1):
        # now this logic is used to determine correct index of element.
        # as indicies+tmin in freq represent elements in data array.
        # => indices in freq + tmin = data[i]
        # => indicies in freq = data[i] -tmin
        # so when we do freq[data[i]-tmin] it will give us elements from freq list, which tells us how many elements
        # exists before current data[i]. so once we get that, we can use same thing for index in new output array.
        # to place data[i] in its correct position. as indicies start from 0 that's why we did -1 at thr end.
        # (freq[data[i]-tmin] -1). now as we know that current element is placed, so the number of elements which exists
        # before current index will be reduced by 1.

        output[freq[data[i]-tmin] -1] = data[i]
        freq[data[i]-tmin] -= 1
    print(output)

# counting_sort( [0,1,1,5,2,3,1,2,3,1,5,2,1,0,3])

## Radix sort is used for some higher ranges than counting sort.
# here we simply sort data start from lsb to msb. and internally we will use count sort only.
# it stable and counting sort is also stable. but these are not inplace.
#  It has a time complexity of O(d * (n + b)), where d is the number of digits, n is the number of elements,
#  and b is the base of the number system being used (like 10 for decimal numbers).
#  Auxiliary Space:  O(n + b)
# it is very difficult to generalize radix and count sort algo.It requires fixed size keys and integer keys
# like we can not sort floating point numbers using it.
# as list does not take floating numbers as index.
def radix_sort(data):
    maxt = max(data)

    exp = 1
    # this loop will run number of digits times, of max number in given list.
    # and exp will represent which position of number we are talking about
    # like for 1 its 1s place and for 10 its 10th places digits.
    while maxt//exp>0:
        counting_sort2(data,exp)
        exp*= 10

def counting_sort2(data,exp):
    # as we have only 10 digits in decimal numbers (0-9)
    count = [0]*10
    output = [0]*len(data)
    for i in range(len(data)):
        # below formula will give us digits at exp position
        count[(data[i]//exp)%10]+=1
    for i in range(1,10):
        count[i] +=count[i-1]

    for i in range(len(data)-1,-1,-1):
        output[count[(data[i]//exp)%10]-1] = data[i]
        count[(data[i] // exp) % 10] -= 1

    for i in range(len(output)):
        data[i] = output[i]

d = [0,1,1,5,2,3,1,2,3,1,5,2,1,0,3]
radix_sort(d)
print(d)
