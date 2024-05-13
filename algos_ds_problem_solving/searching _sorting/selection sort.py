# best n2
# worst n2

# but saves memory swaps operations, so due to this it can save memory writes.
# so this can be used on devices where memory writes operation reduces disk age.

# it is not stable algo
# it is in-place algo

# pick the min element and move it to first index

def sorting(data):
    for x in range(len(data)):
        min = data[x]
        key = x
        for y in range(x+1, len(data)):
            if min > data[y]:
                min = data[y]
                key = y
        # swapping
        data[x], data[key] = data[key], data[x]

    print(data)

sorting([1, 2, 5, 1, -4, 9, 3])
sorting([1, 2, 5, 1, -4, 9])