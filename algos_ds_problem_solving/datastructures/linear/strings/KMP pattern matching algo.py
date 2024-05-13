# KMP algo
# using LPS array of pattern we will find patterns in input string
# LPS array generation already discussed in one notes.
# for example: a,a,a,a; LSP = [0,1,2,3]
# lps[i] -> longest proper prefix of pattern[0...i] which is also a suffix.
# LPS array helps us to figure out form where we need to start pattern searching.
# because in naive approach we are comparing each char of pattern with each char of current window.
# but  LPS tells us which chars of current window we can ignore for comparison.


# Algorithm
# first generate LPS array for pattern.
# then take 2 pointer i and j. i is for input string and j is for pattern.
# start a loop form i>=0 to <=len(input string)
# now inside loop check
# if str[i]==pat[j]; then do i++ and j++
# else
#   if j==0 then we will simply do i++
#   else we will update j=lps[j-1]
# now if j==len(patt); then it means we found 1 pattern we print result i-j
# and we will do j=lps[j-1]
# notice whenever we are gping backward for j we are always using LPS array

# little understanding why we used LPS array
# In case if all the chars in pattern are distinct then in this approach also we have to compare
# all elements of pattern with current window chars. but if we have some duplicate chars then in that
# case if we can ignore few chars of pattern to match again, which we know already matched.
# let us understand with below example.

# for distinct pattern
# input -> abcabcd
# pattern -> abcd
# in naive approach we are doing len(pattern) comparisons for each window.
# but in this case in 0th iteration we found that elements are matching till 2nd index then means we can skip
# 0 to 2nd index elements in input string. as they are never going to match with first element of pattern
# because patter has all elements distinct.they already matched with 1st and 2nd elements of pattern that means
# they are not equal to 0th element of pattern and we can never start pattern from 1st and 2nd index.
# so skip it
# now we start new window from [3rd index ... 3rd index + len(pattern)] and match these chars with pattern.
# so as you can notice we skipped few windows here. same thing is going to happen in KMP algo also. because
# LSP array for all distinct array will be going to be 0. So in every mismatch we will be going to start from 0 index
# of pattern.

# But in case of duplicate chars in pattern
# pat = onions
# data = onionionpl
# LPS = [0,0,0,1,2,0]
# so at index 4, 1 char pattern is repeating and at index 2, 2 chars pattern is repeating.

# now when we are at i=5 our j will be also at 5 and we know i!=s;
# in that case we can not start from j=0 again like we did in distinct case, because we will miss the overlapping chars
# like 'on' which is already compared; so using LPS array we will check how much behind we have to go back for j
# so that we don't miss overlapping chars. we do j = lps[j-1] = lps[4]= 2
# so we will start from j=2 and i still at 5; now we found the match
# and similarly at i=7 we will find complete match of pattern.
# so LPS helped us to do again comparison of same chars in pattern.



# how LPS helps us to optimize this algo ?
# see in normal scenario we will compare complete pattern with each window possible (of same size as pattern). which
# would be (n-k)*k where k is pattern size.
# but if we know that our pattern has few Common proper prefix which is also suffix,
# then it will helps to avoid comparing current window with complete pattern and we can skip few chars in next
# comparisons.
# for example: pattern is onion
# its LPS will be [0,0,0,1,2]
# input string dbonioniondf
# now as you can se our pattern onion exists 2 times in above input string.
# now till 6th index we will get out one match, when we get to 7th index, our input will be i.
# now we have to move j backwards to start matching another pattern, but now we know our pattern 4th index LPS is 2.
# that means first 2 chars and last 2 chars are same. and those last 2 chars are also we compared already in
# i-2 and i-1 indicies. so now we can skip 2 chars in pattern and start with 3rd char.
#   on i  on         dbonioniondf
#  |__|  |__|             |_|
#   are same            we can skip comparsion of this 'on' because it was already compared and
#                       we know last 2 compared chars are same as first 2 chars in our pattern.
# so it basically helps us to avoid comparison of already compared chars.


## Code


def gen_lps_arr(patt):

    i=1
    lps=[0]*len(patt)

    j=0
    while i<len(patt):
        if patt[i] == patt[j]:
            # if found same chars then simply expand the prefix and suffix lenght
            j+=1
            lps[i]=j
            i += 1
        else:
            # if j is 0 that means we didn't found any LPS in previous subarray.
            # and now next chars also didn't matched so just increment i
            if j==0:
                lps[i]=0
                i+=1
            else:
            # using lps array to decrement j. so that 0 to j chars always equal to i-j-1 to i-1 chars.
                j = lps[(j-1)]
    return lps

def find_patt(data,pat):
    lps = gen_lps_arr(pat)
    i,j=0,0

    while i<len(data):

        # if same chars then incrementing pattern length like naive approach
        if data[i]==pat[j]:
            i+=1
            j+=1
        else:
            # if j is 0 then it means there were no similar chars before and alsop there were no match of pat and data chars
            # so simply do i+1
            # its like distinct case we discussed above
            if j==0:
                i+=1
            else:
            # if j was something then we will keep some chars of j which are still matching with (i-new_j) to i chars.
                j = lps[j-1]
        if j == len(pat):
            # it means we found our pattern
            print(i-j)
            # decrement j for same i value to find other patterns.
            j = lps[j-1]

find_patt('abacababcaba', 'aba')