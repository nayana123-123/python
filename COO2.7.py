word=input("enter a word:")
if word.endswith("ing"):
    eord=word+"ly"
else:
    word=word+"ing"
print("Modified word:",word)
