# we have given an array and each element in array tells how many max skips we can make.
# and we have to find the shortest path to reach to end.
# for example:  3,4,2,2,2,1
# one way to reach in 2 steps is first hump from 3 to 4 then 4 to 1
# another way is to 3 to 2 then 2 to 1.

# recursive way to solve is by traversing right to left we will check if
# from current node can we reach to last node. If yes then we will check if from any prev node we can reach to current
# node and recursively we will do it till we reach to first node.
# if we can't reach to first node then it means  traversal to current node is not possible.
# for example: first we will check if we can reach 2 to 1. if yes we can then we check if we can reach to 2 from 2
# then 4 to 2 and 3 to 4. so all these traversal is possible but it is not  our answer, is it is longer path.
# so we just have to store minimum path.

def find_min_jumps(data, n): # O(n2)
    if n == 0:
        # that means we reached to first index. and now no need to go more left side.
        return 0
    res = float('inf')
    # we have to check inside this loop that which element can reach to nth node
    for i in range(0,n):
        print('a')
        # adding current value with current index to figure out from current item,
        # if we are reachable to n index or not.
        if data[i]+i >= n:
            # now we will recursively find min steps to reach index i.
            currnt_path = find_min_jumps(data, i)+1 # adding 1 to include current number.
            # checking which path gives min result.
            res = min(currnt_path, res)

    # if we didn't found node which can reach to nth node, then it will return infinity.
    return res

x = [3,2,2,1,2,1]
print(find_min_jumps(x, len(x)-1 ))

# Now to solve it with DP tabular approach.
# we will start one n sized aux array and initialize it with infinity. as we assume all the node are not reachable to
# last node initially.
# this aux array for each index i will store that how many minimum jumps required to current index i.
# for example for first item it will be 0. for second item it will be 1 jump if 0th index item is >=1.
# else it's not possible to reach to 2nd index.
# for example: [0,3] ; so we can never reach to 3 as first item is 0.

def find_min_jumps_dp(data): # O(n2)
    aux = [float('inf')]*len(data)
    aux[0] = 0

    # now to fill aux array we will reverse the approach we followed for recursion.
    # we will go from left to right and find which items which exists before current index i,
    # that can reach to i in minimum jumps
    for i in range(len(data)):
        for j in range(i):

            # this means current j can reach to index i
            if j+data[j]>=i:
                aux[i] = min(aux[i], aux[j]+1)

    print(aux[-1])

find_min_jumps_dp(x)

# 2,3,2,2,1