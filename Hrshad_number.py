num = int(input("enter the number: "))
sum = 0
number = num
while num > 0:
    sum = sum + num % 10
    num = num // 10
if number % sum == 0:
    print(number, " is harshad number")
else:
    print(number, "is not harshad number")
