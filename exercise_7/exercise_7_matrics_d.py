rows=int(input("Enter the size of matrix: "))
for i in range(rows):
        for j in range(rows):
            if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
                print("2", end="\t")
            else:
                print("1" if i == rows // 2 and j == rows // 2 else "0", end="\t")

        
        print()