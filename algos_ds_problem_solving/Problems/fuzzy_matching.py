# the fuzzy matching problem is to input two strings and return a score quantifying the likelihood that they are
# expressions of the same entity.
# So (John, Jon) should get a high score but not (John, Jane).

# there are several algo for fuzzy match, but they broadly fall into these 2 category:
# lexical matching and phonetic(sound) matching.

# lexical matching: it occurs usually due to typing or spelling mismatch.
# like jonathan and jonahtan has only 'th' difference so it has high match.

# phonetic matching:Phonetic matching algorithms match strings based on how similar they sound.
# Consider Kathy and Cathy. They sound similar enough that one person might spell as Kathy, another as Cathy.
# As in this case, one is not necessarily a misspelling of the other. just sounds similar.

# there is 3rd algo as well in which use maths functions 'cosine similarity'
# here we check vector angle between 2 chars.



#### luxical matching (The Levenshtein Distance)

# here we create 2x2 matrix and set input word as column and out as rows
# by moving top to down and left to right, we decide in how many steps(choose minimum), we can convert current substring
# to target substring.

# in case current chars do not match then we choose minimum (top element, left element and top-left diagonal element)
# and do +1 with minimum one in current position
# and if value is same so just copy-paste number of minimum

# position representation Operations ->
# replace | delete
# insert  | (i,j) [current position]

# example
#   '' r e p l a c e
# '' 0 1 2 3 4 5 6 7  (example: to convert `replace` into '' we need 7 delete operations that's why x[0,7] is 7)
# d  1 1 2 3 5 4 6 7
# e  2 2 1 2 3 4 5 6
# l  3 3 2 2 2 3 4 5
# e  4 4 3 3 3 3 4 4
# t  5 5 4 4 4 4 4 5
# e  6 6 5 5 5 5 5 4


def minDistance(word1, word2):
    dp = list(list() * len(word1))

    # we knew first row and columns are +1 of prev operation so directly assigning it
    # and avoid adding '' as first element on (0,0) position like we did in example
    for i in range(len(word2)):
        dp.append([i] * len(word1))

    for i in range(1, len(word1)):
        dp[0][i] = i

    for row in range(1, len(word2)):
        for col in range(1, len(word1)):
            if (word1[col - 1] == word2[row - 1]):
                # just copy value of top left diagonal element. as diagonal will always going to have min value.
                dp[row][col] = dp[row - 1][col - 1]

            # check min of three operations and do +1 in it
            else:
                dp[row][col] = min({dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]}) + 1
    print(dp)

    # return lat element f dp
    return dp[len(dp) - 1][len(dp[0]) - 1]


print(minDistance('ee', 'eee'))

#   '' e e
#   0  1 2
# e 1  0 1
# e 2  1 0
# e 3  2 1


# for substring/ prefix matching we will simply use TRIE
# for suffix matching we will use suffix trie (In this case first we will generate all suffix of a sting using simple for loop and put it into TRIE ds)
# If words are different by few characters or spelling mistakes or phonetically same, then in that case  we can simply use above mentioned fuzzy matching algos.

# in case of sentence matching:
# for prefix and suffix again use TRIE, just consider sentence as one big word with whitespaces.
# in case setence words does not match then again we can use above mentioned fuzzy match algos, by considering sentence a one big word.
# or we can use cosine similarity algo.
# cosine algo:
# so here first we will remove all punctuations from sentnece, then convert all words into numbers and store them into array
# then we will apply below formula to find out similarity between those 2 arrays.
# Similarity = (A.B) / (||A||.||B||)
# where A and B are vectors:
# A.B is dot product of A and B: It is computed as sum of element-wise product of A and B.
# ||A|| is L2 norm of A: It is computed as square root of the sum of squares of elements of the vector A.

# in case sentence words does not match but we want to compare their literal meaning then we have to use Natural Language Processing machine learning
