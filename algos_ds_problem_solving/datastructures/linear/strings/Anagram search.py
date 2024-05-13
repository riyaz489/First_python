## Check Anagram, here chars will be same bt ordering of chars is different. also both words lenght should be same.
# we create a char freq array, whenever a char appears in first word we will increase its freq
# and whenever a char appears in second word we will decrease its freq.
# and in final freq count dict freq of all chars should be 0.
def check_anagrm(a,b):
    if len(a)!=len(b):
        return False
    freq = {}
    for i in range(len(a)):
# increasing freq for elements occurs in a
        if a[i] in freq:
            freq[a[i]] +=1
        else:
            freq[a[i]] = 1
# subtracting freq for elem occurs in b
        if b[i] in freq:
            freq[b[i]] -=1
        else:
            freq[b[i]] = -1
    for v in freq.values():
        if v!=0:
            return False
    return True
print(check_anagrm('ewqq','qewq'))

## Find Anagram pattern in given string
# our task is to find if anagram of given pattern is present in given input string
# for example: input = helllosam; pat = aso
# now in input string there exists a pattern osa which is anagram of input pattern.

# idea is simple first we generate a chars freq dict for 0 to len(patt)-1 from input string.
# and similarly we generate a freq dict for pattern as well.
# then we eun a loop from 0 to len(input)-len(patt)
# then we compare our current window chaar freq dict with pattern dict
# if it matches then we print current index
# and for next window we will simply decrease freq of 1st char of prev window and increase freq of new char added in
# new window. (its rolling window technique)
# for example: input is `abcd` and pat len is 3
# so char dict for first window will be => a:1, b:1, c:1
# and for second window will be => b:1, c:1, d:1

def is_dict_equal(d1:dict,d2:dict):
    if len(d1)!=len(d2):
        return False
    if set(d1.keys()) != set(d2.keys()):
        return False
    if any(d2[x]!=y for x, y in d1.items()):
        return False
    return True


def find_anagram_pat(data, patt):
    window_char_freq = {}
    patt_char_freq = {}

    # generating first window
    for i in range(len(patt)):
        if data[i] in window_char_freq:
            window_char_freq[data[i]] += 1
        else:
            window_char_freq[data[i]] = 1

        if patt[i] in patt_char_freq:
            patt_char_freq[patt[i]] += 1
        else:
            patt_char_freq[patt[i]] = 1

    # checking if pattern exists:
    for i in range(len(data)-len(patt)+1):

        # compare freq dict
        if is_dict_equal(patt_char_freq, window_char_freq):
            print(i)

        # generate next window

        window_char_freq[data[i]] -= 1

        if i+len(patt)< len(data):
            # removing char if its freq become 0
            if window_char_freq[data[i]] == 0:
                window_char_freq.pop(data[i])

            # adding new char freq to window
            if data[i+len(patt)] in window_char_freq:
                window_char_freq[ data[i+len(patt)]]+=1
            else:
                window_char_freq[ data[i+len(patt)]]=1


find_anagram_pat('fsdfdsasdvcdsfdsf', 'fsd')

