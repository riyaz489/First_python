# lexographic sorting is like we do in dict.
# that is we will start comparing chars from left and whichever string have left most char is smaller will come first.
# for example: s1= abcze; s2= abcde => so s2 will comes first; as first 3 chars are same but 4th char is z which
# will comes after d.
import math


# So to find lexicographic rank of a string. we have to do comparisons of all permutations for given string. where
# length of permutations will same of original string.

# for example : for string abdc rank will be 2 as first rank string will be abcd.
# similarly acdb rank will be 4.
# so naive approach is to make all permutations (which will n!) and then sort them and then find rank.

# another efficient approach is find the count of how many strings have lower rank than current string
# and its time complexity will be O(n*(a-z length which is constant))

# see the example below to understand how we are going to find numbers of string who has lower rank.
# lets take 'dcba' as example:
# if we traverse from left to right, we see d is the leftmost char. and now we see how many chars are smaller than d
# exits in current string. as we can see 'abc' 3 chars are smaller than d.
# now if we replace these 3 chars with d then how many permutatinos we will get.
# a___ -> as a is fixed we left with 3 chars so permutation will be 3!
# b___ ->  as b is fixed we left with 3 chars so permutation will be again 3!
# c___ ->  as b is fixed we left with 3 chars so permutation will be again 3!

# there we will be total 3*3! permutations or we can say strings whose rank is less than current string.
# now we move to next position . we see we have 'c' char and now only 2 chars are smaller than c, which is ba
# so this time we will fix previous char which was d and find permutations, when c (next position char) is
# going to replace with smaller chars.
# da__ -> 2!
# db__ -> 2!
# => it will 2*2!
# similarly we will repeat these steps till we reach to last char
# and we will get result like this 3*3!+2*2!+1  => 23 string permutations has less rank than current string
# so answer will be 24.

def lex_rank(data):
    char_freq = [0]*26
    chars_count_before = [0]*26

    # loop to find freq of chars
    for i in data:
        # char freq can store only lower a-z; so  index will be calculated using   ascii of char - ascii of 'a',
        # as 'a' will be on first index and z will be on last.
        char_freq[ord(i)-ord('a')] += 1

    # doing to cumulative sum to find out, how many lower chars exists before current char
    # for example for cbab -> freq array will look like  [1,2, 1 ,0 ,0, ...]
    # so this cumulative array will be [1,3,4,4,4, ... ]. so if we want to check how many chars are smaller than or
    # equal to than c in current string, then we will simply go to index ord(c) and we can see the count.
    #
    # so we will start with 1, as there is nothing smaller than 'a'.
    chars_count_before[0] = char_freq[0]
    for i in range(1, len(char_freq)):
        chars_count_before[i] = chars_count_before[i-1] + char_freq[i]

    mul_factor = math.factorial(len(data))
    ranks = 0
    for i in range(len(data)):

        # as we have seen in above example, in each step we have n-i chars permutations. for that purpose
        # we have calculated fact here and as after each traversal numbers of char will reduce for permutations
        # that's why we are doing divide. which will result in lower number permutation.
        mul_factor = mul_factor//(len(data)-i)

        # as we don't have an entry for chars count smaller than so we will set it manually to 0.
        # for others we can get smaller chars count by simply accessing prev char index.
        if data[i] == 'a':
            num_of_smaller_chars = 0
        else:
            num_of_smaller_chars = chars_count_before[ord(data[i])-1-ord('a')]

        # now as per formula we have seen in above exmaple:
        ranks = ranks + (mul_factor)*num_of_smaller_chars

        # once current char is traversed we have to reduce char count by 1 for greater and current
        # elements from cumulative array, as current char is used now.
        # because after this traversal this current char is going to be fixed in its original position
        # and we can't use it in future permutations.
        # for example : bcda
        # let say data[i] is b and chars lower than b is a only. for this traversal we could have got
        # a___ -> 3! => 1*3! = 6
        # now after this traversal b is going to be fixed in this position, and next when we are at c
        # number of chars less than c will be one again  which is 'a'. as 'a' is right side of 'c' and b is
        # already fixed we can't use it anymore.
        # next permutations will look like this ba__ -> 1*2!

        # we are reducing 1 from right and current char only because for current and greater elements it means that,
        # now numbers of chars which are lower than current and greater char is reduced by 1. lower chars will not
        # effected, as current char was higher so lower chars count will still remain same.
        # example: 'astu'
        # [0,1,...  2,3,4...]
        # [a,b, ... s,t,u,...]
        # let say s is removed from string, then count of chars lower than or equal to b will still be 1.
        # but now chars count is lower than or equal to s will change, for the all the  chars and
        # effected chars will be s to z.
        # so new count array will be
        # [0,1,... 1,2,3...]
        # [a,b,... s,t,u...]
        for j in range(ord(data[i])-ord('a'), len(chars_count_before)):
            chars_count_before[j] -= 1

    return ranks + 1

print(lex_rank('string'))