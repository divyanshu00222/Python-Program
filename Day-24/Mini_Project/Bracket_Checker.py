def is_valid(expr):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}

    for ch in expr:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return "Invalid"
    return "Valid" if not stack else "Invalid"

expr = input("Enter expression: ")
print(is_valid(expr))
