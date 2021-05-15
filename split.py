# def break_into_words(sentence):
#     return sentence.split()
# word = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system" 
# print(break_into_words(word))



sentence = "navgurukul is an alternative to higher education reducing the barriers of current formal education system"
list1=[]
list2=""
for i in sentence:
    if i == " ":
        list1.append(list2)
        list2 = " "
    else:
        list2 += i
if list2:
    list1.append(list2)
print (list1)
