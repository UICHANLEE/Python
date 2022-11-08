output_list = []
pregress_stack = []

def infix_to_postfix(expression):

    OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
    PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}

    stack = []
    output = ''

    for ch in expression:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()

    return output

exp = "5 * 3 + 12 / ( 4 + 3 * 7 )"
exp_list = exp.split()
infix_to_postfix(exp_list)
print(infix_to_postfix(exp_list))