a=float(input("enter first number:"))
b=float(input("enter second number:"))
c=float(input("enter third number:"))
if a>=b and a>=c:
    biggest=a
elif b>=a and b>=c:
    biggest=b
else:
    biggest=c
print("the biggest number is:",biggest)
