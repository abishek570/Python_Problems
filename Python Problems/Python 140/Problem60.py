# Example usage
def find_words(word_list,k):
    a = []
    for i in word_list:
        if len(i)>k:
            a.append(i)
        else:
            pass
    return a

word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragon"]
k = 5
long_words = find_words(word_list, k)
print(f"Words longer than {k} characters: {long_words}")