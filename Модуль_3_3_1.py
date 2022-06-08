import math
def area(a,b,c):
	import math
a=float(input("Введите число a= "))
b=float(input("Введите число b= "))
c=float(input("Введите число c= "))

# S=math.S(p(p-a)*(p-b)(p-c))
# Находим P - полупериметр
# p=(a+b+c)/2

p=float((a+b+c)/2)
print ("p = ", p)

#Теперь находим площадь по трём стронам S

S=p*(p-a)*(p-b)*(p-c)
S=math.sqrt(S)
print ("Площадь S= ", S)