## Check if string is subseuence of other string or not.
# idea is simple we will traverse long string from start to end. and we will compare each char
# with second string first char if we found match then we will increment second string pointer.
# and this will be repeated till first string all element is traversed.
# if second string is subsequence of first string then second string pointer j will be now equal to length of second
# string. that means second string is completely traversed.

def check_subsequence(a,b):
    j= 0
    for i in a:
        if i==b[j]:
            j+=1
    return len(b) == j

print(check_subsequence('wertgdfg', 'wetfg'))



## Left most repeating character
# exmaple-> geeksforgeeks. so here g is the asnwer as g i left most which is repeated in word.
# we create a empty set 'x'. and then we traverse chars from right to left.
# if current already existed in set x then we update res variable with current index
# else we store that char in set x and proceed further.
# and once all chrs is traversed then we will print res variable as result.
# as we traversed from right to left so res will be having left most repeating char index.

## Left most non repeating char
# example -> geeksforgeeks => f
# similar approach as above, this time we will update res when we are adding new value to set x.
# instead of updating when found existing elem.

## Reverse order of words in sentence
# example -> hey yo output=> yo hey
# idea is simple first reverse the individual words then reverse the whole string.
# this solution works with O(1) space.
# also last word will not have space next to it so our loop which reverse chars in word will not consider the last word.
# so we have to reverse last word explicitly.
# exmaple -> hey yo => (after reversing chars) yeh oy => (after reversal of whole string) yo hey
# def reverse_word(sen):
#     start = 0
#     end = 0
#     for i in range(len(sen)):
#         if sen[i] == ' ':
#             # reversng word
#             temp = sen[start:end + 1][::-1]
#             sen = sen[0:start] + temp + sen[end + 1:]
#             start = i + 1
#         else:
#             end = i
#
#     # explicitly reversing last word
#     if start < len(sen):
#         temp = sen[start:end + 1][::-1]
#         sen = sen[0:start] + temp + sen[end + 1:]
#     print(sen[::-1])
#
# reverse_word(' yo hi hello ')




## FIND PATTERN (or substring) IN STRING ######################
# for example: abcdabcd pattern: abc -> output will be index 0  and index 4



# 1. Naive Apporach:  naive apporach will be to traverse string from left to right and then check for pattern
# from current index i to i+lenght of pattern index.
# time complexity will be O((n-m+1)*m) here n is string length  and m is pattern length.
# n-m+1 will be time to traverse window of size m and O(m) will be to compare current window chars with pattern chars.
# worst case scenario will be if all chars are same in input string and pattern also. like n= 'aaaaaa'  and p='aa


# 2.Rabin Karp:  efficient apporach is to calcualte hash of current window and pattern and then compare them.
# we can use rolling window apporach to calculate hash of next windows.
# i.e first m chars input hash will be calculated manually. then for next window we will remove prev char from previous
# hash function result and add new char. by this way hash calculation will be done in O(1) for next windows.
# This algo is called Rabin Karp algo.
# here hash function will be weighted sum; where weight will depend on position of char. this is to avoid generating
# same hash of different permutations. for example abc and bac.
# first window hash function =( d^m * char1 + d^m-1 *char2 ... d^0 * charm ) % (q)
# here d is some random integer as weight; and q is some large prime number. we did modulo with because in case of
# large patterns our hash result can become very large which our machine couldnot able to store. so that's why we
# choose a prime number and q should be large to reduce possibility of getting same results.
# next window function will be = ((previous hash result - previous window first char *d^m) *d + next_char ) % q
# we simply removed first char with its from prev result then we multiplied by d to increase power of d in each char
# then we added new char with power of d as 0; which is 1.
# this algo also give same time O((n-m+1)*m) complexity in worst case where all char is same in input
# and pattern string. this is even worst than naive implementation as we are calculating hash as well as extra step.
# but in average case it is better than naive solution.
import math
def rabin_karp(data, pat):
    # let take weight as 5
    d = 5
    # let take large prime number 13787
    q = 13787
    pat_hash = 0
    window_hash = 0
    # calculate hash for pattern and first window
    for i in range(len(pat)):
        window_hash = (window_hash*d + ord(data[i])) %q
        pat_hash = (pat_hash*d + ord(pat[i])) %q

    # now compare each window has with pattern hash
    for i in range (len(data)-len(pat)+1):
        # comparing prev hash
        match = True
        if pat_hash == window_hash:

            # in case different string got same hash, so avoid incorrect results in that case we are matching
            # chars one by one
            for j in range(len(pat)):
                if data[i+j]!=pat[j]:
                    match = False
                    break
            if match:
                print(i)
        # calculating next hash
        if i+len(pat) < len(data):
            window_hash = (( (window_hash - (ord(data[i]) * math.pow(d, len(pat)-1)) )*d) + ord(data[i+len(pat)] )) % q
rabin_karp('abcdabcererabcsfabc', 'abc')



## Find if one string is rotation of another string
# for example: S1 = abcd S2 = cdab -> so if we rotate S1 2 times we will get S2 which means its rotation of S2
# to solve this we will simply concatenate S1 with itself S1+S1 = abcdabcd now we try to find S2 as a pattern in it
# if we find S2 in concatenated string then it means its rotation of S1.


