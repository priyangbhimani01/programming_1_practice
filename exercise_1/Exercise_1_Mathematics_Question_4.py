import math
x1=float(input("Enter the value of x1:"))
x2=float(input("Enter the value of x2:"))
y1=float(input("Enter the value of y1:"))
y2=float(input("Enter the value of y2:"))

distance_xy=math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))
print(distance_xy)

x1=float(input("Enter the value of x1:"))
x2=float(input("Enter the value of x2:"))
y1=float(input("Enter the value of y1:"))
y2=float(input("Enter the value of y2:"))
z=float(input("Enter the value of z:"))

pi=3.14

# The distance of both the quarter arc is pi*z + the distance of the straight path - extra length is 2z.
total_distance=z*(pi-2)+ math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))

print(total_distance)




