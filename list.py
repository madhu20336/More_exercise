list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
i=0
list3=[]
while i<len(list1):
    j=0
    while j<len(list2):
        if list1[i] in list2:
            list3.append(list1[i])
            break
        j+=1
    i+=1
print(list3)