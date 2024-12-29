List_1 = [1,2,3,3,4,4,5,5,6,7]
List_2 = []
for i in List_1:
    if i not in List_2:
        List_2.append(i)
print(List_2)