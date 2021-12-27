time, mt, yt = map(int, input().split())

if time%10 == 0:
    goal=(90-time)//5
else:
    goal=(90-time)//5+1

if mt+goal>yt:
    print("win")

elif mt+goal==yt:
    print("same")

else:
    print("lose")