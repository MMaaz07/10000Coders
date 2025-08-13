#checking if num from a numbers list +1 is a prime number or not
numbers=list(map(int,input().split()))
def checkPrime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def get_noof(numbers):
    for num in numbers:
        if(checkPrime(num+1)):
            yield num

result=list(get_noof(numbers))
print(result)        