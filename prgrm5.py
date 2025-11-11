n=int(input("How many numbers do you want to enter?"))
result=[]
for i in range(n):
    num=int(input("enter number:"))
    if num>100:
        result.append("over")
    else:
        result.append(num)
print("Final list:",result)
