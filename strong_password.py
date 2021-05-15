password=input("enter the password: ")
if len(password)>=6 and len(password)<=16:
    if  "A" in password or "Z" in password :
        if "2" in  password  or "8" in password:
            if "$" in password:
                print("your password is strong password")
            else:
                print("In your password not a doller sign")
        else:
            print("In your password not a 2 and 8 digit")
    else:
        print("In your password not a A and Z alphabet")
else:
    print("length is less then 6")
    