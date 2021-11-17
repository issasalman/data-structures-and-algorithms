from stack_and_queue.Stack import Stack

def validate_brackets(brackets):
    """
    Function to check validate brackets to be balanced in closed in right order

    """
    stack = Stack()
    i=0
    while  i < len (brackets):
        if brackets[i] in ["(", "{", "["]:
            stack.push(brackets[i])

        elif brackets[i] in [")", "}", "]"]:
            if stack.is_empty():
                return False
            item = stack.pop()
            if item == '(':
                if brackets[i] != ")":
                    return False
            if item == '{':
                if brackets[i] != "}":
                    return False
            if item == '[':
                if brackets[i] != "]":
                    return False
        i+=1

    return True

print (validate_brackets("(g)"))


print (validate_brackets("{}{Code}[Fellows](())"))

print (validate_brackets("{(})"))



