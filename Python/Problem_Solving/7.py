#1
#1 2
#1 2 3
#1 2 3 4
#print this pattern
num=int(input("Enter a number for pattern: "))
for i in range(1,num):
    for j in range(1,i+1):
        print(j,end=' ')
    print()