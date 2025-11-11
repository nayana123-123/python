text=input("enter a word:")
if len(text)>1:
    modified_text=text[-1]+text[1:-1]+text[0]
else:
    modified_text=text
print("Modified string:",modified_text)
