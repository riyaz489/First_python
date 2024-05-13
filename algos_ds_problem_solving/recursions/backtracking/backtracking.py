# backtracing is a appraoch to optimize recursions.
# here we will return early in recrusive tree, if we found out that current branch is not oging to give us the required
# result.

# its code structure will look like this:

#  recursion break condition and return true/false

#  then we will check if calculation so far is going to give us result or not
# if not then we will do early return form here as False. (this is backtracking optimization)

# then we will add current permutation in result

# call recursive function
# if it returns True then return true from this function also/

# else remove current permutation from result.


#### print all same size permutations which do not contains 'AB' as subtring.

res = []
def swap_chars(data, fi, li):
    if li == fi:
        return data
    if fi > li:
        fi, li = li, fi
    data = data[0:fi] + data[li] + data[fi+1:li] + data[fi]+ data[li+1:]
    return data

def find_all_substrings(data, ind=0):

    # to find all permutations of same lenght we have to swap first char with all remaining chars one by one
    # then second char one by one and so on.
    if ind == len(data):
        if 'ab' not in data:
            res.append(data)
            return True

    if ind > 1 and 'ab' in data[0:ind]:
        return False # bactracking;
        # doing early return for cases where we found 'ab' as substring and
        # from 0 to ind we are not doing swapping below, so we can safely if ab exists

    for i in range(ind,len(data)):
        data = swap_chars(data,ind,i)

        find_all_substrings(data, ind+1)
        # swap them back to get original string
        data = swap_chars(data, i, ind)

find_all_substrings(data='abcd', )
print((len(res)))