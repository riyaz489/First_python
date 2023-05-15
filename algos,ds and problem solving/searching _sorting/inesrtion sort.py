# worst complexity n2
# best complexity n

# take a key here and move element which are greater than key element to +1 index
# and place current key element into correct position once shifting is done
def sorting(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1

        # shifting elements
        while key < data[j] and j>=0:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data

print(sorting([1, 2, 5, 1, -4, 9, 3]))
print(sorting([1, 2, 5, 1, -4, 9]))