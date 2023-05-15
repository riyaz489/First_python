#problem: https://leetcode.com/problems/decode-ways/


# 123
# 1 23
# 12 3
# 1 2 3



#    root
# /       \
# 1(1)   12 (1)   when our pointer s at one then we have 2 decision withe to take only 1 or take 12
# / \        /
# 2 23 (2)  3 (3)
# |
# 3 (3)

# res = []
# def find_possible_patterns(x):
#     # all characters used means we reach to leaf element
#     if len(x) < 1:
#         return 1
#     # if substring starts with 0, it means it is invalid case
#     if x[0] == '0':
#         return 0
#
#     # to include single char
#     single_case = find_possible_patterns(x[1:])
#     double_case = 0
#     if len(x)>=2 and  int(x[0:2]) <27:
#     # to include double chars
#      double_case = find_possible_patterns(x[2:])
#
#     return single_case+double_case
#
# print(find_possible_patterns('226'))
# print(find_possible_patterns('06'))
# print(find_possible_patterns('12'))

# also in some cases like '1111'
#                 root
#        /                 \
#     1(1111)              11(1111)
#  /        \               |     \
# 1(111)    11(111)       1(11)   11(11)
# |    \          \          |
# 1(11) 11(11)     1(1)        1(1)
# |
# 1(1)


# if we see above, few calculation are repeated, like to calculate number of patters for '11' this calculation is
# repeated on left and right side of tree. so can optimize it using dp. like we did in fibonacci series.
dp = dict()
def find_possible_patterns(x):
    # all characters used means we reach to leaf element
    if len(x) < 1:
        return 1
    # if substring starts with 0, it means it is invalid case
    if x[0] == '0':
        return 0

    if x in dp:
        return dp[x]
    # to include single char
    single_case = find_possible_patterns(x[1:])
    double_case = 0
    if len(x)>=2 and  int(x[0:2]) <27:
    # to include double chars
     double_case = find_possible_patterns(x[2:])
    dp[x] = single_case+double_case
    return single_case+double_case


# more faster approach, we used a new var to pass index of given string, because if we pass new substring in each
# function call, then it will create new string in heap, which will take more memory and time.
# but now all 'x' of different function call will point to single string in heap.
class Solution:
    dp = dict()

    @staticmethod
    def numDecodings(x: str, index=0) -> int:

        if len(x) == index:
            return 1
        if x[index] == '0':
            return 0

        if x[index:] in Solution.dp:
            return Solution.dp[x[index:]]
        single_case = Solution.numDecodings(x, index + 1)
        double_case = 0
        if len(x[index:]) >= 2 and int(x[index:index + 2]) < 27:
            double_case = Solution.numDecodings(x, index + 2)
        temp = single_case + double_case
        Solution.dp[x[index:]] = temp
        return temp