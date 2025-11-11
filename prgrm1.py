n=int(input("How many numbers the user wants to enter?"))
numbers=[]
for i in range(n):
    num=int(input("enter number:"))
    numbers.append(num)
positive_numbers=[]
for num in numbers:
    if num>0:
        positive_numbers.append(num)
print("positive numbers are:",positive_numbers)

    
