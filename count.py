str=input("enter a string: ")
unique_char=set(str)
for char in unique_char:
    count=str.count(char)
    print(f"{char} ={count}",end=",")