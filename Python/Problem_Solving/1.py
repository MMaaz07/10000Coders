#check no of vowels in 2 parts of string and if they are equal print true or false
str1=input("Enter a string")
i=0
count=0
count1=0
mid=len(str1)//2
vowels=['a','e','i','o','u']
for i in range(0,mid):
    if str1[i] in vowels:
        count+=1
for i in range(mid,len(str1)):
    if str1[i] in vowels:
        count1+=1
print(count==count1)