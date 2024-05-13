# count how many subsets are possible with sum k.

# recursive is easy, we are going to check all subsets, to do so make 2 recursive call in one include current item and
# in another exclude current item in sum.

def find_subset_sum(data, k, i=0,d=''):
    if k==0:
        print(d)
        return 1
    if k<0:
        return 0
    if i>=len(data):
        return 0

    return find_subset_sum(data,k,i+1,d) + find_subset_sum(data,k-data[i], i+1,d+',' +str(data[i]))

# print(find_subset_sum([3,5,2,7,3], 10))

# so solve it using DP tabulation form we have to create 2D array.
# one dimension will be lenght of data array and another will be given_sum.
# and each grid in 2d array will tell us how many subsets possible for given sum j from 0 to i items.
def find_subset_sum2(data, k):
    # as we know with 0 items there only 0 pairs possible so first row will be 0.
    # for 0 sum we need only one subset,which will be empty subset. so first col be 1.
    arr = []
    for i in range(len(data)+1):

        # it means 0th item is 1 and other k items will be 0.
        arr.append([1, *[0]*k])

    for i in range(1, len(data)+1):
        for j in range(1, k+1):

            if j-data[i-1] < 0: # if it gives negative value it means current item value is greater than given sum j
                # so we can not include it in subset. # so we will just go with exclude case.
                # in exclude case we just copy top row value.
                arr[i][j] = arr[i - 1][j]
            else:
                # data[i-1] is equivalent to current row item. as in arr we did indexing from 1 instead of 0.
                # this case is like recursion one, sum of exclude and include case.
                # exclude case we copied from above.
                # in include case we will check in prev row on j-current_item column.
                # because its like recursion we will check how many subsets possible with without current items (0 to
                # i-1 items) for given sum (k-current_item).
                arr[i][j] = arr[i-1][j] + arr[i-1][j-data[i-1]]

    return arr[-1][-1]

print(find_subset_sum2([3,5,2,7,3], 10))



# code to find max size subset for given sum k
# def find_subset_sum(data, k, i=0,d=''):
#     if k==0:
#         print(d)
#         return 0
#     if k<0:
#         return float('-inf')
#     if i>=len(data):
#         return float('-inf')
#
#     return max(find_subset_sum(data,k,i+1,d), find_subset_sum(data,k-data[i], i+1,d+',' +str(data[i]))+1)
#
# print(find_subset_sum([3,5,2,7,3], 10))
