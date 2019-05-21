#import math

L = [17, 38, 10, 25, 72]

L.append(12)

print(L)

val=L[4]
print(val)

long=len(L)
print(long)

L.remove(38)
print(L)

L.extend([8,14,29])
print(L)

del(L[2])
print(L)

L[0]=55
print(L)

L2=L[1:5]
print(L2)

L3=L[:3]
print(L3)

L4=L[2:]
print(L4)

L5=L2+L3+L4
print(L5)

LL=L[:]  #LL=list(L)
LL.append(99)
print(LL)
print(L)

L6=[x**3 for x in range(5,12)]
print(L6)

L7=[2*x**2-3*x+5 for x in range(1,9)]
print(L7)

L8=[x**2 for x in range(10,21,2)]
print(L8)

L8=[x**2 for x in range(9,21) if x%2==0]
print(L8)

L9=[x for x in range(111,130) if x%3==0]
print(L9)












