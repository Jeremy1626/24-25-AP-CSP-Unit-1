from itertools import product

num1 = int(input("please enter a number"))
num2 = int(input("please enter a number"))

if num1 > num2:
    print("number 1 was bigger")
elif num2 > num1:
    print("number 2 was bigger")
else:
    print("both number are the same")