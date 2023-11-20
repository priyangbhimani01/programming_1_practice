class employee:
    def setdata(self,name,salary,id):
        self.name=name
        self.salary=salary
        self.id=id

    def getdata(self):
        print("The name of employee is " + (self.name))
        print("The salary of " + self.name + " is " + str(self.salary))
        print("The id of " + self.name + " is " + self.id)


name=input("Enter the name: ")
salary=int(input("Enter the salary: "))
id=input("Enter the id: ")

data1 = employee()
data1.setdata(name,salary,id)
data1.getdata()



        

    


