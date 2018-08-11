import numpy as np
import time as tm

a = np.array([1,2,3,4])
print(a)
# checking performance difference between vector processing and explicit for-loop
## vectorised version
a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic  = tm.time()
c = np.dot(a,b)
toc = tm.time()

print("c = " + str(c))
print("Vectorized version : " + str(1000 * (toc - tic)) + " ms")
print("\n")
## explicit for loop

c = 0
tic = tm.time()
for i in range(1000000):
    c += a[i] * b[i]
toc = tm.time()

print("c = " + str(c))
print("Explicit for loop version: " + str(1000 * (toc - tic)) + " ms")