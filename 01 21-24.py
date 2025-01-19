#21
gross_salary=int(input("enter the gross salary"))
allowance=0.1*gross_salary
deduction=0.03*gross_salary
net_salary=gross_salary+allowance+deduction
print("the net salary is",net_salary)

#22
gross_sales=int(input("enter the gross sales"))
net_sales=gross_sales-0.1*gross_sales
print("the net sales is",net_sales)

#23
english=int(input("enter the marks of english"))
history=int(input("enter the marks of history"))
science=int(input("enter the marks of science"))
average_marks=english+history+science
print("the average marks of three subjects is",average_marks/3)
print("the total marks of three subjects is",average_marks)

#24
a=int(input("enter the first nos"))
b=int(input("enter the second nos"))
print("before swapping a =",a,"and b =",b)
a,b=b,a
print("after swapping a =",a,"and b =",b)
