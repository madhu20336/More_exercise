list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
i=0
new_list=[]
while i<len(list1):
    if list1[i] not in new_list:
        new_list.append(list1[i])
    i=i+1
j=0
while j<len(list2):
    if list2[j] not in new_list:
        new_list.append(list2[j])
    j=j+1
print(new_list)


