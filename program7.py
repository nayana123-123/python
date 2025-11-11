n1=int(input("How many numbers in first list?"))
list1=[]
for i in range(n1):
    num=int(input("enter number:"))
    list1.append(num)
n2=int(input("How many numbers in second list?"))
list2=[]
for i in range(n2):
    num=int(input("enter number:"))
    list2.append(num)
same_length=len(list1)==len(list2)
same_sum=sum(list1)==sum(list2)

common_values=[]
for x in list1:
    if x in list2 and x not in common_values:
        common_values.append(x)
print("\nFirst list:",list1)
print("\nSecond list:",list2)
print("\n(a)Lists are of same length:",same_length)
print("(b)Lists have the same sum:",same_sum)
if common_values:
    print("(c)Common values in both lists:",common_values)
else:
    print("(c)No common values found")
