if __name__ == '__main__':
    N = int(input())
    arr=[]

    for i in range(N):
        s= input().split()
        for i in range(1,len(s)):
            s[i]=int(s[i])

        if s[0]== "append":
            arr.append(s[1])

        elif s[0]=="insert":
            arr.insert(s[1],s[2])

        elif s[0]=="remove":
            arr.remove(s[1])

        elif s[0]== "pop":
            arr.pop()

        elif s[0]=="sort":
            arr.sort()

        elif s[0]== "reverse":
            arr.reverse()

        elif s[0]== "print":
            print(arr)
'''
#another solve, not worked in hackerrank
a=int(input())
l=[]

l.insert(0, 5)
l.insert(1, 10)
l.insert(0, 6)
print(l)
l.remove(6)
l.append(9)
l.append(1)
l.sort()
print(l)
l.pop()
l.reverse()
print(l)
'''