# •	Convert rational numbers into p/q form, for recurring numbers only
# Example: 1/3 = 0.333…
# (Main goal is to eliminate recurring element)
# Formula-> (x *10^ (number of recurring element)) - x
# In above example number only 3 is repeating, so number of recurring elements is 1
# So, Let say x = 0.333 and 10x = 3.33
# Sub those 2 equations
# 9x =3-> x = 1/3, we got original p/q form again

# •	Convert rational numbers into p/q form, for recurring and non-recurring numbers mix:
# Formula ->
# X = non repeating and first occurrence of repeating number
# Y= non repeating number)
# Result = (x-y)/(10^ no of digits in x – 10^ no of digits in y)
# Example: 0.5923923…
# X = (5923 – 5)/(9990) = 5918/9990

# •	Count number of digits:
    # o	Count key pressed while writing to 1000
    # 1 digit numbers are 1-9  -> 9 times for 1 digit
    # 2 digit numbers are 10-99 -> 90*2 times for 2 digit
    # Using above be can device a formula: 1*9 + 2*90 + 3*900 + 4*1 = 2893

    # o	Count number of 2 from 1 to 100
    # 2 occur 10 times in 1st place and 10 times in 2nd place
    # Total 20
    # Similarly for 1-1000-> 200 times

    # o	If we write natural numbers what we will get at 426 digit
    # First 9 [1-9]-> 426 – 9-> 417
    # 2 digits numbers [180] -> 417-180 = 237
    # 3 digit numbers -> 237/3 = 79
    # So actual number will be -> 9+90+79 = 178

    # o	How many numbers between and inclusive 200-500 which are divisible by 4 and 5 both:
    # Numbers divisible by 5 -> 500-200 we have 301 numbers-> 301/5[201-500] + 1[200] -> 61
    # Numbers divisible by 4 -> 25[201-300] + 25[301-400] + 25[401-500]+1[200] = 76
    # Numbers divisible by both should be divisible by 20-> 16
    # 			76+61-16 = 121


# •	LCM and HCF- >
    # 	Lcm always multiple of hcf
    # 	Lcm * hcf = product of 2 nos
    # 	Co prime are those numbers which has hcf as 1

# example: 12 and 16
# 12-> 2x3x2       ; lcm-> 2x3x2x4 (common/repeated factors will be consider only once)
# 16 -> 2x2x2x2    ; hcf-> 2x2  (only common)

# algo fo GCD(HCF)
# euclidian algo:
# 1. If we subtract a smaller number from a larger (we reduce a larger number), GCD doesn’t change
# 2. also we know gcd(0,x) will be x
# so here if we  keep subtracting repeatedly the larger of two, we end up with GCD.
# keep subtracting until b become 0. so to speed up process we will use %(mod-> (x mod y) Remainder when you divide x by y).

# complexity: O(log(n))
def GCD(a,b):
    if b==0:
        return a
    else:
        GCD(b, a%b)




# •	Find smallest 4 digit number, which when divided by 8 & 12 leaves same reminder 5
# Lcm*x + 5 >= 1000 -> k>=995/72 -> k=14
# Result = 14*72+5 = 1013

# •	Number of times key pressed while typing 1-1000:
# One digit number are 1-9 -> 1*9 times for 1 digit numbers
# 2 digit number are 10-99 (total 90) -> 2*90 times for 2 digit numbers
# So we can device formula using above: 9+ 2*90 +3*900 + 4*1 = 2893
#

