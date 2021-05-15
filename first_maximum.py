num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
num3=int(input("enter a number: "))
if num1>num2 and num1>num3:
    print(num1,"is maximum")
elif num2>num1 and num2>num3:
    print(num2,"is maixmum")
else:
    print(num3,"is maximum")