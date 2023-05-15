  # complexity best -> o(1) and worst -> O(log(n))

def bin_search(data, x, f, l):
    mid = f + (l-f)//2
    if f > l:
        return -1
    if x == data[mid]:
        return mid
    elif data[mid] > x:
        return bin_search(data, x, f, mid-1)
    elif data[mid]< x:
        return bin_search(data, x, mid+1, l)


x = [1, 2, 3, 4, 5, 6,  7, 8, 9]
print(bin_search(x, 8, 0, 8))
print(bin_search(x, 12, 0, 8))
print(bin_search(x, 2, 0, 8))


# to serach item in infinte list
def find_in_infinite_sized_arr(x, arr):
    # first find the index where elem is greater than our elem, that greater ele will be last ndex for our binary search
    if arr[0] == x:
        return 0
    i = 1
    while arr[i]< x:

        i*=2
    if arr[i] == x:
        return i

    return bin_search(arr, x, i//2, i-1)