def fact(f):
    if f==0 or f==1:
        return 1
    else:
        return f*fact(f-1)
n=int(input("enter number"))
print(fact(n))