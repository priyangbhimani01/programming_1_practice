Normal_price=float(input("Enter the normal price : "))
Operating_system=input("Enter the operating system : ")

if(Operating_system=="MacOS"):
      MacOS=Normal_price+(Normal_price*0.2)
      print("Final price is : ",MacOS)

elif(Operating_system=="Windows"):
      Windows=str(Normal_price)
      print("Final price is : ",Windows)

elif(Operating_system=="Linux"):
        Linux=Normal_price-(Normal_price*0.2)
        print("Final price is : ",Linux)

else:        
     For_other=Normal_price+(Normal_price*0.05)
     print("For other Final price is : ",For_other)

