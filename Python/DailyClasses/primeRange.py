#Using a for loop and range, print only the prime numbers between 100 and 300.
def isPrime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

result=list(filter(isPrime,range(100,300+1)))
print(result)
