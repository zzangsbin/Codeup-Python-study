num = int(input())

if num%10==1 or num%10==2 or num%10==3:
    if num//10==1:
        print("%dth" %num)
    else:
        if num%10==1:
            print("%dst" %num)
        elif num%10==2:
            print("%dnd" %num)
        else:
            print("%drd" %num)

else:
    print("%dth" %num)