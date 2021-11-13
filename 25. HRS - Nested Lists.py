if __name__ == '__main__':
    dic={}
    s=list()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dic:
            dic[score].append(name)
        else:
            dic[score]=[name]
        if score not in s:
            s.append(score)

m=min(s)
s.remove(m)
m1=min(s)
dic[m1].sort()
for i in dic[m1]:
    print(i)


'''
#trial, not a solution
b={}
g=[]
f=[]
c=int(input())

for i in range(c):
    d=input()
    e=int(input())
    b.update({d:e})
    f.append(d)
    g.append(e)
print(b)
print(f)
print(g)
g.sort()
j=set(g)-set(min(g))
print(list(j[0]))
#another, not a solution
d=[]
for i in range(a):
    b = list(map(str, input().split()))
    c = list(map(int, input().split()))
    d.append(b)
    d.append(c)
print(d)
'''
