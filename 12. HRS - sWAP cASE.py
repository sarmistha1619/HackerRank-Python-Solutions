'''
#in this way, the output will come with an "None" word
def swap_case(s):
    for i in s:
        if i==i.lower():
            print(i.upper(), end="")
        elif i == i.upper():
            print(i.lower(), end="")
    return

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
'''
l=[]
def swap_case(s):
    for i in s:
        if i==i.lower():
            l.append(i.upper())
        elif i==i.upper():
            l.append(i.lower())
        #   print(a)
        # convert list to string
        # print(''.join(a))
    return (''.join(l))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)