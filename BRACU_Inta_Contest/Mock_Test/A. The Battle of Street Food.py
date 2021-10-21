import math
n = int(input())
for x in range(n):
    sa = int(input())
    r = (math.sqrt(sa))/2
    A = sa - math.pi * (math.pow(r, 2))
    P = (r * math.pi/2) * 4
    print(A, P)
