'''
without creating function

l = input()
for i in l:
    if i==" ":
        print("-",end='')
        continue
    else:
        print(i, end='')'''

def split_and_join(line):
    # write your code here
    split= line.split(" ")
    join="-".join(split)
    return join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)