storage = int(input())

s = storage

a = s//10
b = s%10

result = (10*b + a)*2

if result>100:
    result=result%100

print(result)

if result<=50:
    print("GOOD")

else:
    print("OH MY GOD")