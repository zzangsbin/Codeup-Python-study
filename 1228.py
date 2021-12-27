키, 몸무게 = map(float, input().split())
표준몸무게 = (키-100)*0.9
비만도 = (몸무게-표준몸무게)*100/표준몸무게

if 비만도<=10:
    print("정상")

elif 10<비만도<=20:
    print("과체중")

else :
    print("비만")