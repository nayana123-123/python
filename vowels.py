word=input("enter a word:")
vowels_list=[]
for ch in word:
    if ch.lower() in['a','e','i','o','u']:
        vowels_list.append(ch)
print("vowels in the word are:",vowels_list)
