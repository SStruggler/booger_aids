n1 = int(input("n1:")) # Don't change this line
n2 = int(input("n2:")) # Don't change this line
op = input() # Don't change this line
result = 0
if op == "+":
    result = n1 + n2
elif op == "-":
    result = n1 - n2
elif op == "/":
    result = n1 / n2
else:
    result = n1 * n2
print(result)