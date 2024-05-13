# we have given few numbers and we have given a bar of size k and now we have to find how many maximum cuts we can make
# on bar. and each cut should be of size of numbers present in put list.
# for example: [1,4,5]
# k = 5
# so max cuts is 5 of size 1.
# [2,3,5,8]
# k= 7
# max cuts is 3 of [2,2,3]
# if cut is not possible then return -1

# idea is simple, we will use recursion calls with all combinations to solve it.
# in call we will include current number and in another we will not.
dp = {}
def find_cuts(data, k,i=0, cut_so_far=''):
    if k==0:
        print('candidate cut which might be our answer -> '+cut_so_far)
        return 0
    if i>=len(data):
        return -1
    if k<0:
        return -1

    if (k,i) in dp:
        return dp[(k,i)]

    include = find_cuts(data, k-data[i], i, cut_so_far+str(data[i]))
    exclude = find_cuts(data, k, i+1, cut_so_far)

    # if we get result -1 which means its not possible to get required sum from provided numbers,
    # so we have to keep -1 include case, otherwise we have to increment count by 1 to the result.
    # as we have included a number which we have to consider by adding 1
    include = -1 if include==-1 else include+1
    dp[(k, i)] = max(include,exclude)
    return dp[(k, i)]

print(find_cuts([2,3,5,8], 7))
