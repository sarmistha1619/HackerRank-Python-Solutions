a=int(input())
b=map(int, input().split())
c=list(b)
d=max(c)
e=set(list([d]))
f=set(c)
g=f-e

h=list(g)
i=max(h)
print(i)