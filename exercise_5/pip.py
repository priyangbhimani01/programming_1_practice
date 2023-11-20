list=[5,10,12,2,14,8,18,20]
list.insert(8,25)
print(list)

del list[2:6]
print(list)

list.sort(reverse=list)
print(list)

list.sort()
print(list)

list=[5,10,18,20,25]
label=['Bob','Adam','Doro','turtle','Asmee']

x = dict(zip(label,list))
for i in x:
   print(i)

turtle_weight = x.get('turtle')
print(turtle_weight)

list={"Bob":5, "Mern":10, "doro":18, "turtle":20, "Asmee":25}
print(list["turtle"])

#print(list["Adam"]) #Here, i got error like not found. So, pip already shipped this package.



