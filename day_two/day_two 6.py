list1=[1,3,5,7]
list2=[2,4,6,8]
i=0
j=0
merge=[]
while i < len(list1) and j < len(list2) :
    if list1[i] <= list2[j] :
        merge.append(list1[i])
        i += 1
    else : 
        merge.append(list2[j])
        j += 1
while i < len(list1) :
    merge.append(list1[i])
    i += 1
while j < len(list2) :
    merge.append(list2[j])
    j += 1
print("marged list is :",merge)