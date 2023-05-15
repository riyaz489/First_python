# << left shift multiply number by 2 (fills void with 0)
# >> right shift divide by 2 ie (n/2 == n>>1) (fills void with 0 and 1 in case of -ve)
# ^ -> different bit are 1
# ~ ->  ~a = -a-1 (once compliment, example: ~10 = -11)
# note: python '-' is 2's complement

# bin(a)
# bit shifting is O(1) in current processors

# find log base 2: We right shift x repeatedly until it becomes 0, meanwhile we keep count on the shift operation.
# This count value is the log2(x).

# bitwise operators has lower precedence than + and -
# The left shift and right shift operators cannot be used with negative numbers.

# xor operator with same number give 0 and with different bits it will give 1

# swapping numbers:
# a ^= b;
# b ^= a;
# a ^= b;
# x = a^b , now if we do x^a it will result b and x^b will result a.
# doing xor with same number twice result original value

# CHECK kth bit is set: left shift number to k-1 times (so that our kth bit become lsb)and
# perform & operation on result with 1, now if result is 1
# then it means kth bit was set other it was not.
#   ((n>>k-1) & 1) == 1

# unset last set bit  (mean make 1010 to 1000 because here last set bit was '1' at 2nd position):
# just do '&' current number  with (current number -1)
# example: n= 40 b = 101000
# n-1 = 39 , b= 100111 and now if we do & we will get 100000
# n&(n-1)

# toggling a bit, means if bit is 1 then set 0 else set to 1
# we will use xor operand for that, because xor with 1 will provide toggle of bit and xor with 0 gives same number
# so for toggle k th bit, we will do left shift of 1 to kth position and do xor with number
# res = x ^ (1<<k)

# How to set a bit in the number 'num' : If we want to set a bit at nth position in number 'num' ,
# it can be done using 'OR' operator( | ).
# First we left shift '1' to n position via (1 << n)
# Then, use 'OR' operator to set bit at that position.'OR' operator is used because it will set the bit even if the bit
# is unset previously in binary representation of number 'num'.

# all even numbers have last bit as 0 and odd has last bit 1, so using this technique also we can find all set bits
# just check last bits and keep doing right shift until original number become 0.

# count all set bits in a number:
# we can use above approach for O(n) but for O(1) solution we need to do some preprocessing
# O(1) solution: we will calculate number of set bits in advance for 8 bits.
# so with 8 bits we can form 0-255 (2^8)numbers. so prepare a table for these numbers range.
# then divide our number in 8 bit chunks and compare those chunks with this table one by one.

# note: first (total_bits of n)-1 bits of number n will be same as (total_bits of n/2) bits of n/2, because (x>>1) == (x/2)
# example: 5 = 101 and 5/2 = 2 = 10 so if we remove last bit of 5 it will be sae as 2

# code:
table = []
def  intialize():

    table.append(0)
    for i in range(256):
        # just check the last bit because other bits counts we can get from already calculated values
        table.append(  (i&1) + table[int(i/2)])

def count(n):
    res = 0

    # we are running for loop because in python int does not have fix sized but in other languages int size is fixed
    # like in java it will be 32 bits, so in that case we can fix this loop size as well, which maks this algo as
    # o(1) time complexity, because this loop will ru always 4  in java or C.
    while n > 0:
        # first take the 8 bit chunks
        res += table[n & 0xff] # 0xff is equivalent to 11111111
        # now remove first 8 bits which already processed
        n = n>>8
    return res
intialize()
print(table)
print(count(12))
print(count(16))

# check power of 2: do and with x-1 and if we got 0 in result it means it's a power of 2.
# because numbers which are power of 2 have only single '1' in MSB.

# find MSB set bit in number: log2(x) will gve bit position and to find number do 2^(log2(x))
# example : 18 -> log2(18) = 4 -> 2^(log2(18)) = 16

# XOR of 1 to N numbers : XOR operations for 1 to N numbers repeat after 4 value.
# solution: Find the remainder of N by moduling it with 4.
# If rem = 0, then xor will be same as N.
# If rem = 1, then xor will be 1.
# If rem = 2, then xor will be N+1.
# If rem = 3 ,then xor will be 0.



# find number which is occuring odd number of times:
# x^0 = x
# x^1 = will result in opposite bits
# x^y = y^x
# x^y^x = y
# x^x = 0
# so we will use above xor operator properties to find number occurring odd times.
# so simpy do xor with all elements in list and result will e the number which is oddly occurring.

# find missing number in a sequence of number:
# sol: (i[0]^i[1] ...)^(1^2 ...)
# so simply xor input list with expected sequence and result will be the missing number.

# find 2 odd occuring numbers:
# first do xor fo all numbers it will result xor of 2 odd ocuring numbers
# example: [1,2,2,4]
# xor of all items  = 1^4 = x
# now find first set bit from right(least significant bit), because set bit means that position bit is
# different in both numbers
# now create 2 lists, in first one put all elements whose bit is set at that particular position
# and in another list bit is 0 at that partiular posisiton.
# now do xor of those list itmes u will get your 2 noumbers
# for example if we get these 2 lists after above operation:
# l1 = [1,2,2] = 1
# l2 = [4,5,5] = 4
# then 1 and 4 is our answer.


# to check first set bit from right:
# ans = n & ~(n-1)
# above eqation will give us number which has only one set, which is at same position as first right set bit of n
# example:
# for n=32, ans will be 8
# now to check if x has that bit set which we got in answer, we will simply do & operation
# result(0/1) = ans & x


# incase we have groups of 1's and 0s in string, and to find which one has min groups:
# in binary numbers we and have either 0 or 1 due to this property, if string start with 1 and end with 1
# it means number of groups of 1 is greater than numer of group of 0's by 1
# it string start with 1 an end with 0, it means we have same number of groups for 0 and 1
# example: 1001-> number of group of 1's = 2
# number of group of 0's = 1

