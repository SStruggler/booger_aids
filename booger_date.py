x = " * "
y = "   "
for i in range(0,10):
    print((10-i)*x+(i*y)+(i*y)+(10-i)*x)
    i += 1
for i in range(0,10):
    print((i+1)*x+((9-i)*y)+((9-i)*y)+(i+1)*x)
    i += 1