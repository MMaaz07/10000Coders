# 4 3 2 1
# 4 3 2
# 4 3
# 4
#print this pattern

num=int(input("Enter a pattern: "))
for i in range(1,num+1):
    for j in range(num,i-1,-1):
        print(j, end=' ')
    print()
