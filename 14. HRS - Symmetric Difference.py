n = int(input())
b=set(map(int, input().split()))

m = int(input())
d=set(map(int, input().split()))

e=b.intersection(d)
h=(b-e)|(d-e)
j=list(h)
j.sort()

for i in j:
    print(i)
'''
#in details.
n = int(input())
a=map(int, input().split())
b=set(a)

m = int(input())
c=map(int, input().split())
d=set(c)

e=b.intersection(d)

f=b-e
g=d-e
h=f|g
j=list(h)
j.sort()
l=len(j)

for i in j:
    print(i)
    '''
'''
#ANOTHER SOLUTION
# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
setM=  set(map(int, input().split()))

n=int(input())
setN=  set(map(int, input().split()))


a=setM.difference(setN)

b=setN.difference(setM)

res=a.union(b)

resL=sorted(res, reverse=False)

for i in resL:
  print(i)

'''