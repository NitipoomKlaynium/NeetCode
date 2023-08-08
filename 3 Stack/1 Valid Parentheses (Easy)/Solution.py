def isValid(s: str) -> bool:
    pair = {")" : "(", "]" : "[", "}" : "{"}
    
    stack = []
    for c in s :
        if c in ")}]" :
            top = stack.pop() if stack else "#"
            if pair[c] != top :
                return False
        else :
            stack.append(c)

    return not stack

if __name__ == "__main__" :
    print(isValid("(([{{()}}]))()"))