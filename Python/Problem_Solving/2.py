#counting in a list of numbers if every numer in a list has starting digit same as last digit(if so return true and count of it) 
def check(num1):
    str1=str(abs(num1))
    return len(str1)>2 and str1[0]==str1[-1]
        
list1=list(map(int,input("Enter few numbers").split()))
result=sum(map(check,list1))
print(result)

