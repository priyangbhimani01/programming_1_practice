
import math
a=4
b=5
c=(math.sqrt(a*a+b*b))                       # calculated hypotenuse and ans is 6.4031242374328485
print(c)

x=a/c                                        # it is angle x

angle_radians = math.asin(x)                 # angle in radians

angle_degrees = math.degrees(angle_radians)

print(angle_degrees)                          #  angle in degree is 38.65980825409009

print(math.cos(angle_degrees))                # cos(x) = 0.5729493530137668

# Calculate the tangent using the sine and cosine
tangent_calculated = math.sin(angle_degrees) / math.cos(angle_degrees)

# Calculate the tangent using the math.tan function
tangent_from_math_tan = math.tan(angle_degrees)

print(tangent_calculated)                      # ans. is 1.4304768317525187
print(tangent_from_math_tan)                   # ans. is 1.4304768317525187
                                               # Results are same in both cases.