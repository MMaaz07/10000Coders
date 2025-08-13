#Factorial of secons input exists in the given number list or not
def factorial(num):
    fact=1
    if num<=1:
        return 1
    else:
        for i in range(2,num+1):
            fact=fact*i
        return fact

numbers=list(map(int,input("Enter few Numbers: ").split()))
second=int(input("Enter second input: "))
value=factorial(second)
count=0
for i in range(len(numbers)):
    if value==numbers[i]:
        print(i)
        count+=1
        break
if count==0:
    print("Number doesnt Exist")

 
