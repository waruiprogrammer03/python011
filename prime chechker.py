num = 13
if num > 1:
    for x in range(2, num):
        if num % x == 0:
            print("Not prime")
        else:
            print("the number is prime")
            break
    else:
        print("The number is not a prime number")