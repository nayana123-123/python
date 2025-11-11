text=input("Enter a line of text:")
text=text.lower()
words=text.split()
word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print("Word occurance:")
for word,count in word_count.items():
    print(word,":",count)
