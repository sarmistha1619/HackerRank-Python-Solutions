'''
a=int(input())
l1=list()

for c in range(a):
    d=input()
    l1.append(d)
s1=set(l1)

b=int(input())
l2=list()
for e in range(b):
    f=input()
    l2.append(f)
s2=set(l2)
print(len(s1&s2))
'''

m=int(input())
a=  set(map(int, input().split()))
n=int(input())
b=  set(map(int, input().split()))
total= a.intersection(b)
print(len(total))