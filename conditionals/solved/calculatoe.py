num1=int(input('Enter number:'))
operation=input("enter operatio to be performed: ")
num2=int(input('enter second number: '))
if operation == "+":
    print(num1+num2)
elif operation == '_':
    print(num1-num2)
elif operation == '/':
    print(num1/num2)
elif operation == '*':
    print(num1*num2)
else:
    print("invalid operator!!!!")


