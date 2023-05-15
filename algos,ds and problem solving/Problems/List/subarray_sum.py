# check leet-code and hackerrank submissions for other problem solutions

##### max size sub-array having k sum

l = [-1,-2,2,1]
k = 1
# store all sum in dict
cal_sum = {0:-1}
index = -1
sum = 0
res = 0
for x in l:
    sum +=x
    index+=1
    # basic formula is last_index - first_index = k
    # so we used above to find complement in dict
    if sum-k in cal_sum:

        t = index - cal_sum[sum-k]
        # if we want min length then revert this if condition
        res = t if  t > res else res
    if sum not in cal_sum:
# if we want min length then revert this if condition
        cal_sum[sum] = index

print(res)


##### subarray with max sum
# according kadane's algo max sum subarray will be max(max_subarray_at_index[i-1] +element[i], element[i])
x = [-2,3,-1,-1,9,-2]


def find_max(x):
    gobal_sum = x[0]
    current_sum = x[0]
    for y in x[1:]:
        # it gives us max sum at each index position
        #(example for index 3 max sum will be 1)
        current_sum = current_sum +y if current_sum +y > y else y
        gobal_sum = gobal_sum if gobal_sum> current_sum else current_sum

    return gobal_sum
print(find_max(x))
