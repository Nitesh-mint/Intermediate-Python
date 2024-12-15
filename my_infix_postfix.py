#my own implementation of infix to postfix implementation
from stack import Stack  

def infx_to_post(expression):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    s = Stack()
    output_list = []
    expression_list = expression.split(" ");
    for item in expression_list:
        if item in "ABC":
            output_list.append(item)
        else:
            if s.is_empty():
                s.push(item)
            else:
                current_stack = s.peek()
                while prec[item] >= prec[current_stack]:
                    output_list.append(item)
                    s.pop()
                    current_stack = s.peek()
    print(output_list)
infx_to_post("A + B * C")

