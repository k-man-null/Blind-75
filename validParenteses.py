def validParenthesis(s):
    stack = []

    for i in range(len(s)):
        if  s[i] in "({[":
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == "(" and s[i] == ")":
                    stack.pop()
                elif stack[-1] == "[" and s[i] == "]":
                    stack.pop()
                elif stack[-1] == "{" and s[i] == "}":
                    stack.pop()
                else:
                    return False
    if len(stack) == 0:
        return True
    else:
        return False
            

print(validParenthesis("{}()[]"))
