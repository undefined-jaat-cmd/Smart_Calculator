def addition(a,b):
    file.write(f"{a} + {b} = {a+b}\n")
    return a+b
def subtraction(a,b):
    file.write(f"{a} - {b} = {a-b}\n")
    return a-b
def multiplication(a,b):
    file.write(f"{a} * {b} = {a*b}\n")
    return a*b
def division(a,b):
    file.write(f"{a} / {b} = {a/b}\n")
    return a/b
def power(a,b):
    file.write(f"{a} ** {b} = {a**b}\n")
    return a**b
def square_root(a):
    file.write(f"√{a} = {a**0.5}\n")
    return a**0.5
def modulus(a,b):
    file.write(f"{a} % {b} = {a%b}\n")
    return a%b
def percentage(a,b):
    file.write(f"{a}% of {b} = {(a/100)*b}\n")
    return (a/100)*b
def view_History():
    file=open(r"history.txt","r")
    print("Calculation History:")
    print(file.read())
    file.close()
file=open(r"history.txt","a")
while True:
    try:
        print("===================================")
        print("         SMART CALCULATOR          ")
        print("===================================")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Power")
        print("6.Square Root")
        print("7.Modulus")
        print("8.Percentage")
        print("9.Check history")
        print("0.Exit")
        
        print("\n \n")
        print("-----------------------------------")
        x=int(input("Enter your choice: "))
        print("\n")
       
        if x==1:
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))
            print("Addition of two numbers is: ",addition(num1,num2))
        elif x==2:
            num1=float(input("Enter first number: ")) 
            num2=float(input("Enter second number: "))
            print("Subtraction of two numbers is: ",subtraction(num1,num2))
        elif x==3:
            num1=float(input("Enter first number: ")) 
            num2=float(input("Enter second number: "))
            print("Multiplication of two numbers is: ",multiplication(num1,num2))
        elif x==4:
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))
            if num2!=0:
                print("Division of two numbers is: ",division(num1,num2))   
            else:
                print("Division by zero is not allowed.")
                    
            
        elif x==5:
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))
            if num2<0:
                print("Power of a number with negative exponent is not allowed.")
            else:
                print("Power of two numbers is: ",power(num1,num2))
        elif x==6:
            num1=float(input("Enter first number: "))
            if num1>=0: 
                print("Square root of first number is: ",square_root(num1))
            else:
                print("Square root of negative number is not allowed.")
        elif x==7:
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))
            if num2!=0:
                print("Modulus of two numbers is: ",modulus(num1,num2))
            else:
                print("Modulus by zero is not allowed.")
        elif x==8:
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))
            if num2!=0:
                print(f"{num1}% of {num2} = ",percentage(num1,num2))
            else:
                print("Percentage calculation by zero is not allowed.")
        elif x==9:
            file.close()
            view_History()
            file=open(r"history.txt","a")
        elif x==0:
            file.close()
            print("Thank you for using Smart Calculator!")
            break
        else:
            print("Invalid choice. Please try again.")
    except FileNotFoundError:
        print("History file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    


