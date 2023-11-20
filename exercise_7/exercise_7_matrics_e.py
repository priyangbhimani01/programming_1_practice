rows=int(input("Enter the size of matrix: "))
for i in range(rows, 0, -1):
    for j in range(rows):
        number = i * rows - j
        if j < rows:
            print(number, end="\t")
        
    print() 