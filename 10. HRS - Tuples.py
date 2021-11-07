n = int(input())
integer_list = map(int, input().split())
a=(list((integer_list)))

tuplex= (*a,)

print(hash(tuplex))