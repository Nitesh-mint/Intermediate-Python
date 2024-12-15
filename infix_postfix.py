from stack import Stack
# Algoritm to convert infix equation to a postfix.
op_stack = Stack()
output_list = []
def infix_to_postfix(expression):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    input_string = expression.split(" ")
    for token in input_string:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            output_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != '(':
                output_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while(not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                output_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        output_list.append(op_stack.pop())
        return " ".join(output_list)
print(infix_to_postfix("A + B * ( C ^ D - E ) ^ ( F + G * H ) - I"))
