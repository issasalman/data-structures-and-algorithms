def validate_brackets(brackets):
    """
    Function to check validate brackets to be balanced in closed in right order

    """
    stack = []
    i=0
    while  i < len (brackets):
        if brackets[i] in ["(", "{", "["]:
            stack.append(brackets[i])

        elif brackets[i] in [")", "}", "]"]:
            if len(stack) ==0:
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



