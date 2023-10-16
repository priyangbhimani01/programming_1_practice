import math
x1=float(input("Enter the value of x1:"))
x2=float(input("Enter the value of x2:"))
y1=float(input("Enter the value of y1:"))
y2=float(input("Enter the value of y2:"))

distance_between_points=math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))
print(distance_between_points)