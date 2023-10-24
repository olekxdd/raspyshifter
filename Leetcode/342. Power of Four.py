import math
from time import sleep
# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
n = 123616
x = 1
while x < (2**31):
    po4 = math.pow(n, 1/x)
    x += 1

    print(x)
    if int(po4) is n:
        print("yo")
        break

