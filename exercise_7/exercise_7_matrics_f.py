num = 1
rows=int(input("Enter the number of rows: "))
for i in range(rows):
        for j in range(rows):
            if i % 2 == 0:
                print(num, end="\t")
                num += 1
            else:
                print(num + rows - 1 - 2 * j, end="\t")

       
        print()