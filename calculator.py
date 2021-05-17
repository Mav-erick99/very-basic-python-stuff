num1=float(input("put in 1st number = "))
op=input("enter operation  ")
num2=float(input("put in 1st number = "))
if op =="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("operation not supported")