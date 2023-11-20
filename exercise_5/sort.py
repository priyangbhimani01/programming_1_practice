list=[1,4,7,3,2,8,6,9,5]

for i in range(0,8):
    for j in range(i+1,9):
        if(list[i]>list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp

print(list)
