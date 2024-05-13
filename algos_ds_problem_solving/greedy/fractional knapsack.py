# this similar problem like 0-1 knapsack, but here we can fill partial items also instead of pushing full item.
# idea is simple here, we will sort data with profit/weight ratio.
# after sorting we will try to push items till bag is completely full.

def fractional_knapsack(data, capacity):
    data = sorted(data, key=lambda x:x[0]/x[1], reverse=True)
    res = 0
    current_weight = 0
    for i in data:

        if current_weight+i[1] <=capacity:
            # adding full item full profit
            res+=i[0]
            current_weight+=i[1]
        else:
            # breaking item, by calculating profit per kg then multiplying it with remaining weight
            res+= (i[0]/i[1]) * (capacity-current_weight)
            current_weight+=capacity - current_weight
            break

    return res


print(fractional_knapsack([(60, 10), (100, 20), (120, 30)], 50 ))
