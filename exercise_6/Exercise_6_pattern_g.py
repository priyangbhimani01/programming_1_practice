rows=int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
        
        for j in range(rows - i):
            print(" ", end=" ")

     
        for k in range(1, i):
            print(chr(65 + k - 1), end=" ")

     
        for l in range(i, 0, -1):
            print(chr(65 + l - 1), end=" ")

       
        print()



