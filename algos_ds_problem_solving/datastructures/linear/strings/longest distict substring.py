# we need to find the longest substring with distinct chars.
# example; abcadbcae -> output=> bdcae

# idea is simple, we will maintain 2 pointers. and maintain a subarry with discinct chars
# whenever we see a char which is not exists in current subarray
# we will simply increase sub array lenght
# otherwise we will  start new subarray from next index of previously found duplicate element.
# for example: ababc
# if we are at current_index=2 and current_sub_array_starting_point = 0 so far.
# but now data[current_index] is 'a' which is already seen. so now we will start new subarray whose start point will be
# index of previous occurance of 'a' +1 which is 0+1 =1 and ending point will be current index.
# so now sub array will look like this data[1 to 2] => 'ba'
# and which will check what was the max subarray lenght we got while doing operations.

# Algo
# we will run a loop for j from 0 to n-1. and i will be another pointer which will start with -1 and represent
# starting point of our substring -1.
# then we will check if j is seen in previous longest subarray
# if not then we will simply do increase subarray length;
#   sub_len = sub_len+1
# else we have to calculate new length sub_len = j - previous occurrence of j
# and update i as previous index of j. (as i start_point -1, so we
# can replace it with j directly as j index is not included as it is already seen)

# how we are going to find previous index of j element, its simple we will store latest indies of traveled elements
# in char to index array.

# time complexity will be O(n).
# space complexity O(m) where m is length of the longest distinct chars substring

from collections import defaultdict
def find_longest_distinct_subarray_len(data):

    # if i still remained -1 till the end that means all chars are distinct so j-i will be
    # equal to (len(data) -1) - (-1) = len(data)
    i = -1
    # setting default index for each cahr to -1
    # we could have used list for a-z chars and index would be [ascii of 'a' - ascii of current char]
    # as list will save of lot of space
    char_to_index_dict = defaultdict(lambda: -1)
    res = 0

    for j in range(len(data)):
        # now of data[j] is not seen in previous substring then i will remain as it is.
        # but if data[j] seen in current substring already, then we have to start new substring.
        # for that i will be replaced with prev index of data[j].
        i = max(i, char_to_index_dict[data[j]])

        # longest substring seen so far.
        # here j is current index and i is starting point of substring-1.
        res = max(res, j-i)

        # updating char_to_index_dict, to add new seen char or to update new index of previously seen char
        char_to_index_dict[data[j]] = j

    return res


print(find_longest_distinct_subarray_len('abcbda'))

