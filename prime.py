x=int(input("enter no: "))
if x>1:
    for i in range(2,int(x/2)+1):
        if (x%i)==0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")           