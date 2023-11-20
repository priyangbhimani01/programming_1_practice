rows=int(input("Enter the number of rows: "))
for i in range(rows):
       
        for j in range(rows - i):
            print(" ", end="  ")

     
        starting_point = 1

        for j in range(i + 1):
            
            print(starting_point, end="  ")
            print("  ", end=" ") 

            starting_point = starting_point * (i - j) // (j + 1)

       
        print()

    
