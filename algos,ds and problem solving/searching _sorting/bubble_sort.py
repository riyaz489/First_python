# compare only consecutive elements [n and n+1] and with this max elements came to right

# worst -> n2
# best -> n
# average -> n2

def sorting(data):
    for x in range(len(data)):
        for y in range(len(data) - x - 1):
            if data[y] > data[y + 1]:
                data[y + 1], data[y] = data[y], data[y + 1]
    return data


print(sorting([1, 2, 5, 1, -4, 9, 3]))
print(sorting([1, 2, 5, 1, -4, 9]))
