for i in range(1,11):
    if i%2==0 and i%5==0:
        print(f"{i} FizzBuzz")
    elif i%2==0:
        print(f"{i} Fizz")
    elif i%5==0:
        print(f"{i} Buzz")
    else:
        print(i)
    