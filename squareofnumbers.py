n=int(input("How many numbers do you want to enter?"))
squares=[]
for i in range(n):
    num=int(input("enter number:"))
    sq=num*num
    squares.append(sq)
print("squares of the given numbers are:",squares)
