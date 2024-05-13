# ##why postfix##
# The compiler first scans the expression to evaluate the expression b * c, then again scans the expression to
# add a to it. The result is then added to d after another scan. The repeated scanning makes it very inefficient and
# Infix expressions are easily readable and solvable by humans whereas the computer cannot differentiate the operators
# and parenthesis easily so, it is better to convert the expression to postfix(or prefix) form before evaluation.
# The corresponding expression in postfix form is abc*+d+. The postfix expressions can be evaluated easily
# using a stack.
# also we don't need brackets to evaluate postfix.

# precedence order -> '^' < '/*' < '+-'
# associativity order for operators -> '^' (right to left) and '*/+-' (left to right)

# ##infix to postfix conversion
# simple thumb of rule, higher precedence operators will always remain at the top of stack.
# and lower precedence operators will be at bottom.

# scan expression from left to right:
# 1. if we found number, then just print it.
# 2. elif we found operator then:
#       2.1 first check current and stack top operator precedence:
#           2.1.1 if precedence is greater than stack top element then just push it to stack
#           2.1.2 if precedence is same like for '+' and '-' or '+' or '+', then we will check
#                   check for associativity. as '+-' is left associative then, we will pop the items
#                   from stack till stack top item precedence is lower.
#            2.1.3 In case of new operator has lower precedence ,then we will remove stack top items till stack
#            top precedence is lower.
# 3. else if we encounter '(' then we will simply push it to stack.
# 4. else if we found ')' then we will pop all operators till we found '('
# 5.after loop ends, then simply print all remaining the items of stack.

import re
def infix_to_postfix(expression):
    op_precedence = {
        '(': -1, # we are giving bracket as lowest precedence as when open bracket received while popping elements,
        # we don't want to remove it until we receive ')', that's why we give it lowest precedence to keep it.
        '+': 1,
        '-': 1,
        '/': 2,
        '*': 2,
        '^': 3
    }
    right_associative_operands = {'^'}
    stack = []
    res = ''
    for i in expression:
        if bool(re.match('[0-9]', i)):
            res += i
        elif i == '(':
            stack.append(i)
        elif i == ')':

            while stack[-1] != '(':
                res += stack.pop()
            # removing opening backert
            stack.pop()
        elif i in op_precedence:
            # if i is operator
            if len(stack) == 0:
                stack.append(i)
            elif op_precedence[stack[-1]] < op_precedence[i]:
                stack.append(i)
            elif op_precedence[stack[-1]] == op_precedence[i] and i in right_associative_operands:
                stack.append(i)
            else:
                while op_precedence[stack[-1]] > op_precedence[i] or (op_precedence[stack[-1]] == op_precedence[i]
                                                                      and i not in right_associative_operands):
                    res += stack.pop()
    # clearing stack
    while len(stack)!=0:
        res+=stack.pop()
    return res

print(infix_to_postfix('((1 + 2) - 3 * (4 / 5)) + 6'))



# ## postfix evaluation
# 1.Create a stack to store operands (or values).
# 2.Scan the given expression from left to right and do the following for every scanned element.
# 3.If the element is a number, push it into the stack
# 4.If the element is an operator, pop operands for the operator from the stack.
#   Evaluate the operator and push the result back to the stack
# 5.When the expression is ended, the number in the stack is the final answer


def postfix_evaluation(expr):
    stack = []
    for i in expr:
        if bool(re.search('[0-9]', i)):
            stack.append(i)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            expression = op2 + i + op1
            print(expression)
            stack.append(str(eval(expression)))

    print(stack[-1])

postfix_evaluation("231*+9-")


# infix to prefix
# Step 1: Reverse the infix expression i.e A+B*C will become C*B+A. Note while reversing each '(' will become ')' and each ')' becomes '('.
# Step 2: Obtain the "nearly" postfix expression of the modified expression i.e CB*A+.
# Step 3: Reverse the postfix expression. Hence in our example prefix is +A*BC.

# prefix evaluation
# 1. simply traverse from right to left
# 2. If character is an operand push it to Stack
# Step 3: If the character is an operator pop two
#         elements from the Stack. Operate on these elements
#         according to the operator, and push the result
#         back to the Stack
# Step 4: repeat above 2 steps, till all the chars travsered from right to left
#          Then The Result is stored at the top of the Stack, return it