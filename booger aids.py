import numpy as np
n = [45,24,66,89,58,85,89,35]
t = [26,68,39,28,90,21,53,20]
p = np.array(n)
m = np.array(t)
print(type(p))
print(n+t)
print(p+m)
for i in n:
    print(n[i])
    i += 1
