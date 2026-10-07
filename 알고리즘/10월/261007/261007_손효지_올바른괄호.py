def solution(s):
    my_stack = []
    
    for cha in s:
        if cha == ')' and my_stack and my_stack[-1] == '(':
            my_stack.pop()
        else:
            my_stack.append(cha)
    if not my_stack:
        return True
    else:
        return False
    