list=[1,2,3,4,5,6,7,8,9,10,11,12]

list[0]=13
print(list)

del list[2:7]
print(list)

list[3:6]=[14,15,16]
print(list)

list.reverse()
print(list)