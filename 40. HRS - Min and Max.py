import numpy
arr=[]
n,m=map(int,input().split())
for row in range(n):
    my_arr=list(map(int,input().split()))
    # print(row)
    arr.append(my_arr)
my_array=numpy.array(arr)
a=(numpy.min(my_array, axis=1))
# print(a)
print(numpy.max(a))
# print(my_array)