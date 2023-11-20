rows=int(input("Enter the number of rows: "))
sum=0
for i in range(1,rows+1):
    for j in range(1,i+1):
        sum=sum+1
        print(sum, end=" ")
    print() 