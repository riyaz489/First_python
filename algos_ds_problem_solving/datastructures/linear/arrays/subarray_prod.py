# we need to find max prod subarray.
# now we can't solve it like max sum problem.
# here we have 4 observations:
# 1. when all numbers are >0, so max prod will be just prod of all numbers.

# 2. when freq of -ve numbers are even, so again max prod will be just prod of a numbers.

# 3. if there are odd numbers of -ve numbers, then we have to omit one -ve number to maximise the result
# so we have to either remove first or last -ve number, i.e our result lie in either suffix/prefix prod of first
# -ve number or prefix/suffix prod of last -ve numbers.
# but why first or last -ve number not the middle one ?
# x ... -1ve ... -2ve ... -3ve ... y
# so if we remove first -ve then our result could be [x to -1ve-1] or [-1ve+1 to y]
# if we remove last -ve then our result could be [x to -3ve-1] or [-3ve+1 to y]
# if we remove middle -ve then our result could be [x to -2ve-1] or [-2ve+1 to y]
# but as you can notice [x to -2ve-1] range is smaller than [x to -3ve-1], that means it will give us lower result than
# [x to -3ve-1]
# and [-2ve+1 to y] is also smaller range than [-1ve+1 to y]. that means our result lies in first/last -ve numbers
# prefix/suffix.

# 4. now if we encounter 0 in list, then we can not include it, as 0 will result our prod as 0 for future numbers.
# so whenever we encounter 0, we will break the list into 2 parts.
# for example: 1,2,3,4, 0, 5,6
# so now instead of find max prod for above list we will find max prod for 1,2,3,4 and 5,6.
# and whichever is max we will return result.

# to solve it we will simply calculate prefix and suffix prod. and fin max of it.
# prefix and suffix will include current numbers also, so this will 1,2 and 3rd scenario.
# and whenever we encounter 0 we will reset prefix and suffix. it will cover 4th scenario.
def maxProduct(self, nums) -> int:
    prefix_prod = [1] * len(nums)
    suffix_prod = [1] * len(nums)

    prefix_prod[0] = nums[0]
    suffix_prod[-1] = nums[-1]

    for i in range(1, len(nums)):

        if prefix_prod[i - 1] == 0:
            prefix_prod[i] = nums[i]
        else:
            prefix_prod[i] = prefix_prod[i - 1] * nums[i]

    for i in range(len(nums) - 2, -1, -1):

        if suffix_prod[i + 1] == 0:
            suffix_prod[i] = nums[i]
        else:
            suffix_prod[i] = suffix_prod[i + 1] * nums[i]

    suffix_prod.extend(prefix_prod)
    return max(suffix_prod)