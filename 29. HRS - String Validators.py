if __name__ == '__main__':
    s = input()
    print(any([i.isalnum() for i in s]))
    print(any([i.isalpha() for i in s]))
    print(any([i.isdigit() for i in s]))
    print(any([i.islower() for i in s]))
    print(any([i.isupper() for i in s]))

'''
#another solution
n=input()

print(n.isalnum())
print(n.isalpha())

l=list(n)
for i in l:
    s = ''.join(i)
    h = s.isdigit()
    j = s.islower()
    k = s.isupper()
    if h == True:
        print(h)
    elif j == True:
        print(j)
    elif k == True:
        print(k)
'''