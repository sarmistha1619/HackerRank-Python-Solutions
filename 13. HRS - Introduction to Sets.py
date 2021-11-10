'''
### this runs so perfectly
#without function
sum=0
n=int(input())
for i in range(n):
    arr = int(input())
    sum = sum + arr
av=round(sum/n,3)
print(av)'''

sum=0

def average(array):
    # your code goes here
    arrL= list(set(arr))
    sum=0
    for i in arrL:
      sum=sum+i
# print(sum)
    res= sum/len(arrL)
    ress=round(res,3)
    return ress

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)