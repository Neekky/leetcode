list1 = [3, 7, 8, 9, 12]
list2 = [5, 6, 10, 13, 25, 30]
list3=list1+list2
list4=[]
def pal():
    if len(list3)==0:
        return list4
    elif len(list3)>0:
        m=min(list3)
        list3.remove(m)
        list4.append(m)
    return pal()
print(pal())



