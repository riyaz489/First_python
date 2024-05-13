# << left shift multiply number by 2 (fills void with 0) (3<<5 == 3*pow(2,5))
# >> right shift divide by 2 ie (n/2 == n>>1) (fills void with 0 and 1 in case of -ve) (13>>4 == int(13/pow(2,4)))
# ^ -> different bit are 1
# ~ ->  ~a = -a-1 (once compliment, example: ~10 = -11)
# note: python '-' is 2's complement
# most of the language use 2's complement because here leading bit always be 1, due to which 0 will have only one
# representation for +ve and -ve numbers. also subtraction and addition to 0 will give correct result in 2s complement.

# bin(a)
# bit shifting is O(1) in current processors


# x// 10 -> removes last digit in decimal number.
# x //2 -> removes last digit in binary number.
# x%10 -> return only last digit in decimal number.
# x%2 -> returns last digit in binary number.


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


# Check if last bit set just do 'and' with 1 as in 1 only last bit is set. so result of AND operation is 1
# then answer is yes otherwise it is no.
# CHECK kth bit is set: right shift number to k-1 times (so that our kth bit become lsb)and
# perform & operation on result with 1.
#  or we will do k-1 left shifts to 1 and then do AND with our number.
# now if result is 1 it means Kth bit was set.
#   ((n>>k-1) & 1) == 1

# To keep only first k numbers of bits in a number we can do AND with k 1s.
# for example in 10101010 to keep only first 3 bit and unset others. we can do AND with 00000111 ( or 2^3-1) then result
# will be 00000010.
# similarly to remove first k bits we can do k right shift. or we don't want to change position of bits like
# above,then after right shit we can do k left shifts.


# Unset last set bit  (mean make 1010 to 1000 because here last set bit was '1' at 2nd position):
# just do '&' current number  with (current number -1)
# example: n= 40 b = 101000
# n-1 = 39 , b= 100111 and now if we do & we will get 100000
# n&(n-1)
# we can repeat this approach to count all 1 in a number binary representation. we can run a loop till n become 0.
# and keep removing 1 from left side.

# Toggling a bit, means if bit is 1 then set 0 else set to 1
# we will use xor operand for that, because xor with 1 will provide toggle of bit and xor with 0 gives same number
# so for toggle k th bit, we will do left shift of 1 to kth position and do xor with number
# res = x ^ (1<<k)

# To toggle all bits in a number : given number - number where all bits are set to 1.


# How to set a bit in the number 'num' : If we want to set a bit at nth position in number 'num' ,
# it can be done using 'OR' operator( | ).
# First we left shift '1' to n position via (1 << n)
# Then, use 'OR' operator to set bit at that position.'OR' operator is used because it will set the bit even if the bit
# is unset previously in binary representation of number 'num'.

# All even numbers have last bit as 0 and odd has last bit 1, so using this technique also we can find all set bits
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

# Check power of 2: do and with x-1 and if we got 0 in result it means it's a power of 2.
# because numbers which are power of 2 have only single '1' in MSB.
# (n & (n-1)) == 0

# Find MSB set bit in number: log2(x) will gve bit position and to find number do 2^(log2(x))
# example : 18 -> log2(18) = 4 -> 2^(log2(18)) = 16

# XOR of 1 to N numbers : XOR operations for 1 to N numbers repeat after 4 value.
# solution: Find the remainder of N by moduling it with 4.
# If rem = 0, then xor will be same as N.
# If rem = 1, then xor will be 1.
# If rem = 2, then xor will be N+1.
# If rem = 3 ,then xor will be 0.



# XOR opertaion -> for same bits it gives us 0
# x^0 = x
# x^1 = will result in opposite bits
# x^y = y^x
# x^y^x = y
# x^x = 0
# a xor b = b xor a # commutative
# a xor (b xor c) = (a xor b) xor c  # associative.

# Find number which is occuring odd number of times:
# so we will use above xor operator properties to find number occurring odd times.
# so simpy do xor with all elements in list and result will e the number which is oddly occurring.

# Find missing number in a sequence of number:
# sol: (i[0]^i[1] ...)^(1^2 ...)
# so simply xor input list with expected sequence and result will be the missing number.

# Find 2 odd occurring numbers:
# first do xor fo all numbers it will result xor of 2 odd occurring numbers
# example: [1,2,2,4]
# xor of all items  = 1^4 = x
# now find first set bit from right(least significant bit), because set bit means that position bit is
# different in both numbers
# now create 2 lists, in first one put all elements whose bit is set at that particular position
# and in another list bit is 0 at that particular position.
# now do xor of those list items u will get your 2 numbers
# for example if we get these 2 lists after above operation:
# l1 = [1,2,2] = 1
# l2 = [4,5,5] = 4
# then 1 and 4 is our answer.
# Now the problem is how we are going to generate number k, such as k contains only one set bit and that set bit
# will be on same position as first set bit of number which results to xor of all input numbers.
# for example : xor of all numbers was 3 (011) now we have to generate  k which will be 001
# (k is generated by keeping only first set bit, using k we can divide input numbers into 2 grps by doing
# AND with k and check if they have 1 or 0 on this position)
# to find k:
# x= 3 = 0011
# x-1 = 2 = 0010  (unset the last set bit)
# ~(x-1) = 1101   (opposite bits of x, except the last set bit which we modified using x-1)
# ~(x-1) AND x = 0001 (we get only first set bit, other bits are 0)
# [after simplification k = n & ~(n-1) ]


# To find first set bit from right:
# ans = n & ~(n-1)


# Incase we have groups of 1's and 0s in string, and to find which one has min groups:
# in binary numbers we and have either 0 or 1 due to this property, if string start with 1 and end with 1
# it means number of groups of 1 is greater than numer of group of 0's by 1
# if string start with 1 an end with 0, it means we have same number of groups for 0 and 1
# example: 1001-> number of group of 1's = 2
# number of group of 0's = 1


# Print all subsets using bitwise operations with iterations instead of recursion:
# as we know number of subset  = 2^n,
# and binary representation of each number from 0 to 2^n will cover all subsets.
# each bit for each number will tell us wether to consider a char or not. for 0 we will skip the index and
# for 1 we will include it.
# for example for set (a,b,c,d),  3 means 0011, i.e a and b will be skipped as we have 0 for their indicies.
# and only c and d will be printed.

# Log base 2:
# We right shift x repeatedly until it becomes 0, meanwhile we keep count on the shift operation.
# This count value is the log2(x)



# break number into power of 2s. every number can be broken down into power of 2
# 10 = bin(1010). if we take 1s position in bin representation of number,  as power of 2.
# then we get  2^3 + 2^1 = 8+2 = 10. here powers are number of 0 after current 1.

# def break_num(n):
#     res = 1
#     while n:
#
#         if n%2!=0: # checking if last bit is 1
#             print(res)
#             n-=1 # removing 1 form last bit
#         else:
#             res*=2 # increasing power if bit is 0
#             n//=2 # removing right bit
#
# break_num(10)