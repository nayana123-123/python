words=input("enter words separated by space:").split()
longest=max(words,key=len)
print("Longest word:",longest)
print("Lenghth of longest word:",len(longest))
