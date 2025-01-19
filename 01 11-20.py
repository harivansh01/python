#11
g=int(input("enter the weight in grams"))
print("the weight in kilograms would be","=",g/1000)

#12
kg=int(input("enter the weight in kilograms"))
print("the weight in grams would be","=",kg*1000)

#13
b=int(input("enter the amount of storage in bytes"))
kb=b/1024
mb=kb/1024
gb=mb/1024
print("the amount of storage in kilobytes","=",kb)
print("the amount of storage in megabytes","=",mb)
print("the amount of storage in gigabytes","=",gb)

#14
t=int(input("enter the temperature in celcius"))
tf=(9/5*t)+32
print("the temperature in fahrenheit",tf)

#15
f=int(input("enter the temperature in fahrenheit"))
c=5/9*(f-32)
print("the temperature in celcius",c)

#16
p=int(input("enter the principal amount in rs"))
r=int(input("enter the interest rate"))
T=int(input("enter the time period"))
print("the interest in rs to be paid is",p*r*T/100)

#17
a=int(input("enter the length of square"))
print("the area of the square is ",a*a)
print("the perimeter of the square is ",4*a)

#18
l=int(input("enter the length of rectangle"))
h=int(input("enter the breadth of rectangle"))
print("the area of the rectangle is ",l*h)
print("the perimeter of the rectangle is ",2*(l+h))

#19
R=int(input("enter the radius of circle"))
area=22/7*R*R
print("the area of the circle is ",area)

#20
x=int(input("enter the length of triangle"))
y=int(input("enter the height of triangle"))
ar=x*y/2
print("the area of the triangle is ",ar)


