# Write a program to calculate the factorial of a number using
# a while loop.
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        fact=1
        while num>0:
            fact*=num
            num-=1
    return fact
num=int(input("Enter a Number: "))
result=factorial(num)
print(result)
    

#Reverse a number using a while loop.
def reverse(num):
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev
num=int(input())
result=reverse(num)
print(result)

#prinr all numbers that are divisible by a and 5 from 1 to 100
num=1
while num<=100:
    if num%3==0 and num%5==0:
        print(num,end=' ')
    num+=1


#Login System
def login():
    username=input("Enter your username: ")
    savedPassword="123456"
    count=1
    while count<4:
        count+=1
        password=input("Enter your password here: ")
        if password==savedPassword:
            print("Login Successfull")
            break
        elif password!=savedPassword:
            print(f"Wrong Password, You have {4-count} more attempts left")
            if count==4:
                print("You have exhaused your login attempts. Revisit after 24hrs.")
        else:
            print("Something went wrong")
login()        

# Menu Driven Calculations
def menu():
    while True:
        arg=input("Enter [Square, cube or 1,2]/[+,-,/,*] and stop or .. to end" )
        res=0
        if arg in ['stop','..']:
            break
        elif arg in ['square','1','cube','2']:
            num=int(input("Enter a number: "))
            arg=arg.lower()
            if arg in ['square','1']:
                res=num**2
                print(f'{num} result: {res}')
            elif arg in ['cube','2']:
                res=num**3
                print(f'{num} result: {res}')
        elif arg in ['square','1','cube','2','+','add','-','sub','mul','*','div','/']:
            num1=int(input("Enter num 1: "))
            num2=int(input("Enter num 2: "))
            if arg in ['+','add']:
                res=num1+num2
                print(f'num1: {num1} num2: {num2} result: {res}')
            elif arg in ['-','sub']:
                res=num1-num2
                print(f'num1: {num1} num2: {num2} result: {res}')
            elif arg in ['*','mul']:
                res=num1*num2
                print(f'num1: {num1} num2: {num2} result: {res}')
            elif arg in ['/','div']:
                if num2!=0:
                    result=num1/num2
                    print(f'num1: {num1} num2: {num2} result: {res}')
                else:
                    print("division error by zero")
        else:
            print("Enter proper operator")
menu()