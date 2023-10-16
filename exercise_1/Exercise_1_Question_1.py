a=8
b=4
c=a+b
print(type(c))       # int
print(id(c))         # 140722280909592
d=c
c=c/3
print(type(d))       # int
print(id(d))         # 140722280909592
print(type(c))       # float
print(id(c))         # 2500220202096
