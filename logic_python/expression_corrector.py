closed_parentheses = []
open_parentheses = []
example = str(input("Enter your expression: "))
for i in example:
    if i == "(":
        closed_parentheses.append('(')
    elif i == ")":
        open_parentheses.append(')')
if len(closed_parentheses) == len(open_parentheses):
    print('Correct expression')
else:
    print('Incorrect expression')
