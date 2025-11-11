dict1={'apple':40,'banana':10,'grapes':30,'mango':20}
ascending_dict1=dict(sorted(dict1.items(),key=lambda item:item[1]))
print("Ascending order:",ascending_dict1)
decending_dict1=dict(sorted(dict1.items(),key=lambda item:item[1],reverse=True))
print("Decending order:",decending_dict1)
