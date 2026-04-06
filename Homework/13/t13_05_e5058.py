brackets = {
    "}" : "{", ")":"(", "]":"["
}
S = input()
stack = []
for p in S:
    if not(stack and (p in brackets)):
        stack.append(p)
        continue
        
    if stack[-1] != brackets[p]:
        break
    stack.pop()
if stack:
    print("no")
else:
    print("yes")


