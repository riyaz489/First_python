# in this problem we have given a bag of of fixed capapcity.
# and also given items list with their weights and value.
# out task is to push items in bag, get the max value as much as possible.

# for example: capacity =10; weights= [5,4,6,3]; values = [10,40,30,50]
# max value we can get is 90 by putting items of weight 3 and 4 & their values are 50 and 40 resp.
# note: we can not fill items partially.
# also we can not fill same item multiple times.
# that's why this problem called 0-1 because either we fill it or not.

# simple idea using recursion is we will make 2 recusrive calls, in one call we will include item
# in another we will not include current item.

def knapsack_0_1(values, weights, total_weight, current_item_index=0): # O(2^n)

    if total_weight == 0 or current_item_index>=len(values):
        return 0
    # first of all we will check if current item be fitted in bag or not.
    # because it might be possible that current is mora than capacity of bag
    if weights[current_item_index]>total_weight:
        # we will make only one recursive call where we will not include this item
        return knapsack_0_1(values,weights,total_weight, current_item_index+1)

    # now we will make 2 calls one to include current item, another one to exlude current item
    return max(
        knapsack_0_1(values,weights, total_weight,current_item_index+1),
        values[current_item_index]+knapsack_0_1(values,weights,total_weight-weights[current_item_index], current_item_index+1)
    )

print(knapsack_0_1([10,40,30,50], [5,4,6,3], 10))


# now DP tabular approach
# In recursion we were chaning 2 param current index and weight.
# so here we will create 2d array one dimension will be current index and another dimension is total capacity.
# each grid in 2d array will tell us that what max value we can get from 0 to i items for capacity j.
# so here also 1st row and column will be 0 which was same as recursion base case.
def knapsack_0_1_dp(values, weights, total_weight): # O(n*w)
    aux = []
    # here we are consider 2d array from 0 to values items lenght where both are boundaries are included.
    # so here rows represent item position not index,  that means row-1 will be equal to index in values dict.
    # 0 row means 0th item, i.e no-item. 1st row means 1st item in list, which is at 0th index in values array.
    for i in range(len(values)+1):
        aux.append([0]*(total_weight+1))

    for i in range(1,len(values)+1):
        for j in range(1,total_weight+1):

            # if wight is mre than current capacity then exclude current item
            if weights[i-1] > j:
                # to ecxlude current item we will just copy result from its prev row.
                # as it contains result of max value so far, so if we exlude current item then that result remain same.
                aux[i][j] = aux[i-1][ j]

            else:
                # else make call like recursion, exclude and include case max
                aux[i][j] = max(
                    aux[i-1][j], # exclude case
                    values[i-1] + aux[i-1][j-weights[i-1]]
                    # else in include case we will first add
                    # current item value to prev-items max value when capacity was current_capacity - current weight
                    # also j-weights[i-1] will never be negative as that base case we already handled above.
                )

    return (aux[-1][-1])

print(knapsack_0_1_dp([10,40,30,50], [5,4,6,3], 10))