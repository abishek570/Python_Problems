
def is_isogram(word):
    word = word.lower()
    for i in word:
        if word.count(i)>1:
            return False
    else:
        return True
    
print(is_isogram("Algorism"))