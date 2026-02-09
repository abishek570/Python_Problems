## Duplicates in a string

def find_duplicates(inp):
    a = []
    for i in range(len(inp)):
        a.append(inp[i])
    b = set()
    for i in a:
        if a.count(i)>1:
            b.add(i)
    return list(b)

# Input a string
input_string = "piyush sharma"
# Find duplicate characters in the string
duplicate_chars = find_duplicates(input_string)
# Print the list of duplicate characters
print("Duplicate characters:", duplicate_chars)
