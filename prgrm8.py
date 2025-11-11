text=input("enter a word:")
first_char=text[0]
modified_text=first_char + text[1:].replace(first_char,'$')
print("Modified string:",modified_text)
