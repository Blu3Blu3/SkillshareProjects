# Christian G
# Skillshare Project: Basic Calculator
# 1/17/2023

# Initiate vars
a = int(input("Enter an integer! "))
b = int(input("Enter another integer! "))
choice = int(input("What do you want to do? Type a number:\n\
                   1 = add, 2 = subtract, 3 = multiply, 4 = divide\n\
                   5 = raise to power, 6 = modulo\n"))

# Debug
#print(a, b, choice)

# Initiate calculator
while((choice<1) or (choice>6)):
    choice = int(input("Invalid option, try again: "))

if(choice==1):
    print(a, " + ", b, " = ", a+b)
elif(choice==2):
    print(a, " - ", b, " = ", a-b)
elif(choice==3):
    print(a, " x ", b, " = ", a*b)
elif(choice==4):
    print(a, " / ", b, " = ", a/b)
elif(choice==5):
    print(a, "^", b, " = ", a**b)
# This should be fine since there was already a check prior...
else:
    print(a, " % ", b, " = ", a%b)
