#adding sum of duplicate didgits in a number
num=int(input("Enter a number: "))
count={}
while num>0:
    rem=num%10
    if rem not in count:
        count[rem]=1
    else:
        count[rem]+=1
    num=num//10

def sumof(count):
    sum=0
    for x,y in count.items():
        if y>1:
            sum+=x
    return sum
print(sumof(count))