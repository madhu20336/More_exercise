number_of_studen=int(input("enter tne number: "))
ek_student_ka_kharcha=int(input("enter the amount: "))
total_kharcha=number_of_studen*ek_student_ka_kharcha
if total_kharcha <= 50000:
    print("Hum budget ke andar hai")
else:
    print("ab paise nhi mileg")
