def is_matched(expression):
    stack = []
    pairs = {'{': '}', '[': ']', '(': ')'}
    
    for char in expression:
        if char in pairs.keys():
            stack.append(pairs[char])
        elif stack != [] and char == stack[-1]:
            stack.pop()
        else:
            return False
        
    return stack == []

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

