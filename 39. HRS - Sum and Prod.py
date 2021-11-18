import numpy as np
arr=[]
n,m=map(int,input().split())
for row in range(n):
    my_arr=list(map(int,input().split()))
    # print(row)
    arr.append(my_arr)
my_array=np.array(arr)
sum= np.sum(my_array,axis=0)
# print(sum)
prod= np.prod(sum)
print(prod)