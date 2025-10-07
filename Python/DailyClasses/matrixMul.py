def multiply(arr1,arr2):
    m=len(arr1)
    n=len(arr1[0])
    p=len(arr2)
    q=len(arr2[0])
    mul=[]
    if n!=p:
        return None,"Cannot Multiply such matrices"
    else:
        for i in range(m):
            sub=[]
            for j in range(q):
                value=0
                for k in range(n):
                    value+=arr1[i][k]*arr2[k][j]
                sub.append(value)
            mul.append(sub)
    return mul,"Matrix Multiplication Successfull"

arr1=[[1,2,3],[4,5,6]]
arr2=[[10,11],[20,21],[30,31]]
result,message=multiply(arr1,arr2)
print(message)
if result:
    print(result)
