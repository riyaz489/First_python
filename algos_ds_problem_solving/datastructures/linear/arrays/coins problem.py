# we have ginve set of coins and we have to find in how many ways we can generate a combinations of coins so that their
# sum is equal to k.
# for example: coins = {1,2,5}
# sum = 3
# ways = {[1,1,1], [1,2]}

# DP using memorization, In this approach we will just recursively include and exclude given coin, to genrate all
# possible combinations.

dp = {}
def find_ways_recur(coins, sum, i=0, pair_so_far=''):
    if sum == 0:
        # if sum equal to 0 that means we found a way
        return 1, pair_so_far+'-'
    if sum<0:
        # sum becomes -ve that means we found wrong way
        return 0, ''
    if i == len(coins):
        # i equal to len of coins that means we already used all coins and still not get required sum

        return 0, ''

    # checking if already exists in DP then return it
    if (pair_so_far, sum) in dp:
        return dp[(pair_so_far,sum)]

    # exclude current coin by incrementing i and in another call we include current coin and reduce sum
    excluded = find_ways_recur(coins, sum, i+1, pair_so_far)
    included = find_ways_recur(coins, sum-coins[i], i, pair_so_far+str(f'{coins[i]}'))
    # adding number of ways seen so far and the pairs seen so far
    # as resuls with 0 ways will return empty strings, so we can safely add patterns, also.
    # as only possible paterns will be added.
    dp[(pair_so_far, sum)] = excluded[0] + included[0], excluded[1]+included[1]
    return dp[(pair_so_far, sum)]
res = find_ways_recur([2,3,5,6], 10)
print(res[0])
print(res[1].split('-'))


# now we have to solve it using tabulation of DP
# we will create 2d array where coins will become one dimension and required sum will become another dimension
# and each for each grid will represent that in how many ways we can get sum j from 0 to i coins.
#        0 1 2 3 4 5 ... k
#coin1   1 0 0 0 0 0     0
#coin2   1
#coin3   1               res


def find_ways_tab(coins, k):

    # for 0 coin its not possible to get any sum so top row will have 0 as number of ways
    # for first column there is only 1 way to get sum as 0. when current coin is not included.
    arr = []
    for i in range(len(coins)+1):
        # for 0th index it will be 1. and for remaining indices adding k 0s and
        arr.append( [1, *[0]*k])

    for i in range(1, len(coins)+1):
        # as first row is already filled so we started with second row.
        # also here rows index represent coin position in coins list not the index.
        # i.e current row -1 = coin index in coins list.
        for j in range(1, k+1):
            # starting form second col as first is already filled with 1s

            # to exclude current coin we have to copy result from top row.
            # as if we exclude current coin then number of ways will be same till prev coin was added.
            arr[i][j] = arr[i-1][j]

            # now as we did in recursion we have to add result, if we have included current coin.
            cur_row_coin = coins[i-1] # as rows are coins position in coins list not index. so we did -1 to get index.
            # to get the ways for included coin, we have to get ways from same coin when sum was sum-coin_value.
            # (same thing what we did in recursion)
            if j-cur_row_coin >=0: # safeguard to make sure j will not become -ve. because if it is negative then we
                # can ignore include case.
                arr[i][j] += arr[i][j-cur_row_coin]
    return arr[-1][-1]

print(find_ways_tab([2,3,5,6], 10))



dp = {}
# now we have to print shortest possible combinations of coins to get sum k
def findShortest_way_recur(coins, sum, i=0, pair_so_far=''):
    if sum == 0:
        # if sum equal to 0 that means we found a way
        return 0, pair_so_far
    if sum<0:
        # sum becomes -ve that means we found wrong way, sop we are returning infinity, so that will be
        # removed when we look for min path
        return float('inf'), ''
    if i == len(coins):
        # i equal to len of coins that means we already used all coins and still not get required sum
        return float('inf'), ''

    if (sum, pair_so_far) in dp:
        return dp[(sum, pair_so_far)]
    # exclude current coin by incrementing i
    exluded_res = findShortest_way_recur(coins, sum, i+1, pair_so_far)
    # in another call we include current coin and reduce sum

    included_res = findShortest_way_recur(coins, sum-coins[i], i, pair_so_far+str(f'{coins[i]},'))
    # we also increased coins count by doing 1+ , as we have included 1 coin in this case
    included_res = (included_res[0]+1, included_res[1])

    res = exluded_res if exluded_res[0] < included_res[0] else included_res
    dp[(sum, pair_so_far)] = res
    return res

print(findShortest_way_recur([2,3,5,6], 10))

# rows represent coins and column represent sum.
# and items represent that how many min pairs of coins needed to generate k sum from 0 to i coins
def find_shortest_way_tab(coins, k):

    # for 0 coin its not possible to get any sum so top row will have infinite as number of ways
    # for first column there no coins needed to get sum as 0. so number of coins for this one will be 0
    arr = [[0, *[float('inf')]*k]]
    for i in range(1,len(coins)+1):
        arr.append([0, *[0]*k])

    for i in range(1, len(coins)+1):
        # as first row is already filled so we started with second row.
        # also here rows index represent coin position in coins list not the index.
        # i.e current row -1 = coin index in coins list.
        for j in range(1, k+1):
            # starting form second col as first is already filled with 1s

            # to exclude current coin we have to copy result from top row.
            # as if we exclude current coin then number of ways will be same till prev coin was added.
            exclude = arr[i-1][j]

            # now as we did in recursion we have to add result, if we have included current coin.
            cur_row_coin = coins[i-1] # as rows are coins position in coins list not index. so we did -1 to get index.
            # to get the ways for included coin, we have to get ways from same coin when sum was sum-coin_value.
            # (same thing what we did in recursion)
            include = float('inf')
            if j-cur_row_coin >=0: # safeguard to make sure j will not become -ve. because if it is negative then we
                # can ignore include case bvy passing default values as infinity.
                include = arr[i][j-cur_row_coin] + 1


            arr[i][j] = min(include, exclude)

    return arr[-1][-1]

print(find_shortest_way_tab([2,3,5,6], 10))

