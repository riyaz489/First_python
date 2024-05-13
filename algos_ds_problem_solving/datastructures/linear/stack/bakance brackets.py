# In this problem we will be given 6 chars (,{,[,),},]
# and we have to check that if some bracket is opened then its same type of bracket sould be next char.
# for example:  {[}] is invalid ; {[]} is valid

def check_balacned_paranthesis(data):
    pairs = {'}': '{',
             ']': '[',
             ')': '('
             }
    opening_chars = { '[', '{', '('}
    stack = []
    if len(data)%2 ==1:
    # as in odd numbers of chars 1 opening or closing bracket will be extra
        return False

    for ch in data:
        if ch in opening_chars:
            stack.append(ch)

        else:
            if len(stack) == 0:
                return False
            if stack.pop() != pairs[ch]:
                return False

    # checking if we still have remaining opening brackets
    return len(stack) == 0


print(check_balacned_paranthesis('([[]]{})'))
print(check_balacned_paranthesis('([[]]{}){{'))