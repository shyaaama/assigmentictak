def cube(n):
    return sum(i**3 for i in range(1,n))
pos_int=int(input("enter a positive integer: "))
res=cube(pos_int)
print(res)