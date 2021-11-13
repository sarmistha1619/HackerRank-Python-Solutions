test= int(input())
for i in range (test):
  numA= int(input())
  eleA= set(map(int, input().split()))
  numB= int(input())
  eleB= set(map(int, input().split()))
  if (eleA&eleB)==eleA:
    print(True)
  else:
    print(False)