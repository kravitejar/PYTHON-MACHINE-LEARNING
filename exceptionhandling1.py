
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

try:
    c=a/b
    print(c)

except ArithmeticError:
    print("Sorry. Please enter a number greater than zero")

else:
    print("Success")
    
