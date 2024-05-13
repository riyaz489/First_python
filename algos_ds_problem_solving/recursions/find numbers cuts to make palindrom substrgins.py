# we need to find how many number of cuts are required in string to make palindrome substrings.
# exmaple: geeks -> need 3 cuts  ->  g|ee|k|s
# now g, ee, k, s all are plandrome.
# abcb -> 1 cut -> a| bcb

# idea is simple we will try to make cut next to all chars and then solve for smaller strings recursively.
# for example:
# for abc
# for we make cut a|bc then solve for a and bc separately.
# then make cut ab|c and then solve recursively.
# and we will find min of all these results.

def is_palindrom(x1:str):
    return x1 == x1[::-1]

dp = {}
def find_cuts(data):

    if is_palindrom(data):
        return 0
    if data in dp:
        return dp[data]
    res = float('inf')
    for i in range(len(data)-1):
        res = min(res,
                  1+ # making 1 cut
                  find_cuts(data[0:i+1])+find_cuts(data[i+1:])
                  )
    dp[data] = res
    return res

print(find_cuts('geeks'))
print(find_cuts('abcb'))
print(find_cuts('agnfdrhbcberet'))