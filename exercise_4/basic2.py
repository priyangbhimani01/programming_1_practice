x=[2,1,5,4,3]
j=len(x)-1
for index in range(j):
    if (x[index]>=x[index+1]):
            temp=x[index]
            x[index]=x[index+1]
            x[index+1]=temp
            j=len(x)

print(x)            