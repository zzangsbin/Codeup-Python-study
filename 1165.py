time, mt = map(int, input().split())

if time%10 == 0:
    goal=(90-time)//5
else:
    goal=(90-time)//5+1

print(mt+goal)
