
'''
#not pressing enter button
n=input()
l=n.split()
s=set(l)

print(len(s))'''
l=list()
m=int(input())
for i in range(m):
    n = input()
    l.append(n)

print(len(set(l)))