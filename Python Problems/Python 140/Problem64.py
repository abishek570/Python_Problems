## uncommon words

def uncommon_words(s1,s2):
    s1 = s1.split()
    s2 = s2.split()
    a = []
    for i in range(len(s2)):
        if s1[i]!=s2[i]:
            a.extend([s1[i],s2[i]])
    return a
        
string1 = "This is the first string"
string2 = "This is the second string"
# Find uncommon words between the two strings
uncommon = uncommon_words(string1, string2)
# Print the uncommon words
print("Uncommon words:", uncommon)