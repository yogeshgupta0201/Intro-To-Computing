#Question 1.
print("\nAverage Of Three Numbers\n")

x= input("Enter first number: ")
y= input("Enter second number: ")
z= input("Enter third number: ")
avg = (int(x)+int(y)+int(z))/3
print("The average of three numbers is: ", avg) 


#Question 2.
'''Program to compute Income tax.'''

print("\n\nIncome Tax Calculator\n")

x = float(input("Enter your Gross income: "))
y= int(input("Enter number of dependents: "))
a = (x-10000-(3000*y))
# a is the taxable income
b = a*0.2
# b is the tax
print("income Tax is:", b)


#Question 3.
print("\n\nStudent Details List\n")

x  =  [ 21104091, "Yogesh Gupta", "M", "Electrical Engineering", 10]
print(x)


#Question 4.
print("\n\nMarks Of Five Students\n")

x= [75, 98, 43, 87, 56]
x.sort()
print(x) 


#Question 5a.
print("\n\nPrinting A Specified List\n")
x = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
x.pop(3)
print(x)


#Question 5b.
del x[3:5]
x.insert(3, "Purple")
print(x)
