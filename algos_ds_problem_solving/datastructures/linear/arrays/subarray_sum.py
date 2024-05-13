# check leet-code and hackerrank submissions for other problem solutions

##### max size sub-array having k sum
# basically we will store sum of 0 to current index elements in cal_sum dict.
# then we will check if (sum till current elem - k) is already seen or not.
# if it is seen then it means sum from that found index till current index is k.
# because in list a...x..y...z; let say sum of a to x is `q` and x to y is `k`; so sum of a to y will be `q+k`.
# =>  = q+k - k = q= sum till x; => sum till y -k = sum till x; so we used similar approach above.
# for example -> [1,2,3]; sum dict will look like {1:0, 3: 1, 6:2}
# for k=2 -> at index 1 our sum will be 3. and when we do 3-k; 3-2=1;
# we see 1 sum was exists for 0th index. => lenght of subarry is current index - found index => 1-0 = 1;
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
    # basically; sum till current current_index - sum till found_index = k
    # so we used above to find starting index of result subarray
    if sum-k in cal_sum:
        t = index - cal_sum[sum-k]
        # if we want min length then revert this if condition
        res = t if t > res else res
    if sum not in cal_sum:
# if we want min length then we will remove this if condition and update cal_sum in all cases
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


