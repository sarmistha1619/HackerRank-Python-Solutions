t=int(input())#this must be an odd number
c="H"

#top cone
for i in  range(t):
    print((c*i).rjust(t)+c+(c*i).ljust(t-1))

#top piller
for i in range(t+1):
    print((c*t).center(t*2)+(c*t).center(t*5-4))

#middle belt
for i in range((t+1)//2):
    print((c*t*5).center(t*6))

#bottom piller
for i in range(t+1):
    print((c*t).center(t*2)+(c*t).center(t*5-4))

#bottom cone
for i in range(t):
    print(((c*(t-i-1)).rjust(t*4)+c+(c*(t-i-1)).ljust(t*5).rjust(t*5-1)))