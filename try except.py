try:
    10/0
    number=int(input("enter a num: "))
    print(number)
#except:#it will catch any error under the sun
    #print("invalid input")
#except ZeroDivisionError:
 #   print("divided by zero")
except ValueError:
    print("invalid input")
except ZeroDivisionError as err:
    print(err)