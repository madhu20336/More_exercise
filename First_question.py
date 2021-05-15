def numbers(num):
    i=1
    while number>=i:
        if i%21==0:
            print(i,"navgurukul")
        elif i%7==0:
            print(i,"gurukul")
        elif i%3==0:
            print(i,"nav")
        else:
            print(i)
        i+=1        
number=int(input("enter the number: "))
numbers(number)
