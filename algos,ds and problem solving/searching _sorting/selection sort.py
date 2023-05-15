# best n2
# worst n2
# but saves memory swaps operations
# pick the min element and move it to first index

def sorting(data):
    for x in range(len(data)):
        min = data[len(data)-1]
        key = len(data)-1
        for y in range(len(data)-1,x-1 ,-1):
            if min>data[y]:
                min = data[y]
                key = y
        # swapping
        data[x], data[key] = data[key], data[x]

    print(data)

sorting([1, 2, 5, 1, -4, 9, 3])
sorting([1, 2, 5, 1, -4, 9])