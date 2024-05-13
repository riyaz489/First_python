# longest common subsequence

# order should be same, and we can skip few characters.
# example:
# str1: abcdefg
# str2: brtdyue
# output is bde


# recursive approach
# we will simply start with 0th char from both string
# if we found match then we will increment both string pointer
# otherwise we will make 2 recursive calls, in one call we will move pointer for 1st string.
# in another call we will move another string pointer. this will give us all the possible combinations of matching.

def find_lcs(str1, str2, l=0, m=0, dp={}):
    # dp for memorization
    if (l,m) in dp:
        return dp[(l,m)]

    if l>=len(str1) or m>=len(str2):
        return ''

    if str1[l] == str2[m]:
        dp[(l,m)] = str1[l] + find_lcs(str1, str2, l+1, m+1)
    else:
        str1_lcs = find_lcs(str1, str2, l + 1, m)
        str2_lcs = find_lcs(str1, str2, l, m + 1)
        dp[(l,m)] = str1_lcs if len(str1_lcs)> len(str2_lcs) else str2_lcs

    return dp[(l,m)]

print(find_lcs(str1='abcdefg', str2='brtdyue'))

# Another approach is iterative
# Its exactly same as Levenshtein Distance algo but here instead of min we will find max value.
# here we will create a 2D array
# on word  chars will represent cols and another word chars will represent rows.
# now moving forward. we will check if char at current row is matching with char at current col.
# if it is not then we will pick max of (left, top) item and place it in current grid.
# if it is matches then we will pick on top-left diagonal item and do +1 and insert it into current row.
# we picked diagonal because in case a character is repeated in a word, then it could lead to wrong result.
# example :
#      A  B C D
#    B 0  1 1 1
#    B 0  1 1 1
#    D 0  1 1 2
#    F 0  1 1 2

# and result will be last row, last col item.

def find_lcs_2(str1, str2):
    res = ''
    arr = []
    # creating empty 2d array
    for i in str1:
        arr.append([0]*len(str2))

    for i in range(len(str1)):
        for j in range(len(str2)):

            if str1[i] == str2[j]:
                # adding 1 to diagonal item, but if diagonal item does not exist then simply copy 1.
                arr[i][j] = (1 + arr[i-1][j-1]) if i>0 and j>0 else 1
            else:
                top_item = arr[i-1][j] if i>0 else 0
                left_item = arr[i][j-1] if j>0 else 0
                arr[i][j] = max(top_item, left_item)

    # now to print the common subsequence from above generated arr matrix
    # we have to reverse the approach we have followed.
    # we will start from last item
    # if we found match then we will add item to res and reduce both pointers by 1.
    # else we will check  which element has bigger value, top or left. and then we will move towards it.

    i=len(str1)-1
    j = len(str2)-1

    while i>=0 and j>=0:

        if str1[i] == str2[j]:
            res= str1[i]+res
            i-=1
            j-=1
        else:
            top_item = arr[i-1][j] if i>0 else 0
            left_item = arr[i][j-1] if j>0 else 0
            if top_item > left_item:
                i-=1
            else:
                j-=1

    return res
print(find_lcs_2('abcdefg', 'brtdyue'))

# VARIANTS OF LCS:
# 1. Find diff in 2 words.
# 2. minimum insertions/deletions to convert s1 into s2.
# 3. shortest common supersequence of s1 and s2.
# simply combining 2 string also will give super-sequence, but to get the shortest one, we have to first find LCS
# then we will add different elements of s1 and then different elements of S2.
# 4. longest palindromic subsequence of a string. for example : abgbae -> abba is palindrome and also subseuence of
# input string. to find it reverse input string and mark it as str2 then find LCS of input string and str2.
# 5. longest repeating subsequence ->
# input: abratb -> output ab
# input: aaa -> output aa # subsequence should not be as same length of input string.
# make input as str1 and copy it to str2 as well.
# now while matching chars in str code add a condition that indicies of both chars should not be same.
# like  -> data[i] == data[j] and i!=j