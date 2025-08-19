def is_rightAngled(a,b,c):
    largest=max(a,b,c)
    x,y=(b,c) if a==largest else (a,c) if b==largest else (a,b)
    if x**2 + y**2==largest**2:
        print("Indeed a Right Angled Triangle")
    else:
        print("Not a Right Angled Triangle")

def is_triangle(a,b,c):
    if (a+b)>c and (b+c)>a and (c+a)>b:
        print("It is a Valid Triangle",end=' ')
        if a==b==c:
            print("and an Equivalent Triangle")
        elif a==b or b==c or c==a:
            print("and an Isosceles Triangle")
        else:
            print("and a Scalene Triangle")
        is_rightAngled(a,b,c)
    else:
        print("Not a valid Triangle")

a=int(input("Enter First Side: "))
b=int(input("Enter Second Side: "))
c=int(input("Enter Third Side: "))
is_triangle(a,b,c)
