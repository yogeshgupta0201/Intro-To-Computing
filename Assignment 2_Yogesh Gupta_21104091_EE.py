print("Question1")

my_string = 'Python is a case sensitive language'

# printing the length.
print("\n (a)")
print(len(my_string))

# printing my_string in reverse order.
print("\n (b)")
print(my_string[::-1])


# slicing and printing the sliced_string.
print("\n (c)")
sliced_string = my_string[10:-9]
print(sliced_string)


# replacing and printing.
print("\n (d)")
print(my_string.replace("a case sensitive", "object oriented"))



# printing index of "a" from my_string.
print("\n (e)")
print(my_string.index("a"))


# replacing blank white spaces.
print("\n (f)")
print(my_string.replace(" ", ""))





print("\n\nQuestion 2\n")


Name = "Yogesh Gupta "
SID = "21104091"
Department = "EE"
CGPA = "9.9"


print(f"Hey, {Name.title()} here! \nMy SID is {SID} \nI am from {Department} and my CGPA is {CGPA}")

                                

                                



print("\n\nQuestion 3\n")


a = 56
b = 10

#a
print(" a&b is : ", a & b)

#b
print(" a|b is : ", a | b)

#c
print(" a^b  is : ", a ^ b)

#d.
print("a<<2 : ", a << 2, "\tb<<2 :", b << 2)

#e.
print("a>>2 : ", a >> 2, "\tb>>2 :", b >> 4)


        


print("\n\nQuestion 4\n")

x = int(input("Enter 1st  : "))
y = int(input("Enter 2nd  : "))
z = int(input("Enter 3rd  : "))

#finding the highest no.
if x > y:
    if x > z:
        highest_number = x
    else:
        highest_number = z

if y > x:
    if y > z:
        highest_number = y
    else:
        highest_number = z


print(f"The Highest number is = {highest_number}")      
    





print("\n\nQuestion 5\n")

in_string = input("Enter input string : ")

if "name" in in_string:
    print("Yes")
else:
    print("No")





print("\n\nQuestion 6\n")

a = int(input("Side a  : ")) 
b = int(input("Side b  : "))
c = int(input("Side c  : "))
outcome="No"

if (a+b>c) and (b+c>a) and (c+a>b):
    outcome="Yes"
print(outcome)
